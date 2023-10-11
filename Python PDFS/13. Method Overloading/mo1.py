class a:
    def method(self, arg1, arg2=None):
        if arg2 is not None:
            print(f"Two arguments: arg1 = {arg1}, arg2 = {arg2}")
        else:
            print(f"One argument: arg1 = {arg1}")

    def method(self, ar1, ar2=None):
        if ar2 is not None:
            print(f"Two arguments: arg1 = {ar1}, arg2 = {ar2}")
        else:
            print(f"One argument: arg1 = {ar1}")

obj = a()


obj.method("First Argument")

obj.method("First Argument", "Second Argument")

