import csv
from mordecai import Geoparser
from functools import reduce
import json

geo = Geoparser()
ALL_Location = []
run_function = lambda x, y: x if y in x else x + [y]

with open('data/water_quality.csv', errors="ignore") as f:
    Reader = csv.DictReader(f)
    for row in Reader:
        a = row["Abstract"]
        t = row["Title"]
        try:
            geoINF = geo.geoparse(a)
        except:
            continue
        for i in range(len(geoINF)):
            location = {'place_name': '', 'country': '', 'lat': '', 'lon': '', 'article': t}
            try:
                a = geoINF[i]['geo']
            except:
                continue
            location['place_name'] = a['place_name']
            location['country'] = a['country_code3']
            location['lat'] = a['lat']
            location['lon'] = a['lon']
            ALL_Location.append(location)

all_location_lean = reduce(run_function, [[], ] + ALL_Location)
filename = 'WaterDataLoc.json'
with open(filename, 'w+') as file_obj:
    json.dump(all_location_lean, file_obj)