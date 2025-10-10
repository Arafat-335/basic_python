# 3 input flowchart

# a = int(input("enter your number: "))
# b = int(input("enter your number: "))
# c = int(input("enter your number: "))

# fast_number = None
# second_number = None
# third_number = None

# if a>b and a>c:
#     fast_number = a
    
#     if b>c:
#         second_number = b
#         third_number = c
#     else:
#         second_number = c
#         third_number = b
        
# else:
#     if b>c and b>a:
#         fast_number = b
        
#         if a>c:
#             second_number = a
#             third_number = c
#         else:
#             second_number = c
#             third_number = a
#     else:
#         fast_number = c
#         if a>b:
#             second_number = a
#             third_number = b
#         else:
#             second_number = b
#             third_number = a
            
# print(fast_number)
# print(second_number)
# print(third_number)


# 4 input flowchart
a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))
d = int(input("Enter your number: "))

first_number = None
second_number = None
third_number = None
fourth_number = None


if a > b and a > c and a > d:
    first_number = a
    if b > c and b > d:
        second_number = b
        if c > d:
            third_number = c
            fourth_number = d
        else:
            third_number = d
            fourth_number = c
    elif c > b and c > d:
        second_number = c
        if b > d:
            third_number = b
            fourth_number = d
        else:
            third_number = d
            fourth_number = b
    else:
        second_number = d
        if b > c:
            third_number = b
            fourth_number = c
        else:
            third_number = c
            fourth_number = b

elif b > a and b > c and b > d:
    first_number = b
    if a > c and a > d:
        second_number = a
        if c > d:
            third_number = c
            fourth_number = d
        else:
            third_number = d
            fourth_number = c
    elif c > a and c > d:
        second_number = c
        if a > d:
            third_number = a
            fourth_number = d
        else:
            third_number = d
            fourth_number = a
    else:
        second_number = d
        if a > c:
            third_number = a
            fourth_number = c
        else:
            third_number = c
            fourth_number = a

elif c > a and c > b and c > d:
    first_number = c
    if a > b and a > d:
        second_number = a
        if b > d:
            third_number = b
            fourth_number = d
        else:
            third_number = d
            fourth_number = b
    elif b > a and b > d:
        second_number = b
        if a > d:
            third_number = a
            fourth_number = d
        else:
            third_number = d
            fourth_number = a
    else:
        second_number = d
        if a > b:
            third_number = a
            fourth_number = b
        else:
            third_number = b
            fourth_number = a

else:
    first_number = d
    if a > b and a > c:
        second_number = a
        if b > c:
            third_number = b
            fourth_number = c
        else:
            third_number = c
            fourth_number = b
    elif b > a and b > c:
        second_number = b
        if a > c:
            third_number = a
            fourth_number = c
        else:
            third_number = c
            fourth_number = a
    else:
        second_number = c
        if a > b:
            third_number = a
            fourth_number = b
        else:
            third_number = b
            fourth_number = a


print(first_number)
print(second_number)
print(third_number)
print(fourth_number)