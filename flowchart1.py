a = int(input("enter your number"))
b = int(input("enter your number"))
c = int(input("enter your number"))
d = int(input("enter your number"))
e = int(input("enter your number"))

first_number = None
second_number = None
third_number = None
fourth_number = None
Fifth_number = None

if a>b and a>c and a>d and a>e:
    first_number = a
    if b>c and b>d and b>e:
        second_number = b
        if c>d and c>e:
            third_number = c
            if d>e:
                fourth_number = d
                Fifth_number = e
            else:
                fourth_number = e
                Fifth_number = d

elif b>c and b>d and b>e and b>a:
    first_number = b
    if c>d and c>e and c>a:
        second_number = c
        if d>e and d>a:
            third_number = d
            if e>a:
                fourth_number = e
                Fifth_number = a
            else:
                fourth_number = a
                Fifth_number = e


print(first_number)
print(second_number)