from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

#print logo at start of game
print(logo)

#empty bid log dictionary
bid_log = {}

def add_bid_entry(name, bid):
  #add the entry into an empty dictionary
  bid_log[name] = bid

more_players_left = True

#variable to store the highest bid
highest_bid = 0

#variable to store the winner
winner = ""

while more_players_left:
  #ask for user name and bid
  user_name = input("What is your name?: ")
  user_bid = int(input("What is your bid?: $"))

  #call on function to add bid entry
  add_bid_entry(user_name, user_bid)

  #check for highest bid
  if user_bid > highest_bid:
    highest_bid = user_bid
    winner = user_name

  #ask for more bidders
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n")

  #switch more players left to False if answer is no so the while loop stops
  if more_bidders == "no":
    more_players_left = False
  elif more_bidders == "yes":
    clear()

print(f"The winner is {winner} with a bid of ${highest_bid}")