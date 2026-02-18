"""Compatibility shim for legacy asl_tb3_msgs used by older navigation code.

Defines minimal `TurtleBotState` and `TurtleBotControl` message-like classes
so existing navigation code can run while we migrate to `tidybot_msgs`.
"""
from dataclasses import dataclass


@dataclass
class TurtleBotState:
    x: float = 0.0
    y: float = 0.0
    theta: float = 0.0


@dataclass
class TurtleBotControl:
    v: float = 0.0
    omega: float = 0.0

    # backwards-compatible alias
    @property
    def _asdict(self):
        return {"v": self.v, "omega": self.omega}
