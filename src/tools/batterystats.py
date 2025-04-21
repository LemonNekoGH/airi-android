from typing import Dict, List, Optional
from mcp.server.fastmcp import FastMCP
from device import DeviceManager


def register_batterystats_tools(mcp: FastMCP, device_manager: DeviceManager):
    @mcp.tool(description="Get battery level of the device")
    def battery_level() -> Optional[int]:
        return device_manager.get_device().get_battery_level()

    @mcp.tool(description="Get detailed battery statistics")
    def battery_stats() -> Dict[str, List]:
        return device_manager.get_device().get_batterystats()
