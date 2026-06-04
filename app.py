import streamlit as st
from graph.workflow import build_graph

st.set_page_config(page_title="AI Multi-Agent RAG", page_icon="🤖", layout="wide")

st.title("🤖 AI Multi-Agent RAG System")
st.markdown("Powered by LangGraph + Groq + ChromaDB")

query = st.text_input("Enter your query:", placeholder="e.g. What is machine learning?")

if st.button("Run Agents"):
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        with st.spinner("Running AI Agents..."):
            graph = build_graph()
            result = graph.invoke({"query": query})

        st.success("Done!")

        with st.expander("📋 Plan", expanded=False):
            st.markdown(result["plan"])

        with st.expander("🔍 Research", expanded=False):
            st.markdown(result["research"])

        st.subheader("📄 Final Output")
        st.markdown(result["final"])