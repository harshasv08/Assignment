#file path
file_path = "11. Files/s.txt"

try:
    # Open the file in read mode
    with open(file_path, "r") as file:
        # Read the entire content of the file
        file_content = file.read()
    
        print("File Contents:")
        print(file_content)
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except IOError as e:
    print(f"An error occurred while reading the file: {e}")
