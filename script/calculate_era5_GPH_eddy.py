'''
This script is for extracting 500hpa eddy geopotential height.
'''

import pandas as pd
import xarray as xr
import os
import numpy as np

os.chdir('/home/xtan/scratch/hzq/HWdna/rawData/era5')

## select domain range
lon_min = 40
lon_max = 160
lat_min = -20
lat_max = 60

## select level
sel_level_GPH1 = 500

## select year
year_start = 1961
year_end   = 2018

############## select 500 hpa GPH ############

i0 = year_start
hgt_i_ds = xr.open_dataset('geopotential_daily_era5_'+str(i0)+'.nc')
hgt_i = hgt_i_ds['z']
hgt_i = hgt_i / 9.80665
hgt_i = hgt_i.sel(level=sel_level_GPH1)
mask_lon = (hgt_i.longitude >= lon_min) & (hgt_i.longitude <= lon_max)
mask_lat = (hgt_i.latitude >= lat_min) & (hgt_i.latitude <= lat_max)
mask_lon_subtropic = (hgt_i.longitude >= 0) & (hgt_i.longitude <= 360)
mask_lat_subtropic = (hgt_i.latitude >= 0) & (hgt_i.latitude <= 40)

hgt_i_subtropic = hgt_i.where(mask_lon_subtropic & mask_lat_subtropic, drop = True)
subtropic_weight = np.cos(np.deg2rad(hgt_i_subtropic.latitude))
subtropic_weight.name = 'weight'
hgt_i_subtropic_weight = hgt_i_subtropic.weighted(subtropic_weight)
hgt_i = hgt_i - hgt_i_subtropic_weight.mean(('longitude','latitude'))
hgt_all_crop_500lev = hgt_i.where(mask_lon & mask_lat, drop=True)

for i in range(year_start+1,year_end+1):
    hgt_i_ds = xr.open_dataset('geopotential_daily_era5_'+str(i)+'.nc')
    hgt_i = hgt_i_ds['z']
    hgt_i = hgt_i / 9.80665
    hgt_i = hgt_i.sel(level=sel_level_GPH1)
    hgt_i_subtropic = hgt_i.where(mask_lon_subtropic & mask_lat_subtropic, drop = True)
    subtropic_weight = np.cos(np.deg2rad(hgt_i_subtropic.latitude))
    subtropic_weight.name = 'weight'
    hgt_i_subtropic_weight = hgt_i_subtropic.weighted(subtropic_weight)
    hgt_i = hgt_i - hgt_i_subtropic_weight.mean(('longitude','latitude'))
    hgt_i_crop = hgt_i.where(mask_lon & mask_lat, drop=True)
    hgt_all_crop_500lev = xr.concat([hgt_all_crop_500lev,hgt_i_crop],'time')
    print(i)

to_path1 = 'GPH_x' + str(lon_min) + '-' + str(lon_max) + '_y' + str(lat_min) + '-' + str(lat_max) + '_t_' + str(year_start) + '-' + str(year_end) + '_' + 'level' + str(sel_level_GPH1) + '_eddy.nc'
hgt_all_crop_500lev.to_netcdf(to_path1)