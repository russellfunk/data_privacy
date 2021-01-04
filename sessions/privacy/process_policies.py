# -*- coding: utf-8 -*-

"""process_policies.py: Process privacy policies using spacy."""

__author__ = "Russell J. Funk"
__date__ = "November 25, 2020"

# load packages
import json
import spacy
import pandas as pd
import tqdm
tqdm.tqdm.pandas()

# configuration
INPUT_FILE = "data/policies.json"
OUTPUT_FILE = "data/policies_df.pickle"

def main():
  
  # load nlp
  print("loading nlp model...")
  nlp = spacy.load("en_core_web_lg")
  nlp.max_length = 2000000  
  
  # load the data
  with open("data/policies.json") as f:
    df = pd.DataFrame({k:" ".join(v) for k,v in json.load(f).items()}.items(), 
                      columns=["url","policy_text"])
    
  # apply nlp
  df["policy_text_processed"] = df.policy_text.progress_apply(nlp)
  
  # save file
  df.to_pickle(OUTPUT_FILE, protocol=4)

if __name__ == "__main__":
  main()
