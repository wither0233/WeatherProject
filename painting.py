from operator import truediv

import matplotlib.pyplot as plt
import xarray as xr
import data_read
import data_clean
import data_select
import data_process
import data_fit
from config import get_config

def paint_wave_period(fit_datas:xr.DataArray, year:int, day_start:int, day_end:int):
    periods = fit_datas["period"].values
    wave_numbers = fit_datas["wave_number"].values
    amplitudes = fit_datas.values
    Project_ROOT = get_config().parent
    Output_ROOT = Project_ROOT / "output"
    Output_ROOT.mkdir(parents = True, exist_ok=True)
    output_file = Output_ROOT / "result.png"
    fig, ax = plt.subplots(figsize=(8, 6))
    contour = ax.contourf(
        wave_numbers,
        periods,
        amplitudes,
        levels = 25
    )
    colorbar = fig.colorbar(
        contour,
        ax = ax
    )
    colorbar.set_label("Amplitude (m/s)")
    ax.set_xlabel("Zonal wave number")
    ax.set_ylabel("Period (hours)")
    ax.set_title(f"Period–Wave Number Spectrum Of {year} - {day_start} to {day_end}")
    plt.tight_layout()
    plt.savefig(output_file, dpi = 300, bbox_inches = "tight")
    plt.show()

if __name__ == "__main__":
    year = 2013
    day_start = 258
    day_end = 273
    ds = data_read.data_load(r"C:\Users\zENITH\Downloads\TIDI_data", year, day_start, day_end)
    # print("dims after read:", ds.dims)
    ds = data_clean.clean_data(ds)
    # print("dims after clean:", ds.dims)
    ds = data_select.select_data(ds, altitude = 95, lat_start = -10, lat_end = 10)
    # print("data after select:", ds.dims, ds['u'].sizes)
    ds = data_process.process_data(ds)
    # print("time after processing:", ds["time"].values)
    # print("lon after processing:", ds["lon"].values)
    ds = data_fit.scan_wave_period(ds, -2, 4, 80, 180)
    paint_wave_period(ds,year, day_start, day_end)