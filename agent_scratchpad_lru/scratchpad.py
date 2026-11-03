"""Bounded LRU scratchpad for agent working memory."""
from collections import OrderedDict
from typing import Any, Dict, Optional


class AgentScratchpad:
    def __init__(self, max_entries: int = 20, max_chars: int = 4000):
        self.max_entries = max_entries
        self.max_chars = max_chars
        # key -> (value, is_pinned)
        self._store: OrderedDict[str, Any] = OrderedDict()

    def set(self, key: str, value: str, pinned: bool = False) -> None:
        if key in self._store:
            self._store.move_to_end(key)
        self._store[key] = (value, pinned)
        self._evict_if_needed()

    def get(self, key: str) -> Optional[str]:
        if key not in self._store:
            return None
        self._store.move_to_end(key)
        return self._store[key][0]

    def _evict_if_needed(self) -> None:
        # Evict unpinned items if over capacity
        while len(self._store) > self.max_entries:
            self._evict_one_unpinned()

        while self._total_chars() > self.max_chars:
            if not self._evict_one_unpinned():
                break

    def _evict_one_unpinned(self) -> bool:
        for k in list(self._store.keys()):
            if not self._store[k][1]:  # not pinned
                del self._store[k]
                return True
        return False

    def _total_chars(self) -> int:
        return sum(len(str(val[0])) for val in self._store.values())

    def format_for_prompt(self) -> str:
        lines = []
        for k, (v, pinned) in self._store.items():
            pin_badge = "[PINNED] " if pinned else ""
            lines.append(f"- {pin_badge}{k}: {v}")
        return "\n".join(lines)
