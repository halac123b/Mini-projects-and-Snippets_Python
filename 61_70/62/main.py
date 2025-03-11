from datetime import datetime, timedelta
import pandas as pd
import requests
import readExcel

GITHUB_TOKEN = "API token"  # Replace with your GitHub token

def get_top_repos(page, start_date, end_date):
    url = "https://api.github.com/search/repositories"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }
    params = {
        "q": f"stars:>1000 created:{start_date}..{end_date}",
        "sort": "stars",
        "order": "desc",
        "per_page": 100,  # Change this number to get more results
        "page": page,
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        repositories = [
            {"name": repo["name"] + " (git)", "full_name": repo["full_name"] + " (git)", "html_url": repo["html_url"]}
            for repo in data["items"]
        ]
        return repositories
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []

# Compare and store matched repos
def match_repos(repos, git_list, output_file, sheet_name):
    unmatched_repos = []
    
    for repo in repos:
        repo_name = repo["name"]
        # repo_full_name = repo["full_name"]

        # If name is not in git_list, it's unmatched (no need to check full_name)
        if repo_name not in git_list:
            unmatched_repos.append(repo)
        # else:
        #     # If name matches but full_name is NOT in git_list, keep it
        #     if repo_full_name not in git_list:
        #         unmatched_repos.append(repo)
    print(f"Match {len(unmatched_repos)} yeah")
    df = pd.DataFrame(unmatched_repos)
    try:
        # Load existing workbook
        with pd.ExcelWriter(output_file, mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False, header=False, startrow=writer.sheets[sheet_name].max_row)
        print(f"Data successfully appended to {output_file}, sheet: {sheet_name}")
    except FileNotFoundError:
        # If the file doesn't exist, create a new one
        df.to_excel(output_file, sheet_name=sheet_name, index=False)
        print(f"File not found. Created new file: {output_file}")

# Example usage
input_file = "readlist.xlsx"   # Replace with your actual file name
sheet_name = "Routine"          # Replace with your actual sheet name
output_file = "output"     # Replace with your desired output
git_list = readExcel.get_git_entries(input_file, sheet_name)


start_date = datetime(2025, 1, 1)  # Adjust to the earliest repo date you want
end_date = datetime.today()

while start_date < end_date:
    next_date = start_date + timedelta(days=30)  # Fetch data month by month
    print("Log next month")
    page = 1  # Start from page 1
    
    while True:
        repos = get_top_repos(page, start_date.strftime("%Y-%m-%d"), next_date.strftime("%Y-%m-%d"))  # Fetch one page

        if not repos:  # Stop when no more repositories
            print("No more repositories to process.")
            break
        
        out_file = output_file + str(start_date.year) + ".xlsx"
        match_repos(repos, git_list, out_file, "Sheet1")
        page += 1  # Move to the next page
    start_date = next_date
    

    # start_date = next_date