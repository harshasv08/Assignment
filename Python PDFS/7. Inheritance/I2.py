class A:
    def methodA1(self):
        print("Method A1 in Class A")

    def methodA2(self):
        print("Method A2 in Class A")

    def common_method(self):
        print("Common Method in Class A (Overridden)")


class B(A):
    def methodB1(self):
        print("Method B1 in Class B")

    def methodB2(self):
        print("Method B2 in Class B")

    def common_method(self):
        print("Common Method in Class B (Overridden)")


class C(B):
    def methodC1(self):
        print("Method C1 in Class C")

    def methodC2(self):
        print("Method C2 in Class C")

    def common_method(self):
        print("Common Method in Class C (Overridden)")


class Main:
    def run(self):
     
        objA = A()
        objB = B()
        objC = C()

       
        objA.methodA1()
        objA.methodA2()
        objA.common_method()

  
        objB.methodB1()
        objB.methodB2()
        objB.common_method()

      
        objC.methodC1()
        objC.methodC2()
        objC.common_method()


#  instance of the Main class and run the program
if __name__ == "__main__":
    main_instance = Main()
    main_instance.run()
