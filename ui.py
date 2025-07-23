import pandas as pd
import streamlit as st

def show_title_and_description():
    """
    Display the app title, description, and search/filter section headers.
    """
    st.title("National Gallery Painting Resolution Database")
    st.markdown(
        """
        <span style='font-size:1.1em;'>
        This app serves as an <b>internal database</b> for the Digital Services team to view, search, \
        and update the <b>highest available pixel dimensions</b> for paintings in the Gallery's collection.
        </span>
        """,
        unsafe_allow_html=True
        )
    st.markdown("##")
    st.subheader("User Guide")
    st.markdown(
        """
        <ul style='font-size:1.05em;'>
            <li><b>Search</b> paintings by <b>NG number</b>, <b>title</b>, <b>artist</b>, or <b>location</b>.</li>
            <li><b>Update</b> Pixel dimensions W x H, File format, Last updated, and Notes directly in the table.</li>
            <li>Click <b>Save Changes</b> to store your edits in the database.</li>
            <li>Click <b>Reset to Original Data</b> to discard all changes and reload the original file.</li>
        </ul>
        """,
        unsafe_allow_html=True
    )
    st.markdown("---")


def show_search():
    """
    Display a text input for searching paintings.

    Returns:
        str: The user's search query.
    """
    return st.text_input("Search by NG number, title, artist or location")

def show_results_count(count: int):
    """
    Display the number of paintings found after filtering.

    Args:
        count (int): The number of paintings found.
    """
    return st.write(f"Found {count} painting(s)")

def show_editable_table(df: pd.DataFrame, column_config: dict):
    """
    Display an editable data table with specified column configuration.

    Args:
        df (pd.DataFrame): The DataFrame to display and edit.
        column_config (dict): Configuration for editable/read-only columns.

    Returns:
        pd.DataFrame: The edited DataFrame as returned by st.data_editor.
    """
    return st.data_editor(df, column_config=column_config, use_container_width=True)