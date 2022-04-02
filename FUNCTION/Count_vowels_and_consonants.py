#Write a Python function which counts vowels and consonant in a word.

def count(s):
  v=0
  c=0
  for i in s:
    if((i=='a') or (i=='e') or (i=='i') or (i=='o') or (i=='u') or(i=='A') or (i=='E') or (i=='I') or(i=='O') or (i=='U')):
      v=v+1
    else:
      c=c+1
  print("\n-----Count of vowels and consonents-----")
  print("number of vowels : ",v)
  print("number of consonents : ",c)

s=str(input("enter a string to count vowels and consonants in it : "))
count(s)
