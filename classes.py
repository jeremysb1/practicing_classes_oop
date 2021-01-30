class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return (self.__length * self.__width)

    def perimeter(self):
        return (2 * (self.__length + self.__width))


# Example using getters and setters


class Student:
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, RollNumber):
        self.__RollNumber = RollNumber

    def getRollNumber(self):
        return self.__RollNumber


demo1 = Student()
demo1.setName("Alex")
print("Name:", demo1.getName())
demo1.setRollNumber(3789)
print("Roll Number:", demo1.getRollNumber())

# class examples using inheritance

class Account:  # parent class
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    # withdrawal method subtracts the amount from the balance

    def withdrawal(self, amount):
        self.balance = self.balance - amount
    # deposit method adds the amount to the balance

    def deposit(self, amount):
        self.balance = self.balance + amount
    # this method just returns the value of balance

    def getBalance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    # computes interest amount using the interest rate

    def interestAmount(self):
        return (self.balance * self.interestRate / 100)


obj1 = SavingsAccount("Steve", 5000, 10)
print("Initial Balance:", obj1.getBalance())
obj1.withdrawal(1000)
print("Balance after withdrawal:", obj1.getBalance())
obj1.deposit(500)
print("Balance after deposit:", obj1.getBalance())
print("Interest on current balance:", obj1.interestAmount())