import os
import pandas as pd
import streamlit as st

@st.cache_data
def load_data(original_file: str, updated_file: str) -> pd.DataFrame:
    """
    Load the painting data from the updated or original csv file.

    Args:
        original_file (str): Path to the original csv file.
        updated_file (str): Path to the updated csv file.

    Returns:
        pd.DataFrame: The loaded painting data as a DataFrame.

    Raises:
        FileNotFoundError: If neither the updated nor the original file is found.
    """
    if os.path.exists(updated_file):
        return pd.read_csv(updated_file)
    elif os.path.exists(original_file):
        return pd.read_csv(original_file)
    else:
        raise FileNotFoundError("Neither updated nor original file found.")
   
def save_data(df: pd.DataFrame, updated_file: str):
    """
    Save the updated painting data to an csv file.

    Args:
        df (pd.DataFrame): The DataFrame to save.
        updated_file (str): Path to the updated csv file.
    """
    df.to_csv(updated_file, index=False)