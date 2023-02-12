#!/usr/bin/python3
"""This module instantiates the FileStorage and reloads
all objects making the instance available on all modules
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
