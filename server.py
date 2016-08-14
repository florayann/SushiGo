import sys
import random
import argparse


class Deck(object):
    def _init_(self, players):
        self.cards = ["tempura"] * 14 + ["sashimi"] * 14 + ["dumpling"] * 14 + ["maki2"] * 12 + ["maki3"] * 8 + ["maki1"] * 6 + ["salmon nigiri"] * 10 + ["squid nigiri"] * 5 + ["egg nigiri"] * 5 + ["pudding"] * 10 + ["wasabi"] * 6 + ["chopsticks"] * 4

        if players == 2
            self.number = 10
        elif players == 3
            self.number = 9
        elif players == 4
            self.number = 8
        else
            self.number = 7
        random.shuffle(self.cards)        
        self.start_index = 0

    def draw():
        r = self.cards[self.start_index, self.start_index + self.number - 1]
        self.start_index += self.number
        return r

class Player(object):
    def _init_(self, deck):
        self.hand = deck.draw()
        self.eaten = Dishes()
        self.score = 0
        self.puddings = 0
        self.makis = 0

    def get_puddings():
        return self.puddings

    def get_makis():
        return self.makis
        
    def turn(hand):
        display(hand)
        i = self.hand.index(card)
        if card == "pudding"
            self.puddings += 1
        elif card == "maki 1"
            self.makis += 1
        elif card == "maki 2"
            self.makis += 2
        elif card == "maki 3"
            self.makis += 3
        else
            self.eaten.add_card(card, wasabi, hand)
        del self.hand[i]
        return self.hand

    def swap(new_hand):
        old_hand = self.hand
        self.hand = new_hand
        return old_hand

    def end_round(deck):
        self.score += self.eaten.calculate_score()
        total_makis = self.makis
        self.makis = 0
        self.eaten = Dishes()
        self.hand = deck.draw()
        return (self.score, total_makis)
    

class Dishes():
    def _init_(self):
        self.dishes = []

    def add_card(input, wasabi, deck):
        if(input in deck)
            if wasabi && ()

            else
                self.dishes.append(input)
                return True
        else return False
        
    def calculate_score():
        sum = 0
        for dish in self.dishes
            sum += dish.points()
        return sum
        

class Nigiri():
    def _init_(self, dish):
        if nigiri == "squid nigiri":
            point = 3
        elif nigiri == "salmon nigiri":
            point = 2
        if nigiri == "egg nigiri":
            point = 1
        
    def points():
        return point

class Dumpling(Dish):
    def _init_(self):
        count = 1

    def add_card():
        count += 1

    def points():
        if count = 1
            return 1
        elif count = 2
            return 3
        elif count = 3
            return 6
        elif count = 4
            return 10
        else
            return 15
        
        
class Sashimi(Dish):
    def _init_(self):
        count = 1

    def add_card():
        if count == 3
            return False
        else
            count += 1
            return True

    def points():
        if count == 3
            return 10
        else return 0

            
class Tempura(Dish):
    def _init_(self):
        count = 1
        
    def add_card():
        if count == 2
            return False
        else
            count += 1
            return True

    def points():
        if count == 2
            return 5
        else return 0
    

class Wasabi(Dish):
    def _init_(self):
        egg = False
        salmon = False
        squid = False

    def add_card(nigiri):
        if !(egg || salmon || squid)
            if nigiri == "squid nigiri"
                squid = True
                return True
            if nigiri == "salmon nigiri"
                salmon = True
                return True
            if nigiri == "egg nigiri"
                egg = True
                return True
            else
                return False
        else
            return False

    def points():
        if egg
            return 3
        if salmon
            return 6
        if squid
            return 9
        return 0

class Game():
    def _init_(self, numplayers):
        deck = Deck(numplayers)
        players = []
        for range(0, numplayers):
            players.append(Player())


            
        
        
        
               
    
        


def main():
    pass

if __name__ == "__main__":
    main()

    
