import xarray as xr
from pandas.core._numba.kernels import mean_

# know data in document
ds = xr.open_dataset(r'C:\Users\zENITH\Downloads\TIDI_data\2019\TIDI_PB_2019290_P0100_S0450_D011_R01.vec',engine='netcdf4')
# print(ds["alt_retrieved"].attrs,ds["alt_retrieved"].values)
ds = ds.set_coords("alt_retrieved")
ds.swap_dims({"nalts":"alt_retrieved"})
u_95 = ds['u'].sel(alt_retrieved = 95)
v_95 = ds['v'].sel(alt_retrieved = 95)
u_95 = u_95.dropna(dim = "nvec")
print(f"mean:{round(float(u_95.mean()),2)}")
print(f"std:{round(float(v_95.std()),2)}")
print(f"min:{round(float(u_95.min()),2)}")
print(f"max:{round(float(u_95.max()),2)}")


# for var in ds.data_vars:
#     print(var,ds[var].dims,ds[var].shape,ds[var].attrs)
#     print(ds[var].coords)
# def weather_data(data_path:tuple[str]):
#     """
#     :param data_path: input all data path
#     :return: list of weather data
#     """
#     data_list = []
#     for file in data_path:
#         with open(file, 'r', encoding = 'gbk') as f:
#             for line in f:
#                 data_list.append(line)
#     return data_list

# if __name__ == '__main__':
#     print(weather_data((r'C:\Users\zENITH\Downloads\TIDI_data\2019\TIDI_PB_2019290_P0100_S0450_D011_R01.vec',)))