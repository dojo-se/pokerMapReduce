import sys

# Python Kernel() : Generate all 5-card poker hands as csv string. 
# e.g. : '3S,QC,AD,AC,7H'  (5 cards in each emitted data line) 
def Kernel(): 
  faces = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'];  
  suits = [ 'S', 'C', 'D', 'H' ] # Spades, Clubs, Diamonds, Hearts  

  # Make a list of all 52 cards in the deck; e.g. '3S' or 'QH'. 
  all_cards = [];  
  for f in range(0, len(faces)): 
    for s in range(0, len(suits)): 
      card = faces[f] + suits[s];  # construct e.g. 'QH' for Q of Hearts 
      all_cards.append(card) 

  # Generate and EMIT all unique 5-card combinations (poker hands). 
  baralho = []
  all_cards_len = len(all_cards)  # 52 
  for i1 in range(0, all_cards_len): 
    for i2 in range(i1+1, all_cards_len): 
      for i3 in range(i2+1, all_cards_len): 
        for i4 in range(i3+1, all_cards_len): 
          for i5 in range(i4+1, all_cards_len): 
               hand = ('["%s","%s","%s","%s","%s"]' % (all_cards[i1], all_cards[i2], all_cards[i3], all_cards[i4], all_cards[i5])) 
               print hand
               baralho.append(hand)
			   
  #print len(hand)
  #print len(baralho)
  #print hand
            #jsmr_context.Emit(hand)  

if __name__ == '__main__':
  Kernel()