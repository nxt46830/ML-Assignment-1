weight=float(input("the given set of weight:"))
 #here Float() is used,float is a method that returns a floating-point number for a provided number or string
unit=input("given unit of weight:")
print("given weight is",weight,unit)
if unit.upper()=="LB": 
    converted = weight*0.45355
    unit1 = "kg"
    print("new weight is:", converted, unit1,'.')
else:
    converted = weight/0.45377
    unit2 = "pounds"
    print("New weight is:")