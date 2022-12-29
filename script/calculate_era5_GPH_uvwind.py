'''
This script is for extracting 500hpa geopotential height and 200hpa, 850hpa zonal and meridional wind from ERA5.
'''

import pandas as pd
import xarray as xr
import os

os.chdir('/home/xtan/scratch/hzq/reanalysis/era5_newversion')

## select domain range
lon_min = 40
lon_max = 160
lat_min = -20
lat_max = 60

## select level
sel_level_GPH1 = 500
sel_level_GPH2 = 850
sel_level_uvwind = 850
sel_level_eaj = 200

## select year
year_start = 1961
year_end   = 2018

############## select 500 hpa and 850 hpa GPH ############
# i0 = year_start
# hgt_i_ds = xr.open_dataset('geopotential_daily_era5_' + str(i0) + '.nc')
# hgt_i = hgt_i_ds['z']
# hgt_i = hgt_i / 9.80665
# mask_lon = (hgt_i.longitude >= lon_min) & (hgt_i.longitude <= lon_max)
# mask_lat = (hgt_i.latitude >= lat_min) & (hgt_i.latitude <= lat_max)
# hgt_i_crop = hgt_i.where(mask_lon & mask_lat, drop=True)
# hgt_all_crop_500lev = hgt_i_crop.sel(level=sel_level_GPH1)
# hgt_all_crop_850lev = hgt_i_crop.sel(level=sel_level_GPH1)

# for i in range(year_start+1,year_end+1):
#     hgt_i_ds = xr.open_dataset('geopotential_daily_era5_'+str(i)+'.nc')
#     hgt_i = hgt_i_ds['z']
#     hgt_i = hgt_i / 9.80665
#     hgt_i_crop = hgt_i.where(mask_lon & mask_lat, drop=True)
#     hgt_i_crop_500lev = hgt_i_crop.sel(level=sel_level_GPH1)
#     hgt_i_crop_850lev = hgt_i_crop.sel(level=sel_level_GPH2)
#     hgt_all_crop_500lev = xr.concat([hgt_all_crop_500lev,hgt_i_crop_500lev],'time')
#     hgt_all_crop_850lev = xr.concat([hgt_all_crop_850lev,hgt_i_crop_850lev],'time')
#     print(i)

# to_path1 = 'GPH_x' + str(lon_min) + '-' + str(lon_max) + '_y' + str(lat_min) + '-' + str(lat_max) + '_t' + str(year_start) + '-' + str(year_end) + '_' + 'level' + str(sel_level_GPH1) + '.nc'
# hgt_all_crop_500lev.to_netcdf(to_path1)
# to_path2 = 'GPH_x' + str(lon_min) + '-' + str(lon_max) + '_y' + str(lat_min) + '-' + str(lat_max) + '_t' + str(year_start) + '-' + str(year_end) + '_' + 'level' + str(sel_level_GPH2) + '.nc'
# hgt_all_crop_850lev.to_netcdf(to_path2)

# ############### select 850 hpa uvwind ####################
# ## uwind
# i0 = year_start
# uwind_i_ds = xr.open_dataset('u_component_of_wind_daily_era5_' + str(i0) + '.nc')
# uwind_i = uwind_i_ds['u']
# mask_lon = (uwind_i.longitude >= lon_min) & (uwind_i.longitude <= lon_max)
# mask_lat = (uwind_i.latitude >= lat_min) & (uwind_i.latitude <= lat_max)
# uwind_i_crop = uwind_i.where(mask_lon & mask_lat, drop=True)
# uwind_all_crop_850lev = uwind_i_crop.sel(level=sel_level_uvwind)

# for i in range(year_start+1,year_end+1):
#     uwind_i_ds = xr.open_dataset('u_component_of_wind_daily_era5_'+str(i)+'.nc')
#     uwind_i = uwind_i_ds['u']
#     uwind_i_crop = uwind_i.where(mask_lon & mask_lat, drop=True)
#     uwind_i_crop_850lev = uwind_i_crop.sel(level=sel_level_uvwind)
#     uwind_all_crop_850lev = xr.concat([uwind_all_crop_850lev,uwind_i_crop_850lev],'time')
#     print(i)

