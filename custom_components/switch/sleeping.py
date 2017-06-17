"""
This swith will be used to track when I am sleeping.  The goal is 
to replace using MQTT and just change the state through HTTP POST
requests.  This will hopefully be more reliable than the MQTT 
Tasker plugin.  
"""
from homeassistant.components.switch import SwitchDevice
from homeassistant.const import DEVICE_DEFAULT_NAME


# pylint: disable=unused-argument
def setup_platform(hass, config, add_devices_callback, discovery_info=None):
    """Set up the demo switches."""
    add_devices_callback([
        sleeping('Sleeping', True, None, True),
    ])


class sleeping(SwitchDevice):
    """Representation of a demo switch."""

    def __init__(self, name, state, icon, assumed):
        """Initialize the Demo switch."""
        self._name = name or DEVICE_DEFAULT_NAME
        self._state = state
        self._icon = icon
        self._assumed = assumed

    @property
    def should_poll(self):
        """No polling needed for a demo switch."""
        return False

    @property
    def name(self):
        """Return the name of the device if any."""
        return self._name

    @property
    def icon(self):
        """Return the icon to use for device if any."""
        return self._icon

    @property
    def assumed_state(self):
        """Return if the state is based on assumptions."""
        return self._assumed

    @property
    def is_on(self):
        """Return true if switch is on."""
        return self._state

    def turn_on(self, **kwargs):
        """Turn the switch on."""
        self._state = True
        self.schedule_update_ha_state()

    def turn_off(self, **kwargs):
        """Turn the device off."""
        self._state = False
        self.schedule_update_ha_state()
