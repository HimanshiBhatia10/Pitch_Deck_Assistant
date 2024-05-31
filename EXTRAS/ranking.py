# Preprocessing and scoring system setup
import numpy as np
import pandas as pd

pitch_decks = pd.read_csv("/Users/thestash/Desktop/Major project/Pitch Decks/train.csv")

# Work Experience scoring
def score_experience(text):
    if "NIL" in text.upper():
        return 1
    elif "years" in text.lower():
        return 3
    else:
        return 2

# Problem Statement scoring
def score_problem(text):
    if "NIL" in text.upper():
        return 1
    elif len(text.split()) > 50:  # Assuming a detailed problem statement is longer
        return 3
    else:
        return 2

# Traction scoring
def score_traction(text):
    if "NIL" in text.upper():
        return 1
    elif "million" in text.lower() or "thousand" in text.lower():
        return 3
    else:
        return 2

# Market Size/Market Trend scoring
def score_market(text):
    if "NIL" in text.upper():
        return 1
    elif "$" in text:
        return 3
    else:
        return 2

# Investment/Fund Ask scoring
def score_investment(text):
    if "NIL" in text.upper():
        return 1
    elif "$" in text:
        return 3
    else:
        return 2

# SWOT scoring
def score_swot(text):
    if "NIL" in text.upper():
        return 1
    else:
        return 2

# Plagiarism adjustment
def adjust_plagiarism(score, plag_percent):
    if plag_percent >= 50:
        return max(1, score - 1)  # Reduce score if high plagiarism
    return score

# Apply scoring
pitch_decks['Experience_Score'] = pitch_decks['Work_Experience'].apply(score_experience)
pitch_decks['Problem_Score'] = pitch_decks['Problem Statement'].apply(score_problem)
pitch_decks['Traction_Score'] = pitch_decks['Traction'].apply(score_traction)
pitch_decks['Market_Score'] = pitch_decks['Market Size/ Market Trend'].apply(score_market)
pitch_decks['Investment_Score'] = pitch_decks['Investment/ Fund Ask'].apply(score_investment)
pitch_decks['SWOT_Score'] = pitch_decks['SWOT'].apply(score_swot)

# Calculate total score and adjust for plagiarism
pitch_decks['Total_Score'] = pitch_decks[['Experience_Score', 'Problem_Score', 'Traction_Score', 'Market_Score', 'Investment_Score', 'SWOT_Score']].sum(axis=1)
pitch_decks['Adjusted_Score'] = pitch_decks.apply(lambda x: adjust_plagiarism(x['Total_Score'], x['Plag_Percent']), axis=1)

# Normalize scores to classify into A, B, C
score_bins = [0, np.percentile(pitch_decks['Adjusted_Score'], 33), np.percentile(pitch_decks['Adjusted_Score'], 66), pitch_decks['Adjusted_Score'].max()]
pitch_decks['Rank'] = pd.cut(pitch_decks['Adjusted_Score'], bins=score_bins, labels=['C', 'B', 'A'], include_lowest=True)

pitch_decks.to_csv("/Users/thestash/Desktop/try.csv")
