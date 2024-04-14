import os
import pandas as pd
from collections import defaultdict

def get_dataset_grouped(folder_path):
    dimensions_group = defaultdict(lambda: {"dataframes": [], "labels": []})
    score_results_path = os.path.join(folder_path, 'score_results.csv')
    
    # Check if the score results file exists
    if not os.path.exists(score_results_path):
        print("Score results file does not exist.")
        return
    
    # Read the score results file
    score_results = pd.read_csv(score_results_path)
    
    # Index to keep track of the current row in score results
    label_index = 0
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv') and filename != 'score_results.csv':
            file_path = os.path.join(folder_path, filename)
            try:
                df = pd.read_csv(file_path)
                rows, cols = df.shape
                
                # Append DataFrame to the group
                dimensions_group[(rows, cols)]["dataframes"].append(df)
                
                # Append corresponding labels
                scoreHome = score_results.iloc[label_index]['scoreHome']
                scoreAway = score_results.iloc[label_index]['scoreAway']
                dimensions_group[(rows, cols)]["labels"].append((scoreHome, scoreAway))
                
                label_index += 1
            except Exception as e:
                print(f"Failed to read {filename}. Error: {e}")
    
    return dimensions_group

