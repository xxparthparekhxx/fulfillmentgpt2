from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .generate_text import generate_text
import json
import requests


@csrf_exempt
def generate_text_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data['queryResult']['action'] == "input.unknown":
            input_text = data['queryResult']['queryText']
            generated_text = generate_text(input_text)
            return JsonResponse({
                "fulfillmentMessages": [
                    {
                        "text": {
                            "text": [
                                generated_text
                            ]
                        }
                    }
                ]
            })
        else:
            response = requests.post(
                'https://dialogflowfullfillment.vercel.app/api/webhook', json=data)
            return JsonResponse(response.json())

@csrf_exempt
def me(request):
    return JsonResponse({
        "student_number":200542362,
        "name":"Parth Hiren Parekh",
    })
