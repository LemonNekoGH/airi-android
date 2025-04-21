from mcp.server.fastmcp import FastMCP
from device import DeviceManager


def register_input_tools(mcp: FastMCP, device_manager: DeviceManager):
    @mcp.tool(description="Tap on the screen at the given coordinates")
    def input_tap(x: int, y: int) -> None:
        device_manager.get_device().input_tap(x, y)

    @mcp.tool(description="Swipe from the given coordinates to the given coordinates")
    def input_swipe(x1: int, y1: int, x2: int, y2: int, duration: int = 500) -> None:
        device_manager.get_device().input_swipe(x1, y1, x2, y2, duration)

    @mcp.tool(description="Input text on the device")
    def input_text(text: str) -> None:
        device_manager.get_device().input_text(text)

    @mcp.tool(description="Send a key event to the device")
    def input_keyevent(keycode: int, longpress: bool = False) -> None:
        device_manager.get_device().input_keyevent(keycode, longpress)

    @mcp.tool(description="Press the current key")
    def input_press() -> None:
        device_manager.get_device().input_press()

    @mcp.tool(description="Roll the trackball")
    def input_roll(dx: int, dy: int) -> None:
        device_manager.get_device().input_roll(dx, dy)
