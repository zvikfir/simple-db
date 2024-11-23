# Simple DB Project

A lightweight database implementation for educational purposes based on the description shown in the book Designing Data Intensive Applications.

## Overview

This project implements a simple database system to demonstrate fundamental database concepts and operations.

Full disclosure, it was mostly (>= 90%) built using Copilot and Claude 3.5 Sonnet model.

## Features

- Basic CRUD operations
- Simple query interface
- Data persistence
- Memory-efficient storage

## Getting Started

```bash
# Clone the repository
git clone https://github.com/yourusername/simple-db.git

# Navigate to project directory
cd simple-db

# Optional: create a python env using venv and requirements file
sh create_venv.sh

# Optional: activate the venv created
source setup_env.sh

# Run an insertion of ~2000 records to db and see wal.log and sstables in data folder
python src/main.py

# Run program again to fetch a record that was saved only in the memtable (and wal.log) but not in a sstable, and was restored to memtable from wal.log file on program init
python src/main2.py
```

You can see an example for data files in the data directory (in case you don't want to run the program yourself and just see the output).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.