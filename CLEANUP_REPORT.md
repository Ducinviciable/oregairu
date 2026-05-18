# Repository Cleanup Report

## Outcome

The repository has been reduced toward a safe public translation-patch layout. Original Ren'Py runtime content, game scripts, compiled files, build/runtime artifacts, screenshots, and diagnostic logs are removed from git tracking or explicitly ignored.

## Kept In Scope

- `README.md`
- `tools/`
- `game/tl/vietnamese/*.rpy`
- translation workflow scripts such as `analyze_unbalanced_quotes.py`
- translation CSV sources such as `tools/E1_IRO.csv`
- patch/workflow documentation: `tools/INSTRUCTION.md` and `tools/TEMPLATE_WORKFLOW_ROUTE.md`

## Removed From Git Tracking

- `game/scripts/`
- `game/add_assets/`
- `renpy/`
- `lib/`
- `update/`
- `*.exe`
- `*.rpyc`
- screenshots
- logs and traceback files
- runtime/build artifacts under `game/`

## Recommended Public Repository Structure

```text
README.md
tools/
  INSTRUCTION.md
  TEMPLATE_WORKFLOW_ROUTE.md
  extract_text.py
  generate_translation.py
  report_cleanup_coverage.py
  game_test.py
  *.csv
game/
  tl/
    vietnamese/
      *.rpy
```

## Git History Risk Check

Repository history still contains copyrighted/runtime trees. The git history shows commits that touched `game/scripts`, `game/add_assets`, `renpy`, `lib`, and `update`.

Recommended action for a public release:

1. Preferred: create a fresh clean repository that contains only the patch/tooling surface.
2. Alternative: use `git filter-repo` to remove the copyrighted/runtime paths from all history.

## Exact Cleanup Commands

```bash
git rm -r --cached game renpy lib update
git rm --cached *.exe screenshot*.png
git rm --cached log.txt errors.txt traceback.txt oregairuzokupc.py
git add .gitignore
git add tools/E1_IRO.csv
git add game/tl/vietnamese/strings.rpy
git status
```

If history cleanup is required, a filter-repo pass should remove at least these paths:

```bash
git filter-repo --path game/scripts --path game/add_assets --path renpy --path lib --path update --invert-paths
```

## Notes

- The working tree still keeps local files in place; the cleanup is done by removing them from git tracking.
- Translation files under `game/tl/vietnamese/` remain the only game-tree content intended for release.
