candies = input("Enter your favorite candies: ") # take in users favorite candies, comma separated list
candyList = candies.split(",") # store the candies in a list, split the strong at the commas
rankingList = [""] * len(candyList) # create an empty list to store ranked candies, same length as the candyList
x = 0 # set iterator for while loop
while x < len(candyList): # have awhile loop that iterate through the candyList
    rank = input("Enter the ranking for " + candyList[x] + " from 1 to " + str(len(candyList)) + ": ") # prompt the user to enter the ranking for each candy
    rankingList[int(rank)-1] = candyList[x] # add the candy into the ranked list based on the position the user asked for
    x += 1 # increment the iterator by 1
print(rankingList)
