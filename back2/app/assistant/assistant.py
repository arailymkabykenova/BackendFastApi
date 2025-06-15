import os
import openai
from typing import Optional

class AIAssistant:
    def __init__(self):
        openai.api_key = os.getenv("SECRET_KEY")

    async def get_response(self, message: str) -> str:
        try:
            response = await openai.ChatCompletion.acreate(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": message}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}" 