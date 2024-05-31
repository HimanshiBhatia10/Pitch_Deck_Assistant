import os
import pandas as pd


pdfs_path = "/Users/thestash/Desktop/Major project/Pitch Decks/Unedited/Alredy Done copy"
data = pd.read_csv("/Users/thestash/Desktop/Major project/Pitch Decks/mask_naming.csv")

rename = {}

for a,b in zip(data["ABC_"],data["Company Name"]):
    rename[b] = str(a)

for pitch in os.listdir(pdfs_path):
    if pitch == '.DS_Store':
        pass
    else:
        os.rename(os.path.join(pdfs_path,pitch), pdfs_path+f"/ABC_{rename[pitch]}.pdf")





