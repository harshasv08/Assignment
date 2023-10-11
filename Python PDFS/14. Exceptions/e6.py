class a(Exception):
    def __init__(self, message="This is a custom exception."):
        super().__init__(message)

def custom_exception_example(age):
    if age < 18:
        raise a("You must be at least 18 years old to continue.")
    else:
        print("You are old enough to proceed.")

try:
    age = int(input("Enter your age: "))
    custom_exception_example(age)
except a as e:
    print(f"Custom Exception: {e}")
