# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 14:20:35 2023

@author: chris
"""

def check_groups():
    with open(all_groups_csv, "r") as f_all:
        all_groups = list(csv.reader(f_all))
    with open(new_groups_csv, "r") as f_new:
        new_groups = list(csv.reader(f_new))
    while True:
        for group in all_groups:
            if group in new_groups:
                make_group() 
            else:
                break