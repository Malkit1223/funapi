from django.http import JsonResponse

def goodnight(request):
    # Full message as one single text
    message = (
        "Ojou-sama, it's time to go to bed!"
      
        " Tomorrow will be the best test for you!"
    )
    return JsonResponse({"message": message})
