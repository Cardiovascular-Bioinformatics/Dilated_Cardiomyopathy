"""Export final Xenium cell annotations as cell_id,label CSV files.

Run this script after executing the annotation notebooks and placing the final
DCM and IHD .h5ad files in the current directory. The CSVs are generated from
the exact saved annotation objects; no labels are inferred by this script.
"""
from pathlib import Path
import scanpy as sc
import pandas as pd

CONFIG = {
    "DCM": (Path("DCM_final.h5ad"), "celltype_corrected", Path("final_cell_labels_DCM.csv")),
    "IHD": (Path("adata_celltype_final_corrected_v4.h5ad"), "celltype_final_corrected_v4", Path("final_cell_labels_IHD.csv")),
}

for dataset, (path, label_col, output) in CONFIG.items():
    if not path.exists():
        raise FileNotFoundError(f"{dataset}: required final annotation file not found: {path.resolve()}")
    adata = sc.read_h5ad(path, backed="r")
    if label_col not in adata.obs.columns:
        raise KeyError(f"{dataset}: expected final label column {label_col!r} is missing from {path}")
    raw_labels = adata.obs[label_col]
    if raw_labels.isna().any():
        n_missing = int(raw_labels.isna().sum())
        raise ValueError(
            f"{dataset}: {n_missing} missing values in {label_col!r}; "
            "refusing to export incomplete labels"
        )
    labels = pd.DataFrame({"cell_id": adata.obs_names.astype(str), "label": raw_labels.astype(str).to_numpy()})
    if labels["label"].str.strip().eq("").any():
        raise ValueError(f"{dataset}: empty labels found in {label_col!r}; refusing to export")
    if labels["cell_id"].duplicated().any():
        raise ValueError(f"{dataset}: cell IDs are not unique; refusing to export ambiguous labels")
    labels.to_csv(output, index=False)
    print(f"Wrote {len(labels):,} {dataset} cell labels to {output.resolve()}")
    adata.file.close()
