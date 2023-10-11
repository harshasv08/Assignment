from abc import ABC, abstractmethod
class MyAbstractClass(ABC):

    @abstractmethod
    def abstract_method(self):
        pass

    def non_abstract_method(self):
        return "This is a non-abstract method."

class MySubclass(MyAbstractClass):

    def abstract_method(self):
        return "This is the implementation of the abstract method."

child_object = MySubclass()

print(child_object.abstract_method())
print(child_object.non_abstract_method())