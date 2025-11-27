#!/usr/bin/env python3
"""
Generate William Goode's professional resume as a PDF.
Enhanced with improved visual hierarchy and spacing.
Resume bullets are dynamically loaded from journal entries via LLM processing.
"""

import os
import json
import yaml
from datetime import datetime
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether, Table, TableStyle, HRFlowable
from reportlab.lib.colors import HexColor

# Output file - always output to the same directory as this script
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent.parent
OUTPUT_FILE = str(SCRIPT_DIR / "William_Goode_Resume_Professional.pdf")
CV_YML_FILE = REPO_ROOT / "_data" / "cv.yml"
RESUME_BULLETS_FILE = REPO_ROOT / ".generated" / "resume_bullets.json"  # Fallback only
RESUME_METADATA_FILE = REPO_ROOT / "_data" / "resume.yml"

# Professional color palette
HEADER_COLOR = HexColor("#1a1a1a")
SECTION_COLOR = HexColor("#2c5282")  # Professional blue
ACCENT_COLOR = HexColor("#4a5568")   # Muted gray-blue
TEXT_COLOR = HexColor("#2d3748")     # Dark gray
LIGHT_TEXT = HexColor("#4a5568")     # Lighter gray for secondary text
LINK_COLOR = HexColor("#2b6cb0")     # Professional blue

# Create PDF with optimized margins for single page
pdf = SimpleDocTemplate(
    OUTPUT_FILE,
    pagesize=letter,
    rightMargin=0.6*inch,
    leftMargin=0.6*inch,
    topMargin=0.5*inch,
    bottomMargin=0.5*inch,
)

# Styles
styles = getSampleStyleSheet()

# Custom styles with improved hierarchy
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=HEADER_COLOR,
    spaceAfter=6,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold',
    leading=28,
)

contact_style = ParagraphStyle(
    'Contact',
    parent=styles['Normal'],
    fontSize=9.5,
    textColor=LIGHT_TEXT,
    alignment=TA_CENTER,
    spaceAfter=12,
    leading=13,
)

section_style = ParagraphStyle(
    'Section',
    parent=styles['Heading2'],
    fontSize=12.5,
    textColor=SECTION_COLOR,
    spaceBefore=10,
    spaceAfter=6,
    fontName='Helvetica-Bold',
    leading=15,
    leftIndent=0,
    underlineProportion=0.15,
)

job_title_style = ParagraphStyle(
    'JobTitle',
    parent=styles['Normal'],
    fontSize=10.5,
    textColor=TEXT_COLOR,
    fontName='Helvetica-Bold',
    leading=14,
    spaceAfter=2,
)

company_style = ParagraphStyle(
    'Company',
    parent=styles['Normal'],
    fontSize=10,
    textColor=LIGHT_TEXT,
    fontName='Helvetica-Oblique',
    leading=13,
    spaceAfter=4,
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontSize=10,
    textColor=TEXT_COLOR,
    leading=13,
    leftIndent=0,
    spaceAfter=2,
    alignment=TA_JUSTIFY,
)

bullet_style = ParagraphStyle(
    'Bullet',
    parent=styles['Normal'],
    fontSize=9.5,
    textColor=TEXT_COLOR,
    leading=12,
    leftIndent=18,
    bulletIndent=6,
    spaceAfter=3,
    firstLineIndent=0,
)

# Content
story = []

# Header with name
story.append(Paragraph("WILLIAM GOODE", title_style))
story.append(Paragraph(
    '<a href="mailto:william.maverick.goode@gmail.com" color="#2b6cb0">william.maverick.goode@gmail.com</a> | '
    '<a href="https://william-goode.github.io" color="#2b6cb0">william-goode.github.io</a><br/>'
    '<a href="https://github.com/william-goode" color="#2b6cb0">github.com/william-goode</a> | '
    '<a href="https://linkedin.com/in/william-goode" color="#2b6cb0">linkedin.com/in/william-goode</a>',
    contact_style
))

# Education
story.append(Paragraph("EDUCATION", section_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=SECTION_COLOR, spaceAfter=6))

story.append(Paragraph("<b>Ph.D. in Mathematics</b>", job_title_style))
story.append(Paragraph("University of North Texas | 2023", company_style))
story.append(Paragraph(
    "<i>Dissertation:</i> Annihilators of irreducible representations of the Lie superalgebra of contact vector fields",
    body_style
))
story.append(Paragraph("4.0 GPA | Published in <i>Expositiones Mathematicae</i>", body_style))
story.append(Spacer(1, 5))

story.append(Paragraph("<b>B.S. in Mathematics, B.S. in Economics</b>", job_title_style))
story.append(Paragraph("University of North Texas | 2017", company_style))
story.append(Paragraph("3.79 GPA, Cum Laude", body_style))
story.append(Spacer(1, 2))

# Load technical skills from cv.yml
def load_technical_skills():
    """Load technical skills from cv.yml."""
    if CV_YML_FILE.exists():
        try:
            with open(CV_YML_FILE, 'r', encoding='utf-8') as f:
                cv_data = yaml.safe_load(f)
            
            skills = cv_data.get('skills', [])
            if skills:
                return skills
        except Exception as e:
            print(f"Warning: Could not load skills from cv.yml: {e}")
    
    # Fallback to default skills
    print("Warning: Using default technical skills (cv.yml not found or incomplete)")
    return [
        {
            'category': 'Programming Languages',
            'items': ['Python', 'SQL (BigQuery, MS SQL Server, PostgreSQL)', 'C# / .NET']
        },
        {
            'category': 'Cloud & Infrastructure',
            'items': ['AWS (Lambda, S3, RDS, Athena)', 'GCP (BigQuery, Cloud Storage, Cloud Run, IAM)', 'Docker']
        },
        {
            'category': 'Backend',
            'items': ['FastAPI', 'ASP.NET Core', 'Entity Framework', 'LLM integration']
        },
        {
            'category': 'Data Engineering & Databases',
            'items': ['Data pipeline development', 'Vector databases', 'Query optimization and performance tuning', 'Schema reconciliation']
        }
    ]

