##########     Binary, Denary, Hex Converter      ##########

def get_binary():
  binstring = ""
  for x in range (8):
    while len(binstring) != 8 or binstring[x] not in "01":
      binstring = input ("Enter a 8 bit string > ")
  return binstring

def get_denary():
  den = -1
  while den < 0 or den > 255:
    den = int(input("Enter a denary number > "))
  return den

def get_hex():
  hex = ""
  for x in range (2):
    while len(hex) != 2 or hex[x] not in "0123456789ABCDEFabcdef":
      hex = input ("Enter a 2 character hex string > ")
  return hex

def binary_to_denary(binstring):
  commonvalue = 128
  out = 0
  for x in range(8):
    out += commonvalue * binstring[x]
    commonvalue /= 2
  return int(out)

def denary_to_binary(den):
  commonvalue = 128
  out = ""
  for x in range(8):
    if den >= commonvalue:
      out += "1"
      den -= commonvalue
    else:
      out += "0"
    commonvalue /= 2
  return out

def hex_to_denary(hex):
  values = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}
  first = values[hex[0]]
  second = values[hex[1]]
  den = first*16 + second
  return den

def denary_to_hex(den):
  values = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}
  inverse = {v:k for k,v in values.items()}
  first = den // 16
  second = den % 16
  char1 = inverse[first]
  char2 = inverse[second]
  return char1 + char2

def binary_to_hex(bin):
  denary = binary_to_denary(bin)
  hexidecimal = denary_to_hex(denary)
  return hexidecimal

def hex_to_binary(hex):
  denary = hex_to_denary(hex)
  binary = denary_to_binary(denary)
  return binary

def menu():
  print ('''Welcome to the Convertor
  Please choose an option
  1. Binary to denary
  2. Denary to binary
  3. Hex to denary
  4. Denary to hex
  5. Binary to hex
  6. Hex to binary
  q. Quit''')
  choice = ""
  while choice.upper() != "Q":
    choice = input ("Your choice > ")
    if choice == "1":
      bin = get_binary()
      print (binary_to_denary(bin))
    if choice == "2":
      den = get_denary()
      print (denary_to_binary(den))
    if choice == "3":
      hex = get_hex()
      print (hex_to_denary(hex))
    if choice == "4":
      den = get_denary()
      print (denary_to_hex(den))
    if choice == "5":
      bin = get_binary()
      print(binary_to_hex(bin))
    if choice == "6":
      hex = get_hex()
      print(hex_to_binary(hex))
  print ("Goodbye!")
menu()
