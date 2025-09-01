from pydantic import BaseModel


class GreetingUpdate(BaseModel):
    new_greeting_text: str


class GreetingResponse(BaseModel):
    current_greeting_text: str
