# Modified version that will work with both direct calls and as a tool
from dotenv import load_dotenv
load_dotenv()
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_community.llms import Ollama
from agents.tools.transaction_analyzer import analyze_user_transactions as raw_analyze_function
from agents.tools.summarizer import summarize_insights

# Test the raw function directly
print("\n=== Testing transaction analyzer directly ===")
analysis_result = raw_analyze_function("transactions.json")
print(f"Direct analyzer result: {analysis_result}")
print("=== End direct test ===\n")

# Only proceed with agent setup if the analyzer works
if "No data to analyze" not in analysis_result:
    # Convert function to a LangChain Tool
    analyze_tool = Tool.from_function(
        func=raw_analyze_function,
        name="analyze_user_transactions",
        description="Analyze user's past bank transactions to summarize trends, spending behavior, and insights."
    )

    summarizer_tool = Tool.from_function(
        func=summarize_insights,
        name="summarize_insights",
        description="Summarize extracted banking insights into user-friendly conclusions."
    )

    # Setup LLM and tools
    llm = Ollama(model="llama3", temperature=0.3)

    tools = [
        analyze_tool,
        summarizer_tool
    ]

    # Initialize agent with error handling
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True  # Add this to handle parsing errors
    )

    # Run agent
    try:
        query = "Analyze the transactions in transactions.json and summarize any risky activity"
        print("\n🤖 Running agent with query:", query)
        response = agent.invoke({"input": query})

        print("\n🔍 Agent response:", response)
        output_text = response.get("output", "")
        
        # Use summarizer
        print("\n📊 Creating final summary...")
        final_summary = summarize_insights(output_text)
        print("\n🧠 Final Summary:\n", final_summary)
    except Exception as e:
        print(f"\n❌ Agent execution error: {e}")
else:
    print("\n❌ Cannot run agent because transaction analyzer isn't working properly.")
    print("Please fix the transaction data issue first.")