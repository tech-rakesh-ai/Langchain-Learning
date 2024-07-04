# Langchain-Learning

## Project Description

Langchain-Learning is a Streamlit-based learning tool that leverages OpenAI's language models (LLMs) to create interactive chains for exploring topics related to cricketers and historical events.

## Features

- **Streamlit Integration**: Utilizes Streamlit for building interactive web interfaces.
- **OpenAI Integration**: Integrates with OpenAI's language models (LLMs) for natural language processing tasks.
- **Chain-based Learning**: Implements sequential chains of prompts to fetch information about cricketers, their birth dates, and related historical events.

## Project Structure

### Files and Modules

- **langchain-chaining.py**:
  - Sets up Streamlit UI to search for cricketer information and retrieves related historical events using chained prompts and OpenAI's LLMs.
  
- **langchain-demo.py**:
  - Provides a demo interface using Streamlit and OpenAI's LLMs to fetch information based on user input topics.

### Components

- **Prompt Templates**:
  - Defines prompt templates for querying cricketer details (`name`), birth dates (`person`), and historical events (`dob`).

- **Memory Handling**:
  - Uses conversation buffer memories (`ConversationBufferMemory`) to store chat histories and descriptions.

- **Chains Setup**:
  - Establishes sequential chains (`SequentialChain`) combining multiple LLM chains (`LLMChain`) to gather and display comprehensive information.

## Getting Started

### Prerequisites

- Python (version 3.8 or higher)
- Streamlit
- OpenAI API Key

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your_username/Langchain-Learning.git
   cd Langchain-Learning
   ```

2. Create a virtual environment:

   ```shell
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   ```shell
   export OPENAI_API_KEY='your_openai_api_key'
   ```

5. Run the Streamlit app:

   ```shell
   streamlit run langchain-chaining.py
   ```

6. Explore the demo:

   ```shell
   streamlit run langchain-demo.py
   ```

### Usage

- Access the Streamlit app for Langchain-Learning to search for cricketer information and related historical events.
- Use the demo interface to interact with OpenAI's LLMs based on input topics.

## Contributors

- Rakesh Kumar (@tech-rakesh-ai)

