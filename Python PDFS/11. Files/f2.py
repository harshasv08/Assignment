file_path = "11. Files/s.txt"

try:
    with open(file_path, "w") as file:
        # Write text to the file
        file.write("This is a line of text.\n")
        file.write("This is another line of text.\n")
        file.write("And a third line of text.\n")
        
    print(f"Text has been written to '{file_path}' successfully.")
except IOError as e:
    print(f"An error occurred while writing to the file: {e}")
