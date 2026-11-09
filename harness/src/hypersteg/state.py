"""Run phases and strict state transitions."""
from __future__ import annotations

from dataclasses import dataclass, field

PHASES = ["INIT", "PRIVATE_PROTOCOL", "PUBLIC_1", "OPPONENT_ANALYSIS", "PRIVATE_REVISION", "PUBLIC_2", "EVALUATE", "COMPLETE"]
C0_PHASES = ["INIT", "PUBLIC_1", "EVALUATE", "COMPLETE"]


@dataclass
class RunState:
    condition: str = "C1"
    phase: str = "INIT"
    history: list[dict] = field(default_factory=list)

    def advance(self, target: str) -> None:
        sequence = C0_PHASES if self.condition == "C0" else PHASES
        if self.phase not in sequence or sequence.index(self.phase) + 1 >= len(sequence):
            raise ValueError(f"Cannot advance from {self.phase}")
        expected = sequence[sequence.index(self.phase) + 1]
        if target != expected:
            raise ValueError(f"Invalid transition {self.phase} -> {target}; expected {expected}")
        self.history.append({"from": self.phase, "to": target})
        self.phase = target
