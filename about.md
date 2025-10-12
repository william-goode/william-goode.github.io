---
layout: page
title: About
permalink: /about/
---

I began at UNT as a classical performance major playing trombone before transitioning to mathematics and economics. I completed my Ph.D. in Mathematics in 2023, studying representations of infinite-dimensional Lie algebras and superalgebras. I now work as a backend engineer, developing data infrastructure for AI-powered business intelligence.

---

## Education

**Ph.D. in Mathematics**, University of North Texas, 2023  
Dissertation: *Annihilators of irreducible representations of the Lie superalgebra of contact vector fields on the superline*  
Advisor: Charles H. Conley  
GPA: 4.0

**B.S. in Mathematics**, University of North Texas, 2017  
**B.S. in Economics**, University of North Texas, 2017  
GPA: 3.79, Cum Laude

---

## Research

My research focuses on representations of infinite-dimensional Lie algebras and superalgebras of vector fields. I develop methods for describing annihilators of modules under conditions that arise in tensor modules of vector field Lie algebras.

**Publications:**
- C. H. Conley, W. Goode. "An approach to annihilators in the context of vector field Lie algebras." *Expositiones Mathematicae* (2024). [arXiv:2403.01728](https://arxiv.org/abs/2403.01728)

**Presentations:**
- Joint Mathematics Meeting, Boston (2023)
- Graduate Algebra Symposium, UT Arlington (2022)
- Southwest Local Algebra Meeting, Baylor University (2022)
- University of North Texas Algebra Seminar (2021-2022)

---

## Current Work

**Backend Engineer**, Scaylor AI (August 2025 - Present)

I develop cloud infrastructure and data pipelines for an AI-powered business intelligence platform. Work includes:

- Architect data ingestion systems for client database integration
- Develop microservices for SQL generation and query execution
- Design data workflows compliant with GDPR requirements
- Manage security and access provisioning
- Serve as technical point of contact for client onboarding

**Previous Positions:**
- Software Engineer, Concan Consulting Corporation (April - June 2025)
- Senior Lecturer, Vanderbilt University (2023-2024)
- Graduate Teaching Fellow, University of North Texas (2017-2023)

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

---

## Contact

**Email**: [{{ site.author.email }}](mailto:{{ site.author.email }})  
**GitHub**: [github.com/william-goode](https://github.com/william-goode)  
**LinkedIn**: [linkedin.com/in/william-goode](https://linkedin.com/in/william-goode)

