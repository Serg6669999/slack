from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def slack(request):
    if request.method == 'POST':
        data = request.body
        data_dict = json.loads(data)
        challenge = data_dict['challenge']
        response_dict = {'challenge': challenge}
        # type = data_dict['url_verification']
        # token = 'snb408WDDGItzsJ9hagIfNHK'
        return JsonResponse(response_dict)
