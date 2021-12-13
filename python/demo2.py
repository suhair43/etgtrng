''' Create a program to compare three numbers and find the bigger numbers. [topics covered:
identified, variable, types, operator, if statement]
'''


def maximum(n1, n2, n3):

    if (n1 > n2) and (n1 > n3):
        largest = n1
    elif (n2 > n1) and (n2 > n3):
        largest = n2
    else:
     largest = n3
     return largest
n1 = int(input("enter the number: "))
n2 = int(input("enter the number: "))
n3 = int(input("enter the number: "))
print(maximum(n1, n2, n3))
