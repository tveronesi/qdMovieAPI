import json

import requests
from flask import Flask, jsonify, request
from lxml import html

app = Flask(__name__)


def parse_imdb(imdb_id):
    url = f"https://www.imdb.com/title/tt{imdb_id}/reference"
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if resp.status_code != 200:
        return jsonify({"error": "Unable to fetch the page"}), 500
    data = {'imdbId': int(imdb_id)}

    tree = html.fromstring(resp.content)

    script = tree.xpath('//script[@id="__NEXT_DATA__"]/text()')
    if not script:
        return jsonify({"error": "No script data found"}), 500
    raw_txt = script[0]
    raw_json = json.loads(raw_txt)

    data['raw_json'] = raw_json

    return data


@app.route("/imdb")
def get_imdb_data():
    imdb_id = request.args.get("imdb_id")
    return jsonify(parse_imdb(imdb_id))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
