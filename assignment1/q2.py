import random
list=[]
for i in range(101):
     list.append(random.randint(0,1))
print(list)
zero_count=0
max_zero_count=0
for i in range(len(list)):
     if list[i]==0:
          zero_count+=1
     if list[i]==1:
          if zero_count>max_zero_count:
               max_zero_count=zero_count
          zero_count=0
print(max_zero_count)
