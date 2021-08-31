import asyncio
from typing import Tuple

import pandas as pd

import hottest
import hottest.models as hm
import hottest.services as hss

app = hottest.create_app()


async def _find(service_name: str) -> str:
    q_cities = hm.City.query.all()
    cities = pd.DataFrame(
        [
            {
                "id": city.__getattribute__("%s_id" % service_name),
                "name": city.name,
                "country": city.country,
            }
            for city in q_cities
            if city.__getattribute__("%s_id" % service_name) is not None
        ]
    )
    service = hss.from_string(service_name)
    cities["temp"] = await asyncio.gather(
        *[service.get_weather(city) for city in cities["id"]]
    )
    cities = cities[cities["temp"] == cities["temp"].max()]
    cities["desc"] = (
        cities["name"]
        + " "
        + cities["country"]
        + " "
        + cities["temp"].astype(str)
    )
    return "\n".join(cities["desc"])


@app.route("/<service_name>", methods=["GET"])
def find(service_name: str) -> Tuple[str, int]:
    try:
        max_temp = asyncio.run(_find(service_name))
    except ConnectionError as exc:
        return str(exc), 429
    return str(max_temp), 200
