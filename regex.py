import re

inpString=input("please enter a string")

pattern=r"()"

matchString=re.search(pattern,inpString)

if matchString:
  print("match")
else:
  print("not valid")



#Car Registration

pattern=r"([A-HJ-PR-Y]{2})([0-9]{2})([A-HJ-PR]{3})"

#Postcode

pattern=r"([A-Z]{2})([0-9]{2})(\ )([0-9])([A-Z]{2})"