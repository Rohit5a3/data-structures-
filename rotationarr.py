t=int(input())
while t!=0:
 n,k=list(map(int,input().split()))
 arr=list(map(int,input().split()))
 index=n-(k%n)
 for i in range(index,n):
  print (arr[i],)
 for i in range(index):
  print (arr[i],)
 t-=1