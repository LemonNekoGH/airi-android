from ppadb.client import Client
from ppadb.device import Device
from typing import Optional


class DeviceManager:
    _adb_client: Client
    _device: Optional[Device]

    def __init__(self):
        self._adb_client = Client()
        self._device = None

    def connect(self, host: str, port: int) -> None:
        """Connect to a device at the specified host and port."""
        self._device = self._adb_client.remote_connect(host, port)

    def get_device(self) -> Device:
        if self._device is None:
            devices = self._adb_client.devices()
            if len(devices) == 0:
                raise Exception("No devices connected")
            self._device = devices[0]
        return self._device

    def reset(self) -> None:
        self._device = None
