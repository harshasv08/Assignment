try:
    file = open("non_existent_file.txt", "r") 
    content = file.read()
    file.close()
except IOError as e:
    print(f"I/O Error: {e}")
