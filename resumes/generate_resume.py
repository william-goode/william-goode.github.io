#!/usr/bin/env python3
"""
Generate William Goode's professional resume as a PDF.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
from reportlab.lib.colors import HexColor

# Output file
OUTPUT_FILE = "William_Goode_Resume_Professional.pdf"

# Colors - subtle and professional
HEADER_COLOR = HexColor("#1e1e1e")
SECTION_COLOR = HexColor("#2a2a2a")
TEXT_COLOR = HexColor("#333333")
LINK_COLOR = HexColor("#0066cc")

# Create PDF
pdf = SimpleDocTemplate(
    OUTPUT_FILE,
    pagesize=letter,
    rightMargin=0.75*inch,
    leftMargin=0.75*inch,
    topMargin=0.6*inch,
    bottomMargin=0.6*inch,
)

# Styles
styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=20,
    textColor=HEADER_COLOR,
    spaceAfter=4,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold',
)

contact_style = ParagraphStyle(
    'Contact',
    parent=styles['Normal'],
    fontSize=10,
    textColor=TEXT_COLOR,
    alignment=TA_CENTER,
    spaceAfter=12,
)

section_style = ParagraphStyle(
    'Section',
    parent=styles['Heading2'],
    fontSize=12,
    textColor=SECTION_COLOR,
    spaceBefore=10,
    spaceAfter=6,
    fontName='Helvetica-Bold',
    borderWidth=0,
    borderPadding=0,
    borderColor=SECTION_COLOR,
    borderRadius=0,
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontSize=10,
    textColor=TEXT_COLOR,
    leading=13,
    leftIndent=0,
    spaceAfter=4,
)

bullet_style = ParagraphStyle(
    'Bullet',
    parent=styles['Normal'],
    fontSize=10,
    textColor=TEXT_COLOR,
    leading=13,
    leftIndent=20,
    bulletIndent=10,
    spaceAfter=3,
)

# Content
story = []

# Header
story.append(Paragraph("<b>WILLIAM GOODE</b>", title_style))
story.append(Paragraph(
    '<a href="mailto:william.maverick.goode@gmail.com" color="#0066cc">william.maverick.goode@gmail.com</a> | '
    '<a href="https://github.com/william-goode" color="#0066cc">github.com/william-goode</a> | '
    '<a href="https://linkedin.com/in/william-goode" color="#0066cc">linkedin.com/in/william-goode</a>',
    contact_style
))

# Education
story.append(Paragraph("<b>EDUCATION</b>", section_style))
story.append(Paragraph(
    "<b>Ph.D. in Mathematics</b> — University of North Texas — 2023",
    body_style
))
story.append(Paragraph(
    "<i>Dissertation:</i> Annihilators of irreducible representations of the Lie superalgebra of contact vector fields<br/>"
    "4.0 GPA | Published in <i>Expositiones Mathematicae</i>",
    body_style
))
story.append(Spacer(1, 6))
story.append(Paragraph(
    "<b>B.S. in Mathematics, B.S. in Economics</b> — University of North Texas — 2017<br/>"
    "3.79 GPA, Cum Laude",
    body_style
))

# Technical Skills
story.append(Paragraph("<b>TECHNICAL SKILLS</b>", section_style))
story.append(Paragraph(
    "<b>Languages:</b> Python, SQL (BigQuery, MS SQL Server, PostgreSQL), C# / .NET",
    body_style
))
story.append(Paragraph(
    "<b>Cloud &amp; Infrastructure:</b> AWS (Lambda, S3, RDS, Athena), GCP (BigQuery, Cloud Storage, Cloud Run, IAM), Docker",
    body_style
))
story.append(Paragraph(
    "<b>Backend:</b> FastAPI, ASP.NET Core, Entity Framework",
    body_style
))
story.append(Paragraph(
    "<b>Data Engineering:</b> Data pipeline development, Vector databases, DuckDB, MongoDB, Query optimization, Schema reconciliation",
    body_style
))
story.append(Paragraph(
    "<b>Machine Learning:</b> SQL generation with LLMs, ML prototyping, scikit-learn, pandas",
    body_style
))

# Experience
story.append(Paragraph("<b>EXPERIENCE</b>", section_style))

# Scaylor
story.append(Paragraph(
    "<b>Backend Engineer</b> — Scaylor AI — August 2025 – Present",
    body_style
))
bullets = [
    "Architected and deployed scalable data pipelines on AWS (Lambda, S3, RDS, Athena) and GCP (BigQuery, Cloud Run)",
    "Developed FastAPI microservices with Docker containerization for production deployment",
    "Led SQL generation service development with performance tuning for multi-tenant BigQuery architecture",
    "Implemented GDPR-compliant data workflows and IAM security provisioning",
    "Engineered database migrations (MS SQL Server → S3 → RDS) and data ingestion systems",
    "Served as technical point of contact for client integrations and onboarding",
    "Built vector database ingestion pipelines and prototype ML-based schema reconciliation",
]
for bullet in bullets:
    story.append(Paragraph(f"• {bullet}", bullet_style))
story.append(Spacer(1, 6))

# Concan
story.append(Paragraph(
    "<b>Software Engineer</b> — Concan Consulting Corporation — April – June 2025",
    body_style
))
bullets = [
    "Developed REST API in C# using ASP.NET Core and Entity Framework",
    "Consulted small e-commerce businesses on best practices",
]
for bullet in bullets:
    story.append(Paragraph(f"• {bullet}", bullet_style))
story.append(Spacer(1, 6))

# Vanderbilt
story.append(Paragraph(
    "<b>Senior Lecturer of Mathematics</b> — Vanderbilt University — August 2023 – August 2024",
    body_style
))
story.append(Paragraph(
    "• Taught calculus, statistics, and survey courses (6 courses total)",
    bullet_style
))

# Projects
story.append(Paragraph("<b>PROJECTS</b>", section_style))

story.append(Paragraph("<b>Data Pipeline Architecture</b>", body_style))
story.append(Paragraph(
    "Evaluated and implemented GCS → BigQuery pipeline from scratch. Assessed multiple approaches (AWS Athena/Glue, DuckDB, MongoDB) before selecting GCP BigQuery based on scalability and cost requirements.",
    bullet_style
))
story.append(Spacer(1, 4))

story.append(Paragraph("<b>Dynamic Data Visualization</b>", body_style))
story.append(Paragraph(
    "Created local database in Microsoft SQL Server and connected to dynamic visualization web app using Dash and Flask.",
    bullet_style
))
story.append(Spacer(1, 4))

story.append(Paragraph("<b>Containerized ML Deployment</b>", body_style))
story.append(Paragraph(
    "Deployed machine learning models on Amazon ECS as containerized web applications.",
    bullet_style
))

# Publication
story.append(Paragraph("<b>PUBLICATION</b>", section_style))
story.append(Paragraph(
    'C. H. Conley, W. Goode. "An approach to annihilators in the context of vector field Lie algebras." '
    '<i>Expositiones Mathematicae</i> (2024). arXiv:2403.01728',
    body_style
))

# Build PDF
pdf.build(story)

print(f"✓ Resume generated: {OUTPUT_FILE}")

