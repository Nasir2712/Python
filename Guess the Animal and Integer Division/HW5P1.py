class Animal:
    def __init__(self,name):
        self.name = name
        
    def guess_who_am_i(self):
        if self.name == "Elephant":
            questions = ['I have exceptional memory','I am the largest land-living mammal in the world','I have a big trunk']
        elif self.name == "Tiger":
            questions = ['I am the biggest cat','I come in black and white or orange and black','I am the symbol of strength and courage']
        elif self.name == "Bat":
            questions = ['I use echo-location','I can fly','I see well in dark']
        count = 0
        for phrase in questions:
            print(phrase)
            names = input("Who am I?")
            if (names == self.name):
                print("You got it! I am ",self.name)
                break
            elif (names != self.name):
                count = count + 1
                print("Please Try Again!!")
            if count == 3:
                print("I am out of hints! The answer is:",self.name)
                
                
print("I will give you three hints,Guess what animal I am ?")
        
e= Animal("Elephant")
t= Animal("Tiger")
b= Animal("Bat")

e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()
