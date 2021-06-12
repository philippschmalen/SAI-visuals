"""
Transform dataframe for plots
"""

import pandas as pd


def group_search_interest_on_time_unit(df, unit="M"):
    """Returns aggregated dataframe specified time unit. Uses pandas grouper
    see frequency options for other time units like weekly or annually"""

    # assert date as index for pd.Grouper
    assert (
        df.index.dtype == "datetime64[ns]"
    ), "Dataframe misses date index. No grouping on date unit possible."
    # assert keyword column
    assert (
        "keyword" in df.columns
    ), "Dataframe misses keyword column. No grouping on date unit possible."

    # groups to unit averages (defaults to monthly)
    df = df.groupby(["keyword", pd.Grouper(freq=unit)]).mean().reset_index()

    return df
