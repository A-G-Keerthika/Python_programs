#	Write a Python function to return product of two numbers. If the product is greater than 500, then return their sum.

def product_or_sum(n1,n2):
  sum=0
  rem=0
  product=n1*n2
  if(product > 500):
    print("product of ",n1," and ",n2," is grater than 500 ")
    print("product of ",n1," and ",n2,"is  : ",product)
    while(product>0):
      rem = product % 10
      sum=sum+rem
      product=product//10
    print("sum of the product of ",n1,"and ",n2," is : ",sum)
  else:
    print("product of ",n1," and ",n2,"is  : ",product)

num1=int(input("enter num1 value : "))
num2=int(input("enter num2 value : "))
product_or_sum(num1,num2)
