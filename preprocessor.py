import pandas as pd


def preprocess(df, region_df):
    # 1. Filtering for summer olympics
    df = df[df['Season'] == 'Summer']

    # 2. Merge with region_df
    df = df.merge(region_df, on='NOC', how='left')

    # 3. Dropping duplicates
    df.drop_duplicates(inplace=True)

    # 4. One-hot encoding medals
    # We use dtype=int to ensure we get 1s and 0s instead of True/False
    dummies = pd.get_dummies(df['Medal'], dtype=int)
    df = pd.concat([df, dummies], axis=1)

    return df