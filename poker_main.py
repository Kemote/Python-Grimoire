import random

class Player: #klasa trzymajaca info o graczu
   def __init__(self, name, chips, AI = False):
       self.name = name
       self.AI = AI
       self.in_game = True #ta wlasnosc bedzie sprawdzana aby potiwerdzic czy gracz jest nadal w grze
       self.chips = chips
       self.__cards = []

   def deal(self, deck):            #metoda pozwalająca wylosować kart dla gracza z obecnej talii
       self.__cards = deck.deal(2) #jak to teksas zawsze losuje się na początek 3 karty

   @property
   def cards_remove(self):
       self.__cards = []

   @property
   def cards(self):
       cards_on_hands = []
       for i in range(2):
           cards_on_hands.append([self.__cards[i].color,self.__cards[i].figure])
       return cards_on_hands

class Card: #klasa odpowiedzialna za przetrzymywanie info o kartach
   def __init__(self, color, figure):
       self.__color = color
       self.__figure = figure
       self.__state_hand = False #ta statystyka bedzie mowic czy karta jwest w rece jakiegos gracza

   @property #ten dekorador pozwala na tworzenie obiektów
   def color(self):
       return self.__color

   @property
   def figure(self):
       return self.__figure

   @property
   def state_hand(self):
       return self.__state_hand

   @state_hand.setter
   def state_hand_set(self, val):
       self.__state_hand = val

class Deck: #klasa odpowiedzialna za tworzenie talii
   def __init__(self):
       colors = ("spades", "hearts", "clubs","diamonds")  # w sumie nie ma sensu robić ich prywatnymi gdyż i tk jest to potrzebne tylkow czasie tworzenia obietku talii
       figures = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
       tmp_deck = []
       tmp = []
       rand = random.randint(0,51)
       self.__cards = []   #karty w talii
       self.__cards_in_game = 0 #okrsla ilos kart w grze

       for col in colors:
           for fig in figures:
               self.__cards.append(Card(col,fig)) # towrzy liste z obiektami klasy Card można się dostać do kart używając gettera cards np nazwaobiektuDeck.cards[3].color

       for i in range(0,52):
           while rand in tmp:
               rand = random.randint(0, 51)
           tmp_deck.append(self.__cards[rand])
           tmp.append(rand)
       self.__cards = tmp_deck

   @property
   def cards(self):
       return self.__cards

   def deal(self, num_cards):  #odpowiada za rozdanie kart graczom, zamysl jest taki zeby podawac ilosc kart w locie
       if self.__cards_in_game + num_cards > 52:
           print("Koniec talii")
           return False #pozawala wyjść z funkcji gdy brakuje kart
       _hand = []
       for i in range(num_cards):
           self.__cards[self.__cards_in_game].state_hand_set = True #zaznacza w tali, ze karta w grze
           _hand.append(self.__cards[self.__cards_in_game])
           self.__cards_in_game += 1
       return _hand

   def shufle(self):   #----------------------------------dorobić metode tasowania tali i jej zerowania po turz!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
       a = True

#testowy modul rozgrywki dla dwych graczy----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Stool:
   def __init__(self, *args):
       self.players = (args) #przekonwertuje tuple na liste, arg podaje argumenty w psotaci tupli warotsci tupli nie da sie edytowac
       #self.deck = deck
       self.pool = 0
       self.cards_on_stool = []

   def deal(self, deck, x):
       self.cards_on_stool += deck.deal(x)

   def cards(self): #jako,ze ta funkcja się powtarza mozna sprobowac jako dekorator
       cards_on_hands = []
       for i in range(len(self.cards_on_stool)):
           cards_on_hands.append([self.cards_on_stool[i].color, self.cards_on_stool[i].figure])
       return cards_on_hands

   def check_poker_hand(self, player):
       print(self.players[player].cards)
       print(str(self.cards()))
       cards = self.players[player].cards + self.cards()
       print("test takie kary sprawdzane " + str(cards))
       for i in cards:
           if i[1] == 'A':
               i[1] = '1'
           elif i[1] == 'J':
               i[1] = '11'
           elif i[1] == 'Q':
               i[1] = '12'
           elif i[1] == 'K':
               i[1] = '13'

       def check_high(cards):
           print("CARDS " + str(cards))
           high = [int(i[1]) for i in cards]
           print("HIGH", high)
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

       # na bank poprawic szyszukiwania dwuch par!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
       def check_two_pairs(cards):
           two_pairs = cards
           #print("first pari", two_pairs)
           first_pair = check_one_pair(two_pairs)
           if first_pair:
               for i in two_pairs:
                   #print(i[1], first_pair[1])
                   if int(i[1]) == int(first_pair[1]):
                       #print("T")
                       two_pairs.remove(i)
               if first_pair[1] == '14':
                   for i in two_pairs:
                       if i[1] == '1':
                           two_pairs.remove(i)
               #cards.reverse()
               #print("secon pari", two_pairs)
               sec_pair = check_one_pair(two_pairs)
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
           if len(streight) < 5:
               return False, 0, "None"
           for i in range(len(streight) - 4):
               if streight[-i] - streight[-i - 4] == 4:
                   return True, streight[-i], "Streight"
           if streight[-1] - streight[-4] == 3 and streight[0] == 1:
               return True, 14, "Streight"

           return False, 0

       def check_flush(cards):
           color = [i[0] for i in cards]
           for i in ['spades', 'hearts', 'clubs', 'diamonds']:
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
                   #print("-----------------------------------------------------")
                   #print(check_streight(cards[-i - 4:-i])[0])
                   #print(check_flush(cards[-i - 4:-i])[0])
                   #print("-----------------------------------------------------")
                   if check_streight(cards[-i - 4:-i])[0] and check_flush(cards[-i - 4:-i])[0]:
                       return True, cards[-i][1], "Streight flush"
               return False, 0, "None"

           cards = sorted(cards, key=lambda x: int(x[1]))
           result = check()
           if result[0]:
               return result
           for i in cards:
               if i[1] == "1":
                   i[1] = "14"
           cards = sorted(cards, key=lambda x: int(x[1]))
           result = check()
           return result

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



#testowa rozgrywka--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print("===|POKEROWA SUPER GRA|===|A||K||Q||J|===" + "\n")
#name = input("Player name:")    making player is last thing to do
#player_one = Player(name, 1000)

player0 = Player("Kemote",1000)
player1 = Player("Alehandro", 1000)
talia0 = Deck()

player0.deal(talia0)
player1.deal(talia0)

print("Hi " + player0.name + " and " + player1.name +" you booth have 1000 chips to play \n")

game0 = Stool(player0, player1)
print(player0.name + " cards " + str(player0.cards))
print(player1.name + " cards " + str(player1.cards) + "\n")

game0.deal(talia0, 5)

print("Karta na stole " + str(game0.cards()) + "\n")
print(game0.check_poker_hand(0))


#konies testowego modulu rozgrywki dla dwych graczy----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------testyyy
#talia = Deck()
#buszmen = Player('buszmen', 1000)
#buszmen.deal(talia)
#print(buszmen.cards)




#for i in range(0,52):
#   print(talia.cards[i].color, talia.cards[i].figure,talia.cards[i].state_hand)
