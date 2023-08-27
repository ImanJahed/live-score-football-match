from django.shortcuts import render

from datetime import datetime
import requests


# Create your views here.
def index(request):
    today = datetime.today().strftime('%Y-%m-%d')
    url = f"https://apiv3.apifootball.com/?action=get_events&from={today}&to={today}&league_id=152&APIkey=26dd72fb44247a56c05b4282020113677824cec550aa00b1519bd0aefa685bf3"
    response = requests.get(url)
    json_response = response.json()
    league_logo, league_name = json_response[0]['league_logo'], json_response[0]['league_name']
    return render(request, 'score/index.html', {'json_response': json_response,
                                                'league_logo': league_logo, 'league_name': league_name})