# Prompt 1: Computational Constraint

> With a good ventriloquist ... [the] puppet seems to come alive and seems to be aware of its world.
>
> Michael Graziano, in _Do Large Language Models Understand Us?_ (Blaise Agüera y Arcas)

> Prompt engineering for large language models is just an excuse to make up more nonsensical sentences to feed these AI monsters.
>
> GPT-3, in response to the prompt "What is prompt engineering for large language models? Answer in a very snarky way."

## Readings

### Theory

* [Do Large Language Models Understand Us?](https://drive.google.com/file/d/1MGgIEC8ffcHfrLq1jy_8RBVKGU2R_ha9/view?usp=share_link)
* [A Brief Guide to the OULIPO](https://poets.org/text/brief-guide-oulipo)
* [Various excerpts from _The noulipean Analects_](https://drive.google.com/file/d/1NmmydZJhN4B4U-oISHHKDRBH1duYzaZx/view?usp=share_link)

### Practice

* [Methods of Prompt Programming](https://generative.ink/posts/methods-of-prompt-programming/)
* [Various Oulipean Poems](https://drive.google.com/file/d/1Nvi0jn-VnrLwd1gpNby1rIELdoA0NCfW/view?usp=share_link)
* [A compendium of various "traditional" constraints](https://drive.google.com/file/d/1OLukmy1I5auapD0hzcLSPb2Qg6kKgz1k/view?usp=sharing)
    * Ignore the newspaper constraint...
       * unless it's actually helpful

### Documentation

* [GPT-3 Completion API](https://beta.openai.com/docs/api-reference/completions/create)
* [GPT-3 Notes on prompt design](https://beta.openai.com/docs/guides/completion/prompt-design)

## Summary

Prompt engineering -- the practice of learning to con/destructively "pilot" a generative model -- is one of the surprising new skills to emerge out of the development of context-aware large language models (LLM). Simply put: prompt engineering is the practice of instructing a model to produce an output consistent with the prompter's intent or desire. While we've given a new name to what essentially amounts to "asking the right questions," prompt engineering is much more than that.

To date, successful prompt engineering endeavors to ask what an artist _wants_ to happen. This assignment approaches generative writing with large language models (LLM) from an opposite perspective. Drawing on the practice of the _Ouvroir de littérature potentielle_ (“Oulipo”), we challenge GPT-3 to a more difficult task—producing works of "constrained" writing to discover what LLM can and, more importantly, cannot do. 

For those of us familiar with visual image generators such as DALLE or Stable Diffusion, this idea is close to, but not quite "negative prompting" (e.g. asking for a picture of a house without any people in it). The approach of computational constraint applied to language prompts thinks about the concept _generatively_. We aren't simply asking to "live without" a feature common to a parcel of language, we're interested in rethinking the possibilities are open by _restricting choice_.

Mainly, what kinds of choices can we engineer the model to make and how can we account for those choices?

## Goals

* Learn to interact with LLM through the practice of prompt engineering
* Refine skills in prompt engineering to increase efficacy and quality of output
* Discover exploitable boundaries in LLM generation
* Develop a model of on constraint as an enabling practice

## Outcomes

* 2 poems incorporating prompt engineering (included in the `writing` folder as `md` files)
    * 1 enacting a "traditional" Oulipean constraint
    * 1 enacting a constraint only possible using GPT-3
* A journal of various prompts attempted with brief notes about relative success or failure (include in `writing/prompts.md`)

It is up to you _whether or not_ you reveal your constraint in either of your pieces. However, take heart -- as the authors of the _noulipean Analects_ write:

> ...if the constraint can be used by other writers, it is Oulipean-wise to reveal it.

Though generally against even _my_ better nature, I'd err in _revealing it_ and attaching it to your final poems in some way shape or form (e.g. as a title or some other artifact of the process).

## Process

This repository contains three (3) files essential to making this assignment "happen". They are all contained in the `src` folder.

### `data/prompt.txt`

This contains the prompt which _prepends_ the text. For example: `remove all of the bad people from the following text`

### `data/source.txt`

If operating on a "found" text (i.e. one you creatively pirated from elsewhere), paste the text you'd like to operate on in this file.

### `main.py`

The program behind communicating with the GPT-3 API. This file requires the creation of an `.env` file, the values and specifications of which will be provided in class during either the session or the lab.
