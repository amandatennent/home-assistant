from homeassistant.components.climate import TEMP_CELSIUS
from homeassistant.components.light import (
    SUPPORT_BRIGHTNESS,
    SUPPORT_COLOR,
)
from homeassistant.components.cover import (
    SUPPORT_CLOSE,
    SUPPORT_OPEN,
    SUPPORT_SET_POSITION,
    SUPPORT_STOP,
)
from homeassistant.components.climate import (
    SUPPORT_TARGET_TEMPERATURE,
    SUPPORT_FAN_MODE,
)

# AiotDevice Mapping
MK_MAPPING_PARAMS = "mapping_params"
MK_INIT_PARAMS = "init_params"
MK_RESOURCES = "resources"

AIOT_DEVICE_MAPPING = {
    # Aqara M1S Gateway
    "lumi.gateway.acn01": {
        "light": {
            MK_INIT_PARAMS: {
                "supported_features": SUPPORT_BRIGHTNESS | SUPPORT_COLOR,
                "color_mode": "hs",
            },
            MK_RESOURCES: {
                "toggle": ("14.7.111", "_attr_is_on"),
                "color": ("14.7.85", "_attr_hs_color"),
                "brightness": ("14.7.1006", "_attr_brightness"),
            },
        }
    },
    # Smart wall switch T1 (single fire and single key)
    "lumi.switch.b1lacn01": {
        "switch": {
            MK_RESOURCES: {"toggle": ("4.1.85", "_attr_is_on")},
        }
    },
    # Smart wall switch T1 (single fire double button)
    "lumi.switch.b2lacn01": {
        "switch": {
            MK_MAPPING_PARAMS: {"ch_count": 2},
            MK_RESOURCES: {"toggle": ("4.{}.85", "_attr_is_on")},
        }
    },
    # Smart wall switch T1 (single fire and three keys)
    "lumi.switch.b3l01": {
        "switch": {
            MK_MAPPING_PARAMS: {"ch_count": 3},
            MK_RESOURCES: {"toggle": ("4.{}.85", "_attr_is_on")},
        }
    },
    # VRF air conditioner controller
    "lumi.airrtc.vrfegl01": {
        "climate": {
            MK_INIT_PARAMS: {
                "supported_features": SUPPORT_TARGET_TEMPERATURE | SUPPORT_FAN_MODE,
                "hvac_modes": ["cool", "heat", "off"],
                "unit_of_measurement": TEMP_CELSIUS,
                "target_temp_step": 1,
                "fan_modes": ["low", "middle", "high"],
                "min_temp": 16,
                "max_temp": 30,
            },
            MK_RESOURCES: {"ac_state": ("14.{}.85", "_state_str")},
        }
    },
    # Aqara Smart Curtain Motor (Lithium Battery Opening and Closing Curtain Version)
    "lumi.curtain.hagl04": {
        "cover": {
            MK_INIT_PARAMS: {
                "supported_features": SUPPORT_OPEN
                | SUPPORT_CLOSE
                | SUPPORT_SET_POSITION
                | SUPPORT_STOP,
                "device_class": "curtain",
            },
            MK_RESOURCES: {
                "curtain_state": ("14.2.85", "_attr_state"),
                "running_state": ("14.4.85", "_attr_state"),
                "position": ("1.1.85", "_attr_current_cover_position"),
            },
        },
        "sensor": {
            MK_INIT_PARAMS: {"device_class": "battery", "state_class": "measurement"},
            MK_RESOURCES: {"battery": ("8.0.2001", "_attr_native_value")},
        },
    },
    # Wireless switch T1 (wall-mounted one-button)
    "lumi.remote.b186acn03": {
        "sensor": {
            MK_INIT_PARAMS: {"device_class": "battery", "state_class": "measurement"},
            MK_RESOURCES: {"battery": ("8.0.2001", "_attr_native_value")},
        }
    },
    # Wireless switch T1 (wall-mounted double button)
    "lumi.remote.b286acn03": {
        "sensor": {
            MK_INIT_PARAMS: {"device_class": "battery", "state_class": "measurement"},
            MK_RESOURCES: {"battery": ("8.0.2001", "_attr_native_value")},
        }
    },
    # High-precision human body sensor
    "lumi.motion.agl04": {
        "sensor": {
            MK_INIT_PARAMS: {"device_class": "battery", "state_class": "measurement"},
            MK_RESOURCES: {"battery": ("8.0.2001", "_attr_native_value")},
        }
    },
}

SPECIAL_DEVICES_INFO = {
    # VRF air conditioner controller
    "lumi.airrtc.vrfegl01": {
        "toggle": {0: "on", 1: "off"},
        "hvac_mode": {
            0: "heat",
            1: "cool",
            2: "auto",
            3: "dry",
            4: "fan_only",
        },
        "fan_mode": {0: "low", 1: "middle", 2: "high", 3: "auto"},
        "swing_mode": {0: "horizontal", 1: "vertical", 2: "both"},
        "swing_toggle": {1: "off"},
    }
}
