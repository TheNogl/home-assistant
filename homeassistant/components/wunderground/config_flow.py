"""Config Flow for WUnderground weather service."""
from collections import OrderedDict

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_API_KEY, CONF_SHOW_ON_MAP
from homeassistant.core import callback
import homeassistant.helpers.config_validation as cv

from .const import (
    CONF_LANG,
    CONF_MONITORED_FORECASTS,
    CONF_MONITORED_MEASUREMENTS,
    CONF_MONITORED_METADATA,
    CONF_NUMERIC_PRECISION,
    CONF_PWS_ID,
    DEFAULT_LANG,
    DOMAIN,
    LANG_CODES,
    NUMERIC_PRECISION,
    SENSOR_TYPES_FORECAST,
    SENSOR_TYPES_MEASUREMENTS,
    SENSOR_TYPES_METADATA,
)

api_schema = vol.Schema(
    {
        vol.Required(CONF_API_KEY): cv.string,
        vol.Required(CONF_PWS_ID): cv.string,
        vol.Required(CONF_NUMERIC_PRECISION): vol.All(vol.In(NUMERIC_PRECISION)),
        vol.Optional(CONF_LANG, default=DEFAULT_LANG): vol.All(vol.In(LANG_CODES)),
    }
)

conditions_schema = vol.Schema(
    {
        vol.Optional(CONF_MONITORED_MEASUREMENTS): cv.multi_select(
            SENSOR_TYPES_MEASUREMENTS
        ),
        vol.Optional(CONF_MONITORED_FORECASTS): cv.multi_select(SENSOR_TYPES_FORECAST),
        vol.Optional(CONF_MONITORED_METADATA): cv.multi_select(SENSOR_TYPES_METADATA),
    }
)

import_schema = vol.Schema(
    {
        vol.Required(CONF_API_KEY): cv.string,
        vol.Required(CONF_PWS_ID): cv.string,
        vol.Required(CONF_NUMERIC_PRECISION): vol.All(vol.In(NUMERIC_PRECISION)),
        vol.Optional(CONF_LANG, default=DEFAULT_LANG): vol.All(vol.In(LANG_CODES)),
        vol.Optional(CONF_MONITORED_MEASUREMENTS): cv.multi_select(
            SENSOR_TYPES_MEASUREMENTS
        ),
        vol.Optional(CONF_MONITORED_FORECASTS): cv.multi_select(SENSOR_TYPES_FORECAST),
        vol.Optional(CONF_MONITORED_METADATA): cv.multi_select(SENSOR_TYPES_METADATA),
    }
)


@callback
def configured_sensors(hass):
    """Return a set of configured WUnderground sensors."""
    return {
        entry.data[CONF_PWS_ID] for entry in hass.config_entries.async_entries(DOMAIN)
    }


class WUndergroundConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""

    def __init__(self):
        """Initialize the config flow."""
        self.data = {}

    @callback
    def _show_form(self, errors=None):
        """Show the form to the user."""
        data_schema = OrderedDict()
        data_schema[vol.Required(CONF_PWS_ID)] = cv.positive_int
        data_schema[vol.Optional(CONF_SHOW_ON_MAP, default=False)] = bool

        return self.async_show_form(
            step_id="user", data_schema=vol.Schema(data_schema), errors=errors or {}
        )

    async def async_step_import(self, user_input=None):
        """Config flow api settings."""
        if user_input is not None:
            if user_input[CONF_PWS_ID] in configured_sensors(self.hass):
                return self._show_form({CONF_PWS_ID: "already_configured"})
            self.data.update(user_input)
            return self.async_create_entry(title="WUnderground", data=self.data)

        return self.async_show_form(
            step_id="import",
            data_schema=import_schema,
        )

    async def async_step_user(self, user_input=None):
        """Config flow api settings."""
        if user_input is not None:
            if user_input[CONF_PWS_ID] in configured_sensors(self.hass):
                return self._show_form({CONF_PWS_ID: "already_configured"})
            self.data.update(user_input)
            return await self.async_step_conditions()

        return self.async_show_form(step_id="user", data_schema=api_schema)

    async def async_step_conditions(self, user_input=None):
        """Config Flow monitored conditions selection."""
        if user_input is not None:
            self.data.update(user_input)
            return self.async_create_entry(title="WUnderground", data=self.data)
        return self.async_show_form(step_id="conditions", data_schema=conditions_schema)
