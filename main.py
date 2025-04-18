from mcp.server.fastmcp import FastMCP

import ppadb.client as client

from ppadb.device import Device

adb_client = client.Client()
device: Device | None = None

# Create an MCP server
mcp = FastMCP("airi-android")


@mcp.tool()
def connect_device(host: str, port: int):
    """Connect to the device"""
    global device
    device = adb_client.connect(f"{host}:{port}")


@mcp.tool()
def tap_screen(x: int, y: int):
    """Tap the screen at the given coordinates"""
    device.shell(f"input tap {x} {y}")


@mcp.resource("adb://devices")
def devices():
    """Get all connected devices"""
    return adb_client.devices()
