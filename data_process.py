import xarray as xr
import data_read
import data_clean
import data_select

def process_data(input_data:xr.Dataset):
    """
    to process dataset "time": begin from 0, units:hours
    lon : units: radions
    :param input_data: input dataset
    :return: the dataset after processing
    """
    input_data["time"] = (input_data["time"] - input_data["time"].isel(time = 0)) / 3600
    input_data["lon"] = input_data["lon"] / 360
    return input_data


if __name__ == "__main__":
    ds = data_read.data_load(r"C:\Users\zENITH\Downloads\TIDI_data", 2019, 250, 290)
    print("dims after read:", ds.dims)
    ds = data_clean.clean_data(ds)
    print("dims after clean:", ds.dims)
    ds = data_select.select_data(ds, altitude=95, lat_start=-30, lat_end=30)
    print("data after select:", ds.dims,ds['u'].sizes)
    ds = process_data(ds)
    print("time after processing:", ds["time"].values)
    print("lon after processing:", ds["lon"].values)