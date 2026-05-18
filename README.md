# Oregairu Zoku PC Translation Project

## Purpose

This repository contains fan-made translation tools, scripts, and workflow utilities for creating an English/Vietnamese Ren'Py-compatible translation patch for the Oregairu visual novel.

This is a non-commercial fan project and is not affiliated with or endorsed by the original copyright holders.

All original game assets, scripts, audio, images, characters, and trademarks belong to their respective owners, including MAGES. and related rights holders.

A legally obtained copy of the original game is required.

## Project Status

1. Saki Route — Finished
2. Yukino Route — Finished
3. Haruno Route — Finished
4. Iroha Route — Finished
5. Hiratsuka Route — Finished
6. Yui Route — Finished
7. Yumiko Route — In Progress

## Repository Contents

This repository primarily contains:

- Translation workflow tools
- CSV extraction/generation scripts
- Ren'Py translation pipeline utilities
- Translation patch files

Original commercial game assets are not included.

## Translation Tools

- `tools/extract_text.py`
  Extract dialogue from `.rpy` files into CSV format.

- `tools/generate_translation.py`
  Generate translated `.rpy` files from CSV data.

- `tools/report_cleanup_coverage.py`
  Validate translation coverage and placeholder handling.

- `tools/game_test.py`
  Run parser and syntax validation checks for generated files.

## Workflow

See:

- `INSTRUCTION.md`
- `TEMPLATE_WORKFLOW_ROUTE.md`

for the full translation workflow and route pipeline documentation.
