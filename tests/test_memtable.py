
import pytest
from src.memtable import MemTable

def test_memtable_basic_operations():
    memtable = MemTable(max_size=3)
    
    # Test put and get
    memtable.put("key1", "value1")
    assert memtable.get("key1") == "value1"
    assert memtable.get("nonexistent") is None
    
    # Test should_flush
    assert not memtable.should_flush()
    memtable.put("key2", "value2")
    memtable.put("key3", "value3")
    assert memtable.should_flush()
    
    # Test get_entries
    entries = memtable.get_entries()
    assert len(entries) == 3
    assert entries == [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]
    
    # Test clear
    memtable.clear()
    assert memtable.get("key1") is None
    assert len(memtable.get_entries()) == 0