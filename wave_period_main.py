import xarray as xr
from data_read import data_load
from data_clean import clean_data
from data_select import select_data
from data_process import process_data
from data_fit import scan_wave_period
from painting import paint_wave_period

year = 2013
day_start = 258
day_end = 273
ds = data_load(r"C:\Users\zENITH\Downloads\TIDI_data", year, day_start, day_end)
ds = clean_data(ds)
ds = select_data(ds, altitude = 95, lat_start = -10, lat_end = 10)
ds = process_data(ds)
ds = scan_wave_period(ds, -2, 4, 80, 180)
paint_wave_period(ds,year, day_start, day_end)