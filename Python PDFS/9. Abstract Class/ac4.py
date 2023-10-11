class MyBaseClass:

    def non_abstract_method(self):
        return "This is a non-abstract method."

class MySubclass(MyBaseClass):

    def call_non_abstract_method(self):
        result = self.non_abstract_method()
        return result

child_object = MySubclass()
result = child_object.call_non_abstract_method()
print(result)