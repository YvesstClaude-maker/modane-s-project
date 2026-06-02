import pandas as pd

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


class AnalyticsReportingEngine:

    def __init__(self):

        self.data = pd.DataFrame(
            columns=[
                "category",
                "amount",
                "month"
            ]
        )

    def add_record(
        self,
        category,
        amount,
        month
    ):

        if amount <= 0:
            raise ValueError(
                "Amount must be positive."
            )

        new_row = pd.DataFrame(
            [{
                "category": category,
                "amount": amount,
                "month": month
            }]
        )

        self.data = pd.concat(
            [
                self.data,
                new_row
            ],
            ignore_index=True
        )

    def category_summary(
        self
    ):

        if self.data.empty:
            return pd.Series()

        return (
            self.data
            .groupby("category")
            ["amount"]
            .sum()
            .sort_values(
                ascending=False
            )
        )

    def monthly_summary(
        self
    ):

        if self.data.empty:
            return pd.Series()

        return (
            self.data
            .groupby("month")
            ["amount"]
            .sum()
        )

    def average_expense(
        self
    ):

        if self.data.empty:
            return 0

        return round(
            self.data[
                "amount"
            ].mean(),
            2
        )

    def highest_expense_category(
        self
    ):

        summary = (
            self.category_summary()
        )

        if summary.empty:
            return None

        return summary.idxmax()

    def generate_report(
        self,
        filename
    ):

        document = (
            SimpleDocTemplate(
                filename
            )
        )

        styles = (
            getSampleStyleSheet()
        )

        elements = []

        elements.append(
            Paragraph(
                "SmartTax Report",
                styles["Title"]
            )
        )

        elements.append(
            Spacer(
                1,
                12
            )
        )

        elements.append(
            Paragraph(
                f"Average Expense: {self.average_expense()}",
                styles["BodyText"]
            )
        )

        elements.append(
            Paragraph(
                f"Highest Expense Category: {self.highest_expense_category()}",
                styles["BodyText"]
            )
        )

        document.build(
            elements
        )

        return filename
