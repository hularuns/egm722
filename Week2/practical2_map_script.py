
import os
import geopandas as gpd
import matplotlib.pyplot as plt
from cartopy.feature import ShapelyFeature
import cartopy.crs as ccrs
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import time
start = time.time()

plt.ion() # make the plotting interactive

# generate matplotlib handles to create a legend of each of the features we put in our map.
def generate_handles(labels, colors, edge='k', alpha=1):
    lc = len(colors)  # get the length of the color list
    handles = [] # create an empty list
    for ii in range(len(labels)): # for each label and color pair that we're given, make an empty box to pass to our legend
        handles.append(mpatches.Rectangle((0, 0), 1, 1, facecolor=colors[ii % lc], edgecolor=edge, alpha=alpha))
    return handles

# create a scale bar of length 20 km in the upper right corner of the map
# adapted this question: https://stackoverflow.com/q/32333870
# answered by SO user Siyh: https://stackoverflow.com/a/35705477
def scale_bar(ax, location=(0.92, 0.95)):
    x0, x1, y0, y1 = ax.get_extent() # get the current extent of the axis
    sbx = x0 + (x1 - x0) * location[0] # get the lower left x coordinate of the scale bar
    sby = y0 + (y1 - y0) * location[1] # get the lower left y coordinate of the scale bar

    ax.plot([sbx, sbx - 20000], [sby, sby], color='k', linewidth=9, transform=ax.projection) # plot a thick black line, 20 km long
    ax.plot([sbx, sbx - 10000], [sby, sby], color='k', linewidth=6, transform=ax.projection) # plot a smaller black line from 0 to 10 km long
    ax.plot([sbx-10000, sbx - 20000], [sby, sby], color='w', linewidth=6, transform=ax.projection) # plot a white line from 10 to 20 km

    ax.text(sbx, sby-5000, '20 km', transform=ax.projection, fontsize=8) # add a label at 20 km
    ax.text(sbx-12500, sby-5000, '10 km', transform=ax.projection, fontsize=8) # add a label at 10 km
    ax.text(sbx-24500, sby-5000, '0 km', transform=ax.projection, fontsize=8) # add a label at 0 km

    return ax

outline = gpd.read_file('Week2/data_files/NI_outline.shp')
towns = gpd.read_file('Week2/data_files/Towns.shp')
water = gpd.read_file('Week2/data_files/Water.shp')
rivers = gpd.read_file('Week2/data_files/Rivers.shp')
counties = gpd.read_file(os.path.abspath('Week2/data_files/Counties.shp'))


ni_utm = ccrs.UTM(29)  # create a Universal Transverse Mercator reference system to transform our data.
# be sure to fill in XX above with the correct number for the UTM Zone that Northern Ireland is part of.

ccrs.CRS(outline.crs) # create a cartopy CRS representation of the CRS associated with the outline dataset

myFig = plt.figure(figsize=(8, 8))  # create a figure of size 8x8 (representing the page size in inches)
ax = plt.axes(projection=ni_utm)  # create an axes object in the figure, using a UTM projection,
# where we can actually plot our data.

# first, we just add the outline of Northern Ireland using cartopy's ShapelyFeature
outline_feature = ShapelyFeature(outline['geometry'], ni_utm, edgecolor='k', facecolor='w')
ax.add_feature(outline_feature) # add the features we've created to the map.

xmin, ymin, xmax, ymax = outline.total_bounds # using the boundary of the shapefile features, zoom the map to our area of interest
# because total_bounds gives output as xmin, ymin, xmax, ymax,
ax.set_extent([xmin-5000, xmax+5000, ymin-5000, ymax+5000], crs = ni_utm)
# but set_extent takes xmin, xmax, ymin, ymax, we re-order the coordinates here.

# get the number of unique municipalities we have in the dataset
num_counties = len(counties.CountyName.unique())
print(f'Number of unique features: {num_counties}') # note how we're using an f-string with {} here!


# pick colors for the individual county boundaries - make sure to add enough for each of the counties
# to add a color, enclose the name above (e.g., violet) with single (or double) quotes: 'violet'
# remember that each colors should be separated by a comma
county_colors = {
                 'ANTRIM': 'orchid',
                 'ARMAGH': 'orange',
                 'DOWN': 'forestgreen',
                 'FERMANAGH': 'peru',
                 'LONDONDERRY': 'darkturquoise',
                 'TYRONE': 'rebeccapurple'}

