st = input("Enter gender code (M/F): ")

gender_mapping = {
    "M": "Male",
    "F": "Female"
}

if st in gender_mapping:
    g = gender_mapping[st]
    print("Gender:"+''+g)
else:
    print("Invalid gender code. Please enter 'M' for Male or 'F' for Female.")
