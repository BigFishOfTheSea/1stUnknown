print("welcome to my multiplication only calculator")
x = float(input("choose your first number:"))
y = float(input("choose your second number:"))
result = x * y
if result.is_integer():
    print(f"the answer is: {int(result)}")
else:
    print(f"the answer is: {result}")
