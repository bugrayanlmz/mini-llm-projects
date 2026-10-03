# Mini LLM Projects

Three small Python experiments with Google's Gemini API using the `google-genai` SDK. All scripts currently select `gemini-2.5-flash`.

## Examples

- [main-1.py](main-1.py): Send a single predefined prompt and print the response.
- [main-2.py](main-2.py): Run an interactive terminal chat with conversation history.
- [main-3.py](main-3.py): Stream chat responses to the terminal as they arrive.

## Setup

Requires Python and a Gemini API key with access to the configured model.

```bash
git clone https://github.com/bugrayanlmz/mini-llm-projects.git
cd mini-llm-projects
python3 -m venv venv
source venv/bin/activate
pip install google-genai python-dotenv
```

The activation command above is for macOS/Linux. Create a `.env` file in the repository root:

```env
GEMINI_API_KEY=your-api-key
```

Run any example:

```bash
python main-1.py
python main-2.py
python main-3.py
```

Use `quit` or `exit` to end either interactive chat. Edit the prompt in `main-1.py` to try a different question. These examples do not enable web search or persist chat history between runs.
