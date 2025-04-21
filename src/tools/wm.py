from typing import Optional
from mcp.server.fastmcp import FastMCP
from ppadb.plugins.device.wm import Size
from device import DeviceManager


def register_wm_tools(mcp: FastMCP, device_manager: DeviceManager):
    @mcp.tool(description="Get the physical size of the device screen")
    def wm_size() -> Optional[Size]:
        return device_manager.get_device().wm_size()

    @mcp.tool(description="Get the display density of the device")
    def wm_density() -> Optional[int]:
        return device_manager.get_device().wm_density()
