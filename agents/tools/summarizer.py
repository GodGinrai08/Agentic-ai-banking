import re
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3", temperature=0.3)

prompt = PromptTemplate.from_template(
    "Summarize these banking insights and flag any anomalies:\n\n{insights}"
)

parser = StrOutputParser()
chain = prompt | llm | parser

def clean_text(text):
    # Remove non-printable characters and unusual unicode
    return re.sub(r"[^\x20-\x7E\n]", "", text)

def summarize_insights(inputs: dict) -> dict:
    insights = inputs.get("insights", [])

    if isinstance(insights, list):
        insights_text = "\n".join(insights)
    else:
        insights_text = str(insights)

    if not insights_text.strip():
        return {"summary": "No insights to summarize."}

    raw_summary = chain.invoke({"insights": insights_text})
    summary = clean_text(raw_summary)

    return {"summary": summary}
