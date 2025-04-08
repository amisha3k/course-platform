# src/chatbot/utils.py

def get_prompt(user_message):
    faq_data = {
        "how to enroll": "To enroll in a course, go to the course page and click 'Enroll Now'.",
        "how to reset password": "Click on 'Forgot Password' on the login page and follow the instructions.",
        "how to access certificate": "Certificates can be accessed from your profile under 'My Certificates'.",
    }

    for question, answer in faq_data.items():
        if question in user_message.lower():
            return f"You are a support assistant. Answer this based on internal knowledge:\nQ: {user_message}\nA: {answer}"

    return f"""
    You are a support + learning assistant on an online course platform.

    If the question is about platform usage (enrollment, login, certificate, etc.), answer directly.
    If the question is about course content, explain the topic simply using examples if possible.

    User: {user_message}
    Assistant:
    """
