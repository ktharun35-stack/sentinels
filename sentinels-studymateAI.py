import fitz  # PyMuPDF
import openai

# Initialize OpenAI API key (replace with your key)
openai.api_key = 'YOUR_OPENAI_API_KEY'

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def ask_studymate(question, context_text):
    """
    Ask a question to the StudyMate model with context.
    We provide the text as context to GPT and ask for a precise answer.
    """
    prompt = f"""You are an AI academic assistant. Use the following context to answer the question accurately and concisely.

Context:
\"\"\"
{context_text}
\"\"\"

Question: {question}

Answer:"""

    response = openai.Completion.create(
        engine="text-davinci-003",  # or "gpt-4" if you have access
        prompt=prompt,
        max_tokens=300,
        temperature=0.2,
        n=1,
        stop=None,
    )
    answer = response.choices[0].text.strip()
    return answer

def main():
    # Load PDFs
    pdf_files = ["example1.pdf", "example2.pdf"]  # Replace with your PDF files
    combined_text = ""

    for pdf_file in pdf_files:
        print(f"Extracting text from {pdf_file}...")
        combined_text += extract_text_from_pdf(pdf_file) + "\n"

    print("Ready to answer your questions! (type 'exit' to quit)")

    while True:
        user_question = input("Ask a question: ")
        if user_question.lower() == "exit":
            break

        answer = ask_studymate(user_question, combined_text)
        print(f"StudyMate answer:\n{answer}\n")

if __name__ == "__main__":
    main()
