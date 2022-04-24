Our detailed findings in a write-up, intended to be generated and served off of GitHub Pages.

Unfortunately, the limitations of (GitHub) Markdown and our interactive needs do not allow us to simply render Markdown for our entire report, so we wrote the report in `Report.md` and compiled it to `index.html` to get served automatically at `/report`. We also manually substitute some generated code-blocks from various sources (listed below) into `index.html`, delimited by comments.

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

The table of contents and enumeration is generated using [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one), which supports the `<!-- omit in toc -->` syntax for ignoring enumeration/TOC for some headers.
