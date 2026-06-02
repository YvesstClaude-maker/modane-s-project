class SavingsGoal:

    def __init__(
        self,
        target_amount: float,
        current_amount: float = 0
    ):

        if target_amount <= 0:
            raise ValueError(
                "Target amount must be positive."
            )

        if current_amount < 0:
            raise ValueError(
                "Current amount cannot be negative."
            )

        self.target_amount = target_amount
        self.current_amount = current_amount

    def add_savings(
        self,
        amount: float
    ):

        if amount <= 0:
            raise ValueError(
                "Savings amount must be positive."
            )

        self.current_amount += amount

    def progress_percentage(
        self
    ):

        return round(
            (
                self.current_amount
                / self.target_amount
            ) * 100,
            2
        )

    def remaining_amount(
        self
    ):

        return round(
            self.target_amount
            - self.current_amount,
            2
        )

    def goal_reached(
        self
    ):

        return (
            self.current_amount
            >= self.target_amount
        )

    def summary(
        self
    ):

        return {

            "target":
                self.target_amount,

            "current":
                self.current_amount,

            "progress":
                self.progress_percentage(),

            "remaining":
                self.remaining_amount(),

            "completed":
                self.goal_reached()
        }
