#Write a Python function to print number ranging from 1 to 25 but excluding number which are the multiples of 5.

def num(sl,el):
  print("numbers ranging from ",sl," to ",el," excluding numbers which are the multiples of 5 :")
  for i in range(sl,el+1):
    if(i%5 != 0):
      print(i)

sl=int(input("enter the starting limit : "))
el=int(input("enter the ending limit : "))
num(sl,el)
