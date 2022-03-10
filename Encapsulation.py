class Bank:
    def __init__(self):
        self.__accNum=12345
        print("someone from outside is trying to change your accnumber")
    def show(self):
        print(self.__accNum)

    def show1(self,accNum):
        self.__accNum=accNum
        print("Account changed successfully")

obj=Bank()
obj.show()

obj.accNum=7890
obj.show()

obj.show1(5678123)
obj.show()