# to_path3 = 'uwind_x' + str(lon_min) + '-' + str(lon_max) + '_y' + str(lat_min) + '-' + str(lat_max) + '_t' + str(year_start) + '-' + str(year_end) + '_' + 'level' + str(sel_level_uvwind) + '.nc'
# uwind_all_crop_850lev.to_netcdf(to_path3)

# ## vwind
# i0 = year_start
# vwind_i_ds = xr.open_dataset('v_component_of_wind_daily_era5_' + str(i0) + '.nc')
# vwind_i = vwind_i_ds['v']
# mask_lon = (vwind_i.longitude >= lon_min) & (vwind_i.longitude <= lon_max)
# mask_lat = (vwind_i.latitude >= lat_min) & (vwind_i.latitude <= lat_max)
# vwind_i_crop = vwind_i.where(mask_lon & mask_lat, drop=True)
# vwind_all_crop_850lev = vwind_i_crop.sel(level=sel_level_uvwind)

# for i in range(year_start+1,year_end+1):
#     vwind_i_ds = xr.open_dataset('v_component_of_wind_daily_era5_'+str(i)+'.nc')
#     vwind_i = vwind_i_ds['v']
#     vwind_i_crop = vwind_i.where(mask_lon & mask_lat, drop=True)
#     vwind_i_crop_850lev = vwind_i_crop.sel(level=sel_level_uvwind)
#     vwind_all_crop_850lev = xr.concat([vwind_all_crop_850lev,vwind_i_crop_850lev],'time')
#     print(i)

# to_path4 = 'vwind_x' + str(lon_min) + '-' + str(lon_max) + '_y' + str(lat_min) + '-' + str(lat_max) + '_t' + str(year_start) + '-' + str(year_end) + '_' + 'level' + str(sel_level_uvwind) + '.nc'
# vwind_all_crop_850lev.to_netcdf(to_path4)

########## 200 hpa uwind ######
# i0 = year_start
# uwind_i_ds = xr.open_dataset('u_component_of_wind_daily_era5_' + str(i0) + '_200hpa.nc')
# uwind_i = uwind_i_ds['u']
# mask_lon = (uwind_i.longitude >= lon_min) & (uwind_i.longitude <= lon_max)
# mask_lat = (uwind_i.latitude >= lat_min) & (uwind_i.latitude <= lat_max)
# uwind_i_crop = uwind_i.where(mask_lon & mask_lat, drop=True)
# uwind_all_crop_250lev = uwind_i_crop #.sel(level=sel_level_eaj)

# for i in range(year_start+1,year_end+1):
#     uwind_i_ds = xr.open_dataset('u_component_of_wind_daily_era5_'+str(i)+'_200hpa.nc')
#     uwind_i = uwind_i_ds['u']
#     uwind_i_crop = uwind_i.where(mask_lon & mask_lat, drop=True)
#     uwind_i_crop_250lev = uwind_i_crop #.sel(level=sel_level_eaj)
#     uwind_all_crop_250lev = xr.concat([uwind_all_crop_250lev,uwind_i_crop_250lev],'time')
#     print(i)

# to_path5 = 'uwind_x' + str(lon_min) + '-' + str(lon_max) + '_y' + str(lat_min) + '-' + str(lat_max) + '_t' + str(year_start) + '-' + str(year_end) + '_' + 'level' + str(sel_level_eaj) + '.nc'
# uwind_all_crop_250lev.to_netcdf(to_path5)

