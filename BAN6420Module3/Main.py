from policyholder import Policyholder
from product import Product
from payment import Payment

# Create policyholders
policyholder1 = Policyholder("Ucheoma", "P001")
policyholder2 = Policyholder("Udoha", "P002")

# Display policyholders' details
print("Policyholder 1:")
policyholder1.display_details()
print("\nPolicyholder 2:")
policyholder2.display_details()

# Create products
product1 = Product("PR001", "Health Insurance", 100)
product2 = Product("PR002", "Life Insurance", 200)

# Display products' details
print("\nProduct 1:")
product1.display_details()
print("\nProduct 2:")
product2.display_details()

# Suspend a product
product1.suspend_product()
product1.display_details()

# Process payments
payment1 = Payment("PAY001", "P001", 100, "2022-05-20")
payment2 = Payment("PAY002", "P002", 200, "2022-05-25")

# Process payment 1
payment1.process_payment()

# Send reminder for payment 2
payment2.send_reminder()

# Apply penalty for payment 2
payment2.apply_penalty()

# Demonstrate Policyholder Management
policyholder1.suspend_policyholder()
policyholder1.reactivate_policyholder()
policyholder1.display_details()

# Demonstrate Policyholder Payment
payment3 = Payment("PAY003", "P001", 150, "2022-05-27")
payment3.process_payment()

# Display policyholder's updated details
print("\nPolicyholder 1 after additional payment:")
policyholder1.display_details()