# get a list of unique names for the county boundaries
county_names = list(counties.CountyName.unique())
county_names.sort() # sort the counties alphabetically by name

# next, add the municipal outlines to the map using the colors that we've picked.
# here, we're iterating over the unique values in the 'CountyName' field.
# we're also setting the edge color to be black, with a line width of 0.5 pt. 
# Feel free to experiment with different colors and line widths.
for index, name in enumerate(county_names):
    feat = ShapelyFeature(counties.loc[counties['CountyName'] == name, 'geometry'], # first argument is the geometry
                          ccrs.CRS(counties.crs), # second argument is the CRS
                          edgecolor='k', # outline the feature in black
                          facecolor=county_colors[name], # set the face color to the corresponding color from the list
                          linewidth=1, # set the outline width to be 3 pt
                          alpha=0.25) # set the alpha (transparency) to be 0.15 (out of 1)
    ax.add_feature(feat) # once we have created the feature, we have to add it to the map using ax.add_feature()
    
# here, we're setting the edge color to be the same as the face color. Feel free to change this around,
# and experiment with different line widths.
water_feat = ShapelyFeature(water['geometry'], # first argument is the geometry
                            ccrs.CRS(water.crs), # second argument is the CRS
                            edgecolor='mediumblue', # set the edgecolor to be mediumblue
                            facecolor='mediumblue', # set the facecolor to be mediumblue
                            linewidth=1) # set the outline width to be 1 pt
ax.add_feature(water_feat) # add the collection of features to the map

river_feat = ShapelyFeature(rivers['geometry'], # first argument is the geometry
                            ccrs.CRS(rivers.crs), # second argument is the CRS
                            edgecolor='royalblue', # set the edgecolor to be royalblue
                            linewidth=0.2) # set the linewidth to be 0.2 pt
ax.add_feature(river_feat) # add the collection of features to the map

# ShapelyFeature creates a polygon, so for point data we can just use ax.plot()
town_handle = ax.plot(
    towns.geometry.x,
    towns.geometry.y,
    "s",
    color="0.5",
    ms=6,
    transform=ccrs.PlateCarree(),
)  # towns is in UTM Zone 29N, so we can use ni_utm


# generate a list of handles for the county datasets
# first, we add the list of names, then the list of colors, and finally we set the transparency
# (since we set it in the map)

# Preparing our colored boxes (handles) for the legend

# creates a list, as county_colors is a dictionary. List is in same order as dictionary
county_colors_list = [county_colors.get(key) for key in county_names]


county_handles = generate_handles(county_names, county_colors_list, alpha=0.25)

# note: if you change the color you use to display lakes, you'll want to change it here, too
water_handle = generate_handles(["Lakes"], ["mediumblue"])

# river handle
river_handle = [mlines.Line2D([], [], color="royalblue", label="River")]

# update county_names to take it out of uppercase text
nice_names = [name.title() for name in county_names]

# ax.legend() takes a list of handles and a list of labels corresponding to the objects 
# you want to add to the legend
handles = county_handles + water_handle + river_handle + town_handle # use '+' to concatenate (combine) lists
labels = nice_names + ['Lakes', 'Rivers', 'Towns']

leg = ax.legend(handles, labels, title='Legend', title_fontsize=12, 
                 fontsize=10, loc='upper left', frameon=True, framealpha=1)

gridlines = ax.gridlines(draw_labels=True, # draw  labels for the grid lines
                         xlocs=[-8, -7.5, -7, -6.5, -6, -5.5], # add longitude lines at 0.5 deg intervals
                         ylocs=[54, 54.5, 55, 55.5]) # add latitude lines at 0.5 deg intervals
gridlines.left_labels = False # turn off the left-side labels
gridlines.bottom_labels = False # turn off the bottom labels

for ind, row in towns.iterrows(): # towns.iterrows() returns the index and row
    x, y = row.geometry.x, row.geometry.y # get the x,y location for each town
    ax.text(x, y, row['TOWN_NAME'].title(), fontsize=7, transform=ccrs.PlateCarree()) # use plt.text to place a label at x,y
    
scale_bar(ax) # place a scale bar in the upper right corner of the map window

myFig.savefig('Week2/map_script.png', bbox_inches='tight', dpi=300)

end = time.time()
print(end-start)