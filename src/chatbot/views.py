from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from dotenv import load_dotenv
import json
from openai import OpenAI  # New-style import for OpenAI v1.x

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Initialize the OpenAI client

@csrf_exempt
def chatbot_view(request):
    if request.method == "GET":
        return render(request, "chatbot/chat.html")

    if request.method == "POST":
        try:
            body = json.loads(request.body)
            message = body.get("message")
            print("Message received:", message)

            # 🧠 OpenAI Chat Completion (v1.x style)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": message}
                ]
            )
            reply = response.choices[0].message.content
            print("AI Reply:", reply)

            return JsonResponse({"response": reply})

        except Exception as e:
            print("🔥 Error occurred:\n", str(e))
            return JsonResponse({"error": "Something went wrong."}, status=500)
