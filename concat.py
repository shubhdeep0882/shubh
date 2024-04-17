a = "Good Afternoon"
b = input("What is your name")
a += b
# c = a + b
print(a)
# print(c)

# f-string
website = "fun learning"
print(f"welcome to{website}")

words =["we", "are", "learning", "python"]
joined = "".join(words)
print(joined)

print(joined.upper)
print(joined.lower)

basket = ["banana", "stawberry", "kiwi"]
price = 3
text = "Welcome to the grocery everything is {} dollars"
print(text.format(price))

quantity = 3
discountCode = 500

Myorder = "I want {} pieces of item under discount code of {} for {}dollars."
print (Myorder.format(quantity, discountCode, price))
total = price * quantity
print(f"Total price: {total}")
