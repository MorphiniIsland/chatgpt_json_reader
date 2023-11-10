#Import ChatGPT to read information in Json files
#Sothat ChatGPT can generat new narratives based on Json files' informaiton

import openai
import json

# Set your OpenAI GPT API key
openai.api_key = "YOUR_API_KEY"

# Load the JSON data from the file
with open("shadows_of_chair.json", "r") as json_file:
    json_data = json.load(json_file)

# Extract relevant information
location_info = json_data["object"]["location"]
ownership_info = json_data["object"]["ownership"]
history_info = json_data["object"]["history"]

# Create a conversation prompt with extracted data
conversation_prompt = f"Can you provide information about the 'Shadows of Chair'? It is currently located at {location_info['current']} and was created in {history_info['creationDate']} by {history_info['creator']}. It has been owned by {', '.join(ownership_info['previousOwners'])}."

# Query the GPT API
response = openai.Completion.create(
  model="text-davinci-002",
  prompt=conversation_prompt,
  temperature=0.7,
  max_tokens=150
)

# Print the GPT response
print(response["choices"][0]["text"].strip())
