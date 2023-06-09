class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name} ：大人です")
        else:
            print(f"{self.name} ：大人ではない")

humans = [
    Human("human1", 10),
    Human("human2", 15),
    Human("human3", 20)
]

for human in humans:
    human.check_adult()