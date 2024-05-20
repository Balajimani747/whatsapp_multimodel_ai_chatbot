from flask import Flask, request

from ai.text import Generate_text_response
from ai.image import Generate_image_response

from twilio.twiml.messaging_response import MessagingResponse


app=Flask(__name__)

@app.route('/webhook', methods=['POST','GET'])
def home():
    data = request.form.to_dict()
    response=MessagingResponse()
    usernumber = data.get('WaId')
    
    if 'MediaUrl0' in data.keys():
        image_url=data['MediaUrl0']
        ai_text_response=Generate_image_response(image_url)
    else:
        message=data['Body']
        ai_text_response=Generate_text_response(message)
        
    response.message(ai_text_response)
    return str(response)

if __name__=='__main__':
    app.run(debug=True,port=8080)
    
    
