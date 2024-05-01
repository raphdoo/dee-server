from openai import OpenAI
from decouple import config
from pathlib import Path
import requests

from helpers.message_helper import get_message_history

client = OpenAI(api_key=config("OPENAI_KEY"))

  
#OpenAI - Getting reponse to messages
def get_response(instruction):

  messages = get_message_history()
  user_message = {"role":"user", "content": instruction}
  messages.append(user_message)

  try:
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages= messages
    )

    response_message = response.choices[0].message.content


    return response_message
  
  except Exception as err:
    print(err)
    return



