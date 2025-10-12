import React, { useState } from 'react';

const CVTimeline = ({ entries }) => {
  const [expandedId, setExpandedId] = useState(null);

  const toggleExpand = (id) => {
    setExpandedId(expandedId === id ? null : id);
  };

  return (
    <div className="cv-timeline">
      {entries.map((entry, index) => (
        <div key={index} className="timeline-entry">
          <div className="timeline-marker"></div>
          <div className="timeline-content">
            <div className="timeline-header" onClick={() => toggleExpand(index)}>
              <time className="timeline-date">{entry.date}</time>
              <h3 className="timeline-title">{entry.title}</h3>
              <p className="timeline-organization">{entry.organization}</p>
            </div>
            {expandedId === index && entry.description && (
              <div className="timeline-details">
                <p>{entry.description}</p>
                {entry.highlights && (
                  <ul>
                    {entry.highlights.map((highlight, idx) => (
                      <li key={idx}>{highlight}</li>
                    ))}
                  </ul>
                )}
              </div>
            )}
          </div>
        </div>
      ))}
    </div>
  );
};

export default CVTimeline;

