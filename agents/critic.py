# # from langchain_google_genai import ChatGoogleGenerativeAI
# # import os

# # llm = ChatGoogleGenerativeAI(
# #     model="gemini-2.5-flash",
# #     google_api_key=os.environ["GOOGLE_API_KEY"]
# # )

# # def run_critic(final_text: str) -> str:
# #     response = llm.invoke(f"""
# # Review this content and improve it:

# # {final_text}

# # Fix:
# # - grammar
# # - structure
# # - remove repetition
# # Return improved final version only.
# # """)
# #     return response.content
# from langchain_groq import ChatGroq
# import os
# from dotenv import load_dotenv

# load_dotenv()

# def get_llm():
#     return ChatGroq(
#         model="llama-3.3-70b-versatile",
#         api_key=os.getenv("GROQ_API_KEY")
#     )

# def run_critic(final_text: str) -> str:
#     llm = get_llm()
#     response = llm.invoke(f"""
# Review this content and improve it:

# {final_text}

# Fix:
# - grammar
# - structure
# - remove repetition
# Return improved final version only.
# """)
#     return response.content
from utils.llm import get_llm

def run_critic(final_text: str) -> str:
    llm = get_llm()
    response = llm.invoke(f"""
Review this content and improve it:

{final_text}

Fix:
- grammar
- structure
- remove repetition
Return improved final version only.
""")
    return response.content