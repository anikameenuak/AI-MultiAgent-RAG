# # from langchain_google_genai import ChatGoogleGenerativeAI
# # import os
# # from dotenv import load_dotenv

# # load_dotenv()

# # llm = ChatGoogleGenerativeAI(
# #     model="gemini-2.5-flash",
# #     google_api_key=os.getenv("GOOGLE_API_KEY"),
# #     temperature=0.3
# # )

# # def run_summarizer(text: str):
# #     prompt = f"""
# # You are a professional AI summarizer.

# # Your job:
# # - Combine all research into a clean final answer
# # - Remove repetition
# # - Make it well structured
# # - Keep it simple and readable

# # INPUT:
# # {text}

# # OUTPUT:
# # Final polished answer only.
# # """

# #     response = llm.invoke(prompt)
# #     return response.content
# from langchain_groq import ChatGroq
# import os
# from dotenv import load_dotenv

# load_dotenv()

# def get_llm():
#     return ChatGroq(
#         model="llama-3.3-70b-versatile",
#         api_key=os.getenv("GROQ_API_KEY"),
#         temperature=0.3
#     )

# def run_summarizer(text: str):
#     llm = get_llm()
    
#     prompt = f"""
# You are a professional AI summarizer.

# Your job:
# - Combine all research into a clean final answer
# - Remove repetition
# - Make it well structured
# - Keep it simple and readable

# INPUT:
# {text}

# OUTPUT:
# Final polished answer only.
# """

#     response = llm.invoke(prompt)
#     return response.content
from utils.llm import get_llm

def run_summarizer(text: str) -> str:
    llm = get_llm()
    prompt = f"""
You are a professional AI summarizer.

Your job:
- Combine all research into a clean final answer
- Remove repetition
- Make it well structured
- Keep it simple and readable

INPUT:
{text}

OUTPUT:
Final polished answer only.
"""
    response = llm.invoke(prompt)
    return response.content