total = float(input("How much was the bill?"))
tip = [1.00 , 1.15 , 1.20 , 1.25]
service = input("How's the service? (Bad, Normal, Good, Fantastic)")
print("The bill is $")
if service == "Bad":
    print (tip[0]*total)
elif service == "Normal":
    print (tip[1]*total)
elif service == "Good":
    print (tip[2]*total)
elif service == "Fantastic":
    print (tip[3]*total)