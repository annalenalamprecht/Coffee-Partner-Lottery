#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 09:13:27 2023

@author: user
"""

import pandas as pd
import csv
import random
import copy
import os

# path to the CSV files with participant data
participants_csv = "Coffee Partner Lottery participants.csv"

# header names in the CSV file (name and e-mail of participants)
header_name = "Your name:"
header_email = "Your e-mail:"

# path to TXT file that stores the groups of this round
new_groups_txt = "Coffee Partner Lottery new groups.txt"

# path to CSV file that stores the groups of this round
new_groups_csv = "Coffee Partner Lottery new groups.csv"

# path to CSV file that stores all groups (to avoid repetition)
all_groups_csv = "Coffee Partner Lottery all groups.csv"
        
# init set of old groups
ogroups = set()

DELIMITER=','

# load all previous groups (to avoid redundancies)
if os.path.exists(all_groups_csv):
    with open(all_groups_csv, "r") as file:
        csvreader = csv.reader(file, delimiter=DELIMITER)
        for row in csvreader:
            group = []
            for i in range(0,len(row)):
                group.append(row[i])                        
            ogroups.add(tuple(group))

# load participant's data
formdata = pd.read_csv(participants_csv, sep=DELIMITER)

# create duplicate-free list of participants
participants = list(set(formdata[header_email]))

 # init set of new groups
ngroups = set()

# running set of participants
nparticipants = copy.deepcopy(participants)

# Boolean flag to check if new groups has been found
new_groups_found = False

# ask for group size, max 5
while True:
    try:
        group_size =  int(input('''
How many people would you like in each group? (Please enter an integer number. 
The minimum group size is 2 and the maximum is 5) '''))
        if group_size < 2 :
            print ('The minimum number of group members is 2. Please try again.')
        if group_size > 1 and group_size < 6:
            break
        else: 
            print('The maximum number of group members is 5. Please try again.')  
    except ValueError:
        print("Please enter an integer number.")

# try creating new groups until successful
while not new_groups_found:   # to do: add a maximum number of tries
  
    # First account for number of participants not being divisible by groupsize
    ''' if number of participants not divisible by chosen group size, create
    one group the size of the remainder (if remainder > 1) or one group with an
    extra group member (if remainder == 1). Then continue making groups of the
    desired group size'''
    
    if len(participants)%group_size != 0 and len(participants)%group_size != 1:
        plist = []
        # create group of size of remainder if remainder >1
        for i in range(0,len(participants)%group_size):
            p = random.choice(nparticipants)
            nparticipants.remove(p)
            plist.append(p)
        plist.sort()
        ngroups.add(tuple(plist))
    
    elif len(participants)%group_size == 1:
        plist = []
        # create group with one extra member if remainder ==1
        for i in range(0,group_size+1):
            p = random.choice(nparticipants)
            nparticipants.remove(p)
            plist.append(p)
        plist.sort()
        ngroups.add(tuple(plist))
            
  
    # while still participants left to groups...
    while len(nparticipants) > 0:
        plist = []
        # create groups of the chosen group size
        for i in range(0,group_size):
            p = random.choice(nparticipants)
            nparticipants.remove(p)
            plist.append(p)
        plist.sort()
        ngroups.add(tuple(plist))
        

    # check if all new groups are indeed new, else reset
    if ngroups.isdisjoint(ogroups):
        new_groups_found3 = True
    else:
        ngroups = set()
        nparticipants = copy.deepcopy(participants)


# assemble output for printout
output_string = ""

output_string += "------------------------\n"
output_string += "Today's coffee partners:\n"
output_string += "------------------------\n"

for group in ngroups:
    group = list(group)
    output_string += "* "
    for i in range(0,len(group)):
        name_email_group = f"{formdata[formdata[header_email] == group[i]].iloc[0][header_name]} ({group[i]})"
        if i < len(group)-1:
            output_string += name_email_group + ", "
        else:
            output_string += name_email_group + "\n"
    
# write output to console
print(output_string)

# write output into text file for later use
with open(new_groups_txt, "wb") as file:
    file.write(output_string.encode("utf8"))

# write new groups into CSV file (for e.g. use in MailMerge)
with open(new_groups_csv, "w") as file:
    header = ["name1", "email1", "name2", "email2", "name3", "email3"]
    file.write(DELIMITER.join(header) + "\n")
    for group in ngroups:
        group = list(group)
        for i in range(0,len(group)):
            name_email_group = f"{formdata[formdata[header_email] == group[i]].iloc[0][header_name]}{DELIMITER} {group[i]}"
            if i < len(group)-1:
                file.write(name_email_group + DELIMITER + " ")
            else:
                file.write(name_email_group + "\n")
                
# append groups to history file
if os.path.exists(all_groups_csv):
    mode = "a"
else:
    mode = "w"

with open(all_groups_csv, mode) as file:
    for group in ngroups:
        group = list(group)
        for i in range(0,len(group)):
            if i < len(group)-1:
                file.write(group[i] + DELIMITER)
            else:
                file.write(group[i] + "\n")


             
# print finishing message
print()
print("Job done.")
