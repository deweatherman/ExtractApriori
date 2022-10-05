
import sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import cartopy
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import pyproj
import pyresample
from pyresample import create_area_def, load_area, data_reduce, utils, AreaDefinition
from pyresample.geometry import SwathDefinition, GridDefinition



def defineArea(corners, proj_id, datum):
    #corners=parseMeta(data_name)

    lat_0 = '{lat_0:5.2f}'.format_map(corners)
    lon_0= '{lon_0:5.2f}'.format_map(corners)
    lon_bbox = [corners['min_lon'],corners['max_lon']]
    lat_bbox = [corners['min_lat'],corners['max_lat']]
    area_dict = dict(datum=datum,lat_0=lat_0,lon_0=lon_0,
                proj=proj_id,units='m')

    #area_dict = dict(datum=datum,lat_0=-15,lon_0=60,
    #            proj=proj_id,units='m',a=6370997.0,)

    prj=pyproj.Proj(area_dict)
    x, y = prj(lon_bbox, lat_bbox)
    xsize=200
    ysize=200
    area_id = 'granule'
    area_name = 'modis swath 5min granule'
    area_extent = (x[0], y[0], x[1], y[1])
    print(area_extent)
    area_def = AreaDefinition(area_id, area_name, proj_id, 
                                   area_dict, xsize, ysize,area_extent)
    return area_def
    
    
def get_Sat_frame(ds, area_interest, chan = 0, var=None, begin_t=None, end_t=None):
    
    grid_lons_interest, grid_lats_interest = area_interest.get_lonlats()

    swathDef = SwathDefinition(lons=ds.lon.values, lats=ds.lat.values)
    lon_scene, lat_scene = swathDef.get_lonlats()

    if(chan>=0):
        
        reduced_lon_scene, reduced_lat_scene, reduced_data_scene = \
                           data_reduce.swath_from_lonlat_grid(
            grid_lons_interest, grid_lats_interest,
            lon_scene, lat_scene, ds[var][:,:,chan].values,
            radius_of_influence=3000)
    else:
        reduced_lon_scene, reduced_lat_scene, reduced_data_scene = \
                           data_reduce.swath_from_lonlat_grid(
            grid_lons_interest, grid_lats_interest,
            lon_scene, lat_scene, ds[var][:,:].values,
            radius_of_influence=3000)

    return reduced_lon_scene, reduced_lat_scene, reduced_data_scene
    
    
    
def basicMapPlotScat1(x,y,data,namefile, area, 
                      vmin=0, vmax=300, proj=None, var=None):
    # Make a Mercator map of the data using Cartopy
    
    fig = plt.figure()
    
    
    if(proj):
        if(proj=="Orthographic"):
            ortho = ccrs.Orthographic(60,-15)
            sizeOfMarker = 0.15
        elif(proj=="PlateCarree"):
            ortho = ccrs.PlateCarree()
            sizeOfMarker = 0.05
        else:
            print("Projection not recognized, plotting PlateCarre as default.")
            ortho = ccrs.PlateCarree()
            sizeOfMarker = 0.05
        # Other projections can be added (check Cartopy)
    else: 
        print("No projection selected; plotting PlateCarre as default.")
        ortho = ccrs.PlateCarree() #
        sizeOfMarker = 0.05
    
    ax = plt.axes(projection=ortho)
    
    geo = ccrs.Geodetic()
    
    ax.add_feature(cartopy.feature.LAND, zorder=0, edgecolor='black')
    
    xy = ortho.transform_points(geo, x, y)

    ax.set_global()
    ax.gridlines()    

    ax.coastlines() 
    
    # Plot the air temperature as colored circles and the wind speed as vectors.
    im = ax.scatter(
        xy[:,0],
        xy[:,1],
        c=data,
        s=sizeOfMarker,
        cmap="viridis",
        edgecolors= 'none',
        marker = matplotlib.markers.MarkerStyle(marker='o',fillstyle='full'),#"o",
        #transform=crs,
        vmin=vmin, vmax=vmax         #180, 270       
    )

    if(vmax>50):  # if the provided vmax is higher than 50, probably the user wants to plot TB's
        if(var):
            ax.set_title(var+" "+"Temperature Brightness")
            fig.colorbar(im).set_label("Temp. Bright [K]")
        else:
            ax.set_title("Temperature Brightness")
            fig.colorbar(im).set_label("Temp. Bright [K]")
    else:          
        
        if(var):
            ax.set_title(var+" "+"10m Wind speed")
            fig.colorbar(im).set_label("Wind Speed [m/s]")  
        else:
            ax.set_title("NameOfVariable"+" "+"10m Wind speed")
            fig.colorbar(im).set_label("Wind Speed [m/s]") 
# Use an utility function to add tick labels and land and ocean features to the map.

    plt.tight_layout()
    #plt.show()
    plt.savefig(namefile+'.png', bbox_inches='tight', dpi=300)      
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
