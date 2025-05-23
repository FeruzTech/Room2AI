# Chatbot Summarizer Project

## Overview
This project is a chatbot that summarizes a given subject prompt for a specified audience age group, using Retrieval Augmented Generation (RAG) and LLMs. It consists of a FastAPI backend and a Vue.js frontend.

## Setup

### Backend
1. `cd backend`
2. Create a `.env` file (see `.env` template)
3. `pip install -r requirements.txt`
4. `uvicorn main:app --reload`

### Frontend
1. `cd frontend`
2. `npm install`
3. `npm run serve`

## Usage
- Select an age group and enter a subject prompt in the frontend UI.
- The backend summarizes the prompt for the selected age group, using RAG and LLMs.

## Project Structure
See `chatbot-copilot-instructions.md` for details.
