from memtable import MemTable
from wal import WAL
from sstable import SSTableManager

class DatabaseEngine:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.memtable = MemTable()
        self.wal = WAL(db_path)
        self.sstable_manager = SSTableManager(db_path)
        
        # Recover memtable state from WAL if exists
        recovered_data = self.wal.recover()
        for key, value in recovered_data.items():
            self.memtable.put(key, value)

    def put(self, key: str, value: str) -> None:
        # Write to WAL first
        self.wal.append(key, value)
        # Then update memtable
        self.memtable.put(key, value)
        
        # If memtable is full, flush to SSTable
        if self.memtable.should_flush():
            self.flush_memtable()

    def get(self, key: str) -> str:
        # First check memtable
        value = self.memtable.get(key)
        if value is not None:
            return value
        
        # Then check SSTables
        return self.sstable_manager.get(key)

    def flush_memtable(self):
        # Create new SSTable from memtable
        self.sstable_manager.create_table(self.memtable.get_entries())
        # Clear memtable
        self.memtable.clear()
        # Truncate WAL
        self.wal.truncate()