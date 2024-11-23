
from typing import Dict, List, Tuple

class MemTable:
    def __init__(self, max_size: int = 1000):
        self.table: Dict[str, str] = {}
        self.max_size = max_size

    def put(self, key: str, value: str) -> None:
        self.table[key] = value

    def get(self, key: str) -> str:
        return self.table.get(key)

    def should_flush(self) -> bool:
        return len(self.table) >= self.max_size

    def get_entries(self) -> List[Tuple[str, str]]:
        return sorted(self.table.items())

    def clear(self) -> None:
        self.table.clear()