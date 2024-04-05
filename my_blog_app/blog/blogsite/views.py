import uuid
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .story_generator import generate_story
from .models import Post
from .whisper_transcribe import transcribe_audio
from .chat_completion import generate_story
from .image_generation import generate_image


def index(request):
    return HttpResponse("Hello, welcome to the index page.")


def individual_post(request):
    recent_post = Post.objects.get(id__exact=1)
    return HttpResponse(recent_post.title + ": " + recent_post.content)


def generate_story_from_words(request):
    words = request.GET.get("words")  # Extract the expected words from the request
    story = generate_story(
        words
    )  # Call the generate_story function with the extracted words
    return JsonResponse({"story": story})  # Return the story as a JSON response


def get_story_from_description(request):
    context = {}
    user_input = ""
    if request.method == "GET":
        return render(request, "story_template.html")
    else:
        if "text_input" in request.POST:
            user_input += request.POST.get("text_input") + "\n"
        if "voice_input" in request.FILES:
            audio_file = request.FILES["voice_input"]
            file_name = str(uuid.uuid4()) + (audio_file.name or "")
            FileSystemStorage(location="/tmp").save(file_name, audio_file)
            user_input += transcribe_audio(f"/tmp/{file_name}")

        generated_story = generate_story(user_input)
        image_prompt = f"Generate an image that visually illustrates the essence of the following story: {generated_story}"
        image_url = generate_image(image_prompt)

        context = {
            "user_input": user_input,
            "generated_story": generated_story.replace("\n", "<br/>"),
            "image_url": image_url,
        }

        return render(request, "story_template.html", context)
