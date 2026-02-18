#!/usr/bin/env python3
"""Rename working group directories and files, fix headers, and update all references."""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WG_DIR = ROOT / "psf" / "working-groups"

# === Directory renames (old basename -> new basename) ===
DIR_RENAMES = {
    "BylawsWG": "Bylaws",
    "ConductWG": "Conduct",
    "ExampleWG": "Example",
    "FellowWG": "Fellow",
    "GrantsWG": "Grants",
    "JobsWG": "Jobs",
    "MarketingWG": "Marketing",
    "MetaWG": "Meta",
    "PackagingWG": "Packaging",
    "ProjectFundingWG": "Project Funding",
    "PydotorgWG": "Pydotorg",
    "PythonCubaWG": "Python Cuba",
    "ScientificWG": "Scientific",
    "SponsorWG": "Sponsor",
    "SponsorshipBundleWG": "Sponsorship Bundle",
    "TranslationWG": "Translation",
}

# === Standalone .md file renames (old stem -> new stem) ===
FILE_RENAMES = {
    "BylawsWG": "Bylaws",
    "ConductWGGroup": "Conduct Group",
    "DiversityandInclusionWG": "Diversity and Inclusion",
    "EducationEcosystem": "Education Ecosystem",
    "EducationWGGroup": "Education Group",
    "FellowWG": "Fellow",
    "FellowWGGroup": "Fellow Group",
    "GrantsWG": "Grants",
    "GrantsWGGroup": "Grants Group",
    "InfrastructureWG": "Infrastructure",
    "JobsWG": "Jobs",
    "MarketingWG": "Marketing",
    "MetaWG": "Meta",
    "PackagingWG": "Packaging",
    "PackagingWGGroup": "Packaging Group",
    "ProjectFundingWG": "Project Funding",
    "PydotorgWG": "Pydotorg",
    "PythonCubaWG": "Python Cuba",
    "PythonEduWG": "Python Edu",
    "PythonEduWGCharter": "Python Edu Charter",
    "ScientificWG": "Scientific",
    "ScientificWGGroup": "Scientific Group",
    "SponsorWG": "Sponsor",
    "SponsorWGGroup": "Sponsor Group",
    "SponsorshipBundleWG": "Sponsorship Bundle",
    "TranslationWG": "Translation",
}

# === H1 header fixes for subdirectory index.md files ===
INDEX_H1_FIXES = {
    "Bylaws": "Bylaws",
    "Conduct": "Conduct",
    "Example": "Example",
    "Fellow": "Fellow",
    "Grants": "Grants",
    "Jobs": "Jobs",
    "Marketing": "Marketing",
    "Meta": "Meta",
    "Packaging": "Packaging",
    "Project Funding": "Project Funding",
    "Pydotorg": "Pydotorg",
    "Python Cuba": "Python Cuba",
    "Scientific": "Scientific",
    "Sponsor": "Sponsor",
    "Sponsorship Bundle": "Sponsorship Bundle",
    "Translation": "Translation",
}

# === Charter H1 header fixes ===
CHARTER_H1_FIXES = {
    "Bylaws": ("BylawsWG/Charter", "Bylaws Charter"),
    "Conduct": ("ConductWG/Charter", "Conduct Charter"),
    "Example": ("ExampleWG/Charter", "Example Charter"),
    "Fellow": ("FellowWG/Charter", "Fellow Charter"),
    "Grants": ("GrantsWG/Charter", "Grants Charter"),
    "Jobs": ("JobsWG/Charter", "Jobs Charter"),
    "Marketing": ("MarketingWG/Charter", "Marketing Charter"),
    "Meta": ("MetaWG/Charter", "Meta Charter"),
    "Packaging": ("PackagingWG/Charter", "Packaging Charter"),
    "Project Funding": ("ProjectFundingWG/Charter", "Project Funding Charter"),
    "Pydotorg": ("PydotorgWG/Charter", "Pydotorg Charter"),
    "Python Cuba": ("PythonCubaWG/Charter", "Python Cuba Charter"),
    "Scientific": ("ScientificWG/Charter", "Scientific Charter"),
    "Sponsor": ("SponsorWG/Charter", "Sponsor Charter"),
    "Sponsorship Bundle": ("SponsorshipBundleWG/Charter", "Sponsorship Bundle Charter"),
    "Translation": ("TranslationWG/Charter", "Translation Charter"),
}


def git_mv(src: Path, dst: Path) -> None:
    """Run git mv, creating parent dirs if needed."""
    dst.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "mv", str(src), str(dst)], cwd=ROOT, check=True)
    print(f"  git mv {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")


