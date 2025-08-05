from langchain_experimental.tools.python.tool import PythonREPLTool

# Create a single instance of the PythonREPLTool
python_repl = PythonREPLTool()

# A list of all tools available to the agent
tools = [python_repl]