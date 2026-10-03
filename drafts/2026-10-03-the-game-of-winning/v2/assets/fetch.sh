#!/bin/sh
# Public-domain NASA maps used by the v2 engine. Re-run to fetch them again; the JPGs are not kept in Git.
set -e
cd "$(dirname "$0")"
curl -fL -o src-blackmarble-2016-3km.jpg "https://assets.science.nasa.gov/content/dam/science/esd/eo/images/imagerecords/144000/144898/BlackMarble_2016_3km.jpg"   # NASA Earth Observatory, Black Marble 2016, 13500x6750
curl -fL -o src-bluemarble-200412.jpg "https://assets.science.nasa.gov/content/dam/science/esd/eo/images/bmng/bmng-topography-bathymetry/december/world.topo.bathy.200412.3x5400x2700.jpg"   # Blue Marble Next Generation, Dec 2004, 5400x2700
curl -fL -o src-mercury-PIA17386.jpg "https://assets.science.nasa.gov/content/dam/science/psd/photojournal/pia/pia17/pia17386/PIA17386.jpg"   # MESSENGER enhanced-colour global map, 4096x2048
curl -fL -o src-moon-lroc-2k.tif "https://svs.gsfc.nasa.gov/vis/a000000/a004700/a004720/lroc_color_poles_2k.tif"   # NASA SVS CGI Moon Kit (LRO), 2048x1024
# Engine-sized copies
sips -s format jpeg -s formatOptions 92 -z 4096 8192 src-blackmarble-2016-3km.jpg --out earth-night.jpg >/dev/null
sips -s format jpeg -s formatOptions 92 -z 4096 8192 src-bluemarble-200412.jpg --out earth-day.jpg >/dev/null
sips -s format jpeg -s formatOptions 92 src-mercury-PIA17386.jpg --out mercury.jpg >/dev/null
sips -s format jpeg -s formatOptions 92 src-moon-lroc-2k.tif --out moon.jpg >/dev/null
curl -fL -o src-clouds-8192.tif "https://eoimages.gsfc.nasa.gov/images/imagerecords/57000/57747/cloud_combined_8192.tif"   # Blue Marble cloud layer, 8192x4096
sips -s format jpeg -s formatOptions 90 -z 2048 4096 src-clouds-8192.tif --out clouds.jpg >/dev/null
