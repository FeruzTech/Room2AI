from fastapi import APIRouter, HTTPException
from models.prompt import PromptRequest, PromptResponse
from services.rag import summarize_with_rag

router = APIRouter()

@router.post("/summarize", response_model=PromptResponse)
def summarize_prompt(request: PromptRequest):
    if not request.age_group:
        raise HTTPException(status_code=400, detail="Please select an age group.")
    summary = summarize_with_rag(request.age_group, request.prompt)
    return PromptResponse(summary=summary)
