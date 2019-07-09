#TEST SYNC

list = [['hearts', 'J'],['vfs','2'],['hearts','2'],['hearts', 'Q'],['hearts', '10'],['spades','5'],['spades','7']]

for i in list:
   if i[1] == 'A':
       i[1] = '1'
   elif i[1] == 'J':
       i[1] = '11'
   elif  i[1] == 'Q':
       i[1] = '12'
   elif i[1] == 'K':
       i[1] = '13'

def check_high(cards):
    high = [int(i[1]) for i in cards]
    if min(high) == 1:
        return True, 14, "High card"
    return True, max(high), "High card"


def check_one_pair(cards):
   pair = [int(i[1]) for i in cards]
   for i in range(len(pair)):
       if pair[i] == 1:
           pair[i] = 14
   pair.sort()
   pair.reverse()
   for i in pair:
       if pair.count(i) == 2:
           return True, i, "Pair"
   return False, 0, "None"

#na bank poprawic szyszukiwania dwuch par!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def check_two_pairs(cards):
   first_pair = check_one_pair(cards)
   if first_pair[0]:
       for i in cards:
           if i[1] == first_pair[1]:
               cards.remove(i)
       if first_pair[1] == '14':
           for i in cards:
               if i[1] == '1':
                   cards.remove(i)
       cards.reverse()
       sec_pair = check_one_pair(cards)
       if sec_pair[0]:
           return first_pair, sec_pair, "Two pair"
   return False, 0, "None"

def check_three_kind(cards):
   kind = [str(i[1]) for i in cards]
   kind.sort()
   for i in kind:
       if kind.count(i) == 3:
           if int(i) == 1: i = 14
           return True, i, "Three of kind"
   return False, 0, "None"

def check_streight(cards):
   streight = [int(i[1]) for i in cards]

   for i in streight:
       if streight.count(i) != 1:
           streight.remove(i)
   streight.sort()
   print(streight)
   if len(streight) < 5:
       return False, 0, "None"
   for i in range(len(streight) - 4):
       if streight[-i] - streight[-i-4] == 4:
           return True, streight[-i], "Streight"
   if streight[-1] - streight[-4] == 3 and streight[0] == 1:
       return True, 14, "Streight"

   return False, 0

def check_flush(cards):
   color = [i[0] for i in cards]
   for i in ['spades','hearts','clubs','diamonds']:
       if color.count(i) >= 5:
           return True, i, "Flush"
   return False, 0, "None"

def check_full_house(cards):
   three = check_three_kind(cards)
   if three[0]:
       for i in cards:
           if i[1] == three[1]:
               cards.remove(i)
       if three[1] == '14':
           for i in cards:
               if i[1] == '1':
                   cards.remove(i)
       three_2 = check_three_kind(cards)
       if three_2[0]:
           return True, three, three_2, "Full house"
       pair = check_one_pair(cards)
       if pair[0]:
           return True, three, pair, "Full house"
   return False, 0, "None"

def check_four_of_kind(cards):
   kind = [str(i[1]) for i in cards]
   kind.sort()
   for i in kind:
       if kind.count(i) == 4:
           if int(i) == 1: i = 14
           return True, i, "Four of kind"
   return False, 0, "None"

def check_poker(cards):
    def check():
        for i in range(1, 3):
            if (int(cards[-i][1]) - int(cards[-i-4][1]) == 4 and check_flush(cards[-i-4:-i])):
                return True, cards[-i][1], "Streight flush"
        return False, 0, "None"
    cards = sorted(cards, key = lambda x: int(x[1]))
    result = check()
    if result[0]:
        return result
    for i in cards:
        if i[1] == "1":
            i[1] = "14"
    cards = sorted(cards, key = lambda x: int(x[1]))
    result = check()
    return result

def check_hand(cards):
    if check_poker(cards)[0]:
        return check_poker(cards)
    if check_four_of_kind(cards)[0]:
        return check_four_of_kind(cards)
    if check_full_house(cards)[0]:
        return check_full_house(cards)
    if check_flush(cards)[0]:
        return check_flush(cards)
    if check_streight(cards)[0]:
        return check_streight(cards)
    if check_three_kind(cards)[0]:
        return check_three_kind(cards)
    if check_two_pairs(cards)[0]:
        return check_two_pairs(cards)
    if check_one_pair(cards)[0]:
        return check_one_pair(cards)
    if check_high(cards)[0]:
        return check_high(cards)

test = check_hand(list)
print("wynik to", test)