class Train():
    def __init__(self,TrainName,station):
        self.TrainName=TrainName
        self.station=station

    def show(self):
        print(self.TrainName)
        print(self.station)

class Passenger(Train):
    def __init__(self,TrainName,station,name,age,Berth,compartmentNum):
        self.name=name
        self.age=age
        self.Berth=Berth
        self.compartmentNum=compartmentNum

        Train.__init__(self,TrainName,station)

    def show1(self):
        print(self.TrainName)
        print(self.station)
        print(self.name)
        print(self.age)
        print(self.Berth)
        print(self.compartmentNum)

obj=Passenger("Palavan","Trichy","Ramya","20","middle","25")
obj.show1()
