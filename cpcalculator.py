#Python compound interest calculator
principle=float(input("Enter your principle amount:"))
rate=float(input("Enter your interest rate:"))
time=float(input("Enter the time in years:"))

while principle<=0:
    principle=float(input("Enter your principle amount:"))
    if principle<=0:
        print("Principle amount can't be less than or equal to zero.")
while rate<=0:
    rate=float(input("Enter your interest rate:"))
    if rate<=0:
        print("Rate can't be less than or equal to zero.")
while time<=0:
    time=float(input("Enter the time in years:"))
    if time<=0:
        print("Time can't be less than or equal to zero.")

total=principle*pow((1+rate/100),time)

print(f"Balance after {time} year/s:{total}")