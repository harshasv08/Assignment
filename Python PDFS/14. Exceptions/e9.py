try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"File Not Found Error: {e}")
