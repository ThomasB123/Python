dict = open("english2.txt","r")
validWords = []
for word in dict:
    count = 0
    for letter in word:
        if letter in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            count += 1
    if 3 <= count <= 16:
        validWords.append(word)
dict.close()
outputfile = open("z.txt","w")
for outword in validWords:
    outputfile.write(outword)
outputfile.close()
