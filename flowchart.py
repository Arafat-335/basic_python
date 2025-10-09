a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))

big_number = None
middle_number = None
small_number = None

if a > b and a > c:
    big_number = a
    if b > c:
        middle_number = b
        small_number = c
    else:
        middle_number = c
        small_number = b
else:
    if b > a and b > c:
        big_number = b
        if a > c:
            middle_number = a
            small_number = c
        else:
            middle_number = c
            small_number = a
    else:
        big_number = c
        if b > a:
            middle_number = b
            small_number = a
        else:
            middle_number = a
            small_number = b
            

print(big_number)
print(middle_number)
print(small_number )
