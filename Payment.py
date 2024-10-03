class Payment:
    def __init__(self, payment_id, policy_number, amount, payment_date):
        self.payment_id = payment_id
        self.policy_number = policy_number
        self.amount = amount
        self.payment_date = payment_date

    def process_payment(self):
        print(f"Payment of {self.amount} received for policy {self.policy_number} on {self.payment_date}.")

    def send_reminder(self):
        print(f"Reminder: Payment for policy {self.policy_number} is due.")

    def apply_penalty(self):
        print(f"Penalty applied for late payment on policy {self.policy_number}.")
