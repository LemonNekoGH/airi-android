from typing import Dict, Optional
from mcp.server.fastmcp import FastMCP
from ppadb.plugins.device.cpustat import TotalCPUStat, ProcessCPUStat
from device import DeviceManager


def register_cpustat_tools(mcp: FastMCP, device_manager: DeviceManager):
    @mcp.tool(description="Get CPU times for the device")
    def cpu_times() -> Optional[TotalCPUStat]:
        return device_manager.get_device().cpu_times()

    @mcp.tool(description="Get CPU usage percentage")
    def cpu_percent(interval: float = 1.0) -> float:
        return device_manager.get_device().cpu_percent(interval)

    @mcp.tool(description="Get the number of CPU cores")
    def cpu_count() -> int:
        return device_manager.get_device().cpu_count()

    @mcp.tool(description="Get total CPU usage statistics")
    def cpu_total() -> Optional[TotalCPUStat]:
        return device_manager.get_device().get_total_cpu()

    @mcp.tool(description="Get CPU usage statistics for a process")
    def cpu_process(pid: int) -> ProcessCPUStat:
        return device_manager.get_device().get_pid_cpu(pid)

    @mcp.tool(description="Get CPU usage statistics for all threads of a process")
    def cpu_threads(pid: int) -> Dict[str, ProcessCPUStat]:
        return device_manager.get_device().get_all_thread_cpu(pid)
