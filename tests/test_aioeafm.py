import pathlib

import aiohttp
import pytest

import aioeafm


async def mock_response(aiohttp_raw_server, aiohttp_client, path):
    async def handler(request):
        with open(pathlib.Path(__file__).parent / "fixtures" / path) as fp:
            return aiohttp.web.Response(text=fp.read())

    raw_server = await aiohttp_raw_server(handler)
    client = await aiohttp_client(raw_server)
    return client.session


async def test_get_stations(aiohttp_raw_server, aiohttp_client):
    session = await mock_response(
        aiohttp_raw_server, aiohttp_client, "get_stations.json"
    )
    stations = await aioeafm.get_stations(session)

    station = stations[0]
    assert station["label"] == "Bourton Dickler"

    measures = station["measures"]
    assert measures[0]["parameter"] == "level"
    assert measures[0]["qualifier"] == "Downstream Stage"


async def test_get_station(aiohttp_raw_server, aiohttp_client):
    session = await mock_response(
        aiohttp_raw_server, aiohttp_client, "get_station_1491TH.json"
    )
    station = await aioeafm.get_station(session, "1491TH")

    assert station["label"] == "Kings Mill"

    measures = station["measures"]
    assert measures[0]["parameter"] == "level"
    assert measures[0]["qualifier"] == "Downstream Stage"
    assert measures[0]["latestReading"]["value"] == 1.885


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
