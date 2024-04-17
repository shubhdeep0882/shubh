print("Welcome to our calculator")
X = int(input("Enter the first number:"))
Y = int(input("Enter the second number:"))
sign = input ("select - or +")
if sign == "+":
    sum = X + Y 
else:
    sum = X - Y 
print("Result",sum) 