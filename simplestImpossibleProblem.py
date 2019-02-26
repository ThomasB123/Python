def impossible(x, count):
  if x != 1:
    count += 1
    if x % 2 == 0:
      x /= 2
      return impossible(x, count)
    if x % 2 == 1:
      x = x*3 + 1
      return impossible(x, count)
  else:
    return 'Found it!', count
for x in range(1,101):
  count = 0
  print (x, impossible(x, count))