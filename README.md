Sure! Below is the complete `README.md` file, including the newly added documentation:


# PDF Chat Application

## Overview
This project is a Streamlit application that allows users to interact with PDF documents by asking questions. It uses natural language processing (NLP) techniques to extract information from uploaded PDFs and provide relevant answers to user queries.

## Technologies Used
The following technologies and libraries were used in this project:

### 1. Streamlit
- **What is it?**
  Streamlit is an open-source app framework for Machine Learning and Data Science projects. It allows for the rapid development of interactive web applications using Python.
  
- **Why use it?**
  Streamlit simplifies the process of building user interfaces for data applications without the need for extensive web development knowledge. Its easy integration with Python makes it ideal for quickly deploying data-driven applications.

### 2. PyPDF2
- **What is it?**
  PyPDF2 is a Python library that enables reading and manipulating PDF files. It can extract text, merge PDFs, and split pages.
  
- **Why use it?**
  This library was used to extract text from uploaded PDF documents, allowing the application to process and analyze the content for answering user questions.

### 3. Transformers
- **What is it?**
  The Transformers library, developed by Hugging Face, provides state-of-the-art natural language processing models, including those for question answering.
  
- **Why use it?**
  We used the Transformers library to leverage pre-trained question-answering models (specifically `deepset/roberta-base-squad2`) to accurately answer user questions based on the context extracted from the PDFs.

### 4. Python-dotenv
- **What is it?**
  Python-dotenv is a library that reads key-value pairs from a `.env` file and can set them as environment variables.
  
- **Why use it?**
  This library is used to manage environment variables for the application, such as API keys or configuration settings, without hardcoding them into the codebase, enhancing security and flexibility.

### 5. Torch
- **What is it?**
  Torch is an open-source machine learning library that provides a flexible framework for building deep learning models.
  
- **Why use it?**
  The Transformers library requires Torch to run the models efficiently. Including it ensures that the NLP models can be loaded and utilized for answering questions.

## Installation
To set up this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root if needed, and add any necessary environment variables.

## Usage
1. Run the application:
   ```bash
   streamlit run app/main.py
   ```

2. Upload your PDF files using the file uploader in the application interface.

3. After processing, type your questions in the provided input box to get answers based on the PDF content.

## Contribution
Contributions are welcome! Please fork the repository and submit a pull request for any changes or enhancements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.





