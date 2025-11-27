# Weekly Update Workflow

## Overview

This document describes the fully automated workflow for keeping your portfolio website, resume, and CV synchronized with your work across all repositories.

## Your Weekly Responsibility

**One simple task**: Come to this repository and ask the AI assistant to review work from other repositories.

That's it. Everything else is automated.

## What Happens Automatically

### 1. AI Assistant Reviews Work

When you ask, the AI will:
- Review commits from ScaylorAI repositories for the week
- Review progress reports from ScaylorAI repositories
- Review completed Linear tickets (assigned to Will)
- Extract accomplishments and major features

### 2. Journal Update

The AI will:
- Add a new week entry to `journal/20250811-current.md`
- Include all significant accomplishments from the week
- Focus on major features and infrastructure work

### 3. You Commit

When you commit the journal update:
```bash
git add journal/20250811-current.md
git commit -m "Update journal for Week X"
```

### 4. Pre-commit Hook Runs Automatically

The pre-commit hook detects journal changes and automatically:

1. **Parses Journal** → Extracts all accomplishments
2. **Generates Resume Bullets** → Uses Gemini API to create 4 high-impact bullets
3. **Updates cv.yml** → Writes bullets to Scaylor highlights (synced with website)
4. **Generates Resume PDF** → Creates updated PDF using cv.yml data
5. **Stages Files** → Adds `cv.yml` and resume PDF to commit

### 5. GitHub Actions (On Push)

When you push to `main`:
- Resume is regenerated in CI/CD
- Website is built with updated content
- Everything deploys automatically

## Complete Workflow

```
You: "Review work from other repos for last week"
    ↓
AI: Reviews commits, progress reports, Linear tickets
    ↓
AI: Updates journal/20250811-current.md
    ↓
You: git commit
    ↓
Pre-commit Hook (automatic):
  ├─→ Parse journal
  ├─→ Generate 4 resume bullets (Gemini API)
  ├─→ Update _data/cv.yml Scaylor highlights
  ├─→ Generate resume PDF
  └─→ Stage cv.yml and PDF
    ↓
You: git push
    ↓
GitHub Actions (automatic):
  ├─→ Regenerate resume
  ├─→ Build website
  └─→ Deploy to GitHub Pages
```

## What Gets Updated

### Journal (`journal/20250811-current.md`)
- Weekly entries with accomplishments
- Updated by AI when you ask

### CV Data (`_data/cv.yml`)
- **Scaylor highlights**: Auto-updated with 4 bullets from journal
- **Technical skills**: Already synced (resume reads from cv.yml)
- **Other experience**: Manual updates (past positions)

### Resume PDF (`assets/resumes/William_Goode_Resume_Professional.pdf`)
- Scaylor bullets: First 4 from `cv.yml`
- Technical skills: From `cv.yml`
- Past positions: Title/date only
- Auto-generated on commit

### Website
- CV page: Shows all data from `cv.yml`
- Engineering page: Shows skills from `cv.yml`
- Auto-updated when `cv.yml` changes

## File Sync Status

| Content | Resume PDF | Website | Auto-Updated? |
|---------|------------|---------|---------------|
| **Scaylor Experience** | 4 bullets | Up to 8 bullets | ✅ Yes (from journal) |
| **Past Experience** | Title only | Full details | ❌ Manual |
| **Technical Skills** | 4 categories | All 5 categories | ❌ Manual (but synced) |
| **Education** | Hardcoded | From cv.yml | ❌ Manual |

## Requirements

- `.env` file with `GEMINI_API_KEY` (for resume bullet generation)
- Python dependencies installed (`google-generativeai`, `reportlab`, `python-dotenv`, `pyyaml`)
- Pre-commit hook enabled (already set up)

## Manual Updates Still Needed

While most things are automated, you may still want to manually update:
- **Past experience highlights** in `cv.yml` (for website display)
- **Technical skills** in `cv.yml` (when you learn new technologies)
- **Education** details in `cv.yml` (if needed)
- **Additional Scaylor bullets** in `cv.yml` (up to 4 more for website, beyond the 4 auto-generated)

## Troubleshooting

**Resume not updating?**
- Check `.env` file has `GEMINI_API_KEY`
- Verify Python dependencies installed
- Check pre-commit hook is executable: `chmod +x .git/hooks/pre-commit`

**cv.yml not updating?**
- Pre-commit hook should update it automatically
- Check Gemini API key is set
- Verify `generate_resume_bullets.py` runs successfully

**Website not showing updates?**
- GitHub Actions builds on push
- Check Actions tab for build status
- Verify `cv.yml` changes were committed

