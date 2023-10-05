# Mindex Coding Challenge

### A few notes
* I don't usually develop in Jupyter notebooks - if there's something I'm doing strangely, or best practices I'm missing, please let me know!
* A lot of the key functionality is in `etl_functions.py`, rather than hardcoded directly into the notebook.
* AWS connection info was saved to a local file (~/.aws/credentials) and is NOT stored directly in this project anywhere. If you encounter an issue with the `download_raw_files()` function, please be sure AWS access is configured.
