#Main Imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

#Custom Imports
from helpers.main_helper import get_response
from helpers.message_helper import save_messages, clear_messages

# Initiate the fastapi
app = FastAPI()

#Configure CORS
app.add_middleware(
  CORSMiddleware, 
  allow_origins= { "http://localhost:4173", "http://localhost:5173", "http://localhost:3000" },
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

# Define a Pydantic model for the request body
class RequestData(BaseModel):
    input_text: str

#bot response handler
@app.post("/bot-handler")
async def bot_handler(data: RequestData):

  audio_text = data.input_text

  response_message = get_response(audio_text)
  
  #Store messages in data.json file
  save_messages(audio_text, response_message)

  return response_message

  


# Clear Messages
@app.get("/clear")
async def clear_msgs():
  clear_messages()
  return {"message": "Messages cleared!"}


# Health checker
@app.get("/checker")
async def checker():
  return {"message": "Hello World, This is working!"}

