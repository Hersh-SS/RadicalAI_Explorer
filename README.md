# **Gemini Explorer**

## **Overview**

Gemini Explorer is an interactive web application built using Streamlit, designed to showcase the capabilities of Vertex AI's generative models. This application features ReX, a personalized assistant powered by Google Gemini, which interacts with users through a chat interface. ReX is designed to respond to user queries and provide a seamless conversational experience, utilizing emojis to enhance interaction.

The project leverages Vertex AI's generative models and Streamlit's interactive web framework to create a dynamic and user-friendly platform for exploring AI capabilities. The application captures user information to personalize interactions, making each session unique and engaging.

## **Key Features**

- **Personalized Interaction**: Captures user information to tailor responses.
- **Generative Model Integration**: Utilizes Vertex AI's generative models for dynamic responses.
- **Interactive Chat Interface**: Built with Streamlit for real-time user interaction.
- **Emoji Integration**: Enhances interaction with emojis for a more engaging experience.

## **Installation**

### **Prerequisites**

Before you begin, ensure you have the following installed on your system:

- Python 3.6 or higher
- Streamlit
- Vertex AI Python SDK

### **Step-by-Step Installation Guide**

#### **1. Clone the Repository**

Start by cloning the repository to your local machine. Use the following command:

```bash
git clone https://github.com/Hersh-SS/RadicalAI_Explorer.git
cd RadicalAI_Explorer
```

#### **2. Set Up a Virtual Environment**

It's a good practice to create a virtual environment for your Python projects. This keeps your project dependencies isolated. If you have virtualenv installed, create a new environment with:

```bash
python -m venv venv
```

Activate the virtual environment:

Windows (PowerShell):
```bash
.\venv\Scripts\Activate.ps1
```

Windows (CMD):
```bash
.\venv\Scripts\activate
```

macOS/Linux:
```bash
source venv/bin/activate
```

#### **3. Install Dependencies**

Inside the virtual environment, install all necessary dependencies by running:
```bash
pip install -r requirements.txt
```

#### **4. Set Up Authentication for Vertex AI**
Download the JSON key file for your Google Cloud service account and set the GOOGLE_APPLICATION_CREDENTIALS environment variable:

Windows (PowerShell):
```bash
$env:GOOGLE_APPLICATION_CREDENTIALS="path\to\your\service-account-file.json"
```

Windows (CMD):
```bash
set GOOGLE_APPLICATION_CREDENTIALS=path\to\your\service-account-file.json
```

macOS/Linux:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-file.json"
```

#### **5. Run the Streamlit Application**
With the virtual environment activated and dependencies installed, you can start the Streamlit application by running:

```bash
streamlit run gemini_explorer.py
```

### **Accessing the Application**
With the server running, you can access the application at http://localhost:8501.

## **How It Works**

#### **1. Initialization:**
- The application initializes the Vertex AI generative model with the specified project ID.
- A chat session is started using the model.

#### **2. User Interaction:**
- The application captures the user's name at the beginning.
- The user's name is used to personalize the interaction with ReX.
- Users can enter queries through a chat input interface.

#### **3. Generative Responses:**
- ReX generates responses using Vertex AI's generative models.
- The responses are displayed in the chat interface, including emojis for enhanced interaction.

#### **4. Session Management:**
- The application maintains the chat history using Streamlit's session state.
- Each interaction is stored and displayed sequentially to simulate a continuous conversation.
