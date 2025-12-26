from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
            model='o4-mini',
            messages=[
                {"role":"user", 
                 "content":[
                    {"type":"text", "text":"Generate a caption for this image about 20 words"},
                    {"type":"image_url", "image_url":{"url":"https://images.squarespace-cdn.com/content/v1/57f3e33c20099e0dd27b624a/1599160622497-VYSRPT1MKNE7K0D7EJV3/Screen+Shot+2020-09-03+at+3.16.32+PM.png?format=2500w"}}
                ]}
            ]

        )

print(f"GPT Response: {response.choices[0].message.content}")