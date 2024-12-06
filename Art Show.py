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
    message_content = response.choices[0].message.content
    print(message_content)
    print(response.citations)

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
    print("Input your ecosystem")
    ecosystem = input("Your ecosystem: ")
    generate_facts(f"Tell me facts about {ecosystem} ecosystems, Include commonly found plants and animals")
    print(f"Here is an image of a {ecosystem}:")
    generate_images(f"a realistic {ecosystem} scene with various commonly found plants and animals")
    print("Here are some plants and animals:")
    generate_images(f"a few commonly found plants and animals in {ecosystem}")
    generate_sound_effect(f"{ecosystem} sounds with some animals in the background", f"{ecosystem}.mp3") 



