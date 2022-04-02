#Write a Python function which counts positive and negative numbers in a given numbers.
def pncount(n,ls):
  n=0;
  p=0;
  for i in ls:
    if(i<0):
      n=n+1
    else:
      p=p+1
  print("\n-----Count of positive and negative numbers-----")
  print("number of positive numbers : ",p)
  print("number of negative numbers : ",n)

ls=[]
n=int(input("enter number of elements in a list : "))
print("enter the elements of list : ")
for i in range(0,n):
  elemt=int(input())
  ls.append(elemt)
pncount(n,ls)
