import pandas as pd

def filter_results(df: pd.DataFrame, search_term: str) -> pd.DataFrame:
    """
    Filter the DataFrame to rows where the search term appears in any of several key columns.

    Args:
        df (pd.DataFrame): The DataFrame to filter.
        search_term (str): User input, should match title, artist, inventory number, or location.

    Returns:
        pd.DataFrame: Filtered and processed DataFrame.
    """
    if df.empty:
        return df

    mask = (
        df["Painting title"].str.contains(search_term, case=False, na=False) | \
        df["Artist's name"].str.contains(search_term, case=False, na=False) | \
        df["Inventory number"].str.contains(search_term, case=False, na=False) | \
        df["Location"].str.contains(search_term, case=False, na=False)
    )

    filtered_df = df[mask] if search_term else df

    # Convert "Last updated" to datetime.date type for proper display/editing
    if "Last updated" in filtered_df.columns:
        filtered_df["Last updated"] = pd.to_datetime(filtered_df["Last updated"], errors="coerce").dt.date

    filtered_df = filtered_df.copy()
    filtered_df.index = filtered_df.index + 1

    return filtered_df