string = str(input("Enter a string. "))

def encode(string):
  if not string:
    return ""
  x = 1
  while x < len(string) and string[0] == string[x]:
    x += 1
  return string[0]+str(x)+encode(string[x:])
  
print(encode(string))