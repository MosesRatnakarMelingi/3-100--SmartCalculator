import os
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from tools import tools

# Load environment variables from the .env file
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables. Please check your .env file.")

# 1. Initialize the LLM
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama3-8b-8192",
    temperature=0.0
)

# 2. Define the static system message
system_message = SystemMessage(
    content=(
        "You are an expert at solving math problems. "
        "Your only job is to translate a given math word problem into a single, valid Python expression. "
        "Do not add any explanations, variable assignments, or `print()` statements. "
        "The output must be a single line of Python code that, when evaluated, produces the final answer. "
        "For example, 'What is 5 + 5?' should be translated to '5 + 5'. "
        "For complex problems, use standard Python libraries. 'What is the square root of 16?' should be translated to '16 ** 0.5'."
    )
)

# 3. Define a function to solve the problem
def solve_math_problem(problem_text):
    print(f"\n--- Solving Problem: {problem_text} ---")
    
    messages = [
        system_message,
        HumanMessage(content=problem_text),
    ]
    
    llm_response = llm.invoke(messages)
    
    llm_output_clean = llm_response.content.strip("'")
    print(f"Cleaned LLM Output: '{llm_output_clean}'")
    
    try:
        final_answer = tools[0].invoke(f"print({llm_output_clean})")
        print(f"Final Answer: {final_answer}")
    except Exception as e:
        print(f"Error during code execution: {e}")

# 4. Interactive loop for user input
if __name__ == "__main__":
    print("Welcome to the Smart Calculator! Type 'exit' to quit.")
    
    while True:
        user_input = input("Enter a math problem: ")
        if user_input.lower() == 'exit':
            break
        
        solve_math_problem(user_input)