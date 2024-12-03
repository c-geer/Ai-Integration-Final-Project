import os
from openai import OpenAI

#Generate Facts about different ecosystems using perpelexity
YOUR_API_KEY = os.environ.get("PERPLEXITY_API_KEY")
client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

#Rainforest Facts
messages = [
    {
        "role": "system",
        "content": (
            "Be precise and very concise."
        ),
    },
    {
        "role": "user",
        "content": (
            "Tell me facts about rainforest ecosystems, Include commonly found plants and animals"
        ),
    },
]
response = client.chat.completions.create(
    model="llama-3.1-sonar-small-128k-online",
    messages=messages,
)
print(response)

#Aquatic Ecosystem Facts
messages = [
    {
        "role": "system",
        "content": (
            "Be precise and very concise."
        ),
    },
    {
        "role": "user",
        "content": (
            "Tell me facts about aquatic ecosystems, Include commonly found plants and animals"
        ),
    },
]
response = client.chat.completions.create(
    model="llama-3.1-sonar-small-128k-online",
    messages=messages,
)
print(response)

#Desert Ecosystem Facts
messages = [
    {
        "role": "system",
        "content": (
            "Be precise and very concise."
        ),
    },
    {
        "role": "user",
        "content": (
            "Tell me facts about desert ecosystems, Include commonly found plants and animals"
        ),
    },
]
response = client.chat.completions.create(
    model="llama-3.1-sonar-small-128k-online",
    messages=messages,
)
print(response)

#Generate Images 
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="a realistic desert ecosystem scene with camels and cacti",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)

response = client.images.generate(
  model="dall-e-3",
  prompt="Desert with camels and ",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)

response = client.images.generate(
  model="dall-e-3",
  prompt="a realistic aquatic ecosystem scene with fish and aquatic plants",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)





