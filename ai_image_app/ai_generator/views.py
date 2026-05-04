import base64
import requests
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from .models import GeneratedImage
from django.core.files.base import ContentFile

def home(request):
    return render(request, "index.html")

def generate(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")

        response = requests.post(
            "https://api.openai.com/v1/images/generations",
            headers={
                "Authorization": f"Bearer {settings.OPENAI_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-image-1",
                "prompt": prompt,
                "size": "1024x1024"
            }
        )

        result = response.json()

        image_base64 = result["data"][0]["b64_json"]
        image_file = ContentFile(base64.b64decode(image_base64), name="img.png")

        obj = GeneratedImage.objects.create(prompt=prompt, image=image_file)

        return JsonResponse({
            "image_url": obj.image.url
        })