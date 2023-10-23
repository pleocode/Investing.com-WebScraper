from db import read_hdf5
from matplotlib import pyplot as plt
import pandas as pd



def plot_data(data, index_name, size):
    # Filter the data to get only the rows with a specific "index_name"
    subset = data.loc[data["index"] == index_name].copy()

    # replace "," by "." to be accepted by pandas as float
    subset["last_price"] = subset["last_price"].str.replace(",", ".").astype(float)

    # Group the subset by "company_name"
    grouped = subset.groupby("company_name")


    # Create a new figure with the specified size
    plt.figure(figsize=size)

    # For each company in "grouped", extract the "date" and "last_price". And plots
    for name, group in grouped:
        plt.plot(group["date"], group["last_price"], label=name)

    # Set plot title and labels axes
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title(f"Company Last Price Over Time - {index_name}")
    plt.xticks(rotation=45)

    # Legend out of the chart
    legend = plt.legend(bbox_to_anchor=(1.05, 1.0), prop= {"size": 6},loc="upper left", facecolor="none")
    legend.get_frame().set_linewidth(0.0)


def chart(index, save):
    # Read data from the HDF5 file
    data = read_hdf5()

    # Define the size of the plot
    size = (16, 9)

    # Call the function plot_data
    plot_data(data, index, size)

    # Save and show the plot as an image with a transparent background
    plt.tight_layout()
    plt.savefig(save, transparent=True)
    plt.show()

def comparison():
    # Read data from the HDF5 file and create the dataframe from the "data" variable
    data = read_hdf5()
    df = pd.DataFrame(data)

    # replace "," by "." to be accepted by pandas as float
    df["last_price"] = df['last_price'].str.replace(",", ".").astype(float)

    # Calculate the average last price per index per date
    average_per_index_date = df.groupby(["index", "date"])["last_price"].mean().reset_index()

    # Create a frame to plot
    chart_frame = average_per_index_date.pivot(index="date", columns="index", values="last_price")

    # Create a line plot with a specific figsize
    chart = chart_frame.plot.line(figsize=(16, 9))

    # Set plot title and labels axes
    plt.title("Average Price per Day per Index")
    chart.set_xlabel("Date")
    plt.xticks(rotation=45)
    chart.set_ylabel("Price")

    # Legend out of the chart
    legend = chart.legend(bbox_to_anchor=(1.05, 1.0), prop={"size": 6}, loc="upper left", facecolor="none")
    legend.get_frame().set_linewidth(0.0)

    # Save and show the plot as an image with a transparent background
    plt.tight_layout()
    plt.savefig("comparison.png", transparent=True)
    plt.show()








