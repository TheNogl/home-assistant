"""The Wunderground integration."""
from homeassistant import config_entries, core
from homeassistant.config_entries import SOURCE_IMPORT
from homeassistant.const import CONF_API_KEY, CONF_LATITUDE, CONF_LONGITUDE

from .const import (  # CONF_MONITORED_FORECASTS,; CONF_MONITORED_MEASUREMENTS,; CONF_MONITORED_METADATA,
    CONF_LANG,
    CONF_MONITORED_CATEGORIES,
    CONF_NUMERIC_PRECISION,
    CONF_PWS_ID,
    DOMAIN,
)


async def async_setup(hass, config):
    """Set up the WUnderground Component."""
    if DOMAIN not in config:
        return True

    conf = config[DOMAIN]
    api_key = conf[CONF_API_KEY]
    pws_id = conf[CONF_PWS_ID]
    numeric_precision = conf.get(CONF_NUMERIC_PRECISION)
    latitude = conf.get(CONF_LATITUDE, hass.config.latitude)
    longitude = conf.get(CONF_LONGITUDE, hass.config.longitude)
    lang = conf[CONF_LANG]
    monitored_categories = conf.get(CONF_MONITORED_CATEGORIES)
    # monitored_measurements = conf.get(CONF_MONITORED_MEASUREMENTS, None)
    # monitored_forecasts = conf.get(CONF_MONITORED_FORECASTS, None)
    # monitored_metadata = conf.get(CONF_MONITORED_METADATA, None)

    hass.async_create_task(
        hass.config_entries.flow.async_init(
            DOMAIN,
            context={"source": SOURCE_IMPORT},
            data={
                CONF_API_KEY: api_key,
                CONF_PWS_ID: pws_id,
                CONF_NUMERIC_PRECISION: numeric_precision,
                CONF_LATITUDE: latitude,
                CONF_LONGITUDE: longitude,
                CONF_LANG: lang,
                # CONF_MONITORED_MEASUREMENTS: monitored_measurements,
                # CONF_MONITORED_FORECASTS: monitored_forecasts,
                # CONF_MONITORED_METADATA: monitored_metadata,
                CONF_MONITORED_CATEGORIES: monitored_categories,
            },
        )
    )

    return True


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
