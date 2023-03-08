# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:54:39 2023

@author: chris
"""
import csv

# path to the CSV file with all previous matchings
all_groups_csv = "Coffee Partner Lottery all groups.csv"

# init dictionary of previous matchings
previous_matchings = {}

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
    
    # Read previous matchings from CSV file into dictionary
    with open(all_groups_csv, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            previous_matchings[tuple(row)] = True

    # Check if the pairing has been used before
    if key in previous_matchings:
        return True
    else:
        # Add the pairing to the dictionary of previous matchings
        previous_matchings[key] = True
        # Write the new dictionary to the CSV file
        with open(all_groups_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            for k, v in previous_matchings.items():
                writer.writerow(list(k))
        return False