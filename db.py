from getdata import get_investing_data
import pandas as pd



def store_csv():
    # Stores the scraped data and appends to a CSV file
    with open("Market Index.csv", "a") as file:
        for line in get_investing_data():
            for i, data in enumerate(line):
                file.write(str(data))
                if i < len(line) - 1:
                    file.write(";")
            file.write("\n")

def read_csv():
    # Define and read the csv file using pandas "read_csv" function while giving names to the column headers and then returns it
    csv_file = "Market Index.csv"
    data = pd.read_csv(csv_file, sep=";", header=None, names=["index", "company_name", "company_code", "last_price", "min_price", "max_price", "date"], encoding="iso-8859-1")
    return data

def store_hdf5():
    # Open an HDF5 file in write mode. If none exists, one will be created
    with pd.HDFStore("hdf5_file.h5") as store:

        # Store the data from "read_csv()" into the HDF5 file
        store["data"] = read_csv()

def read_hdf5():
    # Define the name of the HDF5 file
    hdf5_file = "hdf5_file.h5"
    pd.set_option("display.max_columns", None)

    # Open the HDF5 file for reading
    with pd.HDFStore(hdf5_file, "r") as store:

        # Loads data and returns it
        data = store["data"]
    return data



















