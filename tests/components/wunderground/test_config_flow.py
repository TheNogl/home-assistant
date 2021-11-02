"""Test the Wunderground config flow."""

from homeassistant import config_entries
from homeassistant.components.wunderground import config_flow
from homeassistant.components.wunderground.const import CONF_PWS_ID, DOMAIN
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import RESULT_TYPE_CREATE_ENTRY, RESULT_TYPE_FORM

from tests.common import MockConfigEntry


async def test_form(hass: HomeAssistant) -> None:
    """Test we get the form."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] == RESULT_TYPE_FORM
    assert result["errors"] is None

    result2 = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {
            "api_key": "9cd7ac1125985268d13f1f2548cef358",  # Random Hex String
            "pws_id": "ISTATION_123",
            "numeric_precision": "decimal",
            "lang": "en-US",
        },
    )
    await hass.async_block_till_done()

    assert result2["step_id"] == "conditions"
    assert result2["type"] == RESULT_TYPE_FORM
    result2 = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {
            "monitored_measurements": ["temp", "humidity"],
            "monitored_forecasts": ["today_summary"],
            "monitored_metadata": ["stationID"],
        },
    )
    await hass.async_block_till_done()

    assert result2["type"] == RESULT_TYPE_CREATE_ENTRY


async def test_duplicate_error(hass):
    """Test that errors are shown when duplicates are added."""
    conf = {CONF_PWS_ID: "12345abcde"}

    MockConfigEntry(domain=DOMAIN, data=conf).add_to_hass(hass)
    flow = config_flow.WUndergroundConfigFlow()
    flow.hass = hass

    result = await flow.async_step_user(user_input=conf)
    assert result["errors"] == {CONF_PWS_ID: "already_configured"}

    result2 = await flow.async_step_import(user_input=conf)
    assert result2["errors"] == {CONF_PWS_ID: "already_configured"}

    result3 = await flow.async_step_import()
    assert result3["errors"] is None
