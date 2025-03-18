def print_sum(*sums):
    num1, num2 = sums
    print(f"num1: {num1}, num2: {num2}, sum:{num1+num2}")

print_sum(1+2, 2+3)

def print_mul(num1, num2):
    print(f"num1: {num1}, num2: {num2}, mul:{num1*num2}")

print_mul(2, 4)

def print_num(num1):
    print(f"num1: {num1}")
print_num(5)

def print_string():
    print("This is a string!!")

print_string()