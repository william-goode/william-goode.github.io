---
layout: page
title: Engineering
permalink: /engineering/
---

## Current Work

**Backend Engineer**, Scaylor AI (August 2025 - Present)

I develop cloud infrastructure and data pipelines for an AI-powered business intelligence platform. Work includes:

- Architect data ingestion systems for client database integration
- Develop microservices for SQL generation and query execution
- Design data workflows compliant with GDPR requirements
- Manage security and access provisioning
- Serve as technical point of contact for client onboarding

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

<style>
  .skills-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin: 2rem 0;
  }
  
  .skill-category h3 {
    font-size: 1.2rem;
    margin-bottom: 1rem;
    color: #DCDDDE;
  }
  
  .skill-category ul {
    list-style: none;
    margin-left: 0;
  }
  
  .skill-category li {
    padding: 0.5rem 0;
    border-bottom: 1px solid #2C2F33;
    color: #B9BBBE;
  }
  
  .skill-category li:last-child {
    border-bottom: none;
  }
</style>

