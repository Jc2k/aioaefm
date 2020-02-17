import aiohttp
import pytest

import aioeafm


@pytest.mark.integration
async def test_get_stations():
    async with aiohttp.ClientSession() as session:
        stations = await aioeafm.get_stations(session)
        assert isinstance(stations, list)


@pytest.mark.integration
async def test_get_station():
    async with aiohttp.ClientSession() as session:
        station = await aioeafm.get_station(session, "1771TH")
        assert isinstance(station, dict)
