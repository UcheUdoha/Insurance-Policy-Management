class Policyholder:
    def __init__(self, name, policy_number):
        self.name = name
        self.policy_number = policy_number
        self.status = "Active"

    def suspend_policyholder(self):
        self.status = "Suspended"
        print(f"{self.name}'s policy has been suspended.")

    def reactivate_policyholder(self):
        self.status = "Active"
        print(f"{self.name}'s policy has been reactivated.")

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Policy Number: {self.policy_number}")
        print(f"Status: {self.status}")
