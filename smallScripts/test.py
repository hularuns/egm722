#test enviro
import pywin.dialogs.list
driverOptions = ['GeoJSON', 'GPKG', 'ESRI Shapefile', 'GML']
conversionDriverList=pywin.dialogs.list.SelectFromList('Select Driver', driverOptions )


print(driverOptions[conversionDriverList])