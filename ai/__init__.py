import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

Authentication_ID=os.getenv("TWILIO_ACCOUNT_SID")
Authentication_KEY=os.getenv("TWILIO_AUTH_TOKEN")
