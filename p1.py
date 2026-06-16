a=(input(str("ENTER YOUR NAME ")))
print("hello",a)
b=(input(str("ENTER YOUR BREAKFAST ")))
c=(input(str("ENTER YOUR LUNCH")))
d=(input(str("ENTER YOUR DINNER")))
e=(input(str("ENTER YOUR SNACKS ")))
f=int(input("ENTER YOUR AMOUNT OF WATER DRUNK "))
g=int(input("ENTER HOURS SLEPT "))
print ("------DAILY DIET REPORT---------")
print("NAME :",a)
print("BREAKFAST :", b)
print("LUNCH :",c)
print("DINNER :",d)
print("SNACKS :",e)
print("WATER IN GLASSES :",f)
if f>8:
    print("YOU ARE HYDRATED")
else:
    print("DRINK MORE WATER")
def check_water(water):
    if water >= 8:
        return "HYDRATED"
    else:
        return "DRINK MORE WATER"  
result = check_water(f)
print(result)
print("SLEEP :",g)
if g<7:
    print("have more rest")
elif g>9 :
    print("YOU R SLEEPING TOO MUCH ")
else:
    print(" YOU R HAVING GOOD AMOUNT OF SLEEP")
print("{---END OF REPORT---")

      
