# アイリ Android

A MCP server to allow ~~airi~~ LLM to use Android Device. This project is child project of [airi](https://github.com/moeru-ai/airi).

## Setup development environment

### Package manager

1. Install `uv` [here](https://docs.astral.sh/uv/getting-started/installation/).
2. Install dependencies.

    ```bash
    uv sync
    ```

### ADB connection

1. Install platform-tools from [here](https://developer.android.com/studio/releases/platform-tools).
2. Connect your Android device via USB, or use the AVD (Android Virtual Device) via `adb connect`.

### Start the server

Run the mcp inspector it will start the server.

```bash
uv run mcp dev main.py
```

Open the inspector at `http://localhost:6274`.
