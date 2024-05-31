import os
import google.generativeai as genai
from tqdm import tqdm


os.environ['GOOGLE_API_KEY']= "AIzaSyBCTmcORGK4k7EmSGG_hIGc2qxEK3m9ApA"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-1.0-pro-001')


# summerizer
def summarize(read_location, save_location):
    for pitch in tqdm(os.listdir(read_location)):
      if pitch == ".DS_Store":
        pass
      else:
        with open(os.path.join(read_location,pitch), "r") as file:
          data = file.read()
        response = model.generate_content(f"Summarize the following pitch deck in bullet pointers, also start by giving an introduction of the company: {data}")
        with open(f"{save_location}/{pitch}", "w") as file:
          file.write(response.text)



# #features determination
def features_extraction(read_location, save_location):
    for pitch in tqdm(os.listdir(read_location)):
      if pitch == ".DS_Store":
        pass
      else:
        with open(os.path.join(read_location,pitch), "r") as file:
          data = file.read()
        response = model.generate_content(f'''Extract the following information from the given Pitch deck: {data}, answer in pointers.
    1. work experience
    2. probelm or problem statement
    3. Traction
    4. Market Siz and Market Trend Information
    5. Investment, Fund Ask, Fund Utilisation or Financial Information
    6. SWOT Analysis
    
    Note 1: try to support with numerical data wherever possible
    
    Note 2: while extracting data (in points) make sure the points are strictly numbered (ordered list), eg.
        1.. Work Experience:
        2.. Problem Statement
    
    Note 3: If there is no relevant information available for particular point just write 'NIL' (eg. 1. Work experience: NIL); if no information is available for all the points, write 'NIL' for all points.
    
    ''')
        with open(f"{save_location}/{pitch}", "w") as file:
          file.write(response.text)



if __name__ == "__main__":
    features_extraction("/Users/thestash/Desktop/Major project/Pitch Decks/To_Text_Masked_1","/Users/thestash/Desktop/Major project/Pitch Decks/features determination")








