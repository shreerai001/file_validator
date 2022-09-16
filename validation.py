from utils import csv_to_df, get_first_common_column, sort_df, compare_lengths

file_df = csv_to_df('c1.csv')
database_df = csv_to_df('c2.csv')

a = get_first_common_column(file_df, database_df)

print(sort_df(a, file_df))


def compare():
    if compare_lengths(len(database_df), len(file_df)):
        if compare_lengths(len(database_df.columns), len(file_df.columns)):
            print("File size matched")
            return True
        else:
            print("File columns size does not matched")
            return False
    else:
        print("File Rows size does not matched")
        return False


compare()
