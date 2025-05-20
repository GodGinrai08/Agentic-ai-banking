import re
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

llm = Ollama(model="llama3", temperature=0.3)

prompt = PromptTemplate.from_template(
    "Summarize these banking insights and flag any anomalies:\n\n{insights}"
)

parser = StrOutputParser()
chain = prompt | llm | parser

def clean_text(text):
    # Remove non-printable characters and unusual unicode
    return re.sub(r"[^\x20-\x7E\n]", "", text)

def summarize_insights(insights_text: str):
    if not insights_text.strip():
        return "No insights to summarize."

    return chain.invoke({"insights": insights_text})
    
   
