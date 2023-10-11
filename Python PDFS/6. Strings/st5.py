original_string = "Hello, World!"

try:
    index = original_string.index("World")
    print("Substring 'World' found at index:", index)
except ValueError:
    print("Substring not found in the original string.")
