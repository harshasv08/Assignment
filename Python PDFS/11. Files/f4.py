file_path = "11. Files/s.txt"

try:
    with open(file_path, "rb") as file:
        file.seek(10)

        data = file.read(5)
        print("Data from byte 10 to 14:", data)
        
    print(f"File '{file_path}' has been read with random access.")
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except IOError as e:
    print(f"An error occurred while reading the file: {e}")
