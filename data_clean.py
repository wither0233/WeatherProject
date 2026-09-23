import xarray as xr
import data_read
def clean_data(origin_data:xr.DataArray):
    """
    to clean illegal data include:data_ok == 'F', measure_track == 'W', longitude range > 90, wind speed > 300(fill with nan)
    :param origin_data: dataset input
    :return: dataset output after cleaning data
    """
    mask = (origin_data["data_ok"].astype(str) == 'T') & (origin_data["measure_track"].astype(str) == 'C')  &(origin_data["lat"].astype(float) <= 90) & (origin_data["lat"].astype(float) >= -90)
    origin_data = origin_data.where(mask, drop = True)
    mask_wind = (origin_data["u"].astype(float) <= 300) & (origin_data["u"].astype(float) >= -300)
    origin_data['u'] = origin_data['u'].where(mask_wind)
    return origin_data

if __name__ == "__main__":
    ds = data_read.data_load(r"C:\Users\zENITH\Downloads\TIDI_data",2019,270,290)
    print(ds.dims)
    ds = clean_data(ds)
    print(ds.dims)