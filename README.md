# Team Recovery

Francis Ng `<chiwang@umich.edu>`<br>
Nicholas Dunbar `<nkdunbar@umich.edu>`<br>
Ricky Wong `<rckywong@umich.edu>`<br>
Steven Wang `<stevenzw@umich.edu>`

University of Michigan School of Information (UMSI)<br>
Master of Applied Data Science (MADS)<br>
SIADS 697 - Capstone<br>
Winter 2022

# Key links
- [Project home](https://ricky-wong.github.io/siads697-project)
- **[Project report](https://ricky-wong.github.io/siads697-project/report)**
- [GitHub repository](https://github.com/ricky-wong/siads697-project)

# About this repository
This repository contains work related to render this `README` and our project report, as well as all relevant notebooks, datasets, and utilities.

# Repository structure

## `dataset/`
Copies of the **Treatment Episode Data Set: Discharges** data ([2016](https://www.datafiles.samhsa.gov/dataset/teds-d-2016-ds0001-teds-d-2016-ds0001), [2017](https://www.datafiles.samhsa.gov/dataset/teds-d-2017-ds0001-teds-d-2017-ds0001), [2018](https://www.datafiles.samhsa.gov/dataset/teds-d-2018-ds0001-teds-d-2018-ds0001), [2019](https://www.datafiles.samhsa.gov/dataset/teds-d-2019-ds0001-teds-d-2019-ds0001))

## `notebooks/`
Jupyter Notebooks (`.ipynb` files) used for data ingestion, cleaning, training, modeling, prediction, and visualizations.

Notebooks have been saved with completed executions and rendered charts, for easy browsing. Saved notebooks do not always save completed renders.

Do not rely on GitHub's `.ipynb` renderer, since it will not render all types of outputs.

## `notebooks/lib/`
Convenience functions used among multiple notebooks to do multiple things. Includes the installation of `requirements.txt` packages.

## <a href="https://ricky-wong.github.io/siads697-project/report">`report/`</a>
Our detailed findings in a write-up.

Report originally written in `Report.md`, then compiled to `index.html` to get served automatically at `/report`.

The report consists of various SVGs generated from the notebooks, using different methods:

| Asset                                | Source                                | Method                              |
| ------------------------------------ | ------------------------------------- | ----------------------------------- |
| `completion-rates.html`              | `ExploratoryDataAnalysis.ipynb`       | `altair.save()` with `altair-saver` |
| `substance-rates.html`               | `Visual_Testing.ipynb`                | `altair.save()` with `altair-saver` |
| `most-common-primary-substance.html` | `Visual_Testing.ipynb`                | `altair.save()` with `altair-saver` |
| `violin2016.svg`                     | `Visual_Testing.ipynb`                | `pyplot.savefig()`                  |
| `violin2017.svg`                     | `Visual_Testing.ipynb`                | `pyplot.savefig()`                  |
| `violin2018.svg`                     | `Visual_Testing.ipynb`                | `pyplot.savefig()`                  |
| `violin2019.svg`                     | `Visual_Testing.ipynb`                | `pyplot.savefig()`                  |

# Tested environments
- Coursera's [Milestone 2 (SIADS 694-695) (Jupyter) notebook environment](https://www.coursera.org/learn/siads-694695/ungradedLab/RLLhW/notebook-environment)
  - 4 CPUs, 16GB RAM, 0 GPUs
  - Python 3.7.10
  - `jupyter-core` 4.7.1
  - `jupyter-notebook` 6.2.0
- [University of Michigan's Great Lakes cluster](https://greatlakes.arc-ts.umich.edu/) Jupyter Notebook (`python3.8-anaconda/2021.05`)
  - 4 CPUs, 16/32/64GB RAM, 1 GPU
  - Python 3.8.8
  - `jupyter-core` 4.7.1
  - `jupyter-notebook` 6.4.3
