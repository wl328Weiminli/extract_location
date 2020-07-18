import csv
from mordecai import Geoparser
from functools import reduce
import json

geo = Geoparser()
ALL_Location = []
run_function = lambda x, y: x if y in x else x + [y]

with open('data/covid_19.csv', errors="ignore") as f:
    Reader = csv.DictReader(f)
    for row in Reader:
        a = row["abstract"]
        t = row["title"]
        j = row["journal"]
        url = row["url"]
        try:
            geoINF = geo.geoparse(a)
        except:
            continue
        for i in range(len(geoINF)):
            location = {'word': '', 'place_name': '', 'country': '', 'lat': '', 'lon': '', 'title': t, 'journal': j,
                        'url': url}
            try:
                a = geoINF[i]['geo']
            except:
                continue
            com1 = geoINF[i]['word'].lower()
            com2 = a['place_name'].lower()
            if com1 in com2:
                location['word'] = geoINF[i]['word']
                location['place_name'] = a['place_name']
                location['country'] = a['country_code3']
                location['lat'] = a['lat']
                location['lon'] = a['lon']
                ALL_Location.append(location)

all_location_lean = reduce(run_function, [[], ] + ALL_Location)
filename = 'covid_location-2.json'
with open(filename, 'w+') as file_obj:
    json.dump(all_location_lean, file_obj)
