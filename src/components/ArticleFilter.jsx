import React, { useState, useEffect } from 'react';

const ArticleFilter = ({ articles }) => {
  const [filter, setFilter] = useState('all');
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredArticles, setFilteredArticles] = useState(articles);

  // Extract unique tags from articles
  const allTags = [...new Set(articles.flatMap(article => article.tags || []))];

  useEffect(() => {
    let result = articles;

    // Filter by tag
    if (filter !== 'all') {
      result = result.filter(article => 
        article.tags && article.tags.includes(filter)
      );
    }

    // Filter by search term
    if (searchTerm) {
      result = result.filter(article =>
        article.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
        (article.excerpt && article.excerpt.toLowerCase().includes(searchTerm.toLowerCase()))
      );
    }

    setFilteredArticles(result);
  }, [filter, searchTerm, articles]);

  return (
    <div className="article-filter">
      <div className="filter-controls">
        <div className="search-box">
          <input
            type="text"
            placeholder="Search articles..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="search-input"
          />
        </div>
        
        <div className="tag-filters">
          <button
            className={`tag-button ${filter === 'all' ? 'active' : ''}`}
            onClick={() => setFilter('all')}
          >
            All
          </button>
          {allTags.map(tag => (
            <button
              key={tag}
              className={`tag-button ${filter === tag ? 'active' : ''}`}
              onClick={() => setFilter(tag)}
            >
              {tag}
            </button>
          ))}
        </div>
      </div>

      <div className="articles-list">
        {filteredArticles.length === 0 ? (
          <p className="no-results">No articles found.</p>
        ) : (
          filteredArticles.map(article => (
            <article key={article.url} className="article-card">
              <time className="article-date">{article.date}</time>
              <h3 className="article-title">
                <a href={article.url}>{article.title}</a>
              </h3>
              {article.excerpt && (
                <p className="article-excerpt">{article.excerpt}</p>
              )}
              {article.tags && article.tags.length > 0 && (
                <div className="article-tags">
                  {article.tags.map(tag => (
                    <span key={tag} className="tag">{tag}</span>
                  ))}
                </div>
              )}
            </article>
          ))
        )}
      </div>
    </div>
  );
};

export default ArticleFilter;