def step1_rename_dirs():
    """Rename all 16 working group directories."""
    print("\n=== Step 1: Renaming directories ===")
    for old_name, new_name in DIR_RENAMES.items():
        src = WG_DIR / old_name
        dst = WG_DIR / new_name
        if src.exists():
            git_mv(src, dst)
        else:
            print(f"  SKIP (not found): {src.relative_to(ROOT)}")


def step2_rename_files():
    """Rename all 26 standalone .md files."""
    print("\n=== Step 2: Renaming standalone .md files ===")
    for old_stem, new_stem in FILE_RENAMES.items():
        src = WG_DIR / f"{old_stem}.md"
        dst = WG_DIR / f"{new_stem}.md"
        if src.exists():
            git_mv(src, dst)
        else:
            print(f"  SKIP (not found): {src.relative_to(ROOT)}")


def step3_fix_index_headers():
    """Fix H1 headers in all subdirectory index.md files."""
    print("\n=== Step 3: Fixing index.md H1 headers ===")
    for new_dir_name, clean_title in INDEX_H1_FIXES.items():
        index_path = WG_DIR / new_dir_name / "index.md"
        if not index_path.exists():
            print(f"  SKIP (not found): {index_path.relative_to(ROOT)}")
            continue
        text = index_path.read_text()
        # Replace the first H1 line
        new_text = re.sub(r"^# .+$", f"# {clean_title}", text, count=1, flags=re.MULTILINE)
        if new_text != text:
            index_path.write_text(new_text)
            print(f"  Fixed H1 in {index_path.relative_to(ROOT)}")


def step4_fix_charter_headers():
    """Fix H1 headers in Charter.md files (e.g. '# BylawsWG/Charter' -> '# Bylaws Charter')."""
    print("\n=== Step 4: Fixing Charter.md H1 headers ===")
    for new_dir_name, (old_h1, new_h1) in CHARTER_H1_FIXES.items():
        charter_path = WG_DIR / new_dir_name / "Charter.md"
        if not charter_path.exists():
            continue
        text = charter_path.read_text()
        new_text = text.replace(f"# {old_h1}", f"# {new_h1}", 1)
        if new_text != text:
            charter_path.write_text(new_text)
            print(f"  Fixed H1 in {charter_path.relative_to(ROOT)}")


