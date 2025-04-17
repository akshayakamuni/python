def find_next_permutation(w):
  n=len(w)
  w_list=list(w)
  i=n-2
  while i>=0 and w_list[i]>=w_list[i+1]:
    i-=1
  if i<0:
    return "no answer"
  j=n-1
  while w_list[j]<=w_list[i]:
    j-=1
  w_list[i],w_list[j]=w_list[j],w_list[i]
  w_list[i+1:]=sorted(w_list[i+1:])
  return "".join(w_list)

t=int(input())
for i in range(t):
  w=input().strip()
  result=find_next_permutation(w)
  print(result)
