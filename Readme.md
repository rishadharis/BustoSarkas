# Sarkasin LinkedIn
## Sebuah LLM Application untuk mencari akun linkedin mu dan meroasting nya

### Flow:
Input Nama -> Agents (Mencari url linkedin) -> Tavily (LLM Search Engine API) -> Nubela (Linkedin Scraper) -> Langchain Chain with GPT

## Configuration

This project uses environment variables for configuration. You can set them in a `.env` file (for local development) or use Streamlit secrets.

### Local Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
4. Fill in the required API keys in `.env`.
5. Run the app:
   ```bash
   streamlit run app.py
   ```

### Configuration Options
You can configure the following environment variables:

**Required:**
- `OPENAI_API_KEY`: OpenAI API Key
- `TAVILY_API_KEY`: Tavily API Key
- `NUBELA_API_KEY`: Nubela API Key (if used)
- `ANTHROPIC_API_KEY`: Anthropic API Key (if used)

**Optional:**
- `OPENAI_MODEL_NAME`: OpenAI Model to use (default: `gpt-4o-mini`)
- `APP_TITLE`: Application title shown in the browser
- `APP_CREATOR`: Name of the creator displayed in the app
- `SARKAS_PROMPT`: Custom prompt for the sarkas/roasting generation.
