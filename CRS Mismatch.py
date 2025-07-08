❌ # Incorrect Code (will likely fail or give wrong results):
import geopandas as gpd

Load two layers with different CRS
cities = gpd.read_file("cities.shp")            # EPSG:4326
roads = gpd.read_file("roads.shp")              # EPSG:32633

# Attempt spatial join without CRS alignment
joined = gpd.sjoin(cities, roads, how="inner", predicate='intersects')  # Error or wrong result


✅ # Correct Code:
import geopandas as gpd

# Load the layers
cities = gpd.read_file("cities.shp")     # EPSG:4326
roads = gpd.read_file("roads.shp")       # EPSG:32633

# Reproject roads to match cities
roads = roads.to_crs(cities.crs)

# Perform spatial join correctly
joined = gpd.sjoin(cities, roads, how="inner", predicate='intersects')

# Output the result
joined.to_file("cities_with_roads.shp")


🧠 # Tip:
# Always check and align CRS using:
print(cities.crs)
print(roads.crs)
