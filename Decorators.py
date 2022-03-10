def num(sync):
    def decorate(a,b):
        print(a)
        print(b)
        return sync(a,b)
    return decorate
@num
def show(a,b):
    print(a+b)
show(2,1)

