import os
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_experimental.tools.python.tool import PythonREPLTool

# Load environment variables from the .env file
load_dotenv()

# Get the Groq API key from the environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

# Check if the API key is loaded
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables. Please check your .env file.")

# 1. Initialize the LLM (from Step 2)
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama3-8b-8192",
    temperature=0.0
)

# 2. Define the tool for code execution
# PythonREPLTool allows the agent to execute Python code.
# The agent will call this tool whenever it needs to perform a calculation.
tools = [PythonREPLTool()]

# 3. Define the prompt template for the agent
# The prompt is crucial. It instructs the LLM to 'think' step-by-step (Chain-of-Thought).
# It also defines the instructions for how the agent should use its available tools.
prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                "You are an expert at solving math word problems by writing and executing Python code. "
                "You have access to a Python REPL tool. "
                "Break down the problem step by step, write the code, and execute it to get the final answer. "
                "Return the final numerical answer directly without any additional text."
            )
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

# 4. Create the agent
# 'create_tool_calling_agent' is a constructor for agents that use LLMs with tool-calling capabilities.
# It takes the LLM, the list of tools, and the prompt as input.
agent = create_tool_calling_agent(llm, tools, prompt)

# 5. Create the agent executor
# 'AgentExecutor' is the runtime that will power the agent.
# It takes the agent and the list of tools and is responsible for running the agent's logic.
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 6. Define a function to test the agent
def test_agent_with_math_problem(problem):
    print(f"\n--- Solving Problem: {problem} ---")
    response = agent_executor.invoke({"input": problem, "chat_history": []})
    print(f"Final Answer: {response['output']}")

# 7. Run the test
if __name__ == "__main__":
    problem1 = "What is the square root of 144?"
    test_agent_with_math_problem(problem1)

    problem2 = "A baker has 5 dozen cookies. She sells 25 of them. How many cookies are left?"
    test_agent_with_math_problem(problem2)