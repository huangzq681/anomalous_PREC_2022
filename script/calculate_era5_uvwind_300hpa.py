'''
This script is for extracting 300hpa zonal and meridional wind from ERA5.
'''

import pandas as pd
import xarray as xr
import os

os.chdir('/lustre07/scratch/xtan/hzq/HWdna/rawData/era5')

## select domain range
lon_min = 40
lon_max = 160
lat_min = -20
lat_max = 60

## select level
sel_level_uvwind = 300

## select year
year_start = 1961
year_end   = 2018


# ############### select 300 hpa uvwind ####################
## uwind
i0 = year_start
uwind_i_ds = xr.open_dataset('u_component_of_wind_daily_era5_' + str(i0) + '.nc')
uwind_i = uwind_i_ds['u']
mask_lon = (uwind_i.longitude >= lon_min) & (uwind_i.longitude <= lon_max)
mask_lat = (uwind_i.latitude >= lat_min) & (uwind_i.latitude <= lat_max)
uwind_i_crop = uwind_i.where(mask_lon & mask_lat, drop=True)
uwind_i_crop_300lev = uwind_i_crop.sel(level=sel_level_uvwind)

vwind_i_ds = xr.open_dataset('v_component_of_wind_daily_era5_' + str(i0) + '.nc')
vwind_i = vwind_i_ds['v']
vwind_i_crop = vwind_i.where(mask_lon & mask_lat, drop=True)
vwind_i_crop_300lev = vwind_i_crop.sel(level=sel_level_uvwind)

uvwind_all_300lev = (uwind_i_crop_300lev ** 2 + vwind_i_crop_300lev ** 2) ** 0.5

for i in range(year_start+1,year_end+1):
    uwind_i_ds = xr.open_dataset('u_component_of_wind_daily_era5_'+str(i)+'.nc')
    uwind_i = uwind_i_ds['u']
    uwind_i_crop = uwind_i.where(mask_lon & mask_lat, drop=True)
    uwind_i_crop_300lev = uwind_i_crop.sel(level=sel_level_uvwind)

    vwind_i_ds = xr.open_dataset('v_component_of_wind_daily_era5_'+str(i)+'.nc')
    vwind_i = vwind_i_ds['v']
    vwind_i_crop = vwind_i.where(mask_lon & mask_lat, drop=True)
    vwind_i_crop_300lev = vwind_i_crop.sel(level=sel_level_uvwind)

    uvwind_i_300lev = (uwind_i_crop_300lev ** 2 + vwind_i_crop_300lev ** 2) ** 0.5
    uvwind_all_300lev = xr.concat([uvwind_all_300lev,uvwind_i_300lev],'time')

    print(i)

to_path3 = 'uvwind_x' + str(lon_min) + '-' + str(lon_max) + '_y' + str(lat_min) + '-' + str(lat_max) + '_t' + str(year_start) + '-' + str(year_end) + '_' + 'level' + str(sel_level_uvwind) + '.nc'
uvwind_all_300lev.to_netcdf(to_path3)

