import math

print("*notice that the answer will always show up in cm^2")

# take the user inputs for 2 sides of the triangle

a = float(input("Ente the value of A:"))
b = float(input("Ente the value of B:"))

# now we calculate the value of the other side known as 'c' using math library

c = math.sqrt(pow(a, 2) + pow(b, 2))

# now we print the value of 'c' and round the value so that it looks good!

print(f"The value of C is:{round(c, 2)}cm^2")
