import pandas as pd
from pandas import DataFrame


def csv_to_df(csv_filename: str):
    return pd.read_csv(csv_filename)


def get_first_common_column(df_from_file: DataFrame, df_from_database: DataFrame):
    return [i for i in df_from_file.columns if i in df_from_database.columns][0]


def sort_df(column_name: str, data_frame: DataFrame):
    return data_frame.sort_values(by=column_name, ascending=False)


def compare_lengths(df_from_file_columns_size: int, df_from_database_columns_size: int):
    return df_from_file_columns_size == df_from_database_columns_size
