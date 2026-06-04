# # # # # # import os
# # # # # # from dotenv import load_dotenv
# # # # # # from langchain_google_genai import ChatGoogleGenerativeAI

# # # # # # load_dotenv()

# # # # # # def get_llm():
# # # # # #     api_key = os.getenv("GOOGLE_API_KEY")

# # # # # #     if not api_key:
# # # # # #         raise ValueError("GOOGLE_API_KEY not found in environment variables")

# # # # # #     return ChatGoogleGenerativeAI(
# # # # # #         model="gemini-2.5-flash",
# # # # # #         google_api_key=api_key
# # # # # #     )

# # # # # # def run_planner(query: str):
# # # # # #     llm = get_llm()

# # # # # #     prompt = f"""
# # # # # # You are a planning agent.

# # # # # # Break the following query into a structured step-by-step plan:

# # # # # # Query:
# # # # # # {query}

# # # # # # Return a numbered list plan.
# # # # # # """

# # # # # #     return llm.invoke(prompt).content
# # # # # import os
# # # # # from dotenv import load_dotenv
# # # # # from langchain_google_genai import ChatGoogleGenerativeAI

# # # # # load_dotenv()

# # # # # def get_llm():
# # # # #     api_key = os.getenv("GOOGLE_API_KEY")

# # # # #     if not api_key:
# # # # #         raise ValueError("GOOGLE_API_KEY not found in environment variables")

# # # # #     return ChatGoogleGenerativeAI(
# # # # #         model="gemini-2.5-flash",
# # # # #         google_api_key=api_key
# # # # #     )


# # # # # def run_planner(query: str):
# # # # #     llm = get_llm()

# # # # #     prompt = f"""
# # # # # You are an expert planning agent.

# # # # # Break the user query into a clear, structured step-by-step plan.

# # # # # Rules:
# # # # # - Make steps actionable
# # # # # - Keep steps logically ordered
# # # # # - Each step must be clear and specific
# # # # # - Return ONLY numbered steps

# # # # # User Query:
# # # # # {query}

# # # # # Final Plan:
# # # # # """

# # # # #     return llm.invoke(prompt).content
# # # # def run_planner(query: str):
# # # #     return f"""
# # # # 1. Understand topic: {query}
# # # # 2. Gather key concepts
# # # # 3. Explain step by step
# # # # 4. Provide final structured answer
# # # # """
# # # # from utils.llm import get_llm

# # # # def run_planner(query: str):
# # # #     llm = get_llm()

# # # #     prompt = f"""
# # # # You are a planning agent.

# # # # Break the query into clear steps:

# # # # Query:
# # # # {query}

# # # # Return numbered steps.
# # # # """

# # # #     return llm.invoke(prompt).content
# # # from llm import get_llm

# # # def run_planner(query: str):
# # #     llm = get_llm()

# # #     prompt = f"""
# # # You are a planning agent.

# # # Break this into steps:

# # # Query: {query}

# # # Return numbered list only.
# # # """

# # #     return llm.invoke(prompt).content
# # import os
# # from dotenv import load_dotenv
# # from langchain_google_genai import ChatGoogleGenerativeAI

# # load_dotenv()

# # def get_llm():
# #     api_key = os.getenv("GOOGLE_API_KEY")

# #     if not api_key:
# #         raise ValueError("GOOGLE_API_KEY missing")

# #     return ChatGoogleGenerativeAI(
# #         model="gemini-1.5-flash",   # IMPORTANT FIX
# #         google_api_key=api_key
# #     )

# # def run_planner(query: str):
# #     llm = get_llm()

# #     prompt = f"""
# # You are a planning agent.

# # Break the query into step-by-step plan:

# # {query}

# # Return numbered steps.
# # """

# #     return llm.invoke(prompt).content
# import os
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI

# load_dotenv()

# def get_llm():
#     return ChatGoogleGenerativeAI(
#         model="gemini-2.5-flash",
#         google_api_key=os.getenv("GOOGLE_API_KEY")
#     )

# def run_planner(query: str):
#     llm = get_llm()

#     prompt = f"""
# You are a planning agent.

# Break this query into step-by-step plan:

# {query}
# """

# #     return llm.invoke(prompt).content
# import os
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI

# load_dotenv()

# def get_llm():
#     return ChatGoogleGenerativeAI(
#         model="gemini-2.5-flash",   # ✅ correct model
#         google_api_key=os.getenv("GOOGLE_API_KEY")
#     )

# def run_planner(query: str):
#     llm = get_llm()

#     prompt = f"""
# You are an expert AI planning agent.

# Task: Break the user query into a clear step-by-step execution plan.

# Rules:
# - Keep steps numbered
# - Each step should be actionable
# - Do not add explanations

# User Query:
# {query}

# Return only the plan.
# """

#     return llm.invoke(prompt).content
# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# load_dotenv()

# def get_llm():
#     return ChatGroq(
#         model="llama-3.3-70b-versatile",
#         api_key=os.getenv("GROQ_API_KEY")
#     )

# def run_planner(query: str):
#     llm = get_llm()

#     prompt = f"""
# You are an expert AI planning agent.

# Task: Break the user query into a clear step-by-step execution plan.

# Rules:
# - Keep steps numbered
# - Each step should be actionable
# - Do not add explanations

# User Query:
# {query}

# Return only the plan.
# """

#     return llm.invoke(prompt).content
from utils.llm import get_llm

def run_planner(query: str):
    llm = get_llm()
    prompt = f"""
You are an expert AI planning agent.

Task: Break the user query into a clear step-by-step execution plan.

Rules:
- Keep steps numbered
- Each step should be actionable
- Do not add explanations

User Query:
{query}

Return only the plan.
"""
    return llm.invoke(prompt).content