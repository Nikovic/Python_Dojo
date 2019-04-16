# declaring aVar globally
aVar = "global"



def test():
    aVar = "local"
    print(aVar)


test()
