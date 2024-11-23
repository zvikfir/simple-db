
import os
import json

class WAL:
    def __init__(self, db_path: str):
        self.wal_path = os.path.join(db_path, "wal.log")

    def append(self, key: str, value: str) -> None:
        entry = json.dumps({"key": key, "value": value}) + "\n"
        with open(self.wal_path, "a") as f:
            f.write(entry)

    def truncate(self) -> None:
        with open(self.wal_path, "w") as f:
            f.write("")

    def recover(self) -> dict:
        recovered_data = {}
        if os.path.exists(self.wal_path):
            with open(self.wal_path, "r") as f:
                for line in f:
                    entry = json.loads(line)
                    recovered_data[entry["key"]] = entry["value"]
        return recovered_data