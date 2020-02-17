# aioeafm

This is a thin wrapper for the [Real Time flood monitoring API](https://environment.data.gov.uk/flood-monitoring/doc/reference).

This wrapper is built for home-assistant. We target the same python versions as home-assistant and follow similar code style guidelines.

```bash
pip install aioeafm
```

You can get a list of monitoring stations with:

```python
from aioeafm import get_stations
import aiohttp


async with aiohttp.ClientSession() as session:
    print(await get_stations(session))
```

And you can get the current data for that station with:

```python
from aioeafm import get_station
import aiohttp


async with aiohttp.ClientSession() as session:
    print(await get_station(session, "1491TH"))
```
