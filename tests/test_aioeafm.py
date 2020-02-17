import asyncio
import json
import pathlib
from unittest import mock

import aiohttp
import pytest

import aioeafm


async def mock_session(path):
    with open(pathlib.Path(__file__).parent / "fixtures" / path) as fp:
        fixture = json.load(fp)

    session = mock.Mock()
    get = session.get.return_value = asyncio.Future()

    response = mock.Mock()
    get_json = response.json.return_value = asyncio.Future()
    get_json.set_result(fixture)

    get.set_result(response)

    return session


async def test_get_stations():
    session = await mock_session("get_stations.json")
    stations = await aioeafm.get_stations(session)

    station = stations[0]
    assert station["label"] == "Bourton Dickler"

    measures = station["measures"]
    assert measures[0]["parameter"] == "level"
    assert measures[0]["qualifier"] == "Downstream Stage"


async def test_get_station():
    session = await mock_session("get_station_1491TH.json")
    station = await aioeafm.get_station(session, "1491TH")

    assert station["label"] == "Kings Mill"

    measures = station["measures"]
    assert measures[0]["parameter"] == "level"
    assert measures[0]["qualifier"] == "Downstream Stage"
    assert measures[0]["latestReading"]["value"] == 1.877


@pytest.mark.integration
async def test_integration_get_stations():
    async with aiohttp.ClientSession() as session:
        stations = await aioeafm.get_stations(session)
        assert isinstance(stations, list)


@pytest.mark.integration
async def test_integration_get_station():
    async with aiohttp.ClientSession() as session:
        station = await aioeafm.get_station(session, "1771TH")
        assert isinstance(station, dict)
