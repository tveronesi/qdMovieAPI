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
    def from_dict(cls, data: dict):
        return cls(**
                   {
                       'name': data['name']['nameText']['text'],
                       'id': data['name']['id'],
                       'url': f"https://www.imdb.com/name/{data['name']['id']}"

                   })


class Movie(BaseModel):
    imdbId: str
    title: str
    small_cover: str
    release_date: str | None = None
    certificates: list[dict[str, list[str]]] = []
    directors: list[Person] = []


def parse_json(raw_json) -> Movie:
    data = {}
    mainColumnData = raw_json['props']['pageProps']['mainColumnData']
    aboveTheFoldData = raw_json['props']['pageProps']['aboveTheFoldData']
    if not mainColumnData:
        return {"error": "No data found for the given IMDb ID"}

    data['imdbId'] = mainColumnData['id']
    data['title'] = aboveTheFoldData['originalTitleText']['text']
    data['small_cover'] = aboveTheFoldData['primaryImage']['url']
    release_date = mainColumnData['releaseDate']

    data[
        'release_date'] = f"{release_date['year']}-{release_date['month']:02d}-{release_date['day']:02d}" if release_date else None
    movie = Movie.model_validate(data)
    certificates = mainColumnData['certificates']['edges']
    data['certificates'] = [{cert['node']['country']['id']: [cert['node']['country']['text'], cert['node']['rating']]}
                            for cert in certificates if cert['node']['country']]

    movie.certificates = data['certificates']

    directors_dump = mainColumnData['directorsPageTitle'][0]['credits']
    data['directors'] = []
    for director in directors_dump:
        d = Person.from_dict(director)
        data['directors'].append(d)
    movie.directors = data['directors']

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
