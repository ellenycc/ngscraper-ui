import os

DATA_DIR = "data"
ASSETS_DIR = "assets"

EDITABLE_COLUMNS = [
    "Pixel dimensions W x H",
    "File format",
    "Last updated",
    "Notes"
]

ORIGINAL_FILE = os.path.join(DATA_DIR, "painting-resolution-list.xlsx")
UPDATED_FILE = os.path.join(DATA_DIR, "updated-painting-resolution-list.xlsx")
THUMBNAIL_URL = "Thumbnail URL"
