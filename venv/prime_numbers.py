#4.	Python program to print all Prime numbers in an Interval

lower = int(input("Enter a lower value: "))
upper = int(input("Enter a upper valve: "))

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

print("Prime numbers in between", lower, "and", upper)