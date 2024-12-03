import os
from openai import OpenAI
from elevenlabs import ElevenLabs

#Generate facts about different ecosystems using perplexity
def generate_facts(text: str):
    API_KEY = os.environ.get("PERPLEXITY_API_KEY")
    client = OpenAI(api_key=API_KEY, base_url="https://api.perplexity.ai")
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
                text
            ),
        },
    ]
    response = client.chat.completions.create(
        model="llama-3.1-sonar-small-128k-online",
        messages=messages,
    )
    print(response)

#Generate images using DallE3
def generate_images(text: str):
    client = OpenAI()
    response = client.images.generate(
    model="dall-e-3",
    prompt=text,
    size="1024x1024",
    quality="standard",
    n=1,
    )
    image_url = response.data[0].url
    print(image_url)


#Generate sounds effects using eleven labs
def generate_sound_effect(text: str, output_path: str):
    API_KEY = os.environ.get("ELEVENLABS_API_KEY")
    elevenlabs = ElevenLabs(api_key=API_KEY)
    print("Generating sound effects...")

    result = elevenlabs.text_to_sound_effects.convert(
        text=text,
        duration_seconds=10, 
        prompt_influence=0.3,  
    )

    with open(output_path, "wb") as f:
        for chunk in result:
            f.write(chunk)

    print(f"Audio saved to {output_path}")


if __name__ == "__main__":
    generate_sound_effect("Rain forest noises with rain hitting leafs, birds chirping, monkeys in the background", "rainforest.mp3")
    generate_sound_effect("Underwater aquatic noises with fish swimming and water flowing","aquatic.mp3" )
    generate_sound_effect("Desert noises with wind rustling through sand and desert bird calls and cicada noises","desert.mp3" )
    generate_facts("Tell me facts about rainforest ecosystems, Include commonly found plants and animals")
    generate_facts("Tell me facts about aquatic ecosystems, Include commonly found plants and animals")
    generate_facts("Tell me facts about desert ecosystems, Include commonly found plants and animals")
    generate_images("a realistic desert ecosystem scene with camels and cacti")
    generate_images("Close up camels and other desert plants and animal")
    generate_images("a realistic aquatic ecosystem scene with fish and aquatic plants")
    generate_images("Close up of fish with aquatic plants in the background")
    generate_images("a realistic rainforest ecosystem scene with jaguars and birds")
    generate_images("Close up jaguar with a rainforest scene in the background")

