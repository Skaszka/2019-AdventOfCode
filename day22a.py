#!/usr/bin/python3


def reverse_stack(card_position, deck_size):
        return (deck_size-card_position)

def deal_increment(card_position, deck_size, num_increment):
        return ((card_position*num_increment)%(deck_size+1))      # need to off by one for...whatever reason


def cut_stack(card_position, deck_size, num_cut):
        
        stop_at = num_cut    # if cut 3, then cut 0 1 2 from 3 4 5 ...
        if num_cut < 0:
                stop_at = deck_size+1+num_cut   # if cut -3 on 10, cut 7 8 9 from ... 5 6... cut at 7
                
        # the important thing to remember here is that stop_at is the first position on the right half!
        
        if card_position>=stop_at:
                card_position = card_position-stop_at              # if cut 3, and card was at 4, it is now at 1 (and former 3 at 0)
        elif card_position<stop_at:
                card_position = deck_size - (stop_at-card_position-1)    # if cut 3 on deck 0-9, and card was at 2, card now at 9
                                                                        # if card was at 0, now at 7                        
        return card_position

if __name__ == "__main__":

        input = open("input/day22.txt")
        
        card_position = 2019
        deck_size = 10007 - 1   # technically, deck_size is the max position, aka deck size - 1

        lines = []
        
        for line in input:
                lines.append(line[:-1])
                
                
        
        for line in lines:
                if 'deal into new stack' in line:
                        card_position = reverse_stack(card_position, deck_size)
                elif 'deal with increment' in line:
                        num_increment = int(line.split(" ")[3])
                        card_position = deal_increment(card_position, deck_size, num_increment)
                elif 'cut' in line:
                        num_cut = int(line.split(" ")[1])
                        card_position = cut_stack(card_position, deck_size, num_cut)
        print("Solution to part a is:", card_position)
                
        repeats_every = -1
        stop_at = -1
                
                #8795 is too low (as is 8796)
                
        deck_size = 119315717514047 - 1
        card_position = 2020  
        positions = set()
        positions.add(2020)
        
        print(101741582076661)
        
        # ...hm. Not sure how to optimize this, actually
		exit()
        
        for i in range(101741582076661):
                print(i, end="\r")
                for line in lines:
                        if 'deal into new stack' in line:
                                card_position = reverse_stack(card_position, deck_size)
                        elif 'deal with increment' in line:
                                num_increment = int(line.split(" ")[3])
                                card_position = deal_increment(card_position, deck_size, num_increment)
                        elif 'cut' in line:
                                num_cut = int(line.split(" ")[1])
                                card_position = cut_stack(card_position, deck_size, num_cut)
                if card_position in positions:
                        print(card_position, "at index", i)
                        break
                
                
                        
        # I'm sure this could be improved to half time, but....
        # now, we know how many times it needs to run before stopping.
        print(stop_at)
        exit()
        
        
        #however, we need to run it backwards, and do the operations backwards.
        lines.reverse()
        for i in range(stop_at):
                for line in lines:
                        pass
                
        
        # shuffle it one more time here bcs I forget which answer it should be
        
                        
        exit()
      
        # After shuffling your new, giant, factory order deck that many times,
        # what number is on the card that ends up in position 2020?
                        
                          