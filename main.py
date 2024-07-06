from replit import clear
#HINT: You can call clear() to clear the output in the console.

user_name = input("What is your name?: ")
user_bid = input("What is your bid?: $")

#convert the user bid from string to an integer
user_bid = int(user_bid)

#add the entry into an empty dictionary
bid_log = {}
bid_log[user_name] = user_bid

#ask for more bidders
more_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n")

