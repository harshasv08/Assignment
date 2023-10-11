def a():
    try:
        age = int(input("Enter your age: "))
        if age < 18:
            raise ValueError("You must be at least 18 years old to continue.")
        else:
            print("You are old enough to proceed.")
    except ValueError as e:
        print(f"Custom Exception: {e}")

a()
