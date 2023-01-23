#!/usr/bin/python

import os
import openai
from dotenv import dotenv_values

# Set up OpenAI credentials; you will get the class key
# after we clone the repository

CONFIG = dotenv_values('.env')

OPEN_AI_KEY = CONFIG["KEY"] or os.environ["OPEN_AI_KEY"]
OPEN_AI_ORG = CONFIG["ORG"] or os.environ["OPEN_AI_ORG"]

openai.api_key = OPEN_AI_KEY
openai.organization = OPEN_AI_ORG

def load_file(filename: str = "") -> str:
    """Loads an arbitrary file name"""
    with open(filename, "r") as fh:
        return fh.read()

def main():

    # Load source file
    source = load_file("data/source.txt")
    prompt = load_file("data/prompt.txt")

    # Create constraint
    constraint = f"{prompt}:\n{source}"

    response = openai.Completion.create(
        # The model; other choices (with explanation):
        # https://beta.openai.com/docs/models/gpt-3
        model = "text-davinci-003",
        # Data to feed to the model
        prompt = constraint,
        # "Level of risk" associated with model predictions
        temperature = 0.9,
        top_p = 1,
        # Maximum size of requests (this is already max size)
        max_tokens = (4097 - len(constraint)),
        # Number of results to attempt and return
        n = 1
    )

    # Iterate through the various responses from the model
    for choice in response["choices"]:
        print(choice["text"].strip())

if __name__ == "__main__":
    main()