"""
OSM Tile Downloader -> MBTiles builder
Usage: python3 download_tiles.py
Edit BBOX and ZOOM_RANGE below for your region.
"""
import sqlite3
import urllib.request
import time
import math
import os

# ---- CONFIG: set your bounding box (south, west, north, east) ----
BBOX = (27.6500, 85.2500, 27.7500, 85.4000)  # Kathmandu valley example
ZOOM_RANGE = range(12, 17)  # min_zoom .. max_zoom-1 (17 exclusive -> up to 16)
OUTPUT = "new_map.mbtiles"
USER_AGENT = "livestock_tracker_downloader/1.0 (contact: your_email@example.com)"
TILE_URL = "https://tile.openstreetmap.org/{z}/{x}/{y}.png"
DELAY = 0.3  # seconds between requests -- respect OSM usage policy

def deg2num(lat, lon, zoom):
    lat_rad = math.radians(lat)
    n = 2.0 ** zoom
    x = int((lon + 180.0) / 360.0 * n)
    y = int((1.0 - math.log(math.tan(lat_rad) + 1/math.cos(lat_rad)) / math.pi) / 2.0 * n)
    return x, y

def init_mbtiles(path):
    if os.path.exists(path):
        os.remove(path)
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute("CREATE TABLE metadata (name TEXT, value TEXT)")
    c.execute("CREATE TABLE tiles (zoom_level INTEGER, tile_column INTEGER, tile_row INTEGER, tile_data BLOB)")
    c.execute("CREATE UNIQUE INDEX tile_index ON tiles (zoom_level, tile_column, tile_row)")
    meta = {
        "name": "new_map",
        "type": "baselayer",
        "version": "1.0",
        "description": "Offline tiles for livestock tracker",
        "format": "png",
        "bounds": f"{BBOX[1]},{BBOX[0]},{BBOX[3]},{BBOX[2]}",
        "minzoom": str(min(ZOOM_RANGE)),
        "maxzoom": str(max(ZOOM_RANGE)),
    }
    c.executemany("INSERT INTO metadata VALUES (?, ?)", meta.items())
    conn.commit()
    return conn

def main():
    south, west, north, east = BBOX
    conn = init_mbtiles(OUTPUT)
    c = conn.cursor()
    total = 0

    for z in ZOOM_RANGE:
        x_min, y_max = deg2num(south, west, z)
        x_max, y_min = deg2num(north, east, z)
        x_min, x_max = sorted((x_min, x_max))
        y_min, y_max = sorted((y_min, y_max))

        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                url = TILE_URL.format(z=z, x=x, y=y)
                req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
                try:
                    with urllib.request.urlopen(req, timeout=10) as resp:
                        data = resp.read()
                    # MBTiles spec uses TMS scheme: flip Y
                    tms_y = (2 ** z - 1) - y
                    c.execute(
                        "INSERT OR REPLACE INTO tiles VALUES (?, ?, ?, ?)",
                        (z, x, tms_y, data),
                    )
                    total += 1
                    print(f"z={z} x={x} y={y} ok  ({total} tiles)")
                except Exception as e:
                    print(f"z={z} x={x} y={y} FAILED: {e}")
                time.sleep(DELAY)

        conn.commit()

    conn.close()
    print(f"Done. {total} tiles written to {OUTPUT}")

if __name__ == "__main__":
    main()