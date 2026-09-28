import xarray as xr
import numpy as np
import scipy.optimize as opt
import data_read
import data_clean
import data_select
import data_process

def fit_data(input_data:xr.Dataset, wave_number:int, period:float, sign_direction:int = 1):
    time = input_data["time"].values
    lon = input_data["lon"].values
    u = input_data["u"].values
    omega = 2 * np.pi / period
    def model(x, A, B, C):
        t, l = x
        pause = (omega * t + sign_direction * wave_number * l)
        return A * np.cos(pause) + B * np.sin(pause) + C

    initial_guess = [
        np.std(u),
        np.std(u),
        np.mean(u)
    ]
    popt, pcov = opt.curve_fit(model,(time, lon),u,p0 = initial_guess,maxfev = 20000)
    A, B, C = popt
    amplitude = np.sqrt(
        A ** 2 + B ** 2
    )

    return amplitude

def scan_wave_period(input_data:xr.Dataset, wave_number_start:int, wave_number_end:int, period_start:float, period_end:float):
    """
    to calculate amplitudes in different range of wave_number and period
    :param input_data: dataset after process
    :param wave_number_start: wave_number range to start scanning
    :param wave_number_end: wave_number range to end scanning
    :param period_start: period range to start scanning
    :param period_end: period range to end scanning
    :return: xarray DataArray with value amplitudes,coops:"period", "wave_number"
    """
    wave_numbers = np.arange(wave_number_start, wave_number_end + 1)
    periods = np.arange(period_start, period_end + 1, 2)
    amplitudes = np.full((len(periods),len(wave_numbers)),np.nan)
    for i,period in enumerate(periods):
        for j,wave_number in enumerate(wave_numbers):
            amplitudes[i][j] = fit_data(input_data, wave_number, period)
    return xr.DataArray(amplitudes, dims = ("period","wave_number"),
                        coords={"period":periods, "wave_number":wave_numbers},
                        attrs = {"units":"m/s"} )

if __name__ == "__main__":
    ds = data_read.data_load(r"C:\Users\zENITH\Downloads\TIDI_data", 2019, 258, 272)
    # print("dims after read:", ds.dims)
    ds = data_clean.clean_data(ds)
    # print("dims after clean:", ds.dims)
    ds = data_select.select_data(ds, altitude = 95, lat_start = -5, lat_end = 5)
    # print("data after select:", ds.dims, ds['u'].sizes)
    ds = data_process.process_data(ds)
    # print("time after processing:", ds["time"].values)
    # print("lon after processing:", ds["lon"].values)
    print(scan_wave_period(ds,0,3,88,160))