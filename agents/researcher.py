# # # # # # # 
# # # # # # # import os
# # # # # # # from dotenv import load_dotenv
# # # # # # # from langchain_google_genai import ChatGoogleGenerativeAI

# # # # # # # load_dotenv()

# # # # # # # def get_llm():
# # # # # # #     return ChatGoogleGenerativeAI(
# # # # # # #         model="gemini-2.5-flash",
# # # # # # #         google_api_key=os.getenv("GOOGLE_API_KEY")
# # # # # # #     )


# # # # # # # def run_researcher(plan: str):
# # # # # # #     llm = get_llm()

# # # # # # #     prompt = f"""
# # # # # # # You are a deep research agent.

# # # # # # # Expand the following plan into detailed research content with explanations, examples, and structure.

# # # # # # # PLAN:
# # # # # # # {plan}
# # # # # # # """

# # # # # # #     return llm.invoke(prompt).content
# # # # # # # from tools.web_search import search_web
# # # # # # # from langchain_google_genai import ChatGoogleGenerativeAI
# # # # # # # import os

# # # # # # # llm = ChatGoogleGenerativeAI(
# # # # # # #     model="gemini-2.5-flash",
# # # # # # #     google_api_key=os.environ["GOOGLE_API_KEY"]
# # # # # # # )

# # # # # # # def run_researcher(plan: str) -> str:
# # # # # # #     web_data = search_web(plan)

# # # # # # #     response = llm.invoke(f"""
# # # # # # # Use this research data to expand the plan:

# # # # # # # PLAN:
# # # # # # # {plan}

# # # # # # # WEB DATA:
# # # # # # # {web_data}

# # # # # # # Give detailed structured research notes.
# # # # # # # """)

# # # # # # #     return response.content
# # # # # # # from tools.web_search import search_web
# # # # # # # from langchain_google_genai import ChatGoogleGenerativeAI
# # # # # # # import os

# # # # # # # llm = ChatGoogleGenerativeAI(
# # # # # # #     model="gemini-2.5-flash",
# # # # # # #     google_api_key=os.environ["GOOGLE_API_KEY"]
# # # # # # # )

# # # # # # # def run_researcher(plan: str) -> str:
# # # # # # #     # Step 1: get web info
# # # # # # #     web_data = search_web(plan)

# # # # # # #     # Step 2: build prompt
# # # # # # #     prompt = f"""
# # # # # # # You are a research agent.

# # # # # # # Use the PLAN and WEB DATA to create a detailed research report.

# # # # # # # PLAN:
# # # # # # # {plan}

# # # # # # # WEB DATA:
# # # # # # # {web_data}

# # # # # # # Return a structured, detailed explanation.
# # # # # # # """

# # # # # # #     # Step 3: generate response
# # # # # # #     response = llm.invoke(prompt)

# # # # # # #     # Step 4: return output
# # # # # # #     return response.content
# # # # # # from tools.web_search import search_web
# # # # # # from langchain_google_genai import ChatGoogleGenerativeAI
# # # # # # import os

# # # # # # llm = ChatGoogleGenerativeAI(
# # # # # #     model="gemini-2.5-flash",
# # # # # #     google_api_key=os.environ["GOOGLE_API_KEY"]
# # # # # # )

# # # # # # def run_researcher(plan: str) -> str:
# # # # # #     web_data = search_web(plan)

# # # # # #     prompt = f"""
# # # # # # You are a research agent.

# # # # # # Use the web data and expand the plan into detailed research notes.

# # # # # # PLAN:
# # # # # # {plan}

# # # # # # WEB DATA:
# # # # # # {web_data}

# # # # # # Return structured bullet-point research.
# # # # # # """

# # # # # #     return llm.invoke(prompt).content
# # # # # from tools.web_search import search_web
# # # # # from langchain_google_genai import ChatGoogleGenerativeAI
# # # # # import os
# # # # # from dotenv import load_dotenv

# # # # # load_dotenv()

# # # # # llm = ChatGoogleGenerativeAI(
# # # # #     model="gemini-1.5-flash",
# # # # #     google_api_key=os.getenv("GOOGLE_API_KEY"),
# # # # #     temperature=0.3
# # # # # )

# # # # # def run_researcher(plan: str) -> str:
# # # # #     web_data = search_web(plan)

# # # # #     prompt = f"""
# # # # # You are a research agent.

# # # # # Expand the plan using web data.

# # # # # PLAN:
# # # # # {plan}

# # # # # WEB DATA:
# # # # # {web_data}

