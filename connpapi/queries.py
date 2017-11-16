from datetime import datetime
from urllib.parse import urlencode
from connpass import Connpass


def event_proc(query=None):
    # Context provider to provide event data
    MAPS_URL = "https://www.google.com/maps/search/?api=1&"

    response = {
        "event_url": "https://bpstudy.connpass.com/event/364/",
        "event_type": "participation",
        "owner_nickname": "haru860",
        "series": {
            "url": "https://bpstudy.connpass.com/",
            "id": 1,
            "title": "BPStudy"
        },
        "updated_at": "2014-06-30T10:06:19+09:00",
        "lat": "35.672968000000",
        "started_at": "2012-04-17T18:30:00+09:00",
        "hash_tag": "bpstudy",
        "title": "BPStudy#56",
        "event_id": 364,
        "lon": "139.716904600000",
        "waiting": 3,
        "limit": 4,
        "owner_id": 8,
        "owner_display_name": "佐藤 治夫",
        "description": "<div style=\"font-size:10pt;font-style:normal;font-weight:normal;\"><div style=\"font-size:10pt;\"><span style=\"font-size:10pt;\">BPStudy#56はオープンクラウドキャンパスさん、hbstudyさんとの共同開催です。</span></div></div><div style=\"font-size:10pt;font-style:normal;font-weight:normal;\"><br /></div><div style=\"font-size:10pt;\"><font size=\"4\" color=\"#ff6666\"><span>「</span><font>USクラウド最新動向勉強会 Softlayer社に学ぶ競争力」</font></font></div><div style=\"font-size:10pt;\"><font size=\"2\"><br /></font></div><div style=\"font-style:normal;font-weight:normal;\"><font size=\"4\">参加登録は以下からお願いします。</font></div><div style=\"font-size:10pt;font-style:normal;font-weight:normal;\">↓　↓　↓</div><div><font size=\"4\"><a href=\"http://connpass.com/event/360/\" rel=\"nofollow\">http://connpass.com/event/360/</a></font></div>",
        "address": "東京都港区北青山2-8-44",
        "catch": "株式会社ビープラウドが主催するWeb系技術討論の会",
        "accepted": 4,
        "ended_at": "2012-04-17T20:30:00+09:00",
        "place": "先端技術館＠TEPIA"
    }

    if query:
        keywords = query.get('keywords', None).split()
        count = int(query.get('count', None))
        start_date = query.get('start_date', []).split()
        nickname = query.get('nickname', []).split()
        owner_nickname = query.get('owner_nickname', []).split()

        response = Connpass().search(keyword=keywords, count=count, start=start_date, nickname=nickname,
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
