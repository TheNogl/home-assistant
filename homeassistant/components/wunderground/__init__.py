"""The Wunderground integration."""
# from __future__ import annotations

# from homeassistant.config_entries import ConfigEntry
# from homeassistant.core import HomeAssistant

# from .const import DOMAIN

# List the platforms that you want to support.
# For your initial PR, limit it to 1 platform.
# PLATFORMS: list[str] = ["sensor"]


# async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
# """Set up Wunderground from a config entry."""
# Store an API object for your platforms to access
# hass.data[DOMAIN][entry.entry_id] = MyApi(...)

# hass.config_entries.async_setup_platforms(entry, PLATFORMS)

# return True


# async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
# """Unload a config entry."""
# unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
# if unload_ok:
# hass.data[DOMAIN].pop(entry.entry_id)

# return unload_ok
from homeassistant import config_entries, core

from .const import DOMAIN


async def async_setup_entry(
    hass: core.HomeAssistant, entry: config_entries.ConfigEntry
) -> bool:
    """Set up platform from a ConfigEntry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data

    # Forward the setup to the sensor platform.
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    return True
