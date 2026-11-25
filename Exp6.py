print("Enter passwords to check(type 'stop' to quit):")
while True:
    password = input("Enter password:")
    
    if password.lower() == "stop":
        print("Program stopped.")
        break
    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

        if len(password) >= 8 and has_upper and has_lower and has_digit:
            print("Strong password")
        else:
            print("Weak password")
