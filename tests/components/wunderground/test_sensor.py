"""Test the Wunderground sensor module."""

from asyncio import Future
import json

from pytest_mock import MockerFixture

import homeassistant.components.sensor as sensor_component
import homeassistant.components.wunderground.sensor as wunderground
from homeassistant.setup import async_setup_component

PLATFORM = wunderground
COMPONENT = sensor_component
THING = "wunderground"
GOOD_CONFIG = {
    THING: {
        "api_key": "21eef0f9deb9bf1698dee7e71ddf0e8f",  # Random Hex String
        "pws_id": "ISTATION123",  # ID Similar to actual IDs
        "numeric_precision": "decimal",
        "lang": "en-US",
        "monitored_measurements": ["temp", "humidity"],
        "monitored_forecasts": ["today_summary"],
        "monitored_metadata": ["stationID"],
    }
}


class MockResponse:
    """Create Mock Response for AIOHTTP Request."""

    def __init__(self, text, status):
        """Set up MockResponse class."""
        self._text = text
        self.status = status

    async def text(self):
        """Set response Text."""
        return self._text

    async def json(self):
        """Convert JSON to Dict."""
        return json.loads(self._text)


async def test_setup_correct(hass, mocker: MockerFixture):
    """Test WUnderground Sensors."""
    data = {
        "temp": "24.3",
        "humidity": "70.6",
        "today_summary": "Sunny",
        "stationId": "ISTATION_123",
    }
    resp = MockResponse(json.dumps(data), 200)
    mock = mocker.patch("aiohttp.ClientSession.get", return_value=Future())
    mock.return_value.set_result(resp)
    assert await async_setup_component(hass, THING, GOOD_CONFIG)
    await hass.async_block_till_done()
    entity = hass.states.get("sensor.wu_temp")
    assert entity is not None
    assert len(hass.states.async_entity_ids("sensor")) == 4


async def test_setup_missing_config(hass, mocker: MockerFixture):
    """Test setup with missing configuration."""
    config = {THING: {"platform": "wunderground"}}
    data = {
        "temp": "24.3",
        "humidity": "70.6",
        "today_summary": "Sunny",
        "stationId": "ISTATION_123",
    }
    resp = MockResponse(json.dumps(data), 200)
    mock = mocker.patch("aiohttp.ClientSession.get", return_value=Future())
    mock.return_value.set_result(resp)
    await async_setup_component(hass, THING, config)
    await hass.async_block_till_done()
    assert len(hass.states.async_all(THING)) == 0
