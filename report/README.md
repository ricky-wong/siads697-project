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
