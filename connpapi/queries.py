from datetime import datetime
from urllib.parse import urlencode
from connpass import Connpass


def event_proc(query=None):
    # Context provider to provide event data
    MAPS_URL = "https://www.google.com/maps/search/?api=1&"

    if query:
        keyword = query.get('keyword', '').split()
        keyword_or = query.get('keyword_or', '').split()
        count = query.get('count', '10')
        ym = query.get('ym', []).split()
        nickname = query.get('nickname', '').split()
        owner_nickname = query.get('owner_nickname', '').split()
        response = Connpass().search(keyword=keyword, keyword_or=keyword_or, count=count, ym=ym, nickname=nickname,
                                     owner_nickname=owner_nickname)['events']

    else:
        response = Connpass().search(count=5)['events']

    response = sorted(response, key=lambda event: event['started_at'])

    for event in response:
        start_date = event['started_at']
        end_date = event['ended_at']
        event['started_at'] = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S+09:00")
        event['ended_at'] = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S+09:00")
        event['maps_url'] = MAPS_URL + urlencode({'lat': event['lat'], 'lon': event['lon'], 'query': event['place']})

    return response
