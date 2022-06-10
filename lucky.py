# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:51 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""
import re
import argparse

def longest_lucky_series(trial):
    """Check if there is lucky series presented in the trial.

    Args:
        trial (str): string of roll results
    Returns:
        str | 0: longest lucky series if exists
    
    """

    pattern_split = r'[^56]'    # pattern to split string on lucky series
    pattern_filter = r'56|65'   # pattern to filter of those ones that don't contain different chars
        
    longest_series = ''

    for series in re.split(pattern_split, trial):
        if len(series) > len(longest_series) and re.search(pattern_filter, series):
            longest_series = series
    
    return longest_series if len(longest_series) else 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--trial', type=str)   
    args = parser.parse_args()
    print(args)

    if args.trial is not None:
        trial = args.trial
    else:
        # enter manually
        trial = 54466654644455546655656522356556563435
    
    # double check if trial is string
    trial = str(trial)

    print(f"Detecting longest lucky series in trial: {trial}")
    print("Output:")
    print(f"{longest_lucky_series(trial)}")

