Gravity_Earth = 9.81
Gravity_Moon = 1.62

Mass = float(input("Enter a mass of object:"))

Weight_Earth = Mass * Gravity_Earth
Weight_Moon = Mass * Gravity_Moon

print(f"Weight of object on Earth is {Weight_Earth:.2f} N ")
print(f"Weight of object on Moon is {Weight_Moon:.2f} N ")