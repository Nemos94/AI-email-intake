from openai import OpenAI
from models import AIIntakeResponse
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

client = OpenAI()

# 🔹 Carregar Vector Store (RAG)
db = Chroma(
    persist_directory="vectorstore",
    embedding_function=OpenAIEmbeddings()
)

def retrieve_context(query: str) -> str:
    docs = db.similarity_search(query, k=3)
    return "\n\n".join([d.page_content for d in docs])

SYSTEM_PROMPT = """
You are an AI assistant that classifies customer messages for a CRM system.
Your output will be consumed by automated systems.

IMPORTANT RULES:
- You MUST always return a single valid JSON object.
- Do NOT include explanations, comments, markdown, or extra fields.
- Do NOT infer or add fields not defined in the schema.
- If a value cannot be determined, return null.
- If the answer is not supported by the provided documentation, clearly state that and escalate.

The JSON output MUST strictly follow this schema:

{
  "objectType": "Case | Lead",
  "category": "string | null",
  "priority": "Low | Medium | High",
  "sentiment": "Positive | Neutral | Negative",
  "summary": "string",
  "suggestedResponse": "string"
}
"""

def classify_message(message: str) -> AIIntakeResponse:
    context = retrieve_context(message)

    user_prompt = f"""
Customer message:
{message}

Relevant internal documentation:
{context}

Based ONLY on the information above, generate the JSON response.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0,
        response_format={ "type": "json_object" }
    )

    content = response.choices[0].message.content
    return AIIntakeResponse.model_validate_json(content)
