# Resume Generation Workflow

This directory contains scripts for automatically generating resume bullets from weekly journal entries using LLM processing.

## Workflow Overview

1. **Parse Journal** → Extract all accomplishments from weekly journal entries
2. **Generate Summaries** → Create plain text file (no dates) for LLM processing
3. **LLM Processing** → Use Gemini API to condense into 4 high-impact resume bullets
4. **Update cv.yml** → Write bullets to `_data/cv.yml` Scaylor highlights (synced with website)
5. **Generate Resume** → Create PDF reading first 4 bullets from `cv.yml`

## Setup

### 1. Install Dependencies

```bash
pip install google-generativeai reportlab python-dotenv
```

Note: `python-dotenv` is already installed, but `google-generativeai` may need to be installed.

### 2. Set Gemini API Key

Add your Gemini API key to the `.env` file in the repository root:

```bash
echo "GEMINI_API_KEY=your-api-key-here" >> .env
```

The script will automatically load the key from `.env`.

## Usage

### Step 1: Parse Journal Entries

Extract all accomplishments from the journal:

```bash
cd assets/resumes
python3 parse_journal.py
```

This creates `journal_summaries.txt` with all bullet points (no dates).

### Step 2: Generate Resume Bullets

Use Gemini API to condense into 4 high-impact bullets:

```bash
python3 generate_resume_bullets.py
```

This:
- Generates 4 resume bullets focused on major features
- Updates `_data/cv.yml` Scaylor highlights with these bullets
- Creates `resume_bullets.json` (for backwards compatibility)

**Note**: You can manually add up to 4 more bullets in `cv.yml` Scaylor highlights for website display (website shows up to 8 bullets total).

### Step 3: Generate Resume PDF

Generate the final resume PDF:

```bash
python3 generate_resume.py
```

This creates `William_Goode_Resume_Professional.pdf` using:
- **Scaylor AI**: First 4 bullets from `cv.yml` highlights
- **Past positions**: Title and date only (no bullets)

## Files

- `parse_journal.py` - Extracts accomplishments from journal entries
- `generate_resume_bullets.py` - Uses Gemini API to generate 4 resume bullets
- `generate_resume.py` - Generates PDF resume with dynamic bullets
- `journal_summaries.txt` - Intermediate file with all accomplishments (generated)
- `resume_bullets.json` - Final 4 resume bullets (generated)

## Resume Structure

- **Education** - Ph.D. and B.S. degrees
- **Technical Skills** - Languages, cloud, backend, data engineering
- **Experience**:
  - **Scaylor AI** - 4 bullets from `cv.yml` (synced with website)
  - **Concan Consulting** - Title only (no bullets)
  - **Vanderbilt University** - Title only (no bullets)
- **Publication** - Research publication

**Note**: Projects section has been removed to make room for professional accomplishments.

## Content Sync

**Resume PDF**:
- Scaylor bullets: First 4 from `cv.yml` highlights
- Past positions: Title/date only

**Website CV Page**:
- Scaylor bullets: All highlights from `cv.yml` (up to 8 bullets)
- Past positions: Full details from `cv.yml` (all highlights)

**Single Source of Truth**: `_data/cv.yml` Scaylor highlights are synced between resume and website.

## Updating Resume

When you update the journal with new weekly entries:

1. Run `parse_journal.py` to extract new accomplishments
2. Run `generate_resume_bullets.py` to regenerate bullets (includes all weeks)
3. Run `generate_resume.py` to generate updated PDF

The LLM will automatically prioritize major features and infrastructure work across all weeks.

## Automatic Resume Generation on Commit

The resume is automatically regenerated on commit via:

### Local Pre-commit Hook

A Git pre-commit hook automatically regenerates the resume PDF when:
- Journal entries are modified
- Resume scripts are modified
- Resume PDF is being committed

The hook runs before each commit and automatically adds the updated PDF to the commit.

### GitHub Actions

The resume is also regenerated in CI/CD on every push to `main`:

1. Journal is parsed
2. Resume bullets are generated using Gemini API
3. Resume PDF is generated
4. PDF is included in the Jekyll build

**Setup for GitHub Actions:**

1. Add `GEMINI_API_KEY` as a GitHub secret:
   - Go to repository Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Name: `GEMINI_API_KEY`
   - Value: Your Gemini API key

2. The workflow will automatically use this secret to generate resume bullets.

**Note:** If the API key is not set in GitHub Actions, the resume will use fallback bullets.

