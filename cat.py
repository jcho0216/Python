from Animal import Animal


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def bark(self):
        print("냐옹~")
    