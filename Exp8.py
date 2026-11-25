import math

def calculate_area(shape, *args):
    if shape == "circle":
        radius = args[0]
        return math.pi * radius * radius

    elif shape == "rectangle":
        length, breadth = args
        return length * breadth

    elif shape == "triangle":
        base, height = args
        return 0.5 * base * height

    else:
        return "Invalid shape"

# Display menu
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = input("Enter your choice: ").lower()

if choice == "circle":
    r = float(input("Enter radius: "))
    print("Area of Circle:", calculate_area("circle", r))

elif choice == "rectangle":
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    print("Area of Rectangle:", calculate_area("rectangle", l, b))

elif choice == "triangle":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area of Triangle:", calculate_area("triangle", base, height))

else:
    print("Invalid choice!")