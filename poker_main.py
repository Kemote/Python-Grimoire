import random

class Player: #klasa trzymajaca info o graczu
   def __init__(self, name, chips, AI = False):
       self.name = name
       self.AI = AI
       self.in_game = True #ta wlasnosc bedzie sprawdzana aby potiwerdzic czy gracz jest nadal w grze
       self.chips = chips
       self.__cards = []

   def deal(self, deck):            #metoda pozwalająca wylosować kart dla gracza z obecnej talii
       self.__cards = deck.deal(3) #jak to teksas zawsze losuje się na początek 3 karty

   @property
   def cards_remove(self):
       self.__cards = []

   @property
   def cards(self):
       cards_on_hands = []
       for i in range(3):
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
           return True #pozawala wyjść z funkcji gdy brakuje kart
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
   def __init__(self, deck, *args):
       self.players = (args) #przekonwertuje tuple na liste, arg podaje argumenty w psotaci tupli warotsci tupli nie da sie edytowac
       self.deck = deck
       self.pool = 0
       self.cards_on_stool = ()

   def check_poker_hand(self):
       def check_streight:




print("===|POKEROWA SUPER GRA|===|A||K||Q||J|===" + "\n")
name = input("Player name:")
player_one = Player(name, 1000)
print("Hi " + name + " you have 1000 chips to play with my bot")



#konies testowego modulu rozgrywki dla dwych graczy----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------testyyy
#talia = Deck()
#buszmen = Player('buszmen', 1000)
#buszmen.deal(talia)
#print(buszmen.cards)




#for i in range(0,52):
#   print(talia.cards[i].color, talia.cards[i].figure,talia.cards[i].state_hand)
