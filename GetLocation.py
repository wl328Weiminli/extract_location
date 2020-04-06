import os
from mordecai import Geoparser
from typing import Tuple
from getName import file_name
from functools import reduce
import json

TxtData = file_name('data/docs')
BASE = "data/docs"
DOCS = TxtData

geo = Geoparser()


all_location = []
run_function = lambda x, y: x if y in x else x + [y]


def Get_Places(
        base: str, docs: Tuple[str, ...],
):
    for doc in docs:
        with open(os.path.join(base, doc), errors="ignore") as f:
            str = f.read()
            try:
                geoINF = geo.geoparse(str)
            except:
                continue
            article = os.path.basename(doc).rstrip(".txt")
            for i in range(len(geoINF)):
                location = {'place_name': '', 'country': '', 'lat': '', 'lon': '', 'article': article}
                try:
                    a = geoINF[i]['geo']
                except:
                    continue
                location['place_name'] = a['place_name']
                location['country'] = a['country_code3']
                location['lat'] = a['lat']
                location['lon'] = a['lon']
                all_location.append(location)


if __name__ == '__main__':
    Get_Places(BASE, DOCS)
    all_location_lean = reduce(run_function, [[], ] + all_location)
    filename = 'bioData.json'
    with open(filename, 'w+') as file_obj:
        json.dump(all_location_lean, file_obj)


