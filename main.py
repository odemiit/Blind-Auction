from replit import clear
#HINT: You can call clear() to clear the output in the console.

#empty bid log dictionary
bid_log = {}

def add_bid_entry(name, bid):
  #add the entry into an empty dictionary
  bid_log[name] = bid

more_players_left = True

while more_players_left:
  #ask for user name and bid
  user_name = input("What is your name?: ")
  user_bid = int(input("What is your bid?: $"))

  #call on function to add bid entry
  add_bid_entry(user_name, user_bid)

  #ask for more bidders
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n")

  #switch more players left to False if answer is no so the while loop stops
  if more_bidders == "no":
    more_players_left = False
  elif more_bidders == "yes":
    clear()

