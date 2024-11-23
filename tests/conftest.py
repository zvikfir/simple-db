
import pytest
import os
import shutil

@pytest.fixture
def test_db_path(tmp_path):
    """Provides a temporary directory for database files"""
    db_path = tmp_path / "testdb"
    os.makedirs(db_path, exist_ok=True)
    yield str(db_path)
    # Cleanup
    if os.path.exists(db_path):
        shutil.rmtree(db_path)