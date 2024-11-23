
from db_engine import DatabaseEngine

def main():
    # Initialize database
    db = DatabaseEngine("./data")

    print(db.get('user:1001')) # output: John Doe 1001

if __name__ == "__main__":
    main()