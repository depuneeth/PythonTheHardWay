import http.client, json
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import csv
from tqdm import tqdm


conn = http.client.HTTPSConnection("cricketapi-icc.pulselive.com")
payload = ''
headers = {}

data_rows = []

first_day = (datetime.now() - timedelta(30))
# first_day = datetime.now()

days = (datetime.now() - first_day).days


for date in tqdm([first_day + timedelta(day) for day in range(days + 1)]):
    date = str(date).split(' ')[0]

    urls = {
        'batsman': f"/icc-ratings/ranked/players/odi/bat?pageSize=100&dmsPlayerIdRequired=true&at={date}",
        'bowler': f"/icc-ratings/ranked/players/odi/bowl?pageSize=100&dmsPlayerIdRequired=true&at={date}",
        'all_rounder': f"/icc-ratings/ranked/players/odi/allround?pageSize=20&dmsPlayerIdRequired=true&at={date}"
    }

    for player_type, url in urls.items():

        conn.request("GET", url, payload, headers)
        res = conn.getresponse()
        data = res.read()
        data_json = json.loads(data)
        players_data = data_json['content']

        for player_data in players_data:
            data_row = dict()
            player_data_object = player_data['player']
            data_row['id'] = player_data_object.get('id', 'NA')
            data_row['fullName'] = player_data_object.get('fullName', 'NA')
            data_row['nationality'] = player_data_object.get('nationality', 'NA')
            data_row['rating'] = player_data.get('rating', 'NA')
            data_row['type'] = player_type
            data_row['date'] = date
            data_rows.append(data_row)

keys = data_rows[0].keys()
with open('players_data_sample.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data_rows)
