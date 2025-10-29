import pandas as pd

def load_matches(path):
    matches = pd.read_csv(path)
    matches['date'] = pd.to_datetime(matches['date'], errors='coerce')
    return matches

def load_deliveries(path):
    deliveries = pd.read_csv(path)
    return deliveries

def clean_matches(matches):
    matches_clean = matches.drop_duplicates()
    matches_clean['date'] = pd.to_datetime(matches_clean['date'], errors='coerce')
    matches_clean.fillna({'winner': 'Unknown', 'toss_decision': 'Unknown'}, inplace=True)
    return matches_clean

def clean_deliveries(deliveries):
    deliveries_clean = deliveries.fillna(0)
    return deliveries_clean
