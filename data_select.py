import xarray as xr
import data_read
import data_clean

def select_data(input_data:xr.DataArray,altitude:float,lat_start:float,lat_end:float ):
    """
    select data to calculate and paint, meanwhile delete u == NAN data
    :param input_data: data array to deak with
    :param altitude: selected altitude
    :param lat_start: selected latitude min
    :param lat_end: selected latitude max
    :return: selected data array
    """
    selected_data = input_data.sel(alt_retrieved = altitude)
    selected_data = selected_data.where(selected_data['u'].notnull(), drop = True)
    mask = (selected_data["lat"] >= lat_start) & (selected_data["lat"] <= lat_end)
    selected_data = selected_data.where(mask, drop=True)
    return selected_data


if __name__ == "__main__":
    ds = data_read.data_load(r"C:\Users\zENITH\Downloads\TIDI_data", 2019, 250, 290)
    print(ds.dims)
    ds = data_clean.clean_data(ds)
    print(ds.dims)
    print(select_data(ds, altitude = 95, lat_start = -30, lat_end = 30).dims)
