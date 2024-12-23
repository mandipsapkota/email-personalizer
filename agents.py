from crewai import Agent
from langchain_groq import ChatGroq
import os

class EmailPersonalizerAgent:
    def __init__(self):
        self.llm = ChatGroq(
            api_key=os.getenv("OPENAI_API_KEY"),
            model=os.getenv("OPENAI_MODEL_NAME"),
        )

    def personalize_email_agent(self):
        return Agent(
            role="Email Personalizer",
            model=self.llm,
            goal="""
            To create personalized email content that resonates with the recipient and increases engagement. 
            It should focus on professionally asking clients if they want a website with benefits included.
            """,
            backstory="""
            The agent is designed to understand the context and preferences of the email recipient, using advanced \
            language models to tailor the email content accordingly.
            """,
            verbose=True,
            max_iter=2
        )
    
    def ghostwriter_agent(self):
        return Agent(
            role="Ghostwriter",
            model=self.llm,
            goal="""
            To generate high-quality content that is engaging and informative. 
            It should focus on creating content that resonates with the target audience in a professional sales-oriented tone.
            """,
            backstory="""
            The agent is designed to leverage advanced language models to generate content that is tailored to the \
            turn data given to an compelling email utilising several sales and storytelling conceps.
            """,
            verbose=True,
            max_iter=2
        )
