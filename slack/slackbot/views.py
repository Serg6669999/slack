from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def slack(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_dict = json.loads(data)
        try:
            challenge = data_dict['challenge']
            response_dict = {'challenge': challenge}
            return JsonResponse(response_dict)
            # type = data_dict['url_verification']
            # token = 'snb408WDDGItzsJ9hagIfNHK'
        except KeyError:
            return JsonResponse(data_dict)


post_request = {
                "token": "one-long-verification-token",
                "team_id": "T061EG9R6",
                "api_app_id": "A0PNCHHK2",
                "event": {
                    "type": "message",
                    "channel": "D024BE91L",
                    "user": "U2147483697",
                    "text": "Hello hello can you hear me?",
                    "ts": "1355517523.000005",
                    "event_ts": "1355517523.000005",
                    "channel_type": "im"
                },
                "type": "event_callback",
                "authed_teams": ["T061EG9R6"],
                "event_id": "Ev0PV52K21",
                "event_time": 1355517523
                }
response = {
            "token": "z26uFbvR1xHJEdHE1OQiO6t8",
            "team_id": "T061EG9RZ",
            "api_app_id": "A0FFV41KK",
            "event": {
                    "type": "reaction_added",
                    "user": "U061F1EUR",
                    "item": {
                            "type": "message",
                            "channel": "C061EG9SL",
                            "ts": "1464196127.000002"
                            },
                    "reaction": "slightly_smiling_face",
                    "item_user": "U0M4RL1NY",
                    "event_ts": "1465244570.336841"
                     },
            "type": "event_callback",
            "authed_users": "U061F7AUR",
            "event_id": "Ev9UQ52YNA",
            "event_time": 1234567890
            }
