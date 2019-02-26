class TCard():
    def __init__(self):
        self.Suit = 0
        self.Rank = 0

Deck = [None]
Choice = ''

def GetRank(RankNo):
    Rank = ''
    if RankNo == 1:
        Rank = 'Ace'
    elif RankNo == 2:
        Rank = 'Two'
    elif RankNo == 3:
        Rank = 'Three'
    elif RankNo == 4:
        Rank = 'Four'
    elif RankNo == 5:
        Rank = 'Five'
    elif RankNo == 6:
        Rank = 'Six'
    elif RankNo == 7:
        Rank = 'Seven'
    elif RankNo == 8:
        Rank = 'Eight'
    elif RankNo == 9:
        Rank = 'Nine'
    elif RankNo == 10:
        Rank = 'Ten'
    elif RankNo == 11:
        Rank = 'Jack'
    elif RankNo == 12:
        Rank = 'Queen'
    elif RankNo == 13:
        Rank = 'King'
    return Rank

def GetSuit(SuitNo):
    Suit = ''
    if SuitNo == 1:
        Suit = 'Clubs'
    elif SuitNo == 2:
        Suit = 'Diamonds'
    elif SuitNo == 3:
        Suit = 'Hearts'
    elif SuitNo == 4:
        Suit = 'Spades'
    return Suit

def DisplayCard(ThisCard):
    print()
    print('Card is the', GetRank(ThisCard.Rank), 'of', GetSuit(ThisCard.Suit))
    print()

Count = 0
def GetCard(ThisCard, Deck, Count):
    Suit = [1, 3, 2, 4, 1, 2, 1, 1, 1, 3, 3, 3, 3, 3, 2, 3, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 3, 3, 3, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 1, 4, 4]
    Rank = [1, 2, 2, 2, 3, 3, 4, 6, 5, 4, 5, 6, 7, 8, 12, 9, 4, 5, 6, 7, 13, 8, 9, 10, 11, 12, 10, 11, 12, 7, 8, 9, 1, 4, 5, 6, 7, 10, 11, 12, 13, 8, 9, 10, 11, 1, 3, 13, 1, 2, 3, 13]
    ThisCard.Suit = int(Suit[Count])
    ThisCard.Rank = int(Rank[Count])
    Count += 1

def IsNextCardHigher(LastCard, NextCard):
    Higher = False
    if NextCard.Rank > LastCard.Rank:
        Higher = True
    if (NextCard.Rank == LastCard.Rank) and (NextCard.Suit > LastCard.Suit):
            Higher = True
    return Higher


def GetChoiceFromUser():
    Choice = input('Is it higher than the last one? (enter y or n) Play a Joker? (enter j)')
    return Choice

def DisplayEndOfGameMessage(Score):
    print()
    print('GAME OVER!')
    print('Your score was', Score)
    if Score == 51:
        print('WOW! You completed a perfect game.')
    print()

def DisplayCorrectGuessMessage(Score):
    print()
    print('Well done! You guessed correctly.')
    print('Your score is now ', Score, '.', sep='')
    print()


def PlayGame(Deck):
    LastCard = TCard()
    NextCard = TCard()
    GameOver = False
    GetCard(LastCard, Deck, Count)
    DisplayCard(LastCard)
    NoOfCardsTurnedOver = 1
    NoOfJokers = 0
    while (NoOfCardsTurnedOver < 52) and (not GameOver):
        GetCard(NextCard, Deck, NoOfCardsTurnedOver)
        Choice = ''
        while (Choice != 'y') and (Choice != 'n') and (Choice != 'j'):
            Choice = GetChoiceFromUser()
        while (Choice == 'j' and NoOfJokers > 1):
            Choice = GetChoiceFromUser()
        if Choice == 'j':
            NoOfJokers += 1
        DisplayCard(NextCard)
        NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
        Higher = IsNextCardHigher(LastCard, NextCard)
        if (Higher and Choice == 'y') or (not Higher and Choice == 'n') or (Choice == 'j'):
            DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
            LastCard.Rank = NextCard.Rank
            LastCard.Suit = NextCard.Suit
        else:
            GameOver = True
    if GameOver:
        DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    else:
        DisplayEndOfGameMessage(51)

PlayGame(Deck)