# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:54:08 2023

@author: chris
"""

def check_groups():
    # Load all previous groups
    ogroups = set()
    if os.path.exists(all_groups_csv):
        with open(all_groups_csv, "r") as file:
            csvreader = csv.reader(file, delimiter=DELIMITER)
            for row in csvreader:
                group = []
                for i in range(0,len(row)):
                    group.append(row[i])                        
                ogroups.add(tuple(group))

    # Convert set of new groups to tuple of tuples for comparision
    tngroups = tuple(ngroups)

    # Check if any previous groups have same participants as new groups
    for og in ogroups:
        if len(set(og).intersection(set(tngroups))) == group_size:
            # Found duplicate group
            print(f"Duplicate group found: {og}")
            # Reset new groups
            ngroups.clear()
            nparticipants = copy.deepcopy(participants)
            # Try creating new groups until successful
            while True:
                # ...same code as above...
                if ngroups.isdisjoint(ogroups):
                    break
                else:
                    ngroups = set()
                    nparticipants = copy.deepcopy(participants)
            # Convert set of new groups to tuple of tuples for output
            tngroups = tuple(ngroups)
            break

    return tngroups

# Ask for group size, max 5
while True:
    try:
        group_size = int(input('''
How many people would you like in each group? (Please enter an integer number. 
The minimum group size is 2 and the maximum is 5) '''))
        if group_size < 2:
            print ('The minimum number of group members is 2. Please try again.')
        if group_size > 1 and group_size < 6:
            break
        else: 
            print('The maximum number of group members is 5. Please try again.')  
    except ValueError:
        print("Please enter an integer number.")

# Try creating new groups until successful
while True:
    ### ...same code as before... ####
    # Check if any previous groups have same participants as new groups
    tngroups = check_groups()
    if tngroups:
        break
