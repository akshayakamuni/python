def maxx_chocolate_pieces(k):
  return (k+1)//2*(k-(k+1)//2+1)
T=int(input())
for i in range(T):
  K=int(input())
  result=max_chocolate_pieces(K)
  print(result)
