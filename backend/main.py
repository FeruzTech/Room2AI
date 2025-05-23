from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import prompt
from models.prompt import PromptRequest, PromptResponse
from services.rag import summarize_with_rag

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend URL(s) instead of ["*"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/summarize", response_model=PromptResponse)
def summarize(request: PromptRequest):
    summary = summarize_with_rag(request.age_group, request.prompt)
    return PromptResponse(summary=summary)

# Include API routes
app.include_router(prompt.router)
