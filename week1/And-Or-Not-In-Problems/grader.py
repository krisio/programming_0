pts = input("Enter test points:")
pts = int(pts)

if pts>=0 and pts<=50:
    print("Slab 2")
elif pts>=51 and pts<=60:
    print("Sreden 3")
elif pts>=61 and pts<=70:
    print("Dobyr 4")
elif pts>=71 and pts<=80:
    print("Mn Dobyr 5")
elif pts>=81 and pts<=99:
    print("Otlichen 6")
elif pts==100:
    print("Mnogo otlichen 7")
else:
    print("Nevalidni tochki")
