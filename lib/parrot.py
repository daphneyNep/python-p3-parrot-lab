def parrot(self):
    print(self)
    return("Hello!")

def parrot(arg=None):
    if arg is None:
        print("Squawk!")
        return "Squawk!"
    else:
        print(arg)
        return "Hello!"    
   
