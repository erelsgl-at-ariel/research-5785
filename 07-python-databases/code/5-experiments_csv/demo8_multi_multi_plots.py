"""
Demo 8: plotting experiment results; multiple figures.
"""

from experiments_csv import *
from matplotlib import pyplot as plt

multi_multi_plot_results("results/demo5.csv", save_to_file_template="results/demo5_{}.png", 
    x_field="x", y_fields=["sum","runtime"], z_field="y", mean=True,
    filter={}, subplot_field="z", subplot_rows=2, subplot_cols=2,
    )
    # Should show two-by-two subplots.
