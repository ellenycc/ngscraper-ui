from typing import List
import streamlit as st
from constants import THUMBNAIL_URL


def build_column_config(columns: List[str], editable_columns: List[str], date_column: str = "Last updated") -> dict:
    """
    Build a column_config dictionary for st.data_editor, specifying which columns are editable and their types.

    Args:
        columns (List[str]): List of all DataFrame column names.
        editable (List[str]): Columns allowed to be edited.
        date_column (str): Column that should be editable as a date (default is "Last updated").

    Returns:
        dict: Column configuration for use in st.data_editor, with appropriate types and editability.
    """
    config = {}
    for col in columns:
        if col == THUMBNAIL_URL:
            config[col] = st.column_config.ImageColumn(col, help="Preview", width="small")
        elif col == date_column and col in editable_columns:
            config[col] = st.column_config.DateColumn(col, help="Click to edit",  disabled=False)
        elif col in editable_columns:
            config[col] = st.column_config.TextColumn(col, help="Click to edit", disabled=False)
        else:
            config[col] = st.column_config.TextColumn(col, disabled=True)
    return config