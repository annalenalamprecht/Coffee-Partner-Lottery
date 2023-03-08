# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 09:46:56 2023

@author: chris
"""

import random

previous_matchings = {}

def generate_pairing(people, group_sizes):
    # Shuffle the list of people
    random.shuffle(people)
    # Create a list to store the groups in the pairing
    groups = []
    # Loop through the group sizes and create groups of each size
    for size in group_sizes:
        # Check if there are enough people remaining to create a group of the desired size
        if len(people) >= size:
            # Slice the first "size" number of people from the list of people
            group = people[:size]
            people = people[size:]
            # Check if the pairing has been used before
            while is_pairing_used(groups + [group]):
                # If the pairing has been used before, swap one person from the current group with a person from a different group
                swap_group_index = random.randint(0, len(groups)-1)
                swap_person_index = random.randint(0, len(groups[swap_group_index])-1)
                swap_person = groups[swap_group_index][swap_person_index]
                group.append(swap_person)
                groups[swap_group_index][swap_person_index] = group.pop()
            # Add the group to the list of groups in the pairing
            groups.append(group)
    # Return the pairing
    return groups

# Function to check if a pairing has been used before
def is_pairing_used(pairing):
    # Clear the list of people in the pairing and add new people
    people = []
    for group in pairing:
        for person in group:
            people.append(person)
    # Sort the list of people
    people.sort()
    # Convert the list of people to a tuple
    key = tuple(people)
    # Check if the pairing has been used before
    if key in previous_matchings:
        return True
    else:
        # Add the pairing to the dictionary of previous matchings
        previous_matchings[key] = True
        return False
