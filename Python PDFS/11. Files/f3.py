file_path = "11. Files/s.txt"

try:
    with open(file_path, "r") as file:
        for line in file:
            print(line, end="") 
        
    print(f"File '{file_path}' has been read successfully.")
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except IOError as e:
    print(f"An error occurred while reading the file: {e}")
