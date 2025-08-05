# Smart Calculator Agent

This project demonstrates how to build a highly reliable AI agent that can solve complex math word problems by translating them into executable Python code. The agent uses an LLM to generate the code and a dedicated tool to execute it, ensuring accuracy and consistency.

This project was developed as part of #TheAgenticQuest.

## 🚀 Features

-   **Natural Language to Code:** Translates natural language queries (e.g., "What is 10% of 50?") into valid Python expressions.
-   **Robust Execution:** Uses a sandboxed Python REPL to execute code, providing accurate and consistent results.
-   **Interactive:** An interactive command-line interface allows for continuous problem-solving.

## ⚙️ How It Works Behind the Scenes

The agent's process is a controlled and highly-engineered chain designed to mitigate common LLM weaknesses like arithmetic errors and hallucinations.

1.  **Input:** The user provides a math problem in natural language.
2.  **Translation:** An LLM (Llama 3) receives the problem and, based on a highly-specific prompt, translates it into a single line of Python code (e.g., `(15 * 8) - (10 ** 2)`).
3.  **Execution:** The generated code is passed directly to the `PythonREPLTool`. This tool executes the code and captures the output.
4.  **Output:** The captured result from the REPL is presented as the final answer, bypassing any potential LLM formatting or calculation errors.

## 🛠️ Tech Stack

-   **LLM:** Llama 3 (via Groq)
-   **Framework:** LangChain
-   **Tools:** `PythonREPLTool`
-   **Environment:** GitHub Codespaces

## 🔌 Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd Smart-Calculator-Agent
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(If you don't have a `requirements.txt` file, you can create one by running `pip freeze > requirements.txt`)*

3.  **Set up your Groq API Key:**
    -   Create an account and get your API key from [Groq Console](https://console.groq.com/keys).
    -   Create a file named `.env` in the root directory.
    -   Add your API key to the file:
    ```
    GROQ_API_KEY="your_api_key_here"
    ```
    *Note: The `.env` file is ignored by Git to protect your secret key.*

## 🚀 How to Run

Run the main script from your terminal to start the interactive calculator:

```bash
python main.py
