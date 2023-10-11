# Create an empty dictionary
student_dict = {}

# 1.1. Adding values to the dictionary
student_dict["101"] = "Alice"
student_dict["102"] = "Bob"
student_dict["103"] = "Charlie"
student_dict["104"] = "David"
student_dict["105"] = "Eve"

# 1.2. Updating values in the dictionary
student_dict["103"] = "Charlie Updated"
student_dict["106"] = "Frank"  # Adding a new student

# 1.3. Accessing values in the dictionary
print("Student with ID 102:", student_dict["102"])

# 1.4. Create a nested loop dictionary
nested_dict = {
    "Math": {"101": 95, "102": 85, "103": 90},
    "Science": {"101": 88, "102": 92, "104": 78},
}

# 1.5. Access values of nested loop dictionary
print("Math score for student 102:", nested_dict["Math"]["102"])
print("Science score for student 104:", nested_dict["Science"]["104"])

# 1.6. Print keys present in a particular dictionary
print("Keys in student_dict:", student_dict.keys())
print("Keys in nested_dict['Math']:", nested_dict["Math"].keys())

# 1.7. Delete a value from a dictionary
if "105" in student_dict:
    del student_dict["105"]
    print("Student with ID 105 deleted.")

# Display the updated student dictionary
print("Updated Student Dictionary:")
for student_id, student_name in student_dict.items():
    print(f"Student ID: {student_id}, Name: {student_name}")
