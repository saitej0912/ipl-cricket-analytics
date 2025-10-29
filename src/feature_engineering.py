import pandas as pd

def encode_features(matches_df):
    df = matches_df.copy()
    df['season_encoded'] = pd.factorize(df['season'])[0]
    df['venue_encoded'] = pd.factorize(df['venue'])[0]
    df['toss_decision_encoded'] = df['toss_decision'].apply(lambda x: 1 if x == 'bat' or x == 'bat first' else 0)
    df['team1_encoded'] = pd.factorize(df['team1'])[0]
    df['team2_encoded'] = pd.factorize(df['team2'])[0]
    df['winner_encoded'] = pd.factorize(df['winner'])[0]
    return df

def save_features(df, path):
    df.to_csv(path, index=False)
