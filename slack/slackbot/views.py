from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect
import json
import requests


@csrf_exempt
def slack(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_dict = json.loads(data)
        print(data_dict)
        try:
            challenge = data_dict['challenge']
            response_dict = {'challenge': challenge}
            return JsonResponse(response_dict)
            # type = data_dict['url_verification']
            # token = 'snb408WDDGItzsJ9hagIfNHK'
        except KeyError:
            token = data_dict['token']
            team_id = data_dict['team_id']
            api_app_id = data_dict['api_app_id']
            event = data_dict['event']
            type_event = event['type']
            channel = event['channel']
            user = event['user']
            text = event['text']
            ts = event['ts']
            event_ts = event['event_ts']
            channel_type = event['channel_type']
            type_request = data_dict['type']
            # authed_teams = data_dict['authed_teams']
            event_id = data_dict['event_id']
            event_time = data_dict['event_time']
            response = {"token": token,
                        "team_id": team_id,
                        "api_app_id": api_app_id,
                        "event": {"type": type_event,
                                  "user": user,
                                  "text": text,
                                  "item": {"type": "message",
                                           "channel": channel,
                                           "ts": ts,
                                           },
                                  "reaction": "slightly_smiling_face",
                                  "item_user": user,
                                  "event_ts": event_ts,
                                  "channel_type": channel_type,

                                  },
                        "type": type_request,
                        "authed_users": user,
                        "event_id": event_id,
                        "event_time": event_time,
                        }
            response_3 = {"type": "reaction_added",
                          "user": user,
                          "reaction": "thumbsup",
                          "item_user": user,
                          "item": {"type": "message",
                                   "channel": channel,
                                   "ts": ts,
                                   "text": text,
                                   },
                          "event_ts": event_ts
                          }
            response_massage = {"channel": channel,
                                "text": "Что желаете?",
                                "token": 'xoxp-870665549127-856024027186-857382292611-b0ed9a6bc5e54bb6bc90d9bdbc700b8e'
                                }
            url_slack_massage = 'https://slack.com/api/chat.postMessage'
            send_massage_slack_bot = requests.post(url_slack_massage, json=response_massage)
            print(send_massage_slack_bot.content)


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
response_ = {
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
response_2 = {
    "type": "reaction_added",
    "user": "U024BE7LH",
    "reaction": "thumbsup",
    "item_user": "U0G9QF9C6",
    "item": {
        "type": "message",
        "channel": "C0G9QF9GZ",
        "ts": "1360782400.498405"
    },
    "event_ts": "1360782804.083113"
}
