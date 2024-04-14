import pandas as pd

df = pd.read_csv("nba_games.csv", index_col= 0)

df = df.sort_values("date")
df = df.reset_index(drop=True)

del df["mp.1"]
del df["mp_opp.1"]
del df["index_opp"]

def add_target(group):
    group["target"] = group["won"].shift(-1)
    return group

df = df.groupby("team", group_keys=False).apply(add_target)

#df[df["team"] == "WAS"]

df["target"][pd.isnull(df["target"])] = 2
df["target"] = df["target"].astype(int, errors="ignore")

df["won"].value_counts()

df["target"].value_counts()

nulls = pd.isnull(df).sum()
nulls = nulls[nulls > 0]
valid_columns = df.columns[~df.columns.isin(nulls.index)]

df = df[valid_columns].copy()

from sklearn.linear_model import RidgeClassifier
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.model_selection import TimeSeriesSplit

rr = RidgeClassifier(alpha=1)

split = TimeSeriesSplit(n_splits=3)

sfs = SequentialFeatureSelector(rr, n_features_to_select=30, direction="forward", cv=split, n_jobs=1)

removed_columns = ["season", "date", "won", "target", "team", "team_opp"]
selected_columns = df.columns[~df.columns.isin(removed_columns)]

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df[selected_columns] = scaler.fit_transform(df[selected_columns])

sfs.fit(df[selected_columns], df["target"])
predictors = list(selected_columns[sfs.get_support()])

def backtest(data, model, predictors, start=2, step=1):
    all_predictions = []
    
    seasons = sorted(data["season"].unique())
    
    for i in range(start, len(seasons), step):
        season = seasons[i]
        train = data[data["season"] < season]
        test = data[data["season"] == season]
        
        model.fit(train[predictors], train["target"])
        
        preds = model.predict(test[predictors])
        preds = pd.Series(preds, index=test.index)
        combined = pd.concat([test["target"], preds], axis=1)
        combined.columns = ["actual", "prediction"]
        
        all_predictions.append(combined)
    return pd.concat(all_predictions)

predictions = backtest(df, rr, predictors)

from sklearn.metrics import accuracy_score

accuracy_score(predictions["actual"], predictions["prediction"])

df.groupby(["home"]).apply(lambda x: x[x["won"] == 1].shape[0] / x.shape[0])

df_rolling = df[list(selected_columns) + ["won", "team", "season"]]

import numpy as np

def find_team_averages(team):
    # Select only numeric columns for rolling mean calculation
    numeric_cols = team.select_dtypes(include=[np.number])
    rolling = numeric_cols.rolling(10).mean()
    
    # You can either return just the rolling averages or merge them back with non-numeric columns
    # Here's an example of merging back with non-numeric columns if needed
    team_rolling = team[numeric_cols.columns].copy()
    team_rolling.loc[:, :] = rolling
    
    # If you have non-numeric columns that you need to carry forward, you can concatenate them back
    non_numeric_cols = team.select_dtypes(exclude=[np.number])
    return pd.concat([non_numeric_cols, team_rolling], axis=1)

df_rolling = df_rolling.groupby(["team", "season"], group_keys=False).apply(find_team_averages)

rolling_cols = [f"{col}_10" for col in df_rolling.columns]
df_rolling.columns = rolling_cols
df = pd.concat([df, df_rolling], axis=1)

df = df.dropna()

def shift_col(team, col_name):
    next_col = team[col_name].shift(-1)
    return next_col

def add_col(df, col_name):
    return df.groupby("team", group_keys=False).apply(lambda x: shift_col(x, col_name))

df["home_next"] = add_col(df, "home")
df["team_opp_next"] = add_col(df, "team_opp")
df["date_next"] = add_col(df, "date")

full = df.merge(df[rolling_cols + ["team_opp_next", "date_next", "team"]], left_on=["team", "date_next"], right_on=["team_opp_next", "date_next"])

full[["team_x", "team_opp_next_x", "team_y", "team_opp_next_y", "date_next"]]

removed_columns = list(full.columns[full.dtypes == "object"]) + removed_columns

selected_columns = full.columns[~full.columns.isin(removed_columns)]
sfs.fit(full[selected_columns], full["target"])

predictors = list(selected_columns[sfs.get_support()])

predictions = backtest(full, rr, predictors)

print(accuracy_score(predictions["actual"], predictions["prediction"]))