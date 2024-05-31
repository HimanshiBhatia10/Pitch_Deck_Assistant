#creating Training file
import os
import pandas as pd
import re
from tqdm import tqdm

#patterns
Work_ex = r"1\.+ "
Prob_statement = r"2\.+ "
Tract = r"3\.+ "
Mar = r"4\.+ "
Invest = r"5\.+ "
SWOT = r"6\.+ "
patterns = [Work_ex, Prob_statement, Tract, Mar, Invest, SWOT]

def To_csv(read_location, save_location):
    col = ["Company_Name","Work_Experience", "Problem Statement", "Traction", "Market Size/ Market Trend", "Investment/ Fund Ask", "SWOT"]
    table = pd.DataFrame(columns=col)
    #table = pd.read_csv("/Users/thestash/Desktop/Major project/Pitch Decks/train.csv")
    table.set_index("Company_Name", inplace=True)
    for company in tqdm(os.listdir(read_location)):
        if company == ".DS_Store":
            continue
        else:
            file_path = os.path.join(read_location, company)

        with open(file_path, "r") as file:
            company_data = file.read()
        company_data = company_data.replace("**", "")

        all_patterns = []
        row_wise_data = []
        name = company[:-4]
        for pattern in patterns:
            match = re.search(pattern, company_data, re.IGNORECASE)
            try:
                all_patterns.append(match.start())
            except:
                print(name, "cant match")
        for i in range(len(all_patterns)):
            if i != 5:
                start = all_patterns[i]
                end = all_patterns[i+1]
                row_wise_data.append(company_data[start:end])
            else:
                start = all_patterns[i]
                row_wise_data.append(company_data[start:])
        for i,j in zip(row_wise_data, col[1:]):
            table.loc[name, j] = i
    table.to_csv(save_location)

def Merge(file1, file2, save_location):
    data1 = pd.read_csv(file1)
    data2 = pd.read_csv(file2)
    data1.set_index("Company_Name", inplace=True)
    data2.set_index("Company_Name", inplace=True)
    data3 = pd.merge(data1, data2, left_index=True, right_index=True)
    data3.to_csv(save_location)

if __name__ == "__main__":
    To_csv("/Users/thestash/Desktop/Major project/Pitch Decks/features determination", "/Users/thestash/Desktop/Major project/Pitch Decks/features.csv")
    Merge("/Users/thestash/Desktop/Major project/Pitch Decks/features.csv", "/Users/thestash/Desktop/Major project/Pitch Decks/plag percent_Train/plag.csv", "/Users/thestash/Desktop/Major project/Pitch Decks/final_train.csv")