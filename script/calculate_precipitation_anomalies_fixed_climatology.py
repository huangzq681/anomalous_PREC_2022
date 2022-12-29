'''
This script is for calculating the summer precipitation anomalies (MAY, JUN, JUL, AUG, SEP, OCT) with respect to their climatological mean for CMIP6 simulations
Two scenarios for the CMIP6 simulation applied: historical and ssp585
The CMIP6 simulation datasets are obtained from the global daily downscaled projects of NASA (https://www.nasa.gov/nex/gddp)
All available models in NEX-GDDP-CMIP6 are used.
We first concatenate the historical and ssp585 period, and then calculate the anomalies based on a fixed climatological mean.

The processing procedures include:
1. Aggregate the CMIP6 simulations with the periods of history (1961-2014) and ssp585 (2015-2100) scenarios for each model respectively;
2. Regrid the spatial resolution of the dataset as 0.5X0.5 (same as observation), and select the domain extent of the research area;
3. Trim the regrided dataset with a mask of ROI (China in our study);
4. Calculate 20-year running climatologies of each model;
5. The climatological anomalies are then calculated by subtracting the climatological means from their historical time series.
'''

import xarray as xr
import os
import glob
import numpy as np

dir = '/scratch/xtan/hzq/NASA_down'
os.chdir(dir)

models = [
    'ACCESS-CM2','ACCESS-ESM1-5','BCC-CSM2-MR','CESM2-WACCM','CESM2','CMCC-CM2-SR5','CMCC-ESM2','CNRM-CM6-1','CNRM-ESM2-1','CanESM5',
    'EC-Earth3-Veg-LR','EC-Earth3','FGOALS-g3','GFDL-CM4','GFDL-CM4_gr2','GFDL-ESM4','GISS-E2-1-G','HadGEM3-GC31-LL','HadGEM3-GC31-MM',
    'IITM-ESM','INM-CM4-8','INM-CM5-0','IPSL-CM6A-LR','KACE-1-0-G','KIOST-ESM','MIROC-ES2L','MIROC6','MPI-ESM1-2-HR','MPI-ESM1-2-LR',
    'MRI-ESM2-0','NESM3','NorESM2-LM','NorESM2-MM','TaiESM1','UKESM1-0-LL']
forcings = ['historical','ssp585']
lon_regrid = np.arange(0.25,360.25,0.5)
lat_regrid = np.arange(-59.75,90.25,0.5)

domain_lon_min = 73.75
domain_lon_max = 134.75
domain_lat_min = 18.75
domain_lat_max = 53.25

def sel_domain(dataarray,lon_min,lon_max,lat_min,lat_max):
    mask_lon = (dataarray.lon >= lon_min) & (dataarray.lon <= lon_max)
    mask_lat = (dataarray.lat >= lat_min) & (dataarray.lat <= lat_max)
    dataarray = dataarray.where(mask_lon & mask_lat, drop=True)
    return dataarray

to_dir = '/home/xtan/scratch/hzq/anomalous_PREC/proc_data/'
mask = xr.open_dataarray(to_dir + 'China_mainland_mask_05x05.nc')


