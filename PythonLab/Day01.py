
# Check if a number is even or odd
number = int(input("Enter a number: "))
if number %2 == 0:
   print(f"{number} is even")
else:
   print(f"{number} is odd")

# find the divide 1/2 and soo on
dividen = int(input("Enter the number to be divided: "))
for i in range(1,11):
    result = dividen / i
    print(f"{dividen} divided by {i} is {result}")

# print 1 to 10 number using for Loop
for i in range(1,11):
    print(i)

# using While loop count number in decresasing order
number = int(input("Enter a number to start counting down: "))
while number >= 0:
    print(number)
    number -= 1

 