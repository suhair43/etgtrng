''' Create a program that asks the user to enter their name and their age. Print out a message
addressed to them that tells them the year that they will turn 100 years old.'''
name = input("what is your name: ")
age = int(input("enter your age: "))
#turninto = str((2021 - age)+100)


def userage():
    year = (2021 - age) + 100
    return year

print(name , " will turn 100 years in "+str(userage()))

