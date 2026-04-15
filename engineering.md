---
layout: page
title: Engineering
permalink: /engineering/
---

## Current Work

**Backend Engineer**, Scaylor AI (August 2025 - Present)

I develop cloud infrastructure, data pipelines, and AI-powered services for a business intelligence platform. Work includes:

- Design and manage multi-tenant cloud infrastructure on GCP using Terraform, including IAM, encryption, networking, and scheduled workloads
- Build and operate data pipelines following medallion architecture (bronze/silver/gold) with BigQuery, PySpark, and CI/CD promotion across dev/staging/prod
- Develop LLM-powered query services with ontology-based data access, semantic layers, evaluation harnesses, and usage tracking
- Ship full-stack platforms — FastAPI backends with graph data modeling, React frontends with interactive visualization, and secure code execution sandboxes
- Implement multi-source data ingestion from POS systems, ERP platforms, and third-party APIs with checkpoint resumption and cross-source entity resolution
- Design authentication and authorization systems including OAuth, Workload Identity Federation, and multi-layer service-to-service security
- Build automated data lineage generation and data quality frameworks

---

## Previous Positions

- **Software Engineer**, Concan Consulting Corporation (April - June 2025)
- **Senior Lecturer**, Vanderbilt University (2023-2024)
- **Graduate Teaching Fellow**, University of North Texas (2017-2023)

---

## Technical Skills

<div class="skills-list">
  {% for skill_category in site.data.cv.skills %}
    <div class="skill-category">
      <h3>{{ skill_category.category }}</h3>
      <ul>
        {% for skill in skill_category.items %}
          <li>{{ skill }}</li>
        {% endfor %}
      </ul>
    </div>
  {% endfor %}
</div>


