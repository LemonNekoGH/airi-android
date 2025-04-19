from mcp.server.fastmcp import FastMCP

import ppadb.client as client

from ppadb.device import Device

adb_client = client.Client()
device: Device | None = None

# Create an MCP server
mcp = FastMCP("airi-android")


@mcp.tool(description="Connect to the device")
def connect_device(host: str, port: int):
    """Connect to the device"""
    global device
    device = adb_client.connect(f"{host}:{port}")


@mcp.tool(description="Tap on the screen at the given coordinates")
def input_tap(x: int, y: int):
    device.input_tap(x, y)


@mcp.tool(description="Select the device to use, you can get the list of devices with `devices` command")
def select_device(serial: str):
    global device
    device = adb_client.device(serial)


@mcp.tool(description="Run a shell command")
def shell(command: str):
    device.shell(command)


@mcp.tool(description="List all connected ADB devices")
def devices():
    devices_list: list[str] = []

    for device in adb_client.devices():
        devices_list.append(device.serial)

    return devices_list
