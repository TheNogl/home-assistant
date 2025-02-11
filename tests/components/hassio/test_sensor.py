"""The tests for the hassio sensors."""

import os
from unittest.mock import patch

import pytest

from homeassistant.components.hassio import DOMAIN
from homeassistant.helpers import entity_registry
from homeassistant.setup import async_setup_component

from tests.common import MockConfigEntry

MOCK_ENVIRON = {"HASSIO": "127.0.0.1", "HASSIO_TOKEN": "abcdefgh"}


@pytest.fixture(autouse=True)
def mock_all(aioclient_mock, request):
    """Mock all setup requests."""
    aioclient_mock.post("http://127.0.0.1/homeassistant/options", json={"result": "ok"})
    aioclient_mock.get("http://127.0.0.1/supervisor/ping", json={"result": "ok"})
    aioclient_mock.post("http://127.0.0.1/supervisor/options", json={"result": "ok"})
    aioclient_mock.get(
        "http://127.0.0.1/info",
        json={
            "result": "ok",
            "data": {"supervisor": "222", "homeassistant": "0.110.0", "hassos": None},
        },
    )
    aioclient_mock.get(
        "http://127.0.0.1/store",
        json={
            "result": "ok",
            "data": {"addons": [], "repositories": []},
        },
    )
    aioclient_mock.get(
        "http://127.0.0.1/host/info",
        json={
            "result": "ok",
            "data": {
                "result": "ok",
                "data": {
                    "chassis": "vm",
                    "operating_system": "Debian GNU/Linux 10 (buster)",
                    "kernel": "4.19.0-6-amd64",
                },
            },
        },
    )
    aioclient_mock.get(
        "http://127.0.0.1/core/info",
        json={"result": "ok", "data": {"version_latest": "1.0.0", "version": "1.0.0"}},
    )
    aioclient_mock.get(
        "http://127.0.0.1/os/info",
        json={"result": "ok", "data": {"version_latest": "1.0.0", "version": "1.0.0"}},
    )
    aioclient_mock.get(
        "http://127.0.0.1/supervisor/info",
        json={
            "result": "ok",
            "data": {
                "result": "ok",
                "version_latest": "1.0.0",
                "addons": [
                    {
                        "name": "test",
                        "slug": "test",
                        "installed": True,
                        "update_available": False,
                        "version": "2.0.0",
                        "version_latest": "2.0.1",
                        "repository": "core",
                        "url": "https://github.com/home-assistant/addons/test",
                    },
                    {
                        "name": "test2",
                        "slug": "test2",
                        "installed": True,
                        "update_available": False,
                        "version": "3.1.0",
                        "version_latest": "3.2.0",
                        "repository": "core",
                        "url": "https://github.com",
                    },
                ],
            },
        },
    )
    aioclient_mock.get(
        "http://127.0.0.1/addons/test/stats",
        json={
            "result": "ok",
            "data": {
                "cpu_percent": 0.99,
                "memory_usage": 182611968,
                "memory_limit": 3977146368,
                "memory_percent": 4.59,
                "network_rx": 362570232,
                "network_tx": 82374138,
                "blk_read": 46010945536,
                "blk_write": 15051526144,
            },
        },
    )
    aioclient_mock.get(
        "http://127.0.0.1/addons/test2/stats",
        json={
            "result": "ok",
            "data": {
                "cpu_percent": 0.8,
                "memory_usage": 51941376,
                "memory_limit": 3977146368,
                "memory_percent": 1.31,
                "network_rx": 31338284,
                "network_tx": 15692900,
                "blk_read": 740077568,
                "blk_write": 6004736,
            },
        },
    )
    aioclient_mock.get(
        "http://127.0.0.1/ingress/panels", json={"result": "ok", "data": {"panels": {}}}
    )


async def test_sensors(hass, aioclient_mock):
    """Test hassio OS and addons sensors."""

    with patch.dict(os.environ, MOCK_ENVIRON):
        result = await async_setup_component(
            hass,
            "hassio",
            {"http": {"server_port": 9999, "server_host": "127.0.0.1"}, "hassio": {}},
        )
        assert result

    config_entry = MockConfigEntry(domain=DOMAIN, data={}, unique_id=DOMAIN)
    config_entry.add_to_hass(hass)

    await hass.async_block_till_done()

    sensors = {
        "sensor.home_assistant_operating_system_version": "1.0.0",
        "sensor.home_assistant_operating_system_newest_version": "1.0.0",
        "sensor.test_version": "2.0.0",
        "sensor.test_newest_version": "2.0.1",
        "sensor.test2_version": "3.1.0",
        "sensor.test2_newest_version": "3.2.0",
        "sensor.test_cpu_percent": "0.99",
        "sensor.test2_cpu_percent": "0.8",
        "sensor.test_memory_percent": "4.59",
        "sensor.test2_memory_percent": "1.31",
    }

    """Check that entities are disabled by default."""
    for sensor in sensors:
        assert hass.states.get(sensor) is None

    """Enable sensors."""
    ent_reg = entity_registry.async_get(hass)
    for sensor in sensors:
        ent_reg.async_update_entity(sensor, disabled_by=None)
    await hass.config_entries.async_reload(config_entry.entry_id)

    await hass.async_block_till_done()

    """Check sensor values."""
    for sensor, value in sensors.items():
        state = hass.states.get(sensor)
        assert state.state == value
