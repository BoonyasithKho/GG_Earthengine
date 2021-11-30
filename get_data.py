import ee, json
print("Earth Engine version : " + ee.__version__)

# Initialize the Earth Engine module.
ee.Initialize()

# Print metadata for a DEM dataset.
x = ee.Image('USGS/SRTMGL1_003').getInfo()

a = json.dumps(x, indent=4)
print(a)