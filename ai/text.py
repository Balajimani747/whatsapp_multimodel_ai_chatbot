from ai import client


def Generate_text_response(qestion:str) -> str:
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0.0,
        system='''
You are a helpful assistant for ordering food. Respond to the user in the language they use:
If the user replies in Hindi, respond only in Hindi.
If the user replies in English, respond in English.
If the user replies in Hinglish (a mix of Hindi and English), respond in Hinglish."
''',
        messages=[
            {"role": "user", "content": qestion}
        ],
    )
    #print(message.content[0].text)
    return message.content[0].text
