#!/usr/bin/env python3
"""
Use Gemini API to condense journal summaries into 4 high-impact resume bullets.
Focuses on major features and infrastructure work.
"""

import os
import json
import yaml
from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv

# Paths
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent.parent
ENV_FILE = REPO_ROOT / ".env"
SUMMARIES_FILE = REPO_ROOT / ".generated" / "journal_summaries.txt"
OUTPUT_FILE = REPO_ROOT / ".generated" / "resume_bullets.json"
CV_YML_FILE = REPO_ROOT / "_data" / "cv.yml"


def load_api_key():
    """Load Gemini API key from .env file."""
    # Load .env file from repo root
    if ENV_FILE.exists():
        load_dotenv(ENV_FILE)
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print(f"Error: GEMINI_API_KEY not found in {ENV_FILE}")
        print("Please add GEMINI_API_KEY=your-key-here to .env file")
        return None
    return api_key


def load_summaries():
    """Load journal summaries from text file."""
    if not SUMMARIES_FILE.exists():
        print(f"Error: Summaries file not found at {SUMMARIES_FILE}")
        print("Please run parse_journal.py first")
        return None
    
    with open(SUMMARIES_FILE, 'r', encoding='utf-8') as f:
        return f.read()


def generate_resume_bullets(summaries_text, api_key):
    """Use Gemini to generate 4 high-impact resume bullets."""
    genai.configure(api_key=api_key)
    
    # Use gemini-2.0-flash (fast and capable) or gemini-2.5-flash for latest
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    prompt = f"""You are analyzing work accomplishments from a backend engineer's weekly journal entries.

CRITICAL SECURITY REQUIREMENT: 
- NEVER include customer names, client names, or any identifying information about customers/clients
- Use generic terms like "client", "customer", "enterprise client", or "data source" instead
- Do not mention specific company names, product names, or any information that could identify a customer
- Do not mention specific product interfaces or UI paradigms (e.g., "IDE", "Cursor-like", etc.) - use generic terms like "platform", "tooling system", "interface"
- This is a public resume - customer confidentiality and product confidentiality are paramount

The following text contains all accomplishments from August 2025 to November 2025 at Scaylor AI:

{summaries_text}

Your task: Generate exactly 4 high-impact resume bullet points that:
1. Focus on MAJOR FEATURES and infrastructure work (not minor bug fixes or routine tasks)
2. Capture the full project lifecycle (from design to deployment)
3. Use strong action verbs and quantify results where possible
4. Are concise but impactful (one sentence each)
5. Show progression and increasing responsibility
6. Highlight technical depth (cloud infrastructure, data pipelines, security, etc.)
7. NEVER mention customer names, client names, or any identifying information

Format: Return ONLY a JSON array of exactly 4 strings, no other text:
["bullet point 1", "bullet point 2", "bullet point 3", "bullet point 4"]

Example format (note: no customer names):
["Architected and deployed GDPR-compliant data ingestion infrastructure using Terraform across EU regions", "Developed and deployed NL→SQL microservice on Google Cloud Run with multi-dataset support and security validation", "Built unified data tooling platform for schema reconciliation and AI-powered analysis with multi-panel workspace interface", "Led infrastructure migration projects including billing account consolidation and Workload Identity Federation for secure customer access"]
"""
    
    try:
        response = model.generate_content(prompt)
        response_text = response.text.strip()
        
        # Extract JSON from response (handle markdown code blocks if present)
        if "```json" in response_text:
            response_text = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            response_text = response_text.split("```")[1].split("```")[0].strip()
        
        # Parse JSON
        bullets = json.loads(response_text)
        
        if not isinstance(bullets, list) or len(bullets) != 4:
            print(f"Warning: Expected 4 bullets, got {len(bullets) if isinstance(bullets, list) else 'invalid format'}")
            return None
        
        return bullets
    
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return None


def update_cv_yml(bullets):
    """Update cv.yml with generated Scaylor bullets (up to 8 bullets allowed for website)."""
    if not CV_YML_FILE.exists():
        print(f"Warning: {CV_YML_FILE} not found, skipping cv.yml update")
        return False
    
    try:
        # Read cv.yml
        with open(CV_YML_FILE, 'r', encoding='utf-8') as f:
            cv_data = yaml.safe_load(f)
        
        # Find Scaylor AI experience entry (first entry with "Present" in date)
        scaylor_entry = None
        for entry in cv_data.get('experience', []):
            if entry.get('organization') == 'Scaylor AI' and 'Present' in entry.get('date', ''):
                scaylor_entry = entry
                break
        
        if not scaylor_entry:
            print("Warning: Scaylor AI experience entry not found in cv.yml")
            return False
        
        # Update highlights with generated bullets (replace existing, keep up to 8 total)
        # For now, we'll replace all highlights with the 4 generated bullets
        # User can manually add up to 4 more bullets in cv.yml for website display
        scaylor_entry['highlights'] = bullets
        
        # Write back to cv.yml
        with open(CV_YML_FILE, 'w', encoding='utf-8') as f:
            yaml.dump(cv_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
        
        print(f"✓ Updated cv.yml with Scaylor highlights (4 bullets)")
        print(f"  Note: You can add up to 4 more bullets manually in cv.yml for website display")
        return True
    
    except Exception as e:
        print(f"Error updating cv.yml: {e}")
        return False


def save_bullets(bullets, output_file):
    """Save resume bullets to JSON file (for backwards compatibility)."""
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(bullets, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Generated 4 resume bullets:")
    for i, bullet in enumerate(bullets, 1):
        print(f"  {i}. {bullet}")
    print(f"\n✓ Saved to {output_file}")


def main():
    """Main execution."""
    # Load API key
    api_key = load_api_key()
    if not api_key:
        return
    
    # Load summaries
    summaries_text = load_summaries()
    if not summaries_text:
        return
    
    # Generate bullets
    print("Calling Gemini API to generate resume bullets...")
    bullets = generate_resume_bullets(summaries_text, api_key)
    
    if not bullets:
        print("Failed to generate bullets")
        return
    
    # Update cv.yml with generated bullets
    update_cv_yml(bullets)
    
    # Save bullets to JSON (for backwards compatibility)
    save_bullets(bullets, OUTPUT_FILE)


if __name__ == "__main__":
    main()

