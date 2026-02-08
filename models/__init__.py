#!/usr/bin/python3
import os

storage_type = os.getenv("HBNB_TYPE_STORAGE", "file")

if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Only call reload if the storage has the method
if hasattr(storage, "reload"):
    storage.reload()
