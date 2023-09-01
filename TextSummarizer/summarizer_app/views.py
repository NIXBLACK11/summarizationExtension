from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from transformers import pipeline

model_name = "sshleifer/distilbart-cnn-12-6"
model_revision = "a4f8f3e"
summarizer = pipeline("summarization", model=model_name, revision=model_revision)

@csrf_exempt
def summarize_text(request):
    if request.method == 'POST':
        try:
            input_text = request.POST.get('input_text', '')
            if input_text:
                summary = summarizer(input_text, max_length=150, min_length=40, do_sample=False)
                summarized_text = summary[0]['summary_text']
                return JsonResponse({'summarized_text': summarized_text})
            else:
                return JsonResponse({'error': 'Input text is missing.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)