# ########## total cloud cover ######
# i0 = year_start
# tcc_i_ds = xr.open_dataset('total_cloud_cover_daily_era5_' + str(i0) + '.nc')
# tcc_i = tcc_i_ds['tcc']
# mask_lon = (tcc_i.longitude >= lon_min) & (tcc_i.longitude <= lon_max)
# mask_lat = (tcc_i.latitude >= lat_min) & (tcc_i.latitude <= lat_max)
# tcc_i_crop = tcc_i.where(mask_lon & mask_lat, drop=True)
# tcc_all_crop = tcc_i_crop

# for i in range(year_start+1,year_end+1):
#     tcc_i_ds = xr.open_dataset('total_cloud_cover_daily_era5_'+str(i)+'.nc')
#     tcc_i = tcc_i_ds['tcc']
#     tcc_i_crop = tcc_i.where(mask_lon & mask_lat, drop=True)
#     tcc_all_crop = xr.concat([tcc_all_crop,tcc_i_crop],'time')
#     print(i)

# to_path6 = 'tcc_x' + str(lon_min) + '-' + str(lon_max) + '_y' + str(lat_min) + '-' + str(lat_max) + '_t' + str(year_start) + '-' + str(year_end) + '.nc'
# tcc_all_crop.to_netcdf(to_path6)

# ########## top net thermal radiation ######
# i0 = year_start
# ttr_i_ds = xr.open_dataset('top_net_thermal_radiation_daily_era5_' + str(i0) + '.nc')
# ttr_i = ttr_i_ds['ttr']
# mask_lon = (ttr_i.longitude >= lon_min) & (ttr_i.longitude <= lon_max)
# mask_lat = (ttr_i.latitude >= lat_min) & (ttr_i.latitude <= lat_max)
# ttr_i_crop = ttr_i.where(mask_lon & mask_lat, drop=True)
# ttr_all_crop = ttr_i_crop

# for i in range(year_start+1,year_end+1):
#     ttr_i_ds = xr.open_dataset('top_net_thermal_radiation_daily_era5_'+str(i)+'.nc')
#     ttr_i = ttr_i_ds['ttr']
#     ttr_i_crop = ttr_i.where(mask_lon & mask_lat, drop=True)
#     ttr_all_crop = xr.concat([ttr_all_crop,ttr_i_crop],'time')
#     print(i)

# to_path7 = 'ttr_x' + str(lon_min) + '-' + str(lon_max) + '_y' + str(lat_min) + '-' + str(lat_max) + '_t' + str(year_start) + '-' + str(year_end) + '.nc'
# ttr_all_crop.to_netcdf(to_path7)

# ########## vertical integral of northward water vapour flux ######
# i0 = year_start
# viwvn_i_ds = xr.open_dataset('vertical_integral_of_northward_water_vapour_flux_daily_era5_' + str(i0) + '.nc')
# viwvn_i = viwvn_i_ds['viwvn']
# mask_lon = (viwvn_i.longitude >= lon_min) & (viwvn_i.longitude <= lon_max)
# mask_lat = (viwvn_i.latitude >= lat_min) & (viwvn_i.latitude <= lat_max)
# viwvn_i_crop = viwvn_i.where(mask_lon & mask_lat, drop=True)
# viwvn_all_crop = viwvn_i_crop

# for i in range(year_start+1,year_end+1):
#     viwvn_i_ds = xr.open_dataset('vertical_integral_of_northward_water_vapour_flux_daily_era5_'+str(i)+'.nc')
#     viwvn_i = viwvn_i_ds['viwvn']
#     viwvn_i_crop = viwvn_i.where(mask_lon & mask_lat, drop=True)
#     viwvn_all_crop = xr.concat([viwvn_all_crop,viwvn_i_crop],'time')
#     print(i)

# to_path8 = 'viwvn_x' + str(lon_min) + '-' + str(lon_max) + '_y' + str(lat_min) + '-' + str(lat_max) + '_t' + str(year_start) + '-' + str(year_end) + '.nc'
# viwvn_all_crop.to_netcdf(to_path8)

