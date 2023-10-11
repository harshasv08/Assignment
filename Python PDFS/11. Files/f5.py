file_path = "11. Files/s.txt"

target_index = 20 

try:

    with open(file_path, "rb") as file:
        file.seek(target_index)
        
        data = file.read(target_index) 
        print("Data up to index", target_index, ":", data.decode("utf-8"))
        
    print(f"File '{file_path}' has been read up to index {target_index}.")
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except IOError as e:
    print(f"An error occurred while reading the file: {e}")
