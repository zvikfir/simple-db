
import os
import json
from typing import List, Tuple

class SSTableManager:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.sstable_path = os.path.join(db_path, "sstables")
        self.table_count = 0
        os.makedirs(self.sstable_path, exist_ok=True)

    def create_table(self, entries: List[Tuple[str, str]]) -> None:
        table_file = os.path.join(self.sstable_path, f"table_{self.table_count}.sst")
        with open(table_file, "w") as f:
            for key, value in entries:
                f.write(json.dumps({"key": key, "value": value}) + "\n")
        self.table_count += 1

    def get(self, key: str) -> str:
        # Search from newest to oldest SSTable
        for i in range(self.table_count - 1, -1, -1):
            table_file = os.path.join(self.sstable_path, f"table_{i}.sst")
            value = self._search_table(table_file, key)
            if value is not None:
                return value
        return None

    def _search_table(self, table_file: str, search_key: str) -> str:
        with open(table_file, "r") as f:
            for line in f:
                entry = json.loads(line)
                if entry["key"] == search_key:
                    return entry["value"]
        return None