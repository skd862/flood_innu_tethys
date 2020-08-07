"""
convert simple, single band geotiff files to a netcdf file compatible with thredds data server
author: riley hales, 2020
"""

import netCDF4 as nc
import xarray as xr


path = '/Users/rileyhales/Downloads/reprojected20110102.tif'
a = xr.open_rasterio(path, 'r')

# a tuple showing the dimensions of the geotiff data (# of bands, # of latitude steps, # of longitude steps)
shape = a.values.shape

# for help with the following code, consult: https://unidata.github.io/netcdf4-python/netCDF4/index.html

# create a new netcdf file
new_nc = nc.Dataset('/Users/rileyhales/Downloads/created_nc_20110102.nc', 'w')

# create dimensions, create variable, add values
new_nc.createDimension('latitude', shape[1])
new_nc.createVariable('latitude', 'f', ('latitude', ))
new_nc['latitude'][:] = a.y.values
# create dimensions, create variable, add values
new_nc.createDimension('longitude', shape[2])
new_nc.createVariable('longitude', 'f', ('longitude', ))
new_nc['longitude'][:] = a.x.values
# create dimensions, create variable, add values AND specify the units string (essential for thredds)
new_nc.createDimension('time', 1)
new_nc.createVariable('time', 'i2')
new_nc['time'][:] = 0
new_nc.variables['time'].units = 'months since 2011-01-02 00:00:00'
# now create the variable which shows the flood extents image (use a.values[0] because first dim is the band #)
new_nc.createVariable('extents', 'f', ('latitude', 'longitude'))
new_nc['extents'][:] = a.values[0]

# save and close the new_nc
new_nc.sync()
new_nc.close()