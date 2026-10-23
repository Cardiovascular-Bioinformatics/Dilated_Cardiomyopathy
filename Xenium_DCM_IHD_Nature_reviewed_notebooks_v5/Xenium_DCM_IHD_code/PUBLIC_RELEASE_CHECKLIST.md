# Public-release checklist

- [ ] Run notebooks 01–04 end-to-end with the original study inputs.
- [ ] Confirm final annotation columns and `value_counts()` against the original outputs.
- [ ] Confirm that all reported spatial medians, p-values, FDR values and figure panels come from the exact released code.
- [ ] Confirm whether the manuscript/supplement uses the additional paired Wilcoxon, permutation, spatial-regression or alternative-anchor analyses present in the original spatial notebooks; include only the analyses actually reported.
- [ ] Recover exact package versions from the original working environment and pin them. `requirements.txt` and `environment.yml` currently list packages without version pins and are not lockfiles.
- [ ] Add the Matrisome workbook or a stable, permitted source/access instruction.
- [ ] Provide stable access instructions for the four `Clean_*` input CSVs and the final `.h5ad` objects; do not commit controlled-access data to public GitHub.
- [ ] Confirm permission to redistribute the original summary PDFs and the chosen software license with the code owners/institution.
- [ ] Add the final GitHub repository URL and archived release DOI to the Code availability statement.

- [ ] Confirm the exact study data accession/DOI and document access to all four `Clean_*.csv` files and the matrisome workbook.
- [ ] Run `python capture_environment.py` in the validated analysis environment; pin the recorded versions (including Python, Scanpy, AnnData, BANKSY, igraph/leidenalg, pandas, NumPy, SciPy and statsmodels).
- [ ] Run `python export_final_labels.py` after generating the final DCM/IHD `.h5ad` files; archive the two cell-label CSVs where data policy permits.
- [ ] Confirm whether permutation tests, paired Wilcoxon tests and spatial regression from `IHD_Spatial_plot.html` are reported in the paper/supplement; restore them if they are.
- [ ] Obtain author/institution approval and add a `LICENSE` file.
- [ ] Create a versioned GitHub release and Zenodo DOI.
