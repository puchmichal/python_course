import csv
import os

DATA_PATH = "./data/"

FILE_HEADER_FORMAT = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

CLOSE_COL_NAME = "Close"
OPEN_COL_NAME = "Open"
CHANGE_COL_NAME = "Change"

NEW_FILES_PREFIX = "changes_"


def run():
    files = [file for file in os.listdir(DATA_PATH) if file.endswith(".csv")]

    if len(files) == 0:
        raise FileNotFoundError("No csv files in directory.")

    for file_name in files:
        with open(os.path.join(DATA_PATH, file_name), "r") as f:
            reader = csv.reader(f, delimiter=",")
            header = next(reader)

            if FILE_HEADER_FORMAT != header:
                raise ValueError("Incorrect format of CSV file.")

            with open(os.path.join(DATA_PATH, NEW_FILES_PREFIX + file_name), "w") as output:
                writer = csv.writer(output, delimiter=",")
                writer.writerow(header + [CHANGE_COL_NAME])

                for row in reader:
                    open_value = float(row[header.index(OPEN_COL_NAME)])
                    close_value = float(row[header.index(CLOSE_COL_NAME)])
                    change_value = str((close_value - open_value) / open_value)

                    writer.writerow(row + [change_value])


if __name__ == "__main__":
    run()
