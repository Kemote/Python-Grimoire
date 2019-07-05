list = [['pike', '5'],['hearts','A'],['hearts','3'],['spades', '4'],['spades', '2'],['hearts','5'],['hearts','7']]

for i in list:
   if i[1] == 'A':
       i[1] = '1'
   elif i[1] == 'J':
       i[1] = '11'
   elif  i[1] == 'Q':
       i[1] = '12'
   elif i[1] == 'K':
       i[1] = '13'

def check_flush(cards):
   color = [i[0] for i in cards]
   for i in ['spades','hearts','clubs','diamonds']:
       if color.count(i) >= 5:
           return True, i
   return False, 0

def check_streight(cards):
   #streight = [int(i[1]) for i in cards]
   #streight.sort()
   #streight = dict.fromkeys(streight)
   streight = []
   figures = []

   for i in cards:
       if i not in streight:
           streight.append(i)

   print(streight)
   if len(streight) < 5:
       return False
   for i in range(len(streight) - 4):
       True
   #tutaj pętle sprawdzającą możliwości strita porzadnie zrobiona ta moze miec pomylki


   return False, 0

def check_four_of_kinds(cards):
   kind = [str(i[1]) for i in cards]
   kind.sort()
   for i in kind:
       if kind.count(i) == 4:
           if int(i) == 1: i = 14
           return True, str(i)
   return False, 0

def check_one_pair(cards):
   pair = [int(i[1]) for i in cards]
   for i in range(len(pair)):
       if pair[i] == 1:
           pair[i] = 14
   pair.sort()
   pair.reverse()
   for i in pair:
       if pair.count(i) == 2:
           return True, str(i)
   return False, 0

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
           return first_pair, sec_pair
   return False, 0

def check_three_kind(cards):
   kind = [str(i[1]) for i in cards]
   kind.sort()
   for i in kind:
       if kind.count(i) == 3:
           if int(i) == 1: i = 14
           return True, str(i)
   return False, 0

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
           return True, three, three_2
       pair = check_one_pair(cards)
       if pair[0]:
           return True, three, pair
   return False



test = check_streight(list)
print("wynik to", test)