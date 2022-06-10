# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:22 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""
import argparse

def is_sum_in_array(sorted_array, S):
    """Check if pair of elements in sorted array can sum as a given value.

    Args:
        sorted_array (list): sorted array of numbers
        S (float): given value for sum of two elements
    Returns:
        list | -1: list of two elements if exists
    
    Solution is based on the fact that array is already sorted. 
    Otherwise we should sort it that will increase complexity.
    """
    lp = 0                      # init left pointer
    rp = len(sorted_array) -1   # init right pointer
     
    # iterate over the list from two ends
    while lp < rp:
        current_sum = sorted_array[lp] + sorted_array[rp]
        if (current_sum == S):
            return [sorted_array[lp], sorted_array[rp]]
        elif (current_sum < S):   # increase lower value in pair
            lp += 1
        else:                     # decrease bigger value in pair
            rp -= 1
    
    # if such pair doesn't exist
    return -1
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--sorted-array', nargs='+', type=float)
    parser.add_argument('--given-sum', type=float)   
    args = parser.parse_args()
    print(args)

    if args.sorted_array is not None and args.given_sum is not None:
        sorted_array = args.sorted_array
        given_sum = args.given_sum
    else:
        # enter manually
        sorted_array = [0, 1, 2, 10.5, 23, 44]
        given_sum = 25
    
    # double check if array is sorted
    sorted_array.sort()

    print(f"Checking: sorted array: {sorted_array}, given sum: {given_sum}")
    print("Output:")
    print(f"{is_sum_in_array(sorted_array, given_sum)}")
