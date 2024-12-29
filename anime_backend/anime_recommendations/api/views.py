import json
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def get_anime_list(request):
    data = {
        "anime": [
            {"id": 1, "title": "Naruto"},
            {"id": 2, "title": "One Piece"},
            {"id": 3, "title": "Attack on Titan"}
        ]
    }
    return JsonResponse(data, safe=False)


@csrf_exempt
def anime_recommendation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            user_query = data.get('userQuery', '')

            # Example of using OpenAI (if you want):
            # import os
            # openai.api_key = os.getenv('OPENAI_API_KEY', '')
            # response = openai.Completion.create(
            #     model="text-davinci-003",
            #     prompt=f"Recommend an anime similar to {user_query}",
            #     max_tokens=50
            # )
            # recommendation_text = response.choices[0].text.strip()

            # For demonstration, just return a mock list:
            recommended_titles = [
                "Naruto",
                "One Piece",
                "My Hero Academia"
            ]

            return JsonResponse({"recommendedAnimeTitles": recommended_titles}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
