from pygame_functions import *

screenSize(800,800)
setBackgroundColour("white")


time = makeLabel("You are out of time",60,100,100)
showLabel(time)

score = makeLabel("Your final score was: 14",30,100,250)
showLabel(score)

endWait()
