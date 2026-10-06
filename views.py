from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .ai_model import predict_sentiment


def home(request):

    result = None
    confidence = None
    user_text = ""

    if request.method == "POST":

        user_text = request.POST.get("text", "").strip()

        if user_text:

            result, confidence = predict_sentiment(user_text)

    context = {
        "result": result,
        "confidence": confidence,
        "user_text": user_text
    }

    return render(request, "sentiment/home.html", context)
