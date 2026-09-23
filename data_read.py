import xarray as xr
from pathlib import Path

def data_load(filepath:str,year_file:int,day_start:int,day_end:int):
    """
    Function to load data from file
    :param filepath:your path to store TIDI data.
    :param year_file:choose year in the path to get TIDI data.
    :param day_start:data range start.
    :param day_end:data range end.
    :return:dataset of TIDI data in range.
    :rtype: xarray.Dataset(dims:"time","alt_retrieved")
    """
    ds_list = []
    for day in range(day_start,day_end+1):
        document_name = "TIDI_PB_" + str(year_file) + str(day) + "_P0100_S0450_D011_R01.VEC"
        final_filepath = Path(filepath) / str(year_file) / document_name
        ds = xr.open_dataset(final_filepath)
        ds = ds.set_coords(["time","alt_retrieved"])
        ds = ds.swap_dims({"nvec":"time", "nalts":"alt_retrieved"})
        ds_list.append(ds)
    final_ds = xr.concat(ds_list, dim="time")
    return final_ds


if __name__ == "__main__":
    ds1 = data_load(r"C:\Users\zENITH\Downloads\TIDI_data",2019,270,290)
    print(ds1.dims)

