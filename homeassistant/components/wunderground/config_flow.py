"""Config Flow for WUnderground weather service."""
# from typing_extensions import Required
import logging

# from homeassistant.components.sensor import PLATFORM_SCHEMA
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import (  # CONF_MONITORED_CONDITIONS,; CONF_LATITUDE,; CONF_LONGITUDE,
    CONF_API_KEY,
)
import homeassistant.helpers.config_validation as cv

from .const import (  # CONF_ATTRIBUTION,
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

# from typing import Any

_LOGGER = logging.getLogger(__name__)

# CONF_ATTRIBUTION = "Data provided by the WUnderground weather service"
# CONF_PWS_ID = "pws_id"
# CONF_NUMERIC_PRECISION = "numeric_precision"
# CONF_LANG = "lang"
# CONF_MONITORED_MEASUREMENTS = "monitored_measurements"
# CONF_MONITORED_FORECASTS = "monitored_forecasts"
# CONF_MONITORED_METADATA = "monitored_metadata"

# DEFAULT_LANG = "en-US"

# SENSOR_TYPES_METADATA = {
#     "neighborhood": "Weather Station Reference Name",
#     "obsTimeLocal": "Weather Station Local Time",
#     "stationID": "Weather Station ID",
#     "elev": "Weather Station Elevation",
# }
# SENSOR_TYPES_MEASUREMENTS = {
#     "humidity": "Humidity",
#     "solarRadiation": "Solar Radiation",
#     "uv": "UV Index",
#     "winddir": "Wind Direction",
#     "dewpt": "Dewpoint",
#     "heatIndex": "Heat Index",
#     "windChill": "Windchill",
#     "precipRate": "Precipitation Rate",
#     "precipTotal": "Precipitation Total Today",
#     "pressure": "Air Pressure",
#     "temp": "Temperature",
#     "windGust": "Wind Gust Speed",
#     "windSpeed": "Wind Speed",
# }
# SENSOR_TYPES_FORECAST = {
#     "today_summary": "Summary of Today",
#     "weather_1d": "Weather Day 1 daytime",
#     "weather_1n": "Weather Day 1 nighttime",
#     "weather_2d": "Weather Day 2 daytime",
#     "weather_2n": "Weather Day 2 nighttime",
#     "weather_3d": "Weather Day 3 daytime",
#     "weather_3n": "Weather Day 3 nighttime",
#     "weather_4d": "Weather Day 4 daytime",
#     "weather_4n": "Weather Day 4 nighttime",
#     "weather_5d": "Weather Day 5 daytime",
#     "weather_5n": "Weather Day 5 nighttime",
#     "temp_high_1d": "Temperature High Day 1",
#     "temp_high_2d": "Temperature High Day 2",
#     "temp_high_3d": "Temperature High Day 3",
#     "temp_high_4d": "Temperature High Day 4",
#     "temp_high_5d": "Temperature High Day 5",
#     "temp_low_1d": "Temperature Low Day 1",
#     "temp_low_2d": "Temperature Low Day 2",
#     "temp_low_3d": "Temperature Low Day 3",
#     "temp_low_4d": "Temperature Low Day 4",
#     "temp_low_5d": "Temperature Low Day 5",
#     "wind_1d": "Wind Day 1",
#     "wind_2d": "Wind Day 2",
#     "wind_3d": "Wind Day 3",
#     "wind_4d": "Wind Day 4",
#     "wind_5d": "Wind Day 5",
#     "precip_1d": "Precipitation Day 1",
#     "precip_2d": "Precipitation Day 2",
#     "precip_3d": "Precipitation Day 3",
#     "precip_4d": "Precipitation Day 4",
#     "precip_5d": "Precipitation Day 5",
#     "precip_chance_1d": "Precipitation Chance Day 1",
#     "precip_chance_2d": "Precipitation Chance Day 2",
#     "precip_chance_3d": "Precipitation Chance Day 3",
#     "precip_chance_4d": "Precipitation Chance Day 4",
#     "precip_chance_5d": "Precipitation Chance Day 5",
# }

# # Language Supported Codes
# LANG_CODES = [
#     "ar-AE",
#     "az-AZ",
#     "bg-BG",
#     "bn-BD",
#     "bn-IN",
#     "bs-BA",
#     "ca-ES",
#     "cs-CZ",
#     "da-DK",
#     "de-DE",
#     "el-GR",
#     "en-GB",
#     "en-IN",
#     "en-US",
#     "es-AR",
#     "es-ES",
#     "es-LA",
#     "es-MX",
#     "es-UN",
#     "es-US",
#     "et-EE",
#     "fa-IR",
#     "fi-FI",
#     "fr-CA",
#     "fr-FR",
#     "gu-IN",
#     "he-IL",
#     "hi-IN",
#     "hr-HR",
#     "hu-HU",
#     "in-ID",
#     "is-IS",
#     "it-IT",
#     "iw-IL",
#     "ja-JP",
#     "jv-ID",
#     "ka-GE",
#     "kk-KZ",
#     "kn-IN",
#     "ko-KR",
#     "lt-LT",
#     "lv-LV",
#     "mk-MK",
#     "mn-MN",
#     "ms-MY",
#     "nl-NL",
#     "no-NO",
#     "pl-PL",
#     "pt-BR",
#     "pt-PT",
#     "ro-RO",
#     "ru-RU",
#     "si-LK",
#     "sk-SK",
#     "sl-SI",
#     "sq-AL",
#     "sr-BA",
#     "sr-ME",
#     "sr-RS",
#     "sv-SE",
#     "sw-KE",
#     "ta-IN",
#     "ta-LK",
#     "te-IN",
#     "tg-TJ",
#     "th-TH",
#     "tk-TM",
#     "tl-PH",
#     "tr-TR",
#     "uk-UA",
#     "ur-PK",
#     "uz-UZ",
#     "vi-VN",
#     "zh-CN",
#     "zh-HK",
#     "zh-TW",
# ]
# NUMERIC_PRECISION = {"none": "Integer", "decimal": "Decimal"}


# PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
api_schema = vol.Schema(
    {
        vol.Required(CONF_API_KEY): cv.string,
        vol.Required(CONF_PWS_ID): cv.string,
        vol.Required(CONF_NUMERIC_PRECISION): vol.All(vol.In(NUMERIC_PRECISION)),
        vol.Optional(CONF_LANG, default=DEFAULT_LANG): vol.All(vol.In(LANG_CODES)),
    }
)
# optionals_schema = vol.Schema(
#     {
#         vol.Optional(CONF_LANG, default=DEFAULT_LANG): vol.All(vol.In(LANG_CODES)),
#         vol.Inclusive(
#             CONF_LATITUDE, "coordinates", "Latitude and longitude must exist together"
#         ): cv.latitude,
#         vol.Inclusive(
#             CONF_LONGITUDE, "coordinates", "Latitude and longitude must exist together"
#         ): cv.longitude,
#     }
# )
conditions_schema = vol.Schema(
    {
        vol.Optional(CONF_MONITORED_MEASUREMENTS): cv.multi_select(
            SENSOR_TYPES_MEASUREMENTS
        ),
        vol.Optional(CONF_MONITORED_FORECASTS): cv.multi_select(SENSOR_TYPES_FORECAST),
        vol.Optional(CONF_MONITORED_METADATA): cv.multi_select(SENSOR_TYPES_METADATA),
    }
)
# schema = vol.Schema(
#     {
#         vol.Required(CONF_API_KEY): cv.string,
#         vol.Required(CONF_PWS_ID): cv.string,
#         vol.Required(CONF_NUMERIC_PRECISION): vol.All(
#             vol.In(NUMERIC_PRECISION)
#         ),  # cv.string,
#         vol.Optional(CONF_LANG, default=DEFAULT_LANG): vol.All(vol.In(LANG_CODES)),
#         vol.Inclusive(
#             CONF_LATITUDE, "coordinates", "Latitude and longitude must exist together"
#         ): cv.latitude,
#         vol.Inclusive(
#             CONF_LONGITUDE, "coordinates", "Latitude and longitude must exist together"
#         ): cv.longitude,
#         vol.Optional(CONF_MONITORED_MEASUREMENTS): cv.multi_select(
#             SENSOR_TYPES_MEASUREMENTS
#         ),
#         vol.Optional(CONF_MONITORED_FORECASTS): cv.multi_select(SENSOR_TYPES_FORECAST),
#         vol.Optional(CONF_MONITORED_METADATA): cv.multi_select(SENSOR_TYPES_METADATA),
#         # vol.Required(CONF_MONITORED_CONDITIONS): vol.All(vol.In(SENSOR_TYPES)),
#         # vol.Required(CONF_MONITORED_CONDITIONS): cv.multi_select(SENSOR_TYPES_MEASUREMENTS),
#         # vol.Required(CONF_MONITORED_CONDITIONS): vol.All(
#         # {
#         # vol.Optional(CONF_MONITORED_MEASUREMENTS): cv.multi_select(
#         # SENSOR_TYPES_MEASUREMENTS
#         # ),
#         # vol.Optional(CONF_MONITORED_FORECASTS): cv.multi_select(
#         # SENSOR_TYPES_FORECAST
#         # ),
#         # vol.Optional(CONF_MONITORED_METADATA): cv.multi_select(
#         # SENSOR_TYPES_METADATA
#         # ),
#         # },
#         # {
#         # vol.Required(
#         # Any(
#         # Any(CONF_MONITORED_MEASUREMENTS, CONF_MONITORED_FORECASTS),
#         # CONF_MONITORED_METADATA,
#         # )
#         # )
#         # },
#         # ),
#     }
# )
# conditions_schema = vol.All(
#     vol.Schema(
#         {
#             vol.Required(
#                 vol.Any(
#                     CONF_MONITORED_MEASUREMENTS,
#                     CONF_MONITORED_FORECASTS,
#                     CONF_MONITORED_METADATA,
#                 )
#             ): cv.multi_select(SENSOR_TYPES_MEASUREMENTS)
#         }
#     ),
#     vol.Schema(
#         {
#             vol.Optional(CONF_MONITORED_MEASUREMENTS): cv.multi_select(
#                 SENSOR_TYPES_MEASUREMENTS
#             ),
#             vol.Optional(CONF_MONITORED_FORECASTS): cv.multi_select(
#                 SENSOR_TYPES_FORECAST
#             ),
#             vol.Optional(CONF_MONITORED_METADATA): cv.multi_select(
#                 SENSOR_TYPES_METADATA
#             ),
#         }
#     ),
# )


class WUndergroundConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""

    def __init__(self):
        """Initialize the config flow."""
        self.data = {}
        # self.api_key = None
        # self.pws_id = None
        # self.numeric_precision = None
        # self.lang = DEFAULT_LANG
        # self.latitude = None
        # self.longitude = None
        # self.mon_conditions = None

    async def async_step_user(self, user_input=None):
        """Config flow api settings."""
        if user_input is not None:
            # pass  # TODOs: process info
            # _LOGGER.warning("API set")
            self.data.update(user_input)
            # self.api_key = self.data[CONF_API_KEY]
            # self.pws_id = self.data[CONF_PWS_ID]
            # self.numeric_precision = self.data[CONF_NUMERIC_PRECISION]
            # return await self.async_step_optionals()
            return await self.async_step_conditions()
        # _LOGGER.warning("API not yet set")
        return self.async_show_form(step_id="user", data_schema=api_schema)

    # async def async_step_optionals(self, user_input=None):
    #     """Config Flow optional settings."""
    #     if user_input is not None:
    #         # _LOGGER.warning("Optionals set")
    #         self.data.update(user_input)
    #         # self.lang = self.data[CONF_LANG]
    #         # self.latitude = self.data[CONF_LATITUDE]
    #         # self.longitude = self.data[CONF_LONGITUDE]
    #         return await self.async_step_conditions()
    #     # _LOGGER.warning("Optionals not yet set")
    #     return self.async_show_form(step_id="optionals", data_schema=optionals_schema)

    async def async_step_conditions(self, user_input=None):
        """Config Flow monitored conditions selection."""
        if user_input is not None:
            self.data.update(user_input)
            # _LOGGER.warning(f"Conditions set\n{self.data}")
            # self.mon_conditions = self.data[CONF_MONITORED_MEASUREMENTS]
            # self.mon_conditions.append(self.data[CONF_MONITORED_FORECASTS])
            # self.mon_conditions.append(self.data[CONF_MONITORED_METADATA])
            return self.async_create_entry(title="WUnderground", data=self.data)
        # _LOGGER.warning("Conditions not yet set")
        return self.async_show_form(step_id="conditions", data_schema=conditions_schema)
