# Email Customization AI Agent

Welcome to the Email Customization AI Agent! This project is designed to automate and streamline the process of personalizing and ghostwriting emails using AI.

```
Make sure to give this repo a star, and you can feel free to use it.
```

## How It Works

1. **Personalization:** An AI agent personalizes the email based on data provided.
2. **Ghostwriting:** Another AI agent crafts a professional email by referencing the data in `data/data.csv`.
3. **Output Storage:** The generated emails are saved in `output/personname.txt` for easy retrieval.

## Setup Instructions

To get started, follow the steps below:

```
Creating a virtual environment is optional, but I highly suggest you to do so.
```

### 1. Update Environment Variables
Replace the placeholders in the `.env` file with your Groq API key and model name:

```env
OPENAI_API_KEY = "Your_groq_key"
OPENAI_MODEL_NAME = "groq/model_from_groq"
```

### 2. Install Dependencies
Install the required Python libraries by running:

```bash
pip install -r requirements.txt
```

## Usage
After setting up, you can run the agent to personalize and generate emails. Ensure that the input data is correctly formatted in `data/data.csv` and check the output in the `output` directory.

Feel free to customise email template in `tasks.py`.

You can use this code to run it.
```python
python main.py
```