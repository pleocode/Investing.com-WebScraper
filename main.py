from db import store_csv, store_hdf5
from visualization import chart, comparison
import questionary

def cli():

    stop = False
    while not stop:
        choice = questionary.select("Welcome, select the desired option", choices=["Scrappe and store Investing.com in CSV File", "Store CSV File in HDF5", "PSI20 chart",
                                                                                   "IBEX35 chart", "DAX chart", "All charts", "Compare Indexes", "Exit"]).ask()

        if choice == "Scrappe and store Investing.com in CSV File":
            store_csv()

        elif choice == "Store CSV File in HDF5":
            store_hdf5()

        elif choice == "PSI20 chart":
            chart("PSI (PSI20)", "psi20.png")

        elif choice == "IBEX35 chart":
            chart("IBEX 35 (IBEX)", "ibex35.png")

        elif choice == "DAX chart":
            chart("DAX (GDAXI)", "dax.png")

        elif choice == "All charts":
            chart("PSI (PSI20)", "psi20.png")
            chart("IBEX 35 (IBEX)", "ibex35.png")
            chart("DAX (GDAXI)", "dax.png")

        elif choice == "Compare Indexes":
            comparison()

        else:
            print("See you tomorrow")
            stop = True

if __name__ == "__main__":
    cli()
