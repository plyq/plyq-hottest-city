import pandas as pd

import hottest.scripts.fill_cities as hsfc


def test_get_cities_dataframe1() -> None:
    df = hsfc.get_cities_dataframe()
    assert not df.empty
    assert len(df) > 100


def test_prepare_cities_dataframe1() -> None:
    df = pd.DataFrame(
        {
            "Name": ["Moscow", "Kiev"],
            "Country": ["Russia", "Ukraine"],
            "Field": [10, 10],
        }
    )
    res = hsfc.prepare_cities_dataframe(df)
    assert len(res) == 2
    for column in [
        "name",
        "country",
        "open_weather_id",
    ]:
        assert column in res.columns
    assert res["name"][1] == "Kiev"
    assert res["open_weather_id"][0] == "5601538"
