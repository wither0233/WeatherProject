import xarray as xr
from data_read import data_load
from data_clean import clean_data
from data_select import select_data
from data_process import process_data
from data_fit import scan_wave_period
from painting import paint_wave_period

def main():
    year = 2013
    day_start = 258
    day_end = 272
    ds = data_load( year, day_start, day_end)
    ds = clean_data(ds)
    ds = select_data(ds, altitude = 95, lat_start = -10, lat_end = 10)
    ds = process_data(ds)
    ds = scan_wave_period(ds, -4, 4, 80, 180)
    paint_wave_period(ds,year, day_start, day_end)


if __name__ == "__main__":
    main()