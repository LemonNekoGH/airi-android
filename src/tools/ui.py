from mcp.server.fastmcp import FastMCP
from device import DeviceManager


def register_ui_tools(mcp: FastMCP, device_manager: DeviceManager):
    @mcp.tool(description="Get UI hierarchy")
    def ui_get_hierarchy() -> str:
        command_result = device_manager.get_device().shell("uiautomator dump")

        if command_result.strip() != "UI hierchary dumped to: /sdcard/window_dump.xml":
            raise Exception("Failed to get UI hierarchy")

        return device_manager.get_device().shell("cat /sdcard/window_dump.xml")
