import requests
from django.http import JsonResponse
from django.shortcuts import render

# Replace with your Wit.ai access token
WIT_ACCESS_TOKEN = "your_wit_ai_access_token"

def chatbot(request):
    if request.method == "POST":
        user_message = request.POST.get("message")
        if user_message:
            # Send user input to Wit.ai
            headers = {"Authorization": f"Bearer {WIT_ACCESS_TOKEN}"}
            response = requests.get(f"https://api.wit.ai/message?v=20220714&q={user_message}", headers=headers)
            data = response.json()

            # Extract intent and response
            intent = data.get("intents", [{}])[0].get("name", "no_intent")
            entities = data.get("entities", {})

            # Custom logic based on intent
            if intent == "greeting":
                bot_response = "Hello! How can I assist you with your events today?"
            elif intent == "ask_event":
                bot_response = "Can you specify the event details?"
            elif intent == "book_event":
                bot_response = "Booking your event! Please wait..."
            else:
                bot_response = "Sorry, I didn’t understand that."

            return JsonResponse({"response": bot_response})

    return render(request, "chatbot.html")


# Create your views here.
