import random
length = int(input("Enter length of passwords "))
small = "abcdefghijklmnopwrstuvwxyz"
cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
no = "1234567890"
special = "@#$%^&*()_?><"
final = small + cap + no + special
password = random.sample(final , length)

a = ""
for i in password:
    a = a + i
print(a)