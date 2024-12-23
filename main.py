from crewai import Crew
import agents
import tasks
import csv
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Set environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = os.getenv("OPENAI_MODEL_NAME")


# 1. Create agents
agent = agents.EmailPersonalizerAgent()

email_personalizer_agent = agent.personalize_email_agent()
ghostwriter_agent = agent.ghostwriter_agent()

# 2. Create task
task = tasks.EmailPersonalizationTask()

personalize_email_task = []
ghostwriter_task = []

file_path = "data/data.csv"
with open(file_path, "r") as file:
    csv_reader = csv.DictReader(file)
    for line in csv_reader:
        recipient = {
            "full_name": line["FullName"],
            "college": line["College"],
            "email": line["Email"]
        }

        personalize_email = task.personalize_email(agent=email_personalizer_agent, recipient=recipient)
        personalize_email_task.append(personalize_email)
        ghostwriter = task.ghostwriter_task(agent=ghostwriter_agent, recipient=recipient, draft_email=personalize_email)
        ghostwriter_task.append(ghostwriter)
    
# 3. Setup crew 
crew = Crew(
    agents=[email_personalizer_agent, ghostwriter_agent],
    tasks=[
        *personalize_email_task,
        *ghostwriter_task
    ],
    max_rpm=29
)

# 4. Kickoff crew
crew.kickoff()
