import os
import google.generativeai as genai
import pandas as pd
from tqdm import tqdm

os.environ['GOOGLE_API_KEY']= "AIzaSyBCTmcORGK4k7EmSGG_hIGc2qxEK3m9ApA"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-1.0-pro-001')


def plag(read_location, save_location):
    plag_dict = {}
    for pitch in tqdm(os.listdir(read_location)):
        if pitch == ".DS_Store":
            pass
        else:
            with open(os.path.join(read_location, pitch), "r") as file:
                pitch_deck = file.read()
            response = model.generate_content(f"Generate a plagiarism rating (in percentage) of the following pitch deck: {pitch_deck}, the output must be a number (%) and nothing else (no text)")
            plag_dict[pitch[:-4]] = response.text
    ind = plag_dict.keys()
    data = pd.DataFrame(columns=["Company_Name","Plag_Percent"])
    data.set_index("Company_Name", inplace=True)

    for ind, plag in zip(ind, plag_dict.values()):
        data.loc[ind] = plag
    data.to_csv(save_location)


#not needed anymore
def rename(path):
    data = pd.read_csv(path)
    data.rename(columns={"Unnamed: 0": "Company_Name"}, inplace=True)
    data.set_index("Company_Name", inplace=True)



def corr(path):
    data = pd.read_csv(path)
    plag_data = data["Plag_Percent"]
    ind = data["Company_Name"]
    data.set_index("Company_Name", inplace=True)
    for i,bit in zip(ind,plag_data):
        if "%" in bit:
            bit = bit.replace("%", "")
        data.loc[i ,"Plag_Percent"] = bit
    data["Plag_Percent"] = data["Plag_Percent"].astype("float64")
    data.to_csv(path)

if __name__ == "__main__":
    # plag("/Users/thestash/PycharmProjects/Pitch_Deck_Analysis/Pitch_Decks_Txt", "/Users/thestash/PycharmProjects/Pitch_Deck_Analysis/plagarism_1.csv")
    # corr("/Users/thestash/PycharmProjects/Pitch_Deck_Analysis/plagarism_1.csv")
    pass