#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install openai


# In[2]:


import openai

def complete_sentence(sentence):
    # Set up OpenAI API credentials
    openai.api_key = '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'

    # Generate completions using OpenAI's GPT-3.5 model
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=sentence,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None
    )

    # Extract the completed sentence from the API response
    completed_sentence = response.choices[0].text.strip()

    return completed_sentence

user_sentence = input("Enter a sentence: ")
completed_sentence = complete_sentence(user_sentence)
print(completed_sentence)

