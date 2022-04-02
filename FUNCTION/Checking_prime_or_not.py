#program1 : checking a given number is a prime number/not
def prime_checker(n):
  c=0
  if n!=1:
    for i in range (1,n+1):
      if(n%i==0):
        c=c+1
  if(c==2):
    print(n," is a prime number")
  else:
    print(n," is not a prime number")

n=int(input("enter a number to check whether that is prime number or not : "))
prime_checker(n)
