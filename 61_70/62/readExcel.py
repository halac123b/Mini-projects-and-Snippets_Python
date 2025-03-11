import pandas as pd

def get_git_entries(input_file, sheet_name):
    # Read the Excel file
    df = pd.read_excel(input_file, sheet_name=sheet_name, usecols=["Sleep (life)"])  # Read only column A
    
    # Filter rows where values in column A end with "(git)"
    filtered_list = df[df["Sleep (life)"].astype(str).str.endswith("(git)")]["Sleep (life)"].tolist()
    
    return filtered_list