import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from datasets.load_dataset import load_ionosphere, load_adult, load_wine_quality, load_breast_cancer_diagnosis, \
    load_dataset
from utils.datasets_enum import Datasets


def heatmap_plotting(print_correlation_matrix=True, plot_heatmap_values=True, show_plotting=True, save_plotting=True,
                     plotting_path='heatmap.png', load_dataset_with_extra_pre_processing=True):
    # Dataset list
    datasets = [Datasets.IONOSPHERE, Datasets.ADULT, Datasets.WINE_QUALITY, Datasets.BREAST_CANCER_DIAGNOSIS]

    for dataset_name in datasets:
        if dataset_name == Datasets.IONOSPHERE:
            path = os.path.join(os.getcwd(), 'datasets/data/ionosphere/ionosphere.data')
            if load_dataset_with_extra_pre_processing:
                X_np, y_np = load_ionosphere()
            else: # load all dataset columns
                X_np, y_np = load_dataset(path, header=None)
            X = pd.DataFrame(data=X_np)

        if dataset_name == Datasets.ADULT:
            if load_dataset_with_extra_pre_processing:
                X_np, y_np = load_adult(run_one_hot_encoder=False)
            else:
                X_np, y_np = load_adult(run_one_hot_encoder=True)

            X = pd.DataFrame(data=X_np.astype(float))

        if dataset_name == Datasets.WINE_QUALITY:
            X_np, y_np = load_wine_quality()

            X = pd.DataFrame(data=X_np)

        if dataset_name == Datasets.BREAST_CANCER_DIAGNOSIS:
            path = os.path.join(os.getcwd(), 'datasets/data/breast-cancer-wisconsin/breast-cancer-wisconsin.data')

            if load_dataset_with_extra_pre_processing:
                X_np, y_np = load_breast_cancer_diagnosis()
            else: # load all dataset columns
                X_np, y_np = load_dataset(path, header=None, remove_question_mark=True)
            X = pd.DataFrame(data=X_np.astype(float))

        sns.set(style="white")

        # Compute the correlation matrix
        corr = X.corr()
        if print_correlation_matrix:
            print('\nCorrelation matrix:\n', corr)

        # Generate a custom diverging colormap
        cmap = sns.diverging_palette(220, 10, as_cmap=True)

        heatmap_plot = sns.heatmap(corr, xticklabels=True, yticklabels=True, annot=plot_heatmap_values, cmap=cmap,
                                   vmax=.3, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})
        ax = plt.axes()
        file_name = dataset_name.name
        if plot_heatmap_values:
            file_name = file_name + ' with values, '
        else:
            file_name = file_name + ' without values, '
        if load_dataset_with_extra_pre_processing:
            file_name = file_name + ' with extra pre-processing'
        else:
            file_name = file_name + ' without extra pre-processing'

        ax.set_title(dataset_name.name)

        if show_plotting:
            plt.show()
        if save_plotting:
            fig = heatmap_plot.get_figure()
            fig.savefig(os.path.join(plotting_path, file_name))
