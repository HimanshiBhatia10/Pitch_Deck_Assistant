import convertapi
import os
import pandas as pd

convertapi.api_secret = 'iI8MMtgMR69QgSTT'

## API details
user_info = convertapi.user()
print(user_info['SecondsLeft'])


def to_Text(file, save_location):
    result = convertapi.convert("txt", {'File': file})
    result.file.save(save_location)

#text extraction from pdfs using convert api
if __name__ == "__main__":
    path = "/Users/thestash/Desktop/Major project/Pitch Decks/Unedited/Pitch_Decks_more"
    Pitch_Decks = [i for i in os.listdir(path) if i != '.DS_Store']
    Range = range(53, 73)
    index_pitches = {i: j for i, j in zip(Range,Pitch_Decks)}
    for key, value in zip(index_pitches.keys(),index_pitches.values()):
        to_Text(f'{path}/{value}', f'/Users/thestash/Desktop/Major project/Pitch Decks/To_Text_ unmasked/ABC_{key}.txt')
        print(key, "done")

    # # Creating Csv for mapping not req in testing phase

    data = pd.read_csv("/Users/thestash/Desktop/Major project/Pitch Decks/mask_naming.csv")
    data.drop("Unnamed: 0", inplace=True, axis=1)
    data.set_index("ABC_", inplace=True)
    print(data)
    for key, value in zip(index_pitches.keys(),index_pitches.values()):
        data.loc[key] = [value]
    data.to_csv("/Users/thestash/Desktop/Major project/Pitch Decks/mask_naming.csv")


