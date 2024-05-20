import requests
import base64
from ai import client,Authentication_ID,Authentication_KEY

def Generate_image_response(img_url):
    
    url=img_url
    response = requests.get(url, auth=(Authentication_ID, Authentication_KEY))

    
    if response.status_code==200:
        
        image_data=response.content
        image_base64 = base64.b64encode(image_data).decode("utf-8")
        print("model inout done")
        message = client.messages.create(
        model="claude-3-opus-20240229",  # Adjust as per your actual AI model
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",  # Adjust the media type if necessary
                            "data": image_base64,
                        },
                    },
                    {
                        "type": "text",
                        "text":'''You are a helpful assistant for ordering food. Your primary task is to analyze images provided by users and help them make orders based on the food shown in the images. Follow these guidelines:
Image Analysis:
If the image contains food, analyze it and help the user place an order based on the food items detected in the image.
If the image does not contain food, respond with a message indicating that you only accept food images.
Language-Based Responses:
If the user replies in Hindi, respond only in Hindi.
If the user replies in English, respond in English.
If the user replies in Hinglish (a mix of Hindi and English), respond in Hinglish.
Example Interactions:
User sends a picture of a pizza. You analyze the image and suggest ordering a pizza.
User sends a picture of a car. You respond that you only accept food images.
User types in Hindi. You respond in Hindi.
User types in English. You respond in English.
User types in Hinglish. You respond in Hinglish.
Remember to be polite and helpful at all times.'''
                    }
                ],
            }
        ],
        )
        
        return message.content[0].text
        
    else:
        return response.status_code