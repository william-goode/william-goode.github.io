# William Goode - Academic Portfolio

Academic portfolio website built with Jekyll and React. Hosted on GitHub Pages.

## Features

- Static site generation with Jekyll
- React components for interactive elements
- Catppuccin Mocha color scheme
- GitHub Pages deployment
- Responsive design

## Tech Stack

- **Jekyll**: Static site generator
- **React 18**: Interactive UI components
- **Webpack**: JavaScript bundling
- **SCSS**: Styling with variables and mixins
- **GitHub Pages**: Free hosting

## Getting Started

### Prerequisites

- Ruby (2.7 or higher)
- Node.js (16 or higher)
- Bundler
- npm

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/william-goode/william-goode.github.io.git
   cd william-goode.github.io
   ```

2. **Install Ruby dependencies**
   ```bash
   bundle install
   ```

3. **Install Node dependencies**
   ```bash
   npm install
   ```

4. **Build React components**
   ```bash
   npm run build
   ```

5. **Serve the site locally**
   ```bash
   npm run serve
   ```

The site will be available at `http://localhost:4000`

## Development Workflow

### Working on React Components

To automatically rebuild React components as you work:

```bash
npm run dev
```

This runs webpack in watch mode.

### Working on Jekyll Content

To serve the Jekyll site with live reload:

```bash
npm run jekyll:serve
```

### Full Development Experience

Run both webpack and Jekyll together:

```bash
# In terminal 1
npm run dev

# In terminal 2
npm run jekyll:serve
```

## Project Structure

```
├── _config.yml           # Jekyll configuration
├── _layouts/             # Page layouts
├── _includes/            # Reusable components (nav, footer)
├── _posts/              # Blog articles
├── _data/               # Data files (CV, etc.)
├── src/                 # React source code
│   ├── index.js
│   └── components/
│       ├── ArticleFilter.jsx
│       └── CVTimeline.jsx
├── assets/
│   ├── css/
│   │   └── main.scss    # Styles
│   └── js/
│       └── components.js  # Webpack output (generated)
├── index.html           # Home page
├── about.md             # About page
├── articles.html        # Articles archive
└── cv.html              # CV page
```

## Customization

Edit `_config.yml` for site title, author name, email, and social links.

Edit `_data/cv.yml` for education, experience, and skills.

Modify color variables in `assets/css/main.scss` to change the color scheme.

Change fonts in `_layouts/default.html` and `assets/css/main.scss`.

## Writing Articles

Create files in `_posts/` with format `YYYY-MM-DD-title.md`.

## Deployment

1. Build React components: `npm run build`
2. Commit built files: `git add assets/js/components.js && git commit -m "Build React components"`
3. Push to GitHub: `git push origin master`

GitHub Pages will build and deploy the Jekyll site automatically.

## Adding React Components

1. Create component in `src/components/YourComponent.jsx`
2. Export in `src/index.js`: `window.YourComponent = YourComponent`
3. Mount in Jekyll page using `ReactDOM.createRoot` and `React.createElement`

## Troubleshooting

### React components not showing

1. Run `npm run build`
2. Check that `assets/js/components.js` exists
3. Check browser console for JavaScript errors

### Jekyll build errors

1. Run `bundle install --path vendor/bundle`
2. Verify front matter syntax in posts
3. Check `_config.yml` is valid YAML

### Styles not loading

1. Check SCSS syntax
2. Clear browser cache
3. Verify `assets/css/main.scss` has front matter dashes (`---`)

## Technical Details

- Jekyll 3.9.5
- React 18
- Catppuccin Mocha color palette
- Fonts: Inter and Outfit from Google Fonts


