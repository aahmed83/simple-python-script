import re

# Define email format pattern using regex
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'

# Ask user for email
email = input("Enter an email address to check: ")

# Check if the email matches the pattern
if re.match(email_pattern, email):
    print("This is a valid email format.")
else:
    print(" This is NOT a valid email format.")
