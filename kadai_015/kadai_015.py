class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def printinfo(self):
        print("名前: ", self.name)
        print("年齢: ", self.age)

human = Human("ポンコツAI", 100)
human.printinfo()