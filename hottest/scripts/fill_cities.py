#!/usr/bin/env python
import asyncio
import os

import pandas as pd
import sqlalchemy

import hottest.config as hcfg
import hottest.models as hm
import hottest.service as hs
import hottest.services as hss

CITIES_LIST = "resources/cities.csv.zip"


def get_cities_dataframe():
    full_path = os.path.join(hcfg.get_root_dir(), CITIES_LIST)
    return pd.read_csv(full_path)


async def _add_city_id(
    df: pd.DataFrame, city: str, service: hs.WeatherService, id_field: str
) -> None:
    city_id = await service.get_city_id(city)
    df.loc[df["name"] == city, [id_field]] = [[city_id]]


async def _add_ids_job(df: pd.DataFrame) -> None:
    for service_name in hss.AVAILABLE_SERVICES:
        service = hss.from_string(service_name)
        service_id_field = "%s_id" % service_name
        df[service_id_field] = None
        await asyncio.gather(
            *[
                _add_city_id(df, city, service, service_id_field)
                for city in df["name"]
            ]
        )


def prepare_cities_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    # Rename fields.
    df = df[["Name", "Country"]]
    df = df.rename(columns={"Name": "name", "Country": "country"})
    # Add id-s.
    asyncio.run(_add_ids_job(df))
    return df


def main() -> None:
    df = get_cities_dataframe()
    df = prepare_cities_dataframe(df)
    df.to_sql(
        hm.City.__tablename__,
        sqlalchemy.create_engine(hcfg.get_database_connection_uri()),
        if_exists="replace",
    )


if __name__ == "__main__":
    main()
