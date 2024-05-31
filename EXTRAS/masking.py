import spacy
from spacy.matcher import Matcher
import os

nlp = spacy.load("en_core_web_lg")

#patterns spacy matcher
patterns = [
    [ "9999999999", [{"TEXT":{"REGEX":r"\d{10}"}}] ],
    [ "ABC@gmail.com" ,[{"LIKE_EMAIL": True}]],
    [ "ABC.com", [{"LIKE_URL": True}] ]
]

#for address
num_of_patterns = 3

p = r"/Users/thestash/Desktop/Major project/Pitch Decks/To_Text_ unmasked/ABC_10.txt"
with open(p, "r") as file:
    doc_text = file.read()


#replacing
def replace(doc_text,start, end, i):
        return doc_text[:start] + patterns[i][0] + doc_text[end:]

#pattern_0 : Phone_num
#pattern_1: Email id
def matching(doc_text):
    for i in range(num_of_patterns):
        matcher = Matcher(nlp.vocab)
        matcher.add(f"pattern_{i}", [patterns[i][1]])

        doc = nlp(doc_text)
        found_matches = matcher(doc)

        for id, s, e in found_matches:
            span = doc[s:e]
            start = span.start_char
            end = span.end_char

            doc_text = replace(doc_text,start,end, i)
    return doc_text


























