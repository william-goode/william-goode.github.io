#!/usr/bin/env python3
"""
Parse journal entries and extract Scaylor-related accomplishments.
Outputs a plain text file with summaries (no dates) for LLM processing.
"""

import os
import re
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent.parent
JOURNAL_FILE = REPO_ROOT / "journal" / "20250811-current.md"
OUTPUT_FILE = REPO_ROOT / ".generated" / "journal_summaries.txt"


def extract_scaylor_bullets(journal_content):
    """Extract all bullet points from journal, filtering for Scaylor-related work."""
    bullets = []
    
    # Split by week markers
    week_pattern = r'^## Week \d+.*?\n'
    weeks = re.split(week_pattern, journal_content, flags=re.MULTILINE)
    
    # Skip first element (content before first week)
    for week_content in weeks[1:]:
        # Extract all bullet points (lines starting with *)
        week_bullets = re.findall(r'^\* (.+)$', week_content, flags=re.MULTILINE)
        bullets.extend(week_bullets)
    
    return bullets


def write_summaries(bullets, output_file):
    """Write bullet summaries to plain text file (no dates, just summaries)."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("Scaylor AI Work Accomplishments\n")
        f.write("=" * 50 + "\n\n")
        f.write("Extracted from weekly journal entries. Focus on major features and infrastructure work.\n\n")
        
        for i, bullet in enumerate(bullets, 1):
            # Clean up bullet text (remove any markdown formatting)
            clean_bullet = re.sub(r'\*\*([^*]+)\*\*', r'\1', bullet)  # Remove bold
            clean_bullet = re.sub(r'`([^`]+)`', r'\1', clean_bullet)  # Remove code formatting
            clean_bullet = clean_bullet.strip()
            
            if clean_bullet:
                f.write(f"{i}. {clean_bullet}\n")
    
    print(f"✓ Extracted {len(bullets)} accomplishments to {output_file}")


def main():
    """Main execution."""
    if not JOURNAL_FILE.exists():
        print(f"Error: Journal file not found at {JOURNAL_FILE}")
        return
    
    # Read journal
    with open(JOURNAL_FILE, 'r', encoding='utf-8') as f:
        journal_content = f.read()
    
    # Extract bullets
    bullets = extract_scaylor_bullets(journal_content)
    
    if not bullets:
        print("Warning: No bullets found in journal")
        return
    
    # Write summaries
    write_summaries(bullets, OUTPUT_FILE)
    print(f"\nTotal accomplishments extracted: {len(bullets)}")


if __name__ == "__main__":
    main()

