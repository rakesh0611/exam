#8.	Python program to Multiply all numbers in the list

def multiply(numbers):
    total = 1
    for n in numbers:
        total *= n
    return total
print(multiply((1,2,3,4,5)))