while True: 
    try:
        Hight = float(input("Hur Inte kortt är du i centimeter: "))
        break
    except:
        print("Bara gör rätt nu okej")
        continue

while True: 
    try:
        Weight = float(input("Hur mycket väger du i Kilogram: "))
        break
    except:
        print("Bara gör rätt nu okej")
        continue

while True: 
    try:
        r = int(input("radien på en cirkel: "))
        break
    except:
        print("Bara gör rätt nu okej")
        continue

while True: 
    try:
        AT = int(input("Antal tärningar: "))
        break
    except:
        print("Bara gör rätt nu okej")
        continue

if Hight >= int(160):
    print("Du är tillräkligt long")
else:
    print("Du är inte tillräkligt long")

print("BMI:", Weight/(Hight/100)**2)


print("Cirkelns aria:", r**2*3.14)

print("Tärningar:")

import random

for i in range(0, AT):
    print(random.randint(1, 6))