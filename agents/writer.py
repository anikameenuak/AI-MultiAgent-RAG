# # # # from langchain_google_genai import ChatGoogleGenerativeAI
# # # # import os
# # # # from dotenv import load_dotenv

# # # # load_dotenv()

# # # # def get_llm():
# # # #     return ChatGoogleGenerativeAI(
# # # #         model="gemini-2.5-flash",
# # # #         google_api_key=os.getenv("GOOGLE_API_KEY")
# # # #     )


# # # # def run_writer(research: str):
# # # #     llm = get_llm()

# # # #     prompt = f"""
# # # # You are a professional AI writer.

# # # # Convert the research into a clean final report.

# # # # Research:
# # # # {research}
# # # # """

# # # #     return llm.invoke(prompt).content
# # # from langchain_google_genai import ChatGoogleGenerativeAI
# # # import os
# # # from dotenv import load_dotenv

# # # load_dotenv()

# # # def get_llm():
# # #     api_key = os.getenv("GOOGLE_API_KEY")

# # #     if not api_key:
# # #         raise ValueError("GOOGLE_API_KEY not found in environment variables")

# # #     return ChatGoogleGenerativeAI(
# # #         model="gemini-2.5-flash",
# # #         google_api_key=api_key
# # #     )


# # # def run_writer(research: str):
# # #     llm = get_llm()

# # #     prompt = f"""
# # # You are a professional technical report writer.

# # # Convert the following research into a well-structured FINAL REPORT.

# # # Rules:
# # # - Use clear headings
# # # - Use bullet points where needed
# # # - Keep it professional and readable
# # # - Do NOT repeat raw research
# # # - Improve clarity and structure

# # # RESEARCH:
# # # {research}

# # # FINAL REPORT:
# # # """

# # #     return llm.invoke(prompt).content
# # # from langchain_google_genai import ChatGoogleGenerativeAI
# # # import os
# # # from dotenv import load_dotenv

# # # load_dotenv()

# # # llm = ChatGoogleGenerativeAI(
# # #     model="gemini-1.5-flash",
# # #     google_api_key=os.getenv("GOOGLE_API_KEY"),
# # #     temperature=0.5
# # # )

# # # def run_writer(research: str):
# # #     prompt = f"""
# # # You are an expert technical writer.

# # # Convert this into a clean final report:

# # # {research}

# # # Make it:
# # # - structured
# # # - simple
# # # - 5–10 lines if needed
# # # """

# # #     return llm.invoke(prompt).content
# # # from llm import get_llm

# # # def run_writer(research: str):
# # #     llm = get_llm()

# # #     prompt = f"""
# # # You are a professional writer.

# # # Convert into final report:

# # # {research}
# # # """

# # #     return llm.invoke(prompt).content
# # from langchain_google_genai import ChatGoogleGenerativeAI
# # import os
# # from dotenv import load_dotenv

# # load_dotenv()

# # def get_llm():
# #     return ChatGoogleGenerativeAI(
# #         model="gemini-1.5-flash",
# #         google_api_key=os.getenv("GOOGLE_API_KEY")
# #     )

# # def run_writer(research: str):
# #     llm = get_llm()

# #     prompt = f"""
# # You are a professional writer.

# # Convert this into a clean final report:

# # {research}
# # """

# #     return llm.invoke(prompt).content
# # import os
# # from dotenv import load_dotenv
# # from langchain_google_genai import ChatGoogleGenerativeAI

# # load_dotenv()

# # def get_llm():
# #     return ChatGoogleGenerativeAI(
# #         model="gemini-2.5-flash",   # ✅ correct model
# #         google_api_key=os.getenv("GOOGLE_API_KEY")
# #     )

# # def run_planner(query: str):
# #     llm = get_llm()

# #     prompt = f"""
# # You are an expert AI planning agent.

# # Task: Break the user query into a clear step-by-step execution plan.

# # Rules:
# # - Keep steps numbered
# # - Each step should be actionable
# # - Do not add explanations

# # User Query:
# # {query}

# # Return only the plan.
# # """

# #     return llm.invoke(prompt).content
# # import os
# # from dotenv import load_dotenv
# # from langchain_google_genai import ChatGoogleGenerativeAI

# # load_dotenv()

# # def get_llm():
# #     return ChatGoogleGenerativeAI(
# #         model="gemini-2.5-flash",
# #         google_api_key=os.getenv("GOOGLE_API_KEY")
# #     )

# # def run_writer(research: str):
# #     llm = get_llm()

# #     prompt = f"""
# # You are a professional AI technical writer.

# # Your task is to convert research into a well-structured final report.

# # Rules:
# # - Use clear headings if needed
# # - Keep output clean and readable
# # - Do NOT include planning steps
# # - Do NOT include raw research data

# # Research:
# # {research}

# # Final Answer:
# # """

# #     return llm.invoke(prompt).content.strip()
# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# load_dotenv()

# def get_llm():
#     return ChatGroq(
#         model="llama-3.3-70b-versatile",
#         api_key=os.getenv("GROQ_API_KEY")
#     )

# def run_writer(research: str):
#     llm = get_llm()

#     prompt = f"""
# You are a professional AI technical writer.

# Your task is to convert research into a well-structured final report.

# Rules:
# - Use clear headings if needed
# - Keep output clean and readable
# - Do NOT include planning steps
# - Do NOT include raw research data

# Research:
# {research}

# Final Answer:
# """

#     return llm.invoke(prompt).content.strip()
from utils.llm import get_llm

def run_writer(research: str) -> str:
    llm = get_llm()
    prompt = f"""
You are a professional AI technical writer.

Your task is to convert research into a well-structured final report.

Rules:
- Use clear headings if needed
- Keep output clean and readable
- Do NOT include planning steps
- Do NOT include raw research data

Research:
{research}

Final Answer:
"""
    return llm.invoke(prompt).content.strip()