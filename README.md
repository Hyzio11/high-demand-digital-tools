# High-Demand Digital Tools Analyzer

[![Buy on Gumroad](https://img.shields.io/badge/Buy-%245-ff90e8)](https://maronix2.gumroad.com/l/ejgsjf)
[![Python 3.6+](https://img.shields.io/badge/python-3.6%2B-blue)](https://python.org)

A CLI tool that ranks your digital product ideas by **ROI** and **demand score**. Stop guessing which product to build next — let data decide.

## Quick Start

```bash
# Run with your CSV
python high-demand-digital-tools.py --file ideas.csv --top 10
```

## Input Format

Your CSV needs three columns (case-insensitive):

| Column | Description |
|--------|-------------|
| `name` | Product/tool name |
| `demand` | Demand score (higher = more demand) |
| `roi` | ROI score (higher = better return) |

Example `ideas.csv`:
```csv
name,demand,roi
Bulk Image Resizer,8.5,9.2
JSON to CSV Converter,6.3,7.8
PDF Merger,7.1,6.5
```

## Features

- **ROI-first sorting** — prioritizes what makes the most money
- **Configurable top-N** — see only the best options
- **Custom delimiter** — works with TSV, pipe-delimited, etc.
- **Clear ranked output** — easy to read and share

## Usage

```bash
# Default: top 10 by ROI
python high-demand-digital-tools.py --file tools.csv

# Show top 5
python high-demand-digital-tools.py --file tools.csv --top 5

# Tab-separated file
python high-demand-digital-tools.py --file tools.tsv --delimiter $'	'
```

## Example Output

```
Top 3 high-demand tools by ROI:
1. Bulk Image Resizer: Demand=8.5, ROI=9.2
2. JSON to CSV Converter: Demand=6.3, ROI=7.8
3. PDF Merger: Demand=7.1, ROI=6.5
```

## Why This Tool?

Indie hackers waste months building things nobody wants. This tool takes your raw idea list and gives you a **data-backed priority order** in seconds. Build what sells, not what distracts.

## Buy

**$5 — one-time purchase, no subscriptions.**

👉 https://maronix2.gumroad.com/l/ejgsjf

## License

MIT
