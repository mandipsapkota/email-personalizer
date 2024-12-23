from crewai import Task

email_template = """
Dear {name},

I hope this email finds you well. I am reaching out to you regarding {message}. 

--- body ---

Best regards,  
Mandip Sapkota
"""

class EmailPersonalizationTask:
    def personalize_email(self, agent, recipient):
        return Task(
            description=f"""
            The task is to personalize the email content for the recipient {recipient['full_name']} using the email template provided: 
            The recepient is stdying in {recipient["college"]} and has a email {recipient["email"]}.
            {email_template}
            """,
            agent=agent,
            expected_output="Personalized email draft .",
            async_execution=True,
        )
    
    def ghostwriter_task(self, agent, draft_email, recipient):
        return Task(
            description="""
            The task is to generate high-quality email for a sales pitch. This email should follow sales as well as storytelling concepts.
            """,
            context=[draft_email],
            agent=agent,
            expected_output="A professional, well-structured email.",
            output_file=f"output/{recipient['full_name']}_email.txt"  # Corrected dictionary reference
        )
