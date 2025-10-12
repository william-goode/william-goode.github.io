# Website Restructure Summary

## Changes Implemented

### 1. About Page (about.md)
**Status:** ✅ Complete

Rewritten to focus on personal background and interests:
- Opening paragraph (trombone → mathematics → engineering transition)
- Education section
- Personal interests:
  - Gaming
  - Early work experience (bouncer, teaching assistant)
  - Powerlifting background (with OpenPowerlifting link)
  - Current activities: cycling and yoga (expects bike.jpg)
  - Hiking (expects fuji.jpg from Mt. Fuji)
- Contact information

### 2. Engineering Page (engineering.md)
**Status:** ✅ Complete

New page created with professional/technical content:
- Current Work at Scaylor AI
- Previous Positions
- Technical Skills (using Jekyll data from cv.yml)

### 3. Research Page (research.html)
**Status:** ✅ Complete

Renamed from articles.html:
- Added research description at top
- Listed publications
- Listed presentations
- Kept ArticleFilter React component for article filtering

**Note:** Individual blog posts remain at `/articles/YYYY/MM/DD/title/` URLs for backward compatibility, while the listing page is at `/research/`.

### 4. Navigation (_includes/nav.html)
**Status:** ✅ Complete

Updated navigation menu:
- Added "Engineering" link between "About" and "Research"
- Changed "Articles" to "Research"
- Updated active link detection

### 5. File Management
**Status:** ✅ Complete

- Deleted old articles.html
- Created assets/images/ directory for personal photos

## Pending Actions

### Images Required
The following images need to be uploaded to `/assets/images/`:
- `bike.jpg` - for cycling section in About
- `fuji.jpg` - for Mt. Fuji hiking section in About

### Testing Needed
After images are added and site is rebuilt:
1. Verify all navigation links work
2. Check that About page displays correctly with images
3. Confirm Research page shows articles and filtering works
4. Verify Engineering page displays skills correctly
5. Test that old `/articles/` post URLs still work

## URL Structure

- **Home:** `/`
- **About:** `/about/`
- **Engineering:** `/engineering/` (NEW)
- **Research:** `/research/` (renamed from /articles/)
- **Teaching:** `/teaching/`
- **Resume & CV:** `/cv/`
- **Blog Posts:** `/articles/YYYY/MM/DD/title/` (unchanged for compatibility)
