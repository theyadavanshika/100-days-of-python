import art
print(art.logo)

print("Welcome to Blind Auction Bid!\n")

def highest_bidder(bids):
    print("Calculating highest bid")
    amount = 0
    person = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > amount:
            amount = bid_amount
            person = bidder

    print(f"{person} has the highest bid with the bid value of : {bids[person]}")  

bids = {}

while True:
    name = input("What is your name? : ").lower()
    price = int(input("What is your bid? : $"))
    bids[name] = price
    other_bidders = input("Are there any other bidders? Type 'yes or 'no'").lower()
    print(".\n" * 5)

    if other_bidders == "yes":
        continue
    elif other_bidders == "no":
        highest_bidder(bids)
        break
        
# print(bids)

