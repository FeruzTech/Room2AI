<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Project Instructions
- Build a chatbot that summarizes a given subject prompt for a specified audience age group, providing information that is appropriate and digestible for that age.

## Tech Stack


- **Backend:** Python FastAPI
- **Database:** Vector database (for RAG)
- **LLM Integration:** LangChain, OpenAI (RAG, chunking, function-calling)

## Functional Requirements

- Accept user input for:
  - Audience age group (user must select from options such as: Early Elementary [5-8], Late Elementary [9-11], Middle School [12-14], High School [15-18])
  - Subject prompt (text)
- If the user submits a question without selecting an age group, respond with a friendly message reminding the user to first select an age group.
- Summarize and explain the subject prompt in natural language appropriate for the selected school-age group.
- Use RAG (Retrieval Augmented Generation) to enhance responses with relevant, up-to-date information.
- Store and retrieve context chunks in a vector database.
- Support function-calling with parameters:
  - `context`: Age group
  - `explain`: Text to summarize
- Expose API endpoints for:
  - Submitting a prompt and age group 
  


## Implementation Notes

- Use LangChain for chunking, retrieval, and LLM orchestration.
- Use OpenAI or similar LLM for summarization.
- Ensure summaries are tailored to the cognitive level of the specified age group.
- Design the API to be easily consumable by the Vue.js frontend .

## Recommended Sources for Ingestion

The chatbot should ingest articles and information from the following reputable sources:
1. https://www.nationalgeographic.com/latest-stories
2. https://www.smithsonianmag.com/smart-news/
3. https://www.bbc.com/news/science_and_environment
4. https://www.nasa.gov/news/all-news/
5. https://blog.khanacademy.org/
6. https://www.history.com/this-day-in-history
7. https://www.cdc.gov/media/index.html
8. https://www.nih.gov/news-events/news-releases
9. https://www.scientificamerican.com/section/news/
10. https://www.unicef.org/press-releases


These sources are reputable, frequently updated, and cover a range of general knowledge and educational topics suitable for summarization for different age groups.

## Project Structure Recommendations

1. **Organize by Service/Responsibility**
    - Separate frontend and backend code into distinct directories
    - Use a modular structure for both frontend and backend
    - Example structure:

    ```plaintext
    project-root/
    ├── frontend/                  # Vue.js app for user interface
    │   └── src/
    │       ├── components/        # Reusable UI components (AgeSelector, PromptInput, SummaryDisplay)
    │       ├── views/             # Main views/pages of the app
    │       └── services/          # API client for backend communication
    │   └── public/                # Static assets (favicon, index.html)
    │   └── package.json           # Frontend dependencies and scripts
    ├── backend/                   # FastAPI app for API and business logic
    │   ├── api/                   # API route definitions (prompt submission, summary retrieval)
    │   ├── services/              # Business logic (summarization, RAG, chunking)
    │   ├── models/                # Pydantic models and DB schemas
    │   ├── vectorstore/           # Vector DB integration and management
    │   └── main.py                # FastAPI entry point
    │   └── requirements.txt       # Backend dependencies
    ├── tests/                     # Unit and integration tests for backend and frontend
    ├── .env                       # Environment variables (not committed)
    ├── README.md                  # Project overview and setup instructions
    └── .gitignore                 # Files and directories to ignore in version control
    ```

2. **Use Environment Configuration and Version Control**
   - Store secrets (API keys, DB URIs) in `.env` files (never commit to git)
   - Use `requirements.txt` for Python dependencies
   - Use `package.json` for frontend dependencies
   - Add a root-level `README.md` with setup and usage instructions
   - Use `.gitignore` to exclude node_modules, __pycache__, .env, etc.

3. **Modularize RAG and LLM Integration**
   - Place all LangChain, OpenAI, and vector DB logic in a dedicated backend module (e.g., `/app/services/rag.py`)
   - Abstract summarization and retrieval logic behind service interfaces
   - Keep API endpoints thin—only handle request/response, delegate logic to services
   - Write clear docstrings and type annotations for maintainability