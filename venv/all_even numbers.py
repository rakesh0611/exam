#9.	Python program to print all even numbers in a range

lower = int(input("Enter the lower value: "))
upper = int(input("Enter the upper value: "))
for i in range(lower, upper + 1):
    if i % 2 == 0:
        print(i)