from mcp.server.fastmcp import FastMCP
from device import DeviceManager


def register_device_tools(mcp: FastMCP, device_manager: DeviceManager):
    @mcp.tool(description="Connect to a device at the specified host and port")
    def device_connect(host: str, port: int) -> None:
        """Connect to a device at the specified host and port."""
        device_manager.connect(host, port)

    @mcp.tool(description="Reset the device connection")
    def device_reset() -> None:
        """Reset the device connection."""
        device_manager.reset()
