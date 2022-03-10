class Movie:
    def __init__(self,name,releasedYr,HeroName,HeroineName):
        self.name=name
        self.releasedYr=releasedYr
        self.HeroName=HeroName
        self.HeroineName=HeroineName

    def show(self):
        print(self.name)
        print(self.releasedYr)
        print(self.HeroName)
        print(self.HeroineName)

name=input("Enter name")
releasedYr=input("Enter releasedYr")
HeroName=input("Enter HeroName")
HeroineName=input("Enter HeroineName")

obj=Movie(name,releasedYr,HeroName,HeroineName)
obj.show()