from __future__ import annotations

import asyncio
import json
from typing import Callable, Optional

import websockets
from websockets.asyncio.client import ClientConnection

from mcctp.exceptions import ConnectionError, ActionError
from mcctp.state import GameState


class MCCTPClient:
    """Async WebSocket client for MCCTP."""

    def __init__(self, host: str = "localhost", port: int = 8765):
        self.uri = f"ws://{host}:{port}/mcctp"
        self._ws: Optional[ClientConnection] = None
        self._state: Optional[GameState] = None
        self._state_callback: Optional[Callable[[GameState], None]] = None
        self._running = False

    @property
    def state(self) -> Optional[GameState]:
        return self._state

    def on_state(self, callback: Callable[[GameState], None]):
        self._state_callback = callback

    async def connect(self):
        try:
            self._ws = await websockets.connect(self.uri)
        except Exception as e:
            raise ConnectionError(f"Failed to connect to {self.uri}: {e}") from e
        self._running = True

    async def disconnect(self):
        self._running = False
        if self._ws:
            await self._ws.close()
            self._ws = None

    async def send(self, action: dict):
        if not self._ws:
            raise ConnectionError("Not connected")
        await self._ws.send(json.dumps(action))

    async def recv(self) -> dict:
        if not self._ws:
            raise ConnectionError("Not connected")
        data = await self._ws.recv()
        return json.loads(data)

    async def listen(self):
        """Listen for game state updates. Blocks until disconnected."""
        if not self._ws:
            raise ConnectionError("Not connected")

        try:
            async for message in self._ws:
                data = json.loads(message)
                if data.get("type") == "game_state":
                    self._state = GameState.from_dict(data)
                    if self._state_callback:
                        self._state_callback(self._state)
                elif data.get("type") == "error":
                    raise ActionError(data.get("message", "Unknown error"))
        except websockets.ConnectionClosed:
            pass
        finally:
            self._running = False

    async def send_and_listen(self, action: dict):
        """Send an action and continue listening."""
        await self.send(action)

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, *args):
        await self.disconnect()
