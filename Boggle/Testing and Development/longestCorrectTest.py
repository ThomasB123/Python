
def longestCorrect(correct):
    length = len(correct)
    if length == 0:
        return "You didn't play any correct words."
    out = "The longest word you played was:<br>"
    if length == 1:
        return out + "<br>" + str(correct[0]) + "<br>"
    correct = sorted(correct,key=len)
    if len(correct[-1]) != len(correct[-2]):
        return out + "<br>" + str(correct[-1]) + "<br>"
    out = "The longest words you played were:<br>"
    out += "<br>" + str(correct[length-1])
    counter = 2
    while len(correct[-1]) == len(correct[length-counter]) and counter < length+1:
        out += "<br>" + str(correct[length-counter])
        counter += 1
    return out + "<br>"

correct = ['TES','CAVE','HELLO','BOL','LOB','BLOC','LAVES','OUT','SET','TUBE']
print(correct)
print(longestCorrect(correct))

