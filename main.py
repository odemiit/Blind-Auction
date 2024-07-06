from replit import clear
#HINT: You can call clear() to clear the output in the console.

def add_bid_entry(name, bid):
  #add the entry into an empty dictionary
  bid_log = {}
  bid_log[user_name] = user_bid

more_players_left = True

while more_players_left:
  #ask for user name and bid
  user_name = input("What is your name?: ")
  user_bid = int(input("What is your bid?: $"))

  #ask for more bidders
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n")

  #switch more players left to False if answer is no so the while loop stops
  if more_bidders == "no":
    more_players_left = False

