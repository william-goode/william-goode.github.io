#!/usr/bin/env python3
"""
Generate William Goode's professional resume as a PDF.
Enhanced with improved visual hierarchy and spacing.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether, Table, TableStyle, HRFlowable
from reportlab.lib.colors import HexColor

# Output file
OUTPUT_FILE = "William_Goode_Resume_Professional.pdf"

# Professional color palette
HEADER_COLOR = HexColor("#1a1a1a")
SECTION_COLOR = HexColor("#2c5282")  # Professional blue
ACCENT_COLOR = HexColor("#4a5568")   # Muted gray-blue
TEXT_COLOR = HexColor("#2d3748")     # Dark gray
LIGHT_TEXT = HexColor("#4a5568")     # Lighter gray for secondary text
LINK_COLOR = HexColor("#2b6cb0")     # Professional blue

# Create PDF with generous margins
pdf = SimpleDocTemplate(
    OUTPUT_FILE,
    pagesize=letter,
    rightMargin=0.7*inch,
    leftMargin=0.7*inch,
    topMargin=0.65*inch,
    bottomMargin=0.65*inch,
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
    fontSize=10,
    textColor=LIGHT_TEXT,
    alignment=TA_CENTER,
    spaceAfter=18,
    leading=14,
)

section_style = ParagraphStyle(
    'Section',
    parent=styles['Heading2'],
    fontSize=13,
    textColor=SECTION_COLOR,
    spaceBefore=16,
    spaceAfter=8,
    fontName='Helvetica-Bold',
    leading=16,
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
    spaceAfter=6,
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontSize=10,
    textColor=TEXT_COLOR,
    leading=14,
    leftIndent=0,
    spaceAfter=3,
    alignment=TA_JUSTIFY,
)

bullet_style = ParagraphStyle(
    'Bullet',
    parent=styles['Normal'],
    fontSize=9.5,
    textColor=TEXT_COLOR,
    leading=13,
    leftIndent=18,
    bulletIndent=6,
    spaceAfter=4,
    firstLineIndent=0,
)

# Content
story = []

# Header with name
story.append(Paragraph("WILLIAM GOODE", title_style))
story.append(Paragraph(
    '<a href="mailto:william.maverick.goode@gmail.com" color="#2b6cb0">william.maverick.goode@gmail.com</a> | '
    '<a href="https://github.com/william-goode" color="#2b6cb0">github.com/william-goode</a> | '
    '<a href="https://linkedin.com/in/william-goode" color="#2b6cb0">linkedin.com/in/william-goode</a>',
    contact_style
))

# Education
story.append(Paragraph("EDUCATION", section_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=SECTION_COLOR, spaceAfter=8))

story.append(Paragraph("<b>Ph.D. in Mathematics</b>", job_title_style))
story.append(Paragraph("University of North Texas | 2023", company_style))
story.append(Paragraph(
    "<i>Dissertation:</i> Annihilators of irreducible representations of the Lie superalgebra of contact vector fields",
    body_style
))
story.append(Paragraph("4.0 GPA | Published in <i>Expositiones Mathematicae</i>", body_style))
story.append(Spacer(1, 8))

story.append(Paragraph("<b>B.S. in Mathematics, B.S. in Economics</b>", job_title_style))
story.append(Paragraph("University of North Texas | 2017", company_style))
story.append(Paragraph("3.79 GPA, Cum Laude", body_style))

# Technical Skills
story.append(Paragraph("TECHNICAL SKILLS", section_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=SECTION_COLOR, spaceAfter=8))

story.append(Paragraph(
    "<b>Languages:</b> Python, SQL (BigQuery, MS SQL Server, PostgreSQL), C# / .NET",
    body_style
))
story.append(Spacer(1, 2))
story.append(Paragraph(
    "<b>Cloud &amp; Infrastructure:</b> AWS (Lambda, S3, RDS, Athena), GCP (BigQuery, Cloud Storage, Cloud Run, IAM), Docker",
    body_style
))
story.append(Spacer(1, 2))
story.append(Paragraph(
    "<b>Backend:</b> FastAPI, ASP.NET Core, Entity Framework",
    body_style
))
story.append(Spacer(1, 2))
story.append(Paragraph(
    "<b>Data Engineering:</b> Data pipeline development, Vector databases, DuckDB, MongoDB, Query optimization, Schema reconciliation",
    body_style
))
story.append(Spacer(1, 2))
story.append(Paragraph(
    "<b>Machine Learning:</b> LLM integration for data workflows",
    body_style
))

# Experience
story.append(Paragraph("EXPERIENCE", section_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=SECTION_COLOR, spaceAfter=8))

# Scaylor
story.append(Paragraph("<b>Backend Engineer</b>", job_title_style))
story.append(Paragraph("Scaylor AI | August 2025 – Present", company_style))
bullets = [
    "Architect and deploy data ingestion systems for client database integration",
    "Develop microservices for SQL generation and query execution",
    "Design and implement data workflows compliant with GDPR requirements",
    "Manage security and access provisioning across cloud infrastructure",
    "Execute database migrations and establish data ingestion pipelines",
    "Serve as technical point of contact for client integrations and onboarding",
    "Conduct technical interviews for engineering positions",
]
for bullet in bullets:
    story.append(Paragraph(f"• {bullet}", bullet_style))
story.append(Spacer(1, 10))

# Concan
story.append(Paragraph("<b>Software Engineer</b>", job_title_style))
story.append(Paragraph("Concan Consulting Corporation | April – June 2025", company_style))
bullets = [
    "Developed REST API for client applications",
    "Consulted small e-commerce businesses on technical best practices",
]
for bullet in bullets:
    story.append(Paragraph(f"• {bullet}", bullet_style))
story.append(Spacer(1, 10))

# Vanderbilt
story.append(Paragraph("<b>Senior Lecturer of Mathematics</b>", job_title_style))
story.append(Paragraph("Vanderbilt University | August 2023 – August 2024", company_style))
story.append(Paragraph(
    "• Taught calculus, statistics, and survey courses (6 courses total)",
    bullet_style
))

# Projects
story.append(Paragraph("PROJECTS", section_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=SECTION_COLOR, spaceAfter=8))

story.append(Paragraph("<b>Data Pipeline Architecture</b>", job_title_style))
story.append(Paragraph(
    "Evaluated and implemented GCS → BigQuery pipeline from scratch. Assessed multiple approaches (AWS Athena/Glue, DuckDB, MongoDB) before selecting GCP BigQuery based on scalability and cost requirements.",
    body_style
))
story.append(Spacer(1, 6))

story.append(Paragraph("<b>Dynamic Data Visualization</b>", job_title_style))
story.append(Paragraph(
    "Created local database in Microsoft SQL Server and connected to dynamic visualization web app using Dash and Flask.",
    body_style
))
story.append(Spacer(1, 6))

story.append(Paragraph("<b>Containerized ML Deployment</b>", job_title_style))
story.append(Paragraph(
    "Deployed machine learning models on Amazon ECS as containerized web applications.",
    body_style
))

# Publication
story.append(Paragraph("PUBLICATION", section_style))
story.append(HRFlowable(width="100%", thickness=0.5, color=SECTION_COLOR, spaceAfter=8))
story.append(Paragraph(
    'C. H. Conley, W. Goode. "An approach to annihilators in the context of vector field Lie algebras." '
    '<i>Expositiones Mathematicae</i> (2024). arXiv:2403.01728',
    body_style
))

# Build PDF
pdf.build(story)

print(f"✓ Resume generated: {OUTPUT_FILE}")

