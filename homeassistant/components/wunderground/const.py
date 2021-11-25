"""Constants for WUnderground weather service."""
from datetime import timedelta

DOMAIN = "wunderground"

CONF_ATTRIBUTION = "Data provided by the WUnderground weather service"
CONF_PWS_ID = "pws_id"
CONF_NUMERIC_PRECISION = "numeric_precision"
CONF_LANG = "lang"
CONF_MONITORED_MEASUREMENTS = "monitored_measurements"
CONF_MONITORED_FORECASTS = "monitored_forecasts"
CONF_MONITORED_METADATA = "monitored_metadata"
CONF_MONITORED_CATEGORIES = "monitored_categories"

DEFAULT_LANG = "en-US"

# API_CATEGORIES = {
#     "measurements": "Measurements",
#     "forecasts": "Forecasts",
#     "information": "Weather Station Information",
# }

API_CATEGORIES = {
    CONF_MONITORED_MEASUREMENTS: "Measurements",
    CONF_MONITORED_FORECASTS: "Forecasts",
    # CONF_MONITORED_METADATA: "Weather Station Information",
}

SENSOR_TYPES_METADATA = {
    "neighborhood": "Weather Station Reference Name",
    "obsTimeLocal": "Weather Station Local Time",
    "stationID": "Weather Station ID",
    "elev": "Weather Station Elevation",
    "qcStatus": "Quality Check Status",
    # "realtimeFrequency": "Data Report Frequency"
}
SENSOR_TYPES_MEASUREMENTS = {
    "humidity": "Humidity",
    "solarRadiation": "Solar Radiation",
    "uv": "UV Index",
    "winddir": "Wind Direction",
    "dewpt": "Dewpoint",
    "heatIndex": "Heat Index",
    "windChill": "Windchill",
    "precipRate": "Precipitation Rate",
    "precipTotal": "Precipitation Total Today",
    "pressure": "Air Pressure",
    "temp": "Temperature",
    "windGust": "Wind Gust Speed",
    "windSpeed": "Wind Speed",
}
SENSOR_TYPES_FORECAST = {
    "today_summary": "Summary of Today",
    "weather_1d": "Weather Day 1 daytime",
    "weather_1n": "Weather Day 1 nighttime",
    "weather_2d": "Weather Day 2 daytime",
    "weather_2n": "Weather Day 2 nighttime",
    "weather_3d": "Weather Day 3 daytime",
    "weather_3n": "Weather Day 3 nighttime",
    "weather_4d": "Weather Day 4 daytime",
    "weather_4n": "Weather Day 4 nighttime",
    "weather_5d": "Weather Day 5 daytime",
    "weather_5n": "Weather Day 5 nighttime",
    "temp_high_1d": "Temperature High Day 1",
    "temp_high_2d": "Temperature High Day 2",
    "temp_high_3d": "Temperature High Day 3",
    "temp_high_4d": "Temperature High Day 4",
    "temp_high_5d": "Temperature High Day 5",
    "temp_low_1d": "Temperature Low Day 1",
    "temp_low_2d": "Temperature Low Day 2",
    "temp_low_3d": "Temperature Low Day 3",
    "temp_low_4d": "Temperature Low Day 4",
    "temp_low_5d": "Temperature Low Day 5",
    "wind_1d": "Wind Day 1",
    "wind_2d": "Wind Day 2",
    "wind_3d": "Wind Day 3",
    "wind_4d": "Wind Day 4",
    "wind_5d": "Wind Day 5",
    "precip_1d": "Precipitation Day 1",
    "precip_2d": "Precipitation Day 2",
    "precip_3d": "Precipitation Day 3",
    "precip_4d": "Precipitation Day 4",
    "precip_5d": "Precipitation Day 5",
    "precip_chance_1d": "Precipitation Chance Day 1",
    "precip_chance_2d": "Precipitation Chance Day 2",
    "precip_chance_3d": "Precipitation Chance Day 3",
    "precip_chance_4d": "Precipitation Chance Day 4",
    "precip_chance_5d": "Precipitation Chance Day 5",
}

# Language Supported Codes
LANG_CODES = [
    "ar-AE",
    "az-AZ",
    "bg-BG",
    "bn-BD",
    "bn-IN",
    "bs-BA",
    "ca-ES",
    "cs-CZ",
    "da-DK",
    "de-DE",
    "el-GR",
    "en-GB",
    "en-IN",
    "en-US",
    "es-AR",
    "es-ES",
    "es-LA",
    "es-MX",
    "es-UN",
    "es-US",
    "et-EE",
    "fa-IR",
    "fi-FI",
    "fr-CA",
    "fr-FR",
    "gu-IN",
    "he-IL",
    "hi-IN",
    "hr-HR",
    "hu-HU",
    "in-ID",
    "is-IS",
    "it-IT",
    "iw-IL",
    "ja-JP",
    "jv-ID",
    "ka-GE",
    "kk-KZ",
    "kn-IN",
    "ko-KR",
    "lt-LT",
    "lv-LV",
    "mk-MK",
    "mn-MN",
    "ms-MY",
    "nl-NL",
    "no-NO",
    "pl-PL",
    "pt-BR",
    "pt-PT",
    "ro-RO",
    "ru-RU",
    "si-LK",
    "sk-SK",
    "sl-SI",
    "sq-AL",
    "sr-BA",
    "sr-ME",
    "sr-RS",
    "sv-SE",
    "sw-KE",
    "ta-IN",
    "ta-LK",
    "te-IN",
    "tg-TJ",
    "th-TH",
    "tk-TM",
    "tl-PH",
    "tr-TR",
    "uk-UA",
    "ur-PK",
    "uz-UZ",
    "vi-VN",
    "zh-CN",
    "zh-HK",
    "zh-TW",
]
NUMERIC_PRECISION = {"none": "Integer", "decimal": "Decimal"}

_RESOURCECURRENT = "https://api.weather.com/v2/pws/observations/current?stationId={}&format=json&units={}&apiKey={}"
_RESOURCEFORECAST = "https://api.weather.com/v3/wx/forecast/daily/5day?geocode={},{}&units={}&{}&format=json&apiKey={}"

MIN_TIME_BETWEEN_UPDATES = timedelta(minutes=5)

TEMPUNIT = 0
LENGTHUNIT = 1
ALTITUDEUNIT = 2
SPEEDUNIT = 3
PRESSUREUNIT = 4
RATE = 5
PERCENTAGEUNIT = 6
