# Password Reminder
stored_name = "Leo"
stored_pass = "Leo@123"
name = input("Enter your name: ").title()
if name == stored_name:
    print(f"Hello {name}! The password is: {stored_pass}")
else:
    print(f"Hello {name}! See you later.")
