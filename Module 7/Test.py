class A:
    def __init__(self, x=10):
        self.x = x

class B(A):
    def __init__(self, x = 20):
        self.x = x
        super().__init__()

    def print_x(self):
        print(self.x)

class C(B):
    def __init__(self, x = 40):
        self.x = x
        super().__init__()

class Animal:
    def bark(self):
        print("Woof!")

class Dog(Animal):
    def __init__(self, name):
        self.name = name

def main():
    pooch = Dog("Coach")
    pooch.bark()

if __name__ == "__main__":
    main()