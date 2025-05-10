from mcp.server.fastmcp import FastMCP

from device import DeviceManager
from tools.device import register_device_tools
from tools.input import register_input_tools
from tools.utils import register_utils_tools
from tools.cpustat import register_cpustat_tools
from tools.batterystats import register_batterystats_tools
from tools.wm import register_wm_tools
from tools.ui import register_ui_tools

# Create an MCP server
mcp = FastMCP("airi-android")

# Initialize device manager
device_manager = DeviceManager()

# Register all tools
register_device_tools(mcp, device_manager)
register_input_tools(mcp, device_manager)
register_utils_tools(mcp, device_manager)
register_cpustat_tools(mcp, device_manager)
register_batterystats_tools(mcp, device_manager)
register_wm_tools(mcp, device_manager)
register_ui_tools(mcp, device_manager)
