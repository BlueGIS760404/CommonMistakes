import rasterio

# Common Mistake: Incorrectly handling raster band indexing
def mistake_band_indexing():
    with rasterio.open('...\L8_B1.tif') as src:
        # Incorrect: Assuming band indexing starts at 0
        try:
            band_wrong = src.read(0)  # Wrong: rasterio band indexing starts at 1
        except ValueError as e:
            print("Error in band indexing:", e)
        
        # Fix: Use correct 1-based band indexing
        band_correct = src.read(1)  # Read first band correctly
        print("Successfully read band 1 with shape:", band_correct.shape)

# Example execution
if __name__ == "__main__":
    mistake_band_indexing()
