## Extract location from txt or csv

##  Using mordecai. More about mordecai: https://github.com/openeventdata/mordecai

## environment
python 3.5(better using conda create new one); docker 

## step 1

    pip install mordecai
    
    python -m spacy download en_core_web_lg
    
## docker setting 
In order to work, Mordecai needs access to a Geonames gazetteer running in Elasticsearch. The easiest way to set it up is by running the following commands (you must have Docker installed first).


    docker pull elasticsearch:5.5.2
    wget https://s3.amazonaws.com/ahalterman-geo/geonames_index.tar.gz --output-file=wget_log.txt
    tar -xzf geonames_index.tar.gz
    docker run -d -p 127.0.0.1:9200:9200 -v $(pwd)/geonames_index/:/usr/share/elasticsearch/data elasticsearch:5.5.2

## How to use

    from mordecai import Geoparser
    geo = Geoparser()
    geo.geoparse("string which you want extract location")
    