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
    with open(filename, "r") as fh:
        return fh.read()

def main():

    # Load source file
    source = load_file("data/source.txt")
    prompt = load_file("data/prompt.txt")

    # Create constraint
    constraint = f"{prompt}:\n\n{source}"

    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = constraint,
        temperature = 0.9,
        max_tokens = (4097 - len(constraint)),
        frequency_penalty = 2.0,
        presence_penalty = -2.0
    )

    for choice in response["choices"]:
        print(choice["text"].strip())

if __name__ == "__main__":
    main()