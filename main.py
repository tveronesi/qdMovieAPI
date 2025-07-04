import json
from typing import Any

import requests
from flask import Flask, jsonify, request
from lxml import html
from pydantic import BaseModel, TypeAdapter, model_serializer
from pydantic.dataclasses import dataclass

app = Flask(__name__)


class Person(BaseModel):
    name: str
    id: str
    url: str

    @classmethod
    def from_directors(cls, data: dict):
        return cls(**
                   {
                       'name': data['name']['nameText']['text'],
                       'id': data['name']['id'],
                       'url': f"https://www.imdb.com/name/{data['name']['id']}"

                   })

    @classmethod
    def from_cast(cls, data: dict):
        return cls(**
                   {
                       'name': data['node']['name']['nameText']['text'],
                       'id': data['node']['name']['id'],
                       'url': f"https://www.imdb.com/name/{data['node']['name']['id']}"
                   })



class Movie(BaseModel):
    imdbId: str
    imdb_id: int
    title: str
    url: str = ""
    cover: str
    plot: str | None = None
    release_date: str | None = None
    languages: list[str] = []
    certificates: list[dict[str, list[str]]] = []
    directors: list[Person] = []
    cast: list[Person] = []
    year: int | None = None
    duration: int | None = None
    country_codes: list[str] = []
    rating: float | None = None
    metacritic_rating: int | None = None
    votes: int | None = None
    trailers: list[str] = []
    genres: list[str] = []
    interests : list[str] = []
    worldwide_gross: str | None = None
    production_budget: str | None = None
    storyline_keywords: list[str] = []
    filming_locations: list[str] = []
    sound_mixes: list[str] = []
    processes: list[str] = []
    printed_formats: list[str] = []
    negative_formats: list[str] = []
    laboratories: list[str] = []
    cameras : list[str] = []
    aspect_ratios: list[tuple[str, str]] = []
    summaries : list[str] = []
    synopses : list[str] = []
    production: list[str] = []



