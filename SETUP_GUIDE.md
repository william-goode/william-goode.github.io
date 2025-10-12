# William Goode Portfolio - Setup Guide

## Overview

Academic portfolio website built with Jekyll and React.

### Components

- Jekyll static site generator
- React interactive components (ArticleFilter, CVTimeline)
- Catppuccin Mocha color scheme
- Pages: Home, About, Articles, Teaching, CV, Resume

### Project Structure

```
├── _config.yml              # Jekyll configuration
├── Gemfile                  # Ruby dependencies
├── package.json             # Node dependencies
├── webpack.config.js        # React build configuration
│
├── _layouts/                # Page templates
│   ├── default.html        # Base layout with React
│   ├── page.html           # Static pages
│   └── post.html           # Blog posts
│
├── _includes/               # Reusable components
│   ├── nav.html            # Navigation menu
│   └── footer.html         # Footer
│
├── _posts/                  # Blog articles (Markdown)
│
├── _data/                   # Data files
│   └── cv.yml              # CV content
│
├── src/                     # React source code
│   ├── index.js
│   └── components/
│       ├── ArticleFilter.jsx    # Interactive article filtering
│       └── CVTimeline.jsx       # Expandable CV timeline
│
├── assets/
│   ├── css/
│   │   └── main.scss       # Styles
│   └── js/
│       └── components.js   # Compiled React (141KB)
│
├── index.html              # Home page
├── about.md                # About page
├── articles.html           # Articles archive (with React filter)
└── cv.html                 # CV page (with React timeline)
```

## Customization

1. Edit `_config.yml` for site information
2. Update `_data/cv.yml` with education, experience, skills
3. Edit `about.md` for personal information
4. Create posts in `_posts/` with format `YYYY-MM-DD-title.md`
5. Modify color variables in `assets/css/main.scss` to change theme

## Development

Build React: `npm run build`  
Serve locally: `bundle exec jekyll serve`  
Watch mode: `npm run dev` (in one terminal), `bundle exec jekyll serve --livereload` (in another)

## Deployment

1. Build React: `npm run build`
2. Commit: `git add assets/js/components.js && git commit -m "Build React components"`
3. Push: `git push origin master`

Enable GitHub Pages in repository settings → Settings → Pages → Source: GitHub Actions.

## React Integration

Jekyll generates static HTML. React components are compiled by Webpack to `assets/js/components.js`. Jekyll pages mount React components using `ReactDOM.createRoot`.

## Troubleshooting

**React not showing**: Run `npm run build`, check `assets/js/components.js` exists, check browser console.

**Jekyll build fails**: Run `bundle install --path vendor/bundle`, verify front matter syntax, check `_config.yml`.

**Styles not loading**: Verify `assets/css/main.scss` has front matter dashes, clear cache, check syntax.

## Design

- Color palette: Catppuccin Mocha
- Typography: Outfit (headings), Inter (body)
- Responsive layout


## Support

- **Jekyll Documentation**: https://jekyllrb.com/docs/
- **React Documentation**: https://react.dev/
- **GitHub Pages**: https://docs.github.com/en/pages

---

Built with Jekyll 3.9.5, React 18, and GitHub Pages.

