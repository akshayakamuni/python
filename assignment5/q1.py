def maximal_xor(L,R):
  max_xor=0
  for i in range(L,R+1):
    for j in range(i,R+1):
      max_xor=max(max_xor,i^j)
  return max_xor
L=int(input())
R=int(input())
result=maximal_xor(L,R)
print(result)
