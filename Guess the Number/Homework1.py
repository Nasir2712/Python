print('Hello! What is your name?')
name = input()
print('Well, ' + name + ', Think of random number from 1 to 100, and I will try to guess it!')
lowest = 1
highest = 100
mean = 0
guessestaken = 0
guessing = True
while guessing:
     guessestaken = guessestaken + 1
     mean = int((lowest+highest)/2)
     print('Is it ',mean,' ? ')
     response = input('yes/no : ')
     if response == 'yes':
        print('Yeey! You got it in ' + str(guessestaken) + ' tries')
        if response == input("Do you want to play more ? (yes/no)") :
            lowest = 1
            highest = 100
            guessestaken = 0
            mean = 0
        else:
            print('Bye Bye')
            break
     if response == 'no' :
        print('Is it greater than',mean,"?")
        response_again = input('yes/no : ')
        if response_again == 'yes':
               lowest = mean
        if response_again == 'no' :
               highest = mean
