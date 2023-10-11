class a:
    def __init__(self):
        self.field = 42

try:
    obj = a()
    value = obj.non_existent_field  
except AttributeError as e:
    print(f"Attribute Error: {e}")
