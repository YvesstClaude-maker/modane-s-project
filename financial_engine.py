from dataclasses import dataclass
from typing import List


@dataclass
class Transaction:
    amount: float
    transaction_type: str
    category: str

    def __post_init__(self):

        self.transaction_type = (
            self.transaction_type.lower()
        )

        if self.amount <= 0:
            raise ValueError(
                "Amount must be positive."
            )

        if self.transaction_type not in (
            "income",
            "expense"
        ):
            raise ValueError(
                "Type must be income or expense."
            )


class FinancialEngine:

    def __init__(self):

        self.transactions: List[
            Transaction
        ] = []

    def add_transaction(
        self,
        transaction: Transaction
    ):

        self.transactions.append(
            transaction
        )

    def total_income(self):

        return round(
            sum(
                t.amount
                for t in self.transactions
                if t.transaction_type
                == "income"
            ),
            2
        )

    def total_expenses(self):

        return round(
            sum(
                t.amount
                for t in self.transactions
                if t.transaction_type
                == "expense"
            ),
            2
        )

    def current_balance(self):

        return round(
            self.total_income()
            - self.total_expenses(),
            2
        )

    def calculate_tax(
        self,
        tax_rate
    ):

        income = self.total_income()

        return round(
            income
            * (tax_rate / 100),
            2
        )

    def summary(self):

        return {
            "income":
                self.total_income(),

            "expenses":
                self.total_expenses(),

            "balance":
                self.current_balance(),

            "transactions":
                len(
                    self.transactions
                )
        }
