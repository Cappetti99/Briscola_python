import random

# Initialize the suits and card values
suits = ['Bastoni', 'Denari', 'Spade', 'Coppe']
values = [1, 2, 3, 4, 5, 6, 7, 'Fante', 'Cavallo', 'Re']

# Point values for each card
card_points = {
    1: 11,      # Ace
    3: 10,      # 3
    'Re': 4,    # King
    'Cavallo': 3,  # Queen
    'Fante': 2, # Jack
    2: 0,       # All others
    4: 0,
    5: 0,
    6: 0,
    7: 0
}

# Generate the deck (each card will be a tuple of value and suit)
deck = [(value, suit) for suit in suits for value in values]

# Shuffle the deck
random.shuffle(deck)

# Function to deal hands
def deal_hand(deck, hand_size=3):
    hand = deck[:hand_size]  # Take the top cards for the hand
    del deck[:hand_size]  # Remove those cards from the deck
    return hand

# Function to display a hand
def display_hand(hand):
    for idx, card in enumerate(hand):
        print(f"{idx + 1}: {card[0]} of {card[1]} (Points: {card_points[card[0]]})")

# Function to determine the winner of a turn
def determine_winner(player_card, ai_card, trump_suit):
    player_value, player_suit = player_card
    ai_value, ai_suit = ai_card
    
    # If suits are the same, higher rank wins
    if player_suit == ai_suit:
        return 'player' if card_points[player_value] > card_points[ai_value] else 'ai'
    
    # Trump suit wins
    if player_suit == trump_suit:
        return 'player'
    elif ai_suit == trump_suit:
        return 'ai'
    
    # Otherwise, player who played the same suit as the leading card wins
    return 'player'

# Function for AI to choose a card (random for now, but can be improved)
def ai_choose_card(ai_hand):
    return random.choice(ai_hand)

# Function to play a turn
def play_turn(player_hand, ai_hand, trump_suit):
    # Display player's hand
    print("\nYour hand:")
    display_hand(player_hand)

    # Player chooses a card
    choice = int(input("Choose a card to play (1, 2, 3): ")) - 1
    player_card = player_hand.pop(choice)

    # AI chooses a card
    ai_card = ai_choose_card(ai_hand)
    ai_hand.remove(ai_card)
    
    # Show the cards played
    print(f"\nYou played: {player_card[0]} of {player_card[1]}")
    print(f"AI played: {ai_card[0]} of {ai_card[1]}")

    # Determine who wins the turn
    winner = determine_winner(player_card, ai_card, trump_suit)
    
    print(f"\n{winner.capitalize()} wins the round!")
    
    # Return the points won
    points_won = card_points[player_card[0]] + card_points[ai_card[0]]
    return winner, points_won

# Function to run the game
def run_game():
    # Deal hands to player and AI
    player_hand = deal_hand(deck)
    ai_hand = deal_hand(deck)

    # Set the trump suit (the first card from the remaining deck)
    trump_card = deck.pop()
    trump_suit = trump_card[1]
    
    print(f"\nTrump card: {trump_card[0]} of {trump_card[1]}")

    player_score = 0
    ai_score = 0
    
    # Game loop (3 rounds for now, adjust as needed)
    for _ in range(3):
        winner, points_won = play_turn(player_hand, ai_hand, trump_suit)
        if winner == 'player':
            player_score += points_won
        else:
            ai_score += points_won

        # Refill hands after each round (draw 1 card from the deck for each player)
        if len(deck) >= 2:
            player_hand.append(deck.pop())
            ai_hand.append(deck.pop())

    # Final score
    print("\nFinal Scores:")
    print(f"Player: {player_score} points")
    print(f"AI: {ai_score} points")
    
    if player_score > ai_score:
        print("Congratulations! You won the game.")
    else:
        print("AI wins the game. Better luck next time!")

# Run the game
run_game()
