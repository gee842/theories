# Description ####
This folder contains the scripts and data files necessary to replicate the analyses and figures in the paper, 
“No evidence for curiosity-driven information selection advantage for infants’ novel word learning.”. 

# Data ####
- Zip file "Data.zip": Contains eye-tracking data and information about participants necessary to run the analysis R script
- Please unpack the Zip file before running the R script.

- The 8 other .csv files are generated as part of the analysis R script. They can be imported at certain checkpoints
in the R script, to save on computation time.

# Scripts ####
- "curigaze_OSF.R" contains the whole data tidying and analysis pipeline. It can be run from start to finish without alterations
(aside from installing required R packages) provided that the Data.zip file has been unzipped in the same folder as the R script.