"""Record package versions from the environment used to run the notebooks.

Run with the same activated environment as the analysis: python capture_environment.py
This creates environment_versions.txt. It does not claim to recover the original
environment if run in a different environment.
"""
from importlib.metadata import PackageNotFoundError, version
import platform
from pathlib import Path

packages = ["scanpy", "anndata", "pybanksy", "banksy", "igraph", "leidenalg", "pandas", "numpy", "scipy", "statsmodels", "openpyxl", "matplotlib"]
lines = [f"Python: {platform.python_version()}", f"Platform: {platform.platform()}"]
for package in packages:
    try:
        lines.append(f"{package}: {version(package)}")
    except PackageNotFoundError:
        lines.append(f"{package}: NOT INSTALLED / distribution name may differ")
Path("environment_versions.txt").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
print("\nSaved environment_versions.txt")
