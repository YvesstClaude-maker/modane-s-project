from financial_engine import (
    FinancialEngine,
    Transaction
)

from savings_engine import (
    SavingsGoal
)

from analytics_reporting_engine import (
    AnalyticsReportingEngine
)


def main():

    finance = FinancialEngine()

    savings = SavingsGoal(
        100000,
        45000
    )

    analytics = (
        AnalyticsReportingEngine()
    )

    finance.add_transaction(
        Transaction(
            50000,
            "income",
            "salary"
        )
    )

    finance.add_transaction(
        Transaction(
            12000,
            "expense",
            "rent"
        )
    )

    finance.add_transaction(
        Transaction(
            5000,
            "expense",
            "food"
        )
    )

    analytics.add_record(
        "Rent",
        12000,
        "May"
    )

    analytics.add_record(
        "Food",
        5000,
        "May"
    )

    summary = (
        finance.summary()
    )

    print(
        "\nSMARTTAX SUMMARY"
    )

    print(
        "Income:",
        summary["income"]
    )

    print(
        "Expenses:",
        summary["expenses"]
    )

    print(
        "Balance:",
        summary["balance"]
    )

    print(
        "Tax:",
        finance.calculate_tax(
            30
        )
    )

    print(
        "\nSAVINGS"
    )

    print(
        savings.summary()
    )

    print(
        "\nANALYTICS"
    )

    print(
        analytics.category_summary()
    )

    print(
        analytics.monthly_summary()
    )

    report = (
        analytics.generate_report(
            "smarttax_report.pdf"
        )
    )

    print(
        "\nReport Generated:",
        report
    )


if __name__ == "__main__":
    main()
