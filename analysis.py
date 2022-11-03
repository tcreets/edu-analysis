import csv

list_data = []
with open("states_all.csv", "r") as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        list_data.append(row)


def filter(state,column):
    """
    Function to filter and select clean data of the specified state and column

    Parameters
    ----------
    state: str
    column: str

    Returns
    -------
    column_data: list
    list of strings
    """
    state_data = [row for row in list_data if row["STATE"] == state.upper()]
    column_data = [row[column.upper()] for row in state_data if row[column.upper()] != '']
    return column_data



