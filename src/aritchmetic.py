def aritchmetic(x, operation, y):
    sum = 0
    if operation == "+":
        sum =  x + y
    elif operation == "-":
        sum = x - y
    elif operation == "*":
        sum = x * y
    elif operation == "/":
        sum = x / y
    else: "Unknow operation"
    return sum
x = int(input())
operation = input()
y = int(input())
print(aritchmetic(x, operation, y))