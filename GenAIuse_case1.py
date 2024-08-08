"""pip install google-generativeai"""

import os
import google.generativeai as genai
key="AIzaSyBE2BWu-epSX5kH_ggY6-o_HPgIeAXB-_w"
genai.configure(api_key=key)  # argument_name=key
# We are accessing google Gemini model
# with our api key

"""for m in genai.list_models():
  print(m.name)"""

model=genai.GenerativeModel("gemini-pro")
#model

response=model.generate_content("List of top 5 Indian Cricketers")
print(response.text)