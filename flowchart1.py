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
a = int(input("enter your number: "))
b = int(input("enter your number: "))
c = int(input("enter your number: "))
d = int(input("enter your number: "))

fast_number = None
second_number = None
third_number = None
fourth_number = None

if a>b and a>c and a>d:
    fast_number = a
    if b>c and b>d:
        second_number = b
        if c>d:
            third_number = c
            fourth_number = d
        else:
            third_number = d
            fourth_number = c
            
else:
   if b>a and b>c and b>d:
       fast_number = b
       if a>c and a>d:
           second_number = a
           if a>c:
                third_number = a
                fourth_number = d
           else:
                third_number = d
                fourth_number = a
               
print(fast_number)
print(second_number)
print(third_number)
print(fourth_number)