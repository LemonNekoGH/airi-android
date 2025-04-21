from typing import List, Optional
from mcp.server.fastmcp import FastMCP
from ppadb.plugins.device.utils import Activity, MemInfo
from device import DeviceManager


def register_utils_tools(mcp: FastMCP, device_manager: DeviceManager):
    @mcp.tool(description="Get the top activity on the device")
    def utils_top_activity() -> Optional[Activity]:
        return device_manager.get_device().get_top_activity()

    @mcp.tool(description="Get all top activities on the device")
    def utils_top_activities() -> List[Activity]:
        return device_manager.get_device().get_top_activities()

    @mcp.tool(description="Get memory information for a package")
    def utils_meminfo(package_name: str) -> MemInfo:
        return device_manager.get_device().get_meminfo(package_name)

    @mcp.tool(description="Get process ID for a package")
    def utils_pid(package_name: str) -> Optional[str]:
        return device_manager.get_device().get_pid(package_name)

    @mcp.tool(description="Get user ID for a package")
    def utils_uid(package_name: str) -> Optional[str]:
        return device_manager.get_device().get_uid(package_name)

    @mcp.tool(description="Get thread IDs for a process")
    def utils_tids(pid: int) -> List[str]:
        return device_manager.get_device().get_tids(pid)

    @mcp.tool(description="Get version name of a package")
    def utils_package_version(package_name: str) -> Optional[str]:
        return device_manager.get_device().get_package_version_name(package_name)
