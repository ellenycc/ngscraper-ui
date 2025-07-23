import os
import streamlit as st
from data_handler import load_data, save_data
from constants import EDITABLE_COLUMNS, ORIGINAL_FILE, UPDATED_FILE
from config import build_column_config
from filters import filter_results
from ui import show_title_and_description, show_search, show_results_count, show_editable_table

# Set page config
st.set_page_config(
    page_title="National Gallery Painting Resolution Database",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="expanded"
)

show_title_and_description()

# Load the data
with st.spinner("Loading data..."):
    try:
        df = load_data(ORIGINAL_FILE, UPDATED_FILE)
        if "Notes" in df.columns:
            df["Notes"] = df["Notes"].astype(str)
    except FileNotFoundError as e:
        st.error(str(e))
        st.stop()  # Stop execution if data file is missing

# Search/filter
search = show_search()
filtered_df = filter_results(df, search)
show_results_count(len(filtered_df))

# Build column configuration so only certain columns are editable in the data editor
column_config = build_column_config(filtered_df.columns, EDITABLE_COLUMNS)

# Show the editable data table; only columns specified in column_config are editable
edited_df = show_editable_table(filtered_df, column_config)

# Save changes to the updated file and refresh the app state
if st.button("Save Changes"):
    with st.spinner("Saving data..."):
        try:
            save_data(edited_df, UPDATED_FILE)
            st.success(f"Saved as {UPDATED_FILE}")
            st.cache_data.clear()  # Clear Streamlit's cache to ensure fresh data is loaded
            st.rerun()  # Rerun the app to reflect changes
        except Exception as e:
            st.error(f"Error saving file: {e}")

# Reset to original data by deleting the updated file and refreshing the app
if st.button("Reset to Original Data"):
    with st.spinner("Resetting to original data..."):
        if os.path.exists(UPDATED_FILE):
            os.remove(UPDATED_FILE)
            st.cache_data.clear()
            st.rerun()