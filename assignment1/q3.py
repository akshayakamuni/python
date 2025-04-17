feet=input("Enter the number of feets")
feet=int(feet)
list=[feet*12,feet/3,feet/5280,feet/304.8,feet/30.48,feet*3.281,feet/3281]

i=input("Enter the option:1.inches 2.yards3.miles4.millimeter5.centimeter6.Meter 7.kilometer")
i=int(i)
if i in range(1,7):
    print(list[i-1])
