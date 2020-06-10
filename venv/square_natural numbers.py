#6.	Python Program for Sum of squares of first n natural numbers

n = int(input("Enter a number: "))
def sum(n) :
   return (n * (n + 1) * (2 * n + 1)) // 6
print(sum(n))