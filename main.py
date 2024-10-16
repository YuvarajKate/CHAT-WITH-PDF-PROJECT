import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from transformers import pipeline
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

def get_pdf_text(pdf_docs):
    """Extracts text from uploaded PDFs."""
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text() or ""  # Ensure we handle None types
    return text

def answer_question(question, combined_text, model_name):
    """Uses the model to answer the question based on combined text."""
    st.write("Question:", question)  # Debug: Print the question
    
    # Load the question-answering model
    model = pipeline("question-answering", model=model_name)
    
    if len(combined_text) == 0:
        st.write("Combined text is empty! Please check your PDF input.")  # Check for empty text
        return "No context available."
    
    # Get the answer from the model
    outputs = model(question=question, context=combined_text)
    
    return outputs['answer'] if 'answer' in outputs else "No answer found."

def main():
    """Main function for the Streamlit app."""    
    load_dotenv()
    st.set_page_config(page_title="Chat with PDFs", page_icon=":books:")

    st.header("Chat with PDFs :books:")
    
    # PDF upload section
    pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True)

    # Store chat history in session state
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Process button
    if st.button("Process"):
        if pdf_docs:
            with st.spinner("Processing"):
                # Get PDF text
                combined_text = get_pdf_text(pdf_docs)
                
                st.session_state.combined_text = combined_text  # Store combined text in session state
                
                # Display success message in green box
                st.success("PDF processed successfully. Ask your question now.")

    # Input box for the question
    question = st.text_input("Ask your question:", value=st.session_state.get('question', ""))
    
    if question:  # Check if a question has been entered
        answer = answer_question(question, st.session_state.get('combined_text', ""), "deepset/roberta-base-squad2")

        st.session_state.chat_history.append((question, answer))  # Append to chat history
        
        # Clear the question input after answering
        st.session_state.question = ""  # Clear the question in session state

    # Display chat history
    if st.session_state.chat_history:
        st.subheader("Chat History")
        for q, a in reversed(st.session_state.chat_history):  # Display most recent Q&A first
            st.write(f"**Q:** {q}")
            st.write(f"**A:** {a}")

if __name__ == '__main__':
    main()
