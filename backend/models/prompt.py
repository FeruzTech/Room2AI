from pydantic import BaseModel

class PromptRequest(BaseModel):
    age_group: str
    prompt: str

class PromptResponse(BaseModel):
    summary: str
