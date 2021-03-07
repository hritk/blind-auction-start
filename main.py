from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

print("lets start the auction")

bids={}

end_of_bidding=False
while not end_of_bidding:
  name = input("whats your name\n ")
  bid = int(input("whats your bid\n"))
  bids[name]=  bid
  ques=input("is there any other user yes or no\n")
  if ques=="no":
    end_of_bidding=True
  elif ques=="yes":
    clear() 

highest_bid=0
for i in bids:
  bid_amount=bids[i]
  if bid_amount>highest_bid:
    highest_bid=bid_amount
    winner=i

  

print(bids)  
print(highest_bid)  

print(f"so the highest bid is $ {highest_bid} by {winner}")



