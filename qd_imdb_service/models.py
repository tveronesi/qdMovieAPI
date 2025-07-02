# python
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    id: str
    url: str

    @classmethod
    def from_directors(cls, data: dict):
        return cls(
            name=data['name']['nameText']['text'],
            id=data['name']['id'],
            url=f"https://www.imdb.com/name/{data['name']['id']}"
        )

    @classmethod
    def from_cast(cls, data: dict):
        return cls(
            name=data['node']['name']['nameText']['text'],
            id=data['node']['name']['id'],
            url=f"https://www.imdb.com/name/{data['node']['name']['id']}"
        )


class MovieDetail(BaseModel):
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
    interests: list[str] = []
    worldwide_gross: str | None = None
    production_budget: str | None = None
    storyline_keywords: list[str] = []
    filming_locations: list[str] = []
    sound_mixes: list[str] = []
    processes: list[str] = []
    printed_formats: list[str] = []
    negative_formats: list[str] = []
    laboratories: list[str] = []
    cameras: list[str] = []
    aspect_ratios: list[tuple[str, str]] = []
    summaries: list[str] = []
    synopses: list[str] = []
    production: list[str] = []

class MovieInfo(BaseModel):

    imdbId: str
    imdb_id: str
    title: str
    cover: str | None = None
    url: str | None = None
    year: int | None = None


    @classmethod
    def from_movie_info(cls, data:dict):
        return cls(
            imdbId=data['id'],
            imdb_id=str(data['id'].replace('tt', '')),
            title=data['titleNameText'],
            cover=data.get('titlePosterImageModel', {}).get('url', None),
            url = f"https://www.imdb.com/title/{data['id']}/",
            year=data.get('titleReleaseText',None),

        )