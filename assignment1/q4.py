rem_0=[]
rem_1=[]
rem_2=[]
rem_3=[]
rem_4=[]
list=[]
for i in range(1,10001):
    list.append(i)
for i in list:
    if i%5==0:
        rem_0.append(i)
    elif i%5==1:
        rem_1.append(i)
    elif i%5==2:
        rem_2.append(i)
    elif i%5==3:
        rem_3.append(i)
    elif i%5==4:
        rem_4.append(i)
print(rem_0)
print(rem_1)
print(rem_2)
print(rem_3)
print(rem_4)
if rem_0+rem_1+rem_2+rem_3+rem_4==list:
    print("equivalence class of modulo 5")
rem_0.append(rem_1)
rem_0.append(rem_2)
rem_0.append(rem_3)
rem_0.append(rem_4)
if rem_0==list:
    print("Equivalence class of modulo 5")
