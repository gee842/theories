# Analysis code for molecular communication in ATPS droplet colonies
Custom Python code used for image processing, data preparation, and visualization for the manuscript “Molecular communication enables cooperative genomic RNA replication in all-aqueous droplet colonies.”

The code was tested with Python 3.10.16 on Windows 11.

## Files

#### `droplet_segmentation_and_quantification.ipynb`

Segments droplets in OIR microscopy images using Cellpose and quantifies their fluorescence intensities. The notebook outputs CSV files, segmentation masks, and PNG images.

#### `adjacency_background_correction_and_data_preparation.ipynb`

Performs droplet-adjacency analysis, fluorescence background correction, and data preparation. The notebook generates:

- `prepared_data_dex.pkl`
- `prepared_data_fam_rna.pkl`
- `prepared_data_comm.pkl`

#### `atps_droplet_communication_analysis.ipynb`

Performs normalization, statistical analysis, and plotting for:

- FITC-DEX exchange
- FAM-RNA exchange
- TcRR and TcCRR via inter-droplet molecular diffusion

#### `cellpose3.yml`

Conda environment used for:

- `droplet_segmentation_and_quantification.ipynb`
- `adjacency_background_correction_and_data_preparation.ipynb`

The same environment can also run `atps_droplet_communication_analysis.ipynb` as provided.

## Data

A reduced test dataset is provided for the image-processing and data-preparation workflows.

The following processed pickle files generated from the full dataset are provided for the final statistical analyses and plotting:

- `260710 prepared_data_dex.pkl`
- `260710 prepared_data_fam_rna.pkl`
- `260710 prepared_data_comm.pkl`

The reduced test dataset is not intended to reproduce the complete statistical analyses or manuscript plots.

## Repository structure

```text
.
├── README.md
├── cellpose3.yml
├── droplet_segmentation_and_quantification.ipynb
├── adjacency_background_correction_and_data_preparation.ipynb
├── atps_droplet_communication_analysis.ipynb
├── Test data/
│   └── Microscope images for analysis/
│       └── <imaging date>/
│           └── *.oir
└── Processed data/
    ├── 260710 prepared_data_dex.pkl
    ├── 260710 prepared_data_fam_rna.pkl
    └── 260710 prepared_data_comm.pkl
```

## Workflow

Run the notebooks in the following order:

1. `droplet_segmentation_and_quantification.ipynb`
2. `adjacency_background_correction_and_data_preparation.ipynb`
3. `atps_droplet_communication_analysis.ipynb`

For the reduced test dataset, set:

```python
main_dir = os.path.join(os.path.curdir, "Test data")
```

For the final analysis, set the input directory in `atps_droplet_communication_analysis.ipynb` to the directory containing the three processed full-dataset pickle files.