# Technical Skills
story.append(Paragraph("TECHNICAL SKILLS", section_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=SECTION_COLOR, spaceAfter=6))

technical_skills = load_technical_skills()

# Format skills for resume (condensed format)
skill_categories_map = {
    'Programming Languages': 'Languages',
    'Cloud & Infrastructure': 'Cloud & Infrastructure',
    'Backend': 'Backend',
    'Data Engineering & Databases': 'Data Engineering',
    'Mathematics': None  # Skip Mathematics on resume
}

for skill_category in technical_skills:
    category_name = skill_category.get('category', '')
    resume_category = skill_categories_map.get(category_name)
    
    # Skip Mathematics category on resume
    if resume_category is None:
        continue
    
    items = skill_category.get('items', [])
    if items:
        items_str = ', '.join(items)
        story.append(Paragraph(
            f"<b>{resume_category}:</b> {items_str}",
            body_style
        ))
        story.append(Spacer(1, 1))

# Experience
story.append(Paragraph("EXPERIENCE", section_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=SECTION_COLOR, spaceAfter=6))

# Load Scaylor resume bullets from cv.yml (synced with website)
def load_resume_bullets():
    """Load Scaylor resume bullets from cv.yml (first 4 bullets for resume)."""
    if CV_YML_FILE.exists():
        try:
            with open(CV_YML_FILE, 'r', encoding='utf-8') as f:
                cv_data = yaml.safe_load(f)
            
            # Find Scaylor AI experience entry
            for entry in cv_data.get('experience', []):
                if entry.get('organization') == 'Scaylor AI' and 'Present' in entry.get('date', ''):
                    highlights = entry.get('highlights', [])
                    if highlights:
                        # Resume uses first 4 bullets (website can show up to 8)
                        resume_bullets = highlights[:4]
                        if len(resume_bullets) == 4:
                            return resume_bullets
                        elif len(resume_bullets) > 0:
                            print(f"Warning: Found {len(resume_bullets)} bullets in cv.yml, expected 4")
                            return resume_bullets
        except Exception as e:
            print(f"Warning: Could not load bullets from cv.yml: {e}")
    
    # Fallback to JSON file (backwards compatibility)
    if RESUME_BULLETS_FILE.exists():
        try:
            with open(RESUME_BULLETS_FILE, 'r', encoding='utf-8') as f:
                bullets = json.load(f)
            if isinstance(bullets, list) and len(bullets) >= 4:
                print("Warning: Using resume_bullets.json (cv.yml not found or incomplete)")
                return bullets[:4]
        except Exception as e:
            print(f"Warning: Could not load resume bullets: {e}")
    
    # Final fallback to default bullets
    print("Warning: No resume bullets found. Using default bullets.")
    print("Run 'python3 generate_resume_bullets.py' to generate from journal entries.")
    return [
        "Architect and deploy data ingestion systems for client database integration",
        "Develop microservices for SQL generation and query execution",
        "Design and implement data workflows compliant with GDPR requirements",
        "Manage security and access provisioning across cloud infrastructure",
    ]

# Scaylor
story.append(Paragraph("<b>Backend Engineer</b>", job_title_style))
story.append(Paragraph("Scaylor AI | August 2025 – Present", company_style))
scaylor_bullets = load_resume_bullets()
for bullet in scaylor_bullets:
    story.append(Paragraph(f"• {bullet}", bullet_style))
story.append(Spacer(1, 6))

# Concan (title only, no bullets)
story.append(Paragraph("<b>Software Engineer</b>", job_title_style))
story.append(Paragraph("Concan Consulting Corporation | April – June 2025", company_style))
story.append(Spacer(1, 6))

# Vanderbilt (title only, no bullets)
story.append(Paragraph("<b>Senior Lecturer of Mathematics</b>", job_title_style))
story.append(Paragraph("Vanderbilt University | August 2023 – August 2024", company_style))

# Publication
story.append(Paragraph("PUBLICATION", section_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=SECTION_COLOR, spaceAfter=6))
story.append(Paragraph(
    'C. H. Conley, W. Goode. "An approach to annihilators in the context of vector field Lie algebras." '
    '<i>Expositiones Mathematicae</i> (2024). arXiv:2403.01728',
    body_style
))

# Build PDF
pdf.build(story)

# Update resume metadata with current date
try:
    current_date = datetime.now().strftime("%B %d, %Y")
    resume_metadata = {
        'last_updated': current_date
    }
    with open(RESUME_METADATA_FILE, 'w', encoding='utf-8') as f:
        yaml.dump(resume_metadata, f, indent=2, default_flow_style=False, allow_unicode=True)
    print(f"✓ Resume metadata updated: {current_date}")
except Exception as e:
    print(f"Warning: Could not update resume metadata: {e}")

print(f"✓ Resume generated: {OUTPUT_FILE}")