for model in models:
    if model != 'GFDL-CM4_gr2':
        file_names = []
        for i in range(1961,2100):
            if i in range(1961,2015):
                forcing = 'historical'
            else:
                forcing = 'ssp585'
            if os.path.exists(to_dir + forcing+'_pr_'+model+'_'+str(i)+'_masked.nc'):
                continue
            else:
                ds_file = glob.glob(forcing+'/pr/*_'+model+'_*'+str(i)+'.nc')[0]
                file_names.append(ds_file)
                da = xr.open_dataarray(ds_file)
                da = da.interp(lat=lat_regrid,lon=lon_regrid,method='nearest')
                print(i)
                da = sel_domain(da,lon_min=domain_lon_min,lon_max=domain_lon_max,lat_min=domain_lat_min,lat_max=domain_lat_max)
                da = da * mask
                da = da.to_dataset(name='precipitation')
                da = da * 86400
                da.to_netcdf(to_dir + forcing+'_pr_'+model+'_'+str(i)+'_masked.nc')
        ds1 = xr.open_mfdataset(to_dir+'{}_pr_{}_*_masked.nc'.format('historical',model), combine='nested', concat_dim='time', parallel=True)
        ds2 = xr.open_mfdataset(to_dir+'{}_pr_{}_*_masked.nc'.format('ssp585',model), combine='nested', concat_dim='time', parallel=True)
        ds = xr.concat([ds1,ds2],dim='time')
        ds = ds['precipitation']
        prec_1981_2000 = ds.sel(time = slice('1981','2000'))
        prec_clim = prec_1981_2000.groupby('time.dayofyear').mean()
        prec_ano = ds.groupby('time.dayofyear') - prec_clim
        prec_array = prec_ano.values
        # calculate 5-day running-average anomalies to remove the effect of short-term synoptic weather
        prec_array = (prec_array[:-4,:,:] + prec_array[1:-3,:,:] + prec_array[2:-2,:,:] + prec_array[3:-1,:,:] + prec_array[4:,:,:]) / 5
        prec_ano[2:-2,:,:] = prec_array
        prec_ano = prec_ano.sel(time = np.in1d(prec_ano['time.month'], [5,6,7,8,9,10]))
        prec_ano.to_netcdf(to_dir + forcing + '_pr_' + model + '_1961_2099_summer_anomalies.nc')
        prec_clim.to_netcdf(to_dir + forcing + '_pr_' + model + '_1981_2000_summer_climatologies.nc')
    
    else: #model = 'GFDL-CM4_gr2'

        file_names = []
        for i in range(1961,2100):
            if i in range(1961,2015):
                forcing = 'historical'
            else:
                forcing = 'ssp585'
            if os.path.exists(to_dir + forcing+'_pr_'+model+'_'+str(i)+'_masked.nc'):
                continue
            else:
                ds_file = glob.glob(forcing+'/pr/*_'+'GFDL-CM4'+'_*' + '_gr2_' +str(i)+'.nc')[0]
                file_names.append(ds_file)
                da = xr.open_dataarray(ds_file)
                da = da.interp(lat=lat_regrid,lon=lon_regrid,method='nearest')
                print(i)
                da = sel_domain(da,lon_min=domain_lon_min,lon_max=domain_lon_max,lat_min=domain_lat_min,lat_max=domain_lat_max)
                da = da * mask
                da = da.to_dataset(name='precipitation')
                da = da * 86400
                da.to_netcdf(to_dir + forcing+'_pr_'+model+'_'+str(i)+'_masked.nc')
        ds1 = xr.open_mfdataset(to_dir+'{}_pr_{}_*_masked.nc'.format('historical',model), combine='nested', concat_dim='time', parallel=True)
        ds2 = xr.open_mfdataset(to_dir+'{}_pr_{}_*_masked.nc'.format('ssp585',model), combine='nested', concat_dim='time', parallel=True)
        ds = xr.concat([ds1,ds2],dim='time')
        ds = ds['precipitation']
        prec_1981_2000 = ds.sel(time = slice('1981','2000'))
        prec_clim = prec_1981_2000.groupby('time.dayofyear').mean()
        prec_ano = ds.groupby('time.dayofyear') - prec_clim
        prec_array = prec_ano.values
        # calculate 5-day running-average anomalies to remove the effect of short-term synoptic weather
        prec_array = (prec_array[:-4,:,:] + prec_array[1:-3,:,:] + prec_array[2:-2,:,:] + prec_array[3:-1,:,:] + prec_array[4:,:,:]) / 5
        prec_ano[2:-2,:,:] = prec_array
        prec_ano = prec_ano.sel(time = np.in1d(prec_ano['time.month'], [5,6,7,8,9,10]))
        prec_ano.to_netcdf(to_dir + forcing + '_pr_' + model + '_1961_2099_summer_anomalies.nc')
        prec_clim.to_netcdf(to_dir + forcing + '_pr_' + model + '_1981_2000_summer_climatologies.nc')

