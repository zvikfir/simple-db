
from db_engine import DatabaseEngine

def main():
    """
    Main function to demonstrate the usage of the DatabaseEngine.
    This function initializes a new database instance and performs various operations:
    1. Creates a new database in the './data' directory
    2. Inserts initial key-value pairs
    3. Retrieves values from the database
    4. Performs bulk insertion of ~2000 records
    Note on SSTable creation and WAL behavior:
    - With 2000 records being inserted, assuming a default memtable size of 1000 entries:
        * First SSTable (SSTable_1.db) will be created when records 1-1000 fill the memtable
        * Second SSTable (SSTable_2.db) will be created with records 1001-2000
    - The WAL.log file is:
        1. Written to continuously during put operations
        2. Truncated when memtable is flushed to disk (at 1000 records)
        3. Continues logging new operations after truncation
    """
    # Initialize database
    db = DatabaseEngine("./data")

    # Example usage
    db.put("user:1", "John Doe")
    db.put("user:2", "Jane Doe")

    # Retrieve values
    print(db.get("user:1"))  # Output: John Doe
    print(db.get("user:2"))  # Output: Jane Doe

    
    # Populate database with more data
    for i in range(3, 2000):
        db.put(f'user:{i}', f'John Doe {i}')

if __name__ == "__main__":
    main()