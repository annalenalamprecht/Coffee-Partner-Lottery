# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 14:20:35 2023

@author: chris
"""
# try creating new groups until successful
max_attempts = 10
attempts = 0
new_groups_found = False
while not new_groups_found and attempts < max_attempts: # to do: add a maximum number of tries
    attempts += 1   
  
    # Calculate remainder when dividing number of participants by chosen group size
    remainder = len(participants)%group_size
    
    # If there is 2 or more people left over, make a group of this size
    if remainder != 0 and remainder != 1:
        make_group(remainder)
        
    # If there is exactly 1 person left over, create a group with an extra member
    elif remainder == 1:
        make_group(group_size+1)
  
    # while still participants left to group, create groups of the chosen group size
    while len(nparticipants) > 0:
        make_group(group_size) 
    try:
        # check if all new groups are indeed new, else reset
        if len(ngroups - ogroups) == len(ngroups):
            new_groups_found = True
        else:
            ngroups = set()
            nparticipants = copy.deepcopy(participants)
    except IndexError:
       # If ngroups and ogroups have different lengths, continue loop
        continue