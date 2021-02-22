import pandas as pd
import csv
import random
import copy

# path to the CSV files with participant data
participants_csv = "Coffee Partner Lottery participants.csv"

# header names in the CSV file (name and e-mail of participants)
header_name = "Your name:"
header_email = "Your e-mail:"

# e-mail of game master, used as a "joker"
gamemaster_email = "a.l.lamprecht@uu.nl"

# path to CSV file that stores the pairings of this round
new_pairs_csv = "new_pairs.csv"

# path to CSV file that stores all pairings (to avoid repetition)
all_pairs_csv = "all_pairs.csv"


# init set of old pairs
opairs = set()

# load all previous pairings (to avoid redundancies)
with open(all_pairs_csv, "r") as file:
    csvreader = csv.reader(file, delimiter=',')
    for row in csvreader:
        opairs.add((row[0],row[1]))
        
# get participant's emails, remove duplicates, create list
formdata = pd.read_csv(participants_csv)
participants = list(set(formdata[header_email]))

# if odd number of participants, add/remove gamemaster from the list
if len(participants)%2 != 0:
    participants.append(gamemaster_email)
#    participants.remove(gamemaster_email)

# init set of new pairs
npairs = set()

# running set of participants
nparticipants = copy.deepcopy(participants)

# Boolean flag to check if new pairing has been found
new_pairs_found = False

while not new_pairs_found:   # to do: add a maximum number of tries
    
    # while still participants left to pair...
    while len(nparticipants) > 0:
    
        # take two random participants from list of participants
        p1 = random.choice(nparticipants)
        nparticipants.remove(p1)
        
        p2 = random.choice(nparticipants)
        nparticipants.remove(p2)
        
        # add alphabetically sorted tuple to set of pairs
        if p1 < p2:
            npairs.add((p1,p2))
        else:
            npairs.add((p2,p1))
 
    # check if all new pairs are indeed new, else reset
    if npairs.isdisjoint(opairs):
        new_pairs_found = True
    else:
        npairs = set()
        nparticipants = copy.deepcopy(participants)
 
# print out new pairs
print(npairs)

# append pairs to masterfile
with open(all_pairs_csv, "a") as file:
    for pair in npairs:
        pair = list(pair)
        file.write(pair[0] + "," + pair[1] + "\n")

# write new pairs into separate file (easier processing)
with open(new_pairs_csv, "w") as file:
    file.write("name1,email1,name2,email2\n")
    for pair in npairs:
        pair = list(pair)
        file.write(formdata[formdata[header_email]==pair[0]].iloc[0][header_name] + \
                   "," + pair[0] + "," + \
                   formdata[formdata[header_email]==pair[1]].iloc[0][header_name] + \
                   "," + pair[1] + "\n")
             
# print finishing message
print("Job done.")