# # # # # Return structured bullet points.
# # # # # """

# # # # # #     return llm.invoke(prompt).content
# # # # # from tools.web_search import search_web
# # # # # from utils.llm import get_llm

# # # # # def run_researcher(plan: str):
# # # # #     llm = get_llm()

# # # # #     web_data = search_web(plan)

# # # # #     prompt = f"""
# # # # # You are a research agent.

# # # # # Use the web data to expand the plan into detailed information.

# # # # # PLAN:
# # # # # {plan}

# # # # # WEB DATA:
# # # # # {web_data}

# # # # # Return structured research notes.
# # # # # """

# # # # #     return llm.invoke(prompt).content
# # # # from tools.web_search import search_web
# # # # from llm import get_llm

# # # # def run_researcher(plan: str):
# # # #     llm = get_llm()

# # # #     web_data = search_web(plan)

# # # #     prompt = f"""
# # # # You are a research agent.

# # # # Plan:
# # # # {plan}

# # # # Web data:
# # # # {web_data}

# # # # Expand the research clearly.
# # # # """

# # # #     return llm.invoke(prompt).content
# # # from tools.web_search import search_web
# # # from langchain_google_genai import ChatGoogleGenerativeAI
# # # import os
# # # from dotenv import load_dotenv

# # # load_dotenv()

# # # llm = ChatGoogleGenerativeAI(
# # #     model="gemini-1.5-flash",
# # #     google_api_key=os.getenv("GOOGLE_API_KEY")
# # # )

# # # def run_researcher(plan: str) -> str:
# # #     web_data = search_web(plan)

# # #     prompt = f"""
# # # You are a research agent.

# # # Plan:
# # # {plan}

# # # Web Data:
# # # {web_data}

# # # Expand into detailed explanation.
# # # """

# # #     return llm.invoke(prompt).content
# # # from tools.web_search import search_web
# # # from langchain_google_genai import ChatGoogleGenerativeAI
# # # import os
# # # from dotenv import load_dotenv

# # # load_dotenv()

# # # llm = ChatGoogleGenerativeAI(
# # #     model="models/gemini-2.5-flash",
# # #     google_api_key=os.getenv("GOOGLE_API_KEY")
# # # )

# # # def run_researcher(plan: str) -> str:
# # #     web_data = search_web(plan)

# # #     prompt = f"""
# # # You are a research agent.

# # # PLAN:
# # # {plan}

# # # WEB DATA:
# # # {web_data}

# # # Expand into detailed explanation.
# # # """

# # #     return llm.invoke(prompt).content
# # from tools.web_search import search_web
# # from langchain_groq import ChatGroq
# # import os
# # from dotenv import load_dotenv

# # load_dotenv()

# # def get_llm():
# #     return ChatGroq(
# #         model="llama-3.3-70b-versatile",
# #         api_key=os.getenv("GROQ_API_KEY")
# #     )

# # def run_researcher(plan: str) -> str:
# #     llm = get_llm()

# #     web_data = search_web(plan)

# #     prompt = f"""
# # You are a research agent.

# # Task: Expand the given plan using web data and add useful insights.

# # PLAN:
# # {plan}

# # WEB DATA:
# # {web_data}

# # Return a detailed explanation.
# # """

# #     return llm.invoke(prompt).content.strip()
# from tools.web_search import search_web
# from utils.llm import get_llm

# def run_researcher(plan: str) -> str:
#     llm = get_llm()
#     web_data = search_web(plan)
#     prompt = f"""
# You are a research agent.

# Task: Expand the given plan using web data and add useful insights.

# PLAN:
# {plan}

# WEB DATA:
# {web_data}

# Return a detailed explanation.
# """
#     return llm.invoke(prompt).content.strip()
from tools.web_search import search_web
from tools.rag_tool import add_to_vectordb, search_vectordb
from utils.llm import get_llm

def run_researcher(plan: str) -> str:
    llm = get_llm()

    # Search web
    web_data = search_web(plan)

    # Store web results in vector DB
    chunks = [chunk.strip() for chunk in web_data.split("\n") if chunk.strip()]
    add_to_vectordb(chunks)

    # Retrieve relevant context from vector DB
    rag_context = search_vectordb(plan)

    prompt = f"""
You are a research agent.

Task: Expand the given plan using web data and retrieved context.

PLAN:
{plan}

WEB DATA:
{web_data}

RELEVANT CONTEXT FROM KNOWLEDGE BASE:
{rag_context}

Return a detailed explanation.
"""
    return llm.invoke(prompt).content.strip()