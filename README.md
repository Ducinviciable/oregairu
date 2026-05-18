# Oregairu Zoku PC

## Purpose

This project aims to faithfully recreate the Oregairu VN in English on PC using the Ren'py engine. This is a fan project. All assets are the property and copyright of Mages Publishing.

## Routes to Finish (In Order)

1. Saki Route
   - Finished!
   - Build 0.2 was distributed on 9/4
2. Yukino Route
   - Finished!
3. Haruno Route
   - Finished!
4. Iroha Route
   - Finished!
5. Hiratsuka Route
   - Finished!
6. Yui Route
   - Finished!
7. Yumiko Route
   - ETA unknown

## File management TODO

1. SFX throughout the entire game
2. Change upscaler for backgrounds, too much exposure
3. Find file for the student council line in the valentines day scene

## Tools for Translation

- `tools/extract_text.py`: Extracts dialogue from `.rpy` files into a CSV for translation.
- `tools/generate_translation.py`: Generates a translated `.rpy` file from the CSV
- `tools/report_cleanup_coverage.py`: Compares source and translation `.rpy` files to report coverage and placeholders.
- `tools/game_test.py`: Basic parser test to check for missing translations or syntax errors.

## Workflow for New Routes

Read INSTRUCTION.md and TEMPLATE_WORKFLOW_ROUTE.md for detailed instructions on how to translate a new route using the tools provided.
