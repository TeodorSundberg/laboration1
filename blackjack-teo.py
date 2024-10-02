import random 


'''
Skapa ett program som simulerar ett blackjack-spel mellan en spelare och en dator.
- Spelet spelas med en vanlig kortlek som blandas innan varje runda.
- Varje spelare får två kort i början av spelet. Datorn visar bara upp ett av sina kort.
- Spelaren kan välja att ta fler kort (hit) eller stanna på sina nuvarande kort (stand).
- Spelaren kan fortsätta att ta kort tills hen når 21 poäng eller över.
- Om spelaren går över 21 poäng förlorar hen direkt.
- När spelaren stannar, spelar datorn sin tur. Datorn måste ta kort så länge summan av korten är mindre än 17 poäng och stanna när datorns kortsumma är 17 poäng eller mer.
- Om datorn går över 21 poäng vinner spelaren oavsett vilka kort spelaren har.
- Om varken spelaren eller datorn går över 21 poäng så vinner den som har högst kortsumma.
'''
                                        # You could create here another loop that while run as long as you want to play the game
                                         # intial values to keep track of actions
                                        # i keeps track of the game state
                                        # j keeps track of the postition in the deck array
i = 1
j = 0
string1 = ""
                                        # starting hands (no card or 0)    I guess it could be empty, but I don't like that                          
player_hand = [0]
dealer_hand = [0]
                                        
    
# create deck -- I assume there might a be a function in python, but I liek to create my own
                                        # 2-10 + ace
lowsuit = list(range(2, 12)) 
                                        # add the value of knight, queen and king to suit                                       
highsuit = [10,10,10] 
                                        # combine to create 13 cards     
suit =  highsuit + lowsuit
                                        # 1 of each suit gives us 52 cards
deck = suit + suit + suit + suit
                                        # test to show that deck is correct
## print(deck)
## print(len(deck))
                                        # Randomize deck
random.shuffle(deck)

## print(deck)

# pull 1 card from deck at the time, by going through the array
# First deal 1 card to player and 2 cards to dealer and only inform the player of 1 of the dealers cards

player_hand = player_hand + [deck[j]]
j = j + 1
dealer_hand = dealer_hand + [deck[j]]
j = j + 1
dealer_hand = dealer_hand + [deck[j]]
j = j + 1

# sum(dealer_hand) - dealer_hand[1] will let us ignore the first card of the dealer (and the empty array
# ask player to hit, add the value from ace as 11, if larger than 21, then look through array to change 11 to 1
## if larger than 21 and no 1 in array then bust


''' The game is played by asking the simple question hit or stand, after each ask  I intend to check the state before going back to the loop. I am using the same loop for all action while i = 1 the game is basically not decided yet, at any point where someone loses it will turn to 0 or it will turn to 0 at the point the dealer decides to quit the game.

The player plays first and once he done all actions the computer decides by algorithm when to stop.

The outcomes that need to be checked for are
first outcome 
Loop 1 
Player stands -- pass the action to dealer (loop 2)
player hits -- if below 21, goes back to start 
            -- if above 21, with aces, convert 1 ace from 11 to 1, goes back to start
            -- if above 21 with no aces, loses game - game stops i = 0 
Loop 2
Dealer checks both cards    -- if above or at 17 stay and decide result -- i = 0 (I did not consider downgrading the ace here) and did not consider draws, house always win
                            -- if above 21, with aces, convert 1 ace from 11 to 1, goes back to start
                            -- if above 21 with no aces, loses game - game stops i = 0 
                            

'''


print(f"The dealer has {sum(dealer_hand) - dealer_hand[1]} + one more unknown card and you have  {sum(player_hand)} ")
while i == 1:
    if string1 != "pass to dealer":
        string1 = input("Hit or Stand?: ")
        string1 = string1.lower()
    if string1 == "hit":
        player_hand = player_hand + [deck[j]]
        print(f"You get 1 more card and now you have  {sum(player_hand)}")
        j = j + 1    
    elif  string1 == "stand":
        print(f" You choose to stay at {sum(player_hand)} ")
        string1 = "pass to dealer"
        print(f"The dealer has {sum(dealer_hand)} ")
    if sum(player_hand) > 21:
        try:
            position = player_hand.index(11)  # Get the index of the first occurrence of 11
            player_hand[position] -= 10 
            print(f"you have  {sum(player_hand)}")
        except ValueError:
            print(f"You lost the game the dealer had {sum(dealer_hand)} ")
            i = 0
    if string1 == "pass to dealer":
        if sum(dealer_hand) < 17: # makes more sense to hit until he wins or loses<= sum(player_hand):
            dealer_hand = dealer_hand + [deck[j]]
            try:
                position = dealer_hand.index(11)  # Get the index of the first occurrence of 11
                dealer_hand[position] -= 10 
                print(f"The dealer has 1 more card and now has {sum(dealer_hand)} ")
            except ValueError:
                print(f"The dealer has 1 more card and now has  {sum(dealer_hand)} ")
            j = j + 1
        if sum(dealer_hand) >= 17 and sum(dealer_hand) < sum(player_hand):
            print(f"The dealer lost and had {sum(dealer_hand)} compared to your winning {sum(player_hand)}")
            i = 0
        if sum(dealer_hand) > 21:
            try:
                position = dealer_hand.index(11)  # Get the index of the first occurrence of 11
                dealer_hand[position] -= 10 
            except ValueError:
                print(f"The dealer lost and had {sum(dealer_hand)} ")
                i = 0
        if sum(dealer_hand) < 22 and sum(dealer_hand) >= sum(player_hand):
            print(f"The dealer won and had {sum(dealer_hand)} compared to you {sum(player_hand)}")
            i = 0