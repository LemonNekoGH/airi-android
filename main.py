from mcp.server.fastmcp import FastMCP, Image

import ppadb.client as client

adb_client = client.Client()

# Create an MCP server
mcp = FastMCP("airi-android")


def first_device():
    return adb_client.devices()[0]


@mcp.tool(description="Connect to the device")
def connect_device(host: str, port: int):
    """Connect to the device"""
    adb_client.connect(f"{host}:{port}")


@mcp.tool(description="Tap on the screen at the given coordinates")
def input_tap(x: int, y: int) -> None:
    first_device().input_tap(x, y)


@mcp.tool(description="Swipe from the given coordinates to the given coordinates")
def input_swipe(x1: int, y1: int, x2: int, y2: int, duration: int = 500) -> None:
    first_device().input_swipe(x1, y1, x2, y2, duration)


@mcp.tool(description="Run a shell command")
def shell(command: str) -> str:
    return first_device().shell(command)


@mcp.tool(description="List all connected ADB devices")
def devices() -> list[str]:
    devices_list: list[str] = []

    for device in adb_client.devices():
        devices_list.append(device.serial)

    return devices_list


@mcp.tool(description="Get UI hierarchy")
def get_ui_hierarchy() -> str:
    command_result = first_device().shell("uiautomator dump")

    if command_result.strip() != "UI hierchary dumped to: /sdcard/window_dump.xml":
        raise Exception("Failed to get UI hierarchy")

    return first_device().shell("cat /sdcard/window_dump.xml")


@mcp.tool(description="Take a screenshot of the device")
def screenshot() -> Image:
    result = first_device().screencap()

    return Image(data=result, format="png")