# ########## vertical integral of eastward water vapour flux ######
# i0 = year_start
# wiwve_i_ds = xr.open_dataset('vertical_integral_of_eastward_water_vapour_flux_daily_era5_' + str(i0) + '.nc')
# wiwve_i = wiwve_i_ds['wiwve']
# mask_lon = (wiwve_i.longitude >= lon_min) & (wiwve_i.longitude <= lon_max)
# mask_lat = (wiwve_i.latitude >= lat_min) & (wiwve_i.latitude <= lat_max)
# wiwve_i_crop = wiwve_i.where(mask_lon & mask_lat, drop=True)
# wiwve_all_crop = wiwve_i_crop

# for i in range(year_start+1,year_end+1):
#     wiwve_i_ds = xr.open_dataset('vertical_integral_of_eastward_water_vapour_flux_daily_era5_'+str(i)+'.nc')
#     wiwve_i = wiwve_i_ds['wiwve']
#     wiwve_i_crop = wiwve_i.where(mask_lon & mask_lat, drop=True)
#     wiwve_all_crop = xr.concat([wiwve_all_crop,wiwve_i_crop],'time')
#     print(i)

# to_path9 = 'wiwve_x' + str(lon_min) + '-' + str(lon_max) + '_y' + str(lat_min) + '-' + str(lat_max) + '_t' + str(year_start) + '-' + str(year_end) + '.nc'
# wiwve_all_crop.to_netcdf(to_path9)

# ########## sea surface temperature ######
# i0 = year_start
# sst_i_ds = xr.open_dataset('sea_surface_temperature_daily_era5_' + str(i0) + '.nc')
# sst_i = sst_i_ds['sst']
# mask_lon = (sst_i.longitude >= lon_min) & (sst_i.longitude <= lon_max)
# mask_lat = (sst_i.latitude >= lat_min) & (sst_i.latitude <= lat_max)
# sst_i_crop = sst_i.where(mask_lon & mask_lat, drop=True)
# sst_all_crop = sst_i_crop

# for i in range(year_start+1,year_end+1):
#     sst_i_ds = xr.open_dataset('sea_surface_temperature_daily_era5_'+str(i)+'.nc')
#     sst_i = sst_i_ds['sst']
#     sst_i_crop = sst_i.where(mask_lon & mask_lat, drop=True)
#     sst_all_crop = xr.concat([sst_all_crop,sst_i_crop],'time')
#     print(i)

# to_path10 = 'sst_x' + str(lon_min) + '-' + str(lon_max) + '_y' + str(lat_min) + '-' + str(lat_max) + '_t' + str(year_start) + '-' + str(year_end) + '.nc'
# sst_all_crop.to_netcdf(to_path10)

########## vertically_integrated_moisture_divergence ######
i0 = year_start
vimd_i_ds = xr.open_dataset('vertically_integrated_moisture_divergence_daily_era5_' + str(i0) + '.nc')
vimd_i = vimd_i_ds['vimd']
mask_lon = (vimd_i.longitude >= lon_min) & (vimd_i.longitude <= lon_max)
mask_lat = (vimd_i.latitude >= lat_min) & (vimd_i.latitude <= lat_max)
vimd_i_crop = vimd_i.where(mask_lon & mask_lat, drop=True)
vimd_all_crop = vimd_i_crop

for i in range(year_start+1,year_end+1):
    vimd_i_ds = xr.open_dataset('vertically_integrated_moisture_divergence_daily_era5_'+str(i)+'.nc')
    vimd_i = vimd_i_ds['vimd']
    vimd_i_crop = vimd_i.where(mask_lon & mask_lat, drop=True)
    vimd_all_crop = xr.concat([vimd_all_crop,vimd_i_crop],'time')
    print(i)

to_path11 = 'vimd_x' + str(lon_min) + '-' + str(lon_max) + '_y' + str(lat_min) + '-' + str(lat_max) + '_t' + str(year_start) + '-' + str(year_end) + '.nc'
vimd_all_crop.to_netcdf(to_path11)