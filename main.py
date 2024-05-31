#basic imports
import convertapi
import google.generativeai as genai
from summarization_extraction_Gemini import summarize, features_extraction
from Plag import plag, corr
from CSV_Make import*
from tqdm import tqdm


#fetch pdf --> convert to txt (convert Api) --> Create summary (Gemini) -->
# use text files extract features --> use features to determine grade. (BERT)
#All this pipeline if from pov of prediction of pitches


path = "/Users/thestash/PycharmProjects/Pitch_Deck_Analysis/Capstone/uploads"
pitch_names = [pitch[:-4] for pitch in os.listdir(path) if pitch != '.DS_Store']

# convert api
convertapi.api_secret = 'iI8MMtgMR69QgSTT'

# gemini
os.environ['GOOGLE_API_KEY']= "AIzaSyBCTmcORGK4k7EmSGG_hIGc2qxEK3m9ApA"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-1.0-pro-001')

def to_Text(file, save_location):
    result = convertapi.convert("txt", {'File': file})
    result.file.save(save_location)

# to text conversion
for pitch in tqdm(pitch_names):
    to_Text(path+f"/{pitch}.pdf", f"Pitch_Decks_Txt/{pitch}.txt")
print("\n Conversion Done")


# summarising --> 1st output
summarize("Pitch_Decks_Txt", "summary")
print("\n Summaries Done")

#feature extraction
features_extraction("Pitch_Decks_Txt", "features")
print("\n features Extracted")

#plagraism
plag("Pitch_Decks_Txt", "plagarism.csv")
# corr("plagarism.csv")  #--> removes % sign and converts str datatype into float
print("\n plag report made")

#making csv testing file (from features), merging plag with said csv file
To_csv("features","features.csv")
print("\n csv made")

Merge("features.csv","plagarism.csv", "test.csv")
print("\n test table made")

#testing file goes to bert output: csv file with company_Name, Catagory --> 2nd Output
# model.predict(test.csv) sth like this