def step5_update_references():
    """Update all internal references across the wiki."""
    print("\n=== Step 5: Updating internal references ===")

    # Build replacement map for link targets (sorted longest-first to avoid partial matches)
    # These are path-based replacements for markdown link targets and toctree entries
    replacements = []

    # Directory-based paths (e.g., BylawsWG/index -> Bylaws/index, BylawsWG/Charter -> Bylaws/Charter)
    for old_name, new_name in DIR_RENAMES.items():
        replacements.append((f"{old_name}/", f"{new_name}/"))

    # Standalone file references (without .md extension, as used in links)
    # Must come after directory replacements and be careful not to match directory prefixes
    for old_stem, new_stem in FILE_RENAMES.items():
        # These are used in various contexts - we'll handle them file-by-file
        pass

    # Process specific files that contain WG references
    files_to_update = []

    # Collect all .md files under psf/working-groups/ (now renamed)
    for md_file in WG_DIR.rglob("*.md"):
        files_to_update.append(md_file)

    # Other files with known references
    other_files = [
        ROOT / "psf" / "about" / "Contents.md",
        ROOT / "psf" / "governance" / "Info for new PSF members.md",
        ROOT / "psf" / "governance" / "NewMembershipModel.md",
        ROOT / "psf" / "packaging" / "WarehouseRoadmap.md",
        ROOT / "psf" / "packaging" / "Fundable Packaging Improvements.md",
        ROOT / "psf" / "packaging" / "Pip2020DonorFundedRoadmap.md",
        ROOT / "psf" / "packaging" / "WarehousePackageMaintainerTesting.md",
        ROOT / "people" / "R-S" / "Sumana Harihareswara.md",
        ROOT / "contributing" / "development.md",
        ROOT / "README.md",
    ]
    for f in other_files:
        if f.exists():
            files_to_update.append(f)

    # Build a comprehensive ordered replacement list for link targets/paths
    # Order: longer strings first to avoid partial matches
    path_replacements = []

    # Directory path replacements (with slash to avoid partial matches on standalone files)
    for old_name, new_name in sorted(DIR_RENAMES.items(), key=lambda x: -len(x[0])):
        path_replacements.append((f"{old_name}/", f"{new_name}/"))

    # Standalone file replacements - these need word-boundary-aware regex
    # We'll handle these with regex in a second pass
    standalone_replacements = []
    for old_stem, new_stem in sorted(FILE_RENAMES.items(), key=lambda x: -len(x[0])):
        standalone_replacements.append((old_stem, new_stem))

    updated_count = 0
    for filepath in files_to_update:
        text = filepath.read_text()
        original = text

        # Pass 1: Replace directory paths (XyzWG/ -> New Name/)
        for old_path, new_path in path_replacements:
            text = text.replace(old_path, new_path)

        # Pass 2: Replace standalone references that appear as link targets
        # These show up in patterns like:
        #   (BylawsWG)  or  (../working-groups/BylawsWG)
        #   BylawsWG\n  (in toctree entries)
        # We need to be careful not to replace inside already-replaced directory paths
        for old_stem, new_stem in standalone_replacements:
            # In markdown link targets: (BylawsWG) or (../working-groups/BylawsWG)
            text = re.sub(
                rf"(\((?:\.\./working-groups/)?){re.escape(old_stem)}(\))",
                rf"\g<1>{new_stem}\g<2>",
                text,
            )
            # In toctree entries (bare name on its own line, no trailing slash)
            text = re.sub(
                rf"^({re.escape(old_stem)})$",
                new_stem,
                text,
                flags=re.MULTILINE,
            )
            # H1 headers like "# BylawsWG" or "# GrantsWG"
            text = re.sub(
                rf"^# {re.escape(old_stem)}$",
                f"# {new_stem}",
                text,
                flags=re.MULTILINE,
            )
            # "subpages, e.g. BylawsWG/Charter" pattern (advisory text in some files)
            text = re.sub(
                rf"e\.g\. {re.escape(old_stem)}/",
                f"e.g. {new_stem}/",
                text,
            )

        # Pass 3: Fix SECTION=PackagingWG references in docs
        text = text.replace("SECTION=PackagingWG", "SECTION=Packaging")

        # Pass 4: Fix absolute wiki URLs like https://wiki.python.org/psf/PackagingWG
        for old_name, new_name in sorted(DIR_RENAMES.items(), key=lambda x: -len(x[0])):
            text = text.replace(
                f"wiki.python.org/psf/{old_name}",
                f"wiki.python.org/psf/{new_name}",
            )

        if text != original:
            filepath.write_text(text)
            updated_count += 1
            print(f"  Updated {filepath.relative_to(ROOT)}")

    print(f"  Total files updated: {updated_count}")


def step6_update_redirects():
    """Update _redirects.json target values from old names to new names."""
    print("\n=== Step 6: Updating _redirects.json ===")
    redirects_path = ROOT / "_redirects.json"
    text = redirects_path.read_text()

    # Build replacement map for redirect targets (values)
    # Directory paths in targets
    for old_name, new_name in sorted(DIR_RENAMES.items(), key=lambda x: -len(x[0])):
        # Targets look like: psf/working-groups/BylawsWG/Charter
        old_target = f"psf/working-groups/{old_name}/"
        new_target = f"psf/working-groups/{new_name}/"
        text = text.replace(old_target, new_target)

        # Also the directory itself as a target (no trailing slash after dir name)
        # e.g., "psf/working-groups/BylawsWG/index" already handled by above
        # but "psf/working-groups/BylawsWG" (exact, as the standalone .md)
        # Need to be careful - only replace in value position

    # Standalone file targets
    for old_stem, new_stem in sorted(FILE_RENAMES.items(), key=lambda x: -len(x[0])):
        old_target = f"psf/working-groups/{old_stem}\""
        new_target = f"psf/working-groups/{new_stem}\""
        text = text.replace(old_target, new_target)

    redirects_path.write_text(text)

    # Verify it's still valid JSON
    with open(redirects_path) as f:
        data = json.load(f)
    print(f"  Updated {redirects_path.relative_to(ROOT)} ({len(data)} entries, valid JSON)")


def main():
    print("Working group rename script")
    print(f"Root: {ROOT}")

    step1_rename_dirs()
    step2_rename_files()
    step3_fix_index_headers()
    step4_fix_charter_headers()
    step5_update_references()
    step6_update_redirects()

    print("\n=== Done! ===")
    print("Next steps:")
    print("  1. Run: python3 scripts/gen_redirect_pages.py")
    print("  2. Review changes with: git diff --stat")
    print("  3. Build and verify: make docs-serve-fast WIKI=psf")


if __name__ == "__main__":
    main()