def parse_json(raw_json) -> Movie:
    data = {}
    mainColumnData = raw_json['props']['pageProps']['mainColumnData']
    aboveTheFoldData = raw_json['props']['pageProps']['aboveTheFoldData']
    if not mainColumnData:
        return {"error": "No data found for the given IMDb ID"}

    data['imdbId'] = mainColumnData['id']
    data['imdb_id'] = int(data['imdbId'].replace('tt', ''))
    data['url'] = f"https://www.imdb.com/title/{data['imdbId']}/"
    data['title'] = aboveTheFoldData['originalTitleText']['text']
    data['metacritic_rating'] = mainColumnData['metacritic']['metascore']['score'] if mainColumnData['metacritic'] else None
    data['cover'] = aboveTheFoldData['primaryImage']['url']
    data['plot'] = mainColumnData['plot']['plotText']['plainText'] if mainColumnData['plot'] else None
    release_date = mainColumnData['releaseDate']
    data['year'] = aboveTheFoldData['releaseYear']['year']
    data['duration'] = aboveTheFoldData['runtime']['seconds'] / 60 if aboveTheFoldData['runtime'] else None
    data['rating'] = mainColumnData['ratingsSummary']['aggregateRating']
    data['votes'] = mainColumnData['ratingsSummary']['voteCount']
    data['genres'] = [genre['genre']['text'] for genre in mainColumnData['titleGenres']['genres']]
    data['worldwide_gross'] = f"{mainColumnData['worldwideGross']['total']['amount']} {mainColumnData['worldwideGross']['total']['currency']}" if mainColumnData['worldwideGross'] else None
    data['production_budget'] = f"{mainColumnData['productionBudget']['budget']['amount']} {mainColumnData['productionBudget']['budget']['currency']}" if mainColumnData['productionBudget'] else None

    trailers = mainColumnData['primaryVideos']['edges']
    data['trailers'] = [
    f"https://www.imdb.com/video/{trailer['node']['id']}" for trailer in trailers if trailer['node']['id']
    ]

    interests = mainColumnData['interests']['edges']
    data['interests'] = [interest['node']['primaryText']['text'] for interest in interests ]

    data['release_date'] = f"{release_date['year']}-{release_date['month']:02d}-{release_date['day']:02d}" if release_date else None

    certificates = mainColumnData['certificates']['edges']
    data['certificates'] = [{cert['node']['country']['id']: [cert['node']['country']['text'], cert['node']['rating']]} for cert in certificates if cert['node']['country']]

    directors_dump = mainColumnData['directorsPageTitle'][0]['credits']
    data['directors'] = []
    for director in directors_dump:
        d = Person.from_directors(director)
        data['directors'].append(d)

    cast_dump = aboveTheFoldData['castPageTitle']['edges']
    data['cast'] = []
    for cast_member in cast_dump:
        c = Person.from_cast(cast_member)
        data['cast'].append(c)

    filming_locations_dump = mainColumnData['filmingLocations']['edges']
    data['filming_locations'] = [location['node']['text'] for location in filming_locations_dump]

    country_codes_dump = mainColumnData['countriesDetails']['countries']
    data['country_codes'] = [country['id'] for country in country_codes_dump]

    storyline_keywords_dump = mainColumnData['storylineKeywords']['edges']
    data['storyline_keywords'] = [keyword['node']['text'] for keyword in storyline_keywords_dump]

    production_dump = mainColumnData['production']['edges']
    data['production'] = [prod['node']['company']['companyText']['text'] for prod in production_dump]

    summaries_dump = mainColumnData['summaries']['edges']
    data['summaries'] = [summary['node']['plotText']['plaidHtml'] for summary in summaries_dump]

    synopses_dump = mainColumnData['synopses']['edges']
    data['synopses'] = [synopsis['node']['plotText']['plaidHtml'] for synopsis in synopses_dump]

    sound_mixed_dump = mainColumnData['technicalSpecifications']['soundMixes']['items']
    data['sound_mixes'] = [sound['text'] for sound in sound_mixed_dump]

    processes_dump = mainColumnData['technicalSpecifications']['processes']['items']
    data['processes'] = [process['process'] for process in processes_dump]

    printed_formats_dump = mainColumnData['technicalSpecifications']['printedFormats']['items']
    data['printed_formats'] = [format['printedFormat'] for format in printed_formats_dump]

    negative_formats_dump = mainColumnData['technicalSpecifications']['negativeFormats']['items']
    data['negative_formats'] = [format['negativeFormat'] for format in negative_formats_dump]

    laboratories_dump = mainColumnData['technicalSpecifications']['laboratories']['items']
    data['laboratories'] = [lab['laboratory'] for lab in laboratories_dump]

    cameras_dump = mainColumnData['technicalSpecifications']['cameras']['items']
    data['cameras'] = [camera['camera'] for camera in cameras_dump]

    aspect_ratios_dump = mainColumnData['technicalSpecifications']['aspectRatios']['items']
    data['aspect_ratios'] = [ ( ratio['aspectRatio'], ( ' '.join([atrb['text'] for atrb in ratio['attributes']] ))) for ratio in aspect_ratios_dump]

    languages_dump = mainColumnData['spokenLanguages']['spokenLanguages']
    data['languages'] = [lang['id'] for lang in languages_dump]



    movie = Movie.model_validate(data)

    return movie


def parse_imdb(imdb_id):
    url = f"https://www.imdb.com/title/tt{imdb_id}/reference"
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if resp.status_code != 200:
        return jsonify({"error": "Unable to fetch the page"}), 500
    data = {'imdb_id': int(imdb_id)}

    tree = html.fromstring(resp.content)

    script = tree.xpath('//script[@id="__NEXT_DATA__"]/text()')
    if not script:
        return jsonify({"error": "No script data found"}), 500
    raw_txt = script[0]
    raw_json = json.loads(raw_txt)

    # data['raw_json'] = raw_json
    data['parsed_json'] = parse_json(raw_json).model_dump()

    return data


@app.route("/imdb")
def get_imdb_data():
    imdb_id = request.args.get("imdb_id")
    return jsonify(parse_imdb(imdb_id))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
