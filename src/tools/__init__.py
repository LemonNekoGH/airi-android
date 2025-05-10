from .device import register_device_tools
from .input import register_input_tools
from .utils import register_utils_tools
from .cpustat import register_cpustat_tools
from .batterystats import register_batterystats_tools
from .wm import register_wm_tools
from .ui import register_ui_tools

__all__ = [
    "register_device_tools",
    "register_input_tools",
    "register_utils_tools",
    "register_cpustat_tools",
    "register_batterystats_tools",
    "register_wm_tools",
    "register_ui_tools",
]
