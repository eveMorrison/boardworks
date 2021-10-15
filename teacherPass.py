scores = [] # create an empty list that will be used to store the teacher's scores
addScores = True # variable that controls the while loop. 
passing = 0 # keeps track of the number of passing scores
while(addScores): # if true scores will be added false no more scores need to be added
    score = float(input("Enter a score: ")) # obtain a score from the teacher, use a float since there can be decimals
    scores.append(score) # store the entered score in the list
    if(score >=60): # test wether the score is passing or not
        passing += 1 # if score is a pass increment by 1
    choice = input("Would you like to add another score?(y/n) ") # as the teacher if they would like to continue
    if(choice != "y"): # only continue asking for scores if they enter y
        addScores = False
print(passing," students passed.")