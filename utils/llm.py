
# # # import os
# # # from dotenv import load_dotenv
# # # from langchain_google_genai import ChatGoogleGenerativeAI

# # # load_dotenv()

# # # def get_llm():
# # #     api_key = os.getenv("GOOGLE_API_KEY")

# # #     if not api_key:
# # #         raise ValueError("GOOGLE_API_KEY missing in .env")

# # #     return ChatGoogleGenerativeAI(
# # #         model="gemini-1.5-flash",   # ✅ FIXED MODEL
# # #         google_api_key=api_key,
# # #         temperature=0.3
# # #     )

# # import os
# # from dotenv import load_dotenv
# # from langchain_google_genai import ChatGoogleGenerativeAI

# # load_dotenv()

# # def get_llm():
# #     api_key = os.getenv("GOOGLE_API_KEY")

# #     if not api_key:
# #         raise ValueError("GOOGLE_API_KEY missing")

# #     return ChatGoogleGenerativeAI(
# #         model="gemini-pro",   # ✅ MOST STABLE FIX
# #         google_api_key=api_key,
# #         temperature=0.3
# #     )
# import os
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI

# load_dotenv()

# def get_llm():
#     api_key = os.getenv("GOOGLE_API_KEY")

#     if not api_key:
#         raise ValueError("GOOGLE_API_KEY missing")

#     return ChatGoogleGenerativeAI(
#         model=""gemini-2.5-flash"",
#         google_api_key=api_key,
#         temperature=0.3
# #     )
# import os
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI

# load_dotenv()

# def get_llm():
#     return ChatGoogleGenerativeAI(
#         model="gemini-2.5-flash",   # ✅ FIXED MODEL
#         google_api_key=os.getenv("GOOGLE_API_KEY")
#     )
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def get_llm():
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY")
    )