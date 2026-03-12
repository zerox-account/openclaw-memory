// Dashboard.jsx - Zero-X Control Center
// Minimalist, Fast Money Focus

import React, { useState, useEffect } from 'react';
import './Dashboard.css';

const Dashboard = () => {
  const [activeTab, setActiveTab] = useState('fast-money');
  
  // Fast Money Opportunities
  const fastMoneyOpps = [
    {
      id: 1,
      name: "Golden Foods Uganda",
      type: "PPA",
      value: "€2.4M",
      timeline: "30 days",
      probability: "85%",
      status: "LOI signed",
      action: "Finalize financing",
      urgency: "HIGH"
    },
    {
      id: 2,
      name: "DBFZ Consortium",
      type: "Grant",
      value: "€500K-2M",
      timeline: "90 days",
      probability: "70%",
      status: "Meeting done",
      action: "Submit Horizon Europe",
      urgency: "HIGH"
    },
    {
      id: 3,
      name: "Data Center COOLSTACK",
      type: "PPA",
      value: "€8.5M",
      timeline: "60 days",
      probability: "60%",
      status: "Proposal sent",
      action: "Technical demo",
      urgency: "MEDIUM"
    },
    {
      id: 4,
      name: "Klärschlamm Deutschland",
      type: "Service",
      value: "€1.2M/year",
      timeline: "45 days",
      probability: "75%",
      status: "Research phase",
      action: "Pilot offer",
      urgency: "MEDIUM"
    }
  ];

  // Active Pipeline
  const pipeline = {
    contacted: 53,
    responses: 9,
    meetings: 3,
    proposals: 4,
    closing: 2
  };

  // Daily Actions
  const todayActions = [
    { task: "DBFZ Summary senden", done: false, time: "10 min" },
    { task: "Schildhauer (PSI) antworten", done: false, time: "15 min" },
    { task: "Golden Foods financing call", done: false, time: "30 min" },
    { task: "Neom follow-up email", done: false, time: "10 min" },
    { task: "Ledendecker Zoom terminieren", done: false, time: "5 min" }
  ];

  // Metrics
  const metrics = {
    emailsSent: 53,
    responses: 9,
    meetings: 3,
    pipelineValue: "€12.1M",
    probability: "68%"
  };

  return (
    <div className="dashboard">
      {/* Header */}
      <header className="header">
        <h1>ZERO-X CONTROL CENTER</h1>
        <div className="date">{new Date().toLocaleDateString('de-DE')}</div>
      </header>

      {/* Navigation */}
      <nav className="nav">
        <button 
          className={activeTab === 'fast-money' ? 'active' : ''}
          onClick={() => setActiveTab('fast-money')}
        >
          💰 FAST MONEY
        </button>
        <button 
          className={activeTab === 'pipeline' ? 'active' : ''}
          onClick={() => setActiveTab('pipeline')}
        >
          📊 PIPELINE
        </button>
        <button 
          className={activeTab === 'actions' ? 'active' : ''}
          onClick={() => setActiveTab('actions')}
        >
          ✅ ACTIONS
        </button>
      </nav>

      {/* Main Content */}
      <main className="main">
        
        {/* FAST MONEY TAB */}
        {activeTab === 'fast-money' && (
          <div className="tab-content">
            <h2>🚀 FAST MONEY OPPORTUNITIES</h2>
            <div className="opportunities">
              {fastMoneyOpps.map(opp => (
                <div key={opp.id} className={`opp-card urgency-${opp.urgency.toLowerCase()}`}>
                  <div className="opp-header">
                    <h3>{opp.name}</h3>
                    <span className={`badge urgency-${opp.urgency.toLowerCase()}`}>
                      {opp.urgency}
                    </span>
                  </div>
                  <div className="opp-details">
                    <div className="detail">
                      <label>Value:</label>
                      <span className="value">{opp.value}</span>
                    </div>
                    <div className="detail">
                      <label>Timeline:</label>
                      <span>{opp.timeline}</span>
                    </div>
                    <div className="detail">
                      <label>Probability:</label>
                      <span className="probability">{opp.probability}</span>
                    </div>
                    <div className="detail">
                      <label>Status:</label>
                      <span>{opp.status}</span>
                    </div>
                  </div>
                  <div className="opp-action">
                    <button className="action-btn">
                      {opp.action} →
                    </button>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* PIPELINE TAB */}
        {activeTab === 'pipeline' && (
          <div className="tab-content">
            <h2>📈 RESEARCH OUTREACH PIPELINE</h2>
            <div className="metrics-grid">
              <div className="metric-card">
                <div className="metric-number">{metrics.emailsSent}</div>
                <div className="metric-label">Contacted</div>
              </div>
              <div className="metric-card">
                <div className="metric-number">{metrics.responses}</div>
                <div className="metric-label">Responses</div>
              </div>
              <div className="metric-card">
                <div className="metric-number">{metrics.meetings}</div>
                <div className="metric-label">Meetings</div>
              </div>
              <div className="metric-card highlight">
                <div className="metric-number">{metrics.pipelineValue}</div>
                <div className="metric-label">Pipeline Value</div>
              </div>
            </div>
            
            <div className="funnel">
              <h3>Conversion Funnel</h3>
              <div className="funnel-bar">
                <div className="stage" style={{width: '100%'}}>
                  Contacted: {pipeline.contacted}
                </div>
              </div>
              <div className="funnel-bar">
                <div className="stage" style={{width: '85%'}}>
                  Responses: {pipeline.responses}
                </div>
              </div>
              <div className="funnel-bar">
                <div className="stage" style={{width: '60%'}}>
                  Meetings: {pipeline.meetings}
                </div>
              </div>
              <div className="funnel-bar">
                <div className="stage" style={{width: '40%'}}>
                  Proposals: {pipeline.proposals}
                </div>
              </div>
              <div className="funnel-bar">
                <div className="stage closing" style={{width: '20%'}}>
                  Closing: {pipeline.closing}
                </div>
              </div>
            </div>
          </div>
        )}

        {/* ACTIONS TAB */}
        {activeTab === 'actions' && (
          <div className="tab-content">
            <h2>⚡ TODAY'S ACTIONS</h2>
            <div className="actions-list">
              {todayActions.map((action, idx) => (
                <div key={idx} className={`action-item ${action.done ? 'done' : ''}`}>
                  <input 
                    type="checkbox" 
                    checked={action.done}
                    onChange={() => {}}
                  />
                  <span className="action-text">{action.task}</span>
                  <span className="action-time">{action.time}</span>
                </div>
              ))}
            </div>
            
            <div className="progress">
              <h3>Progress</h3>
              <div className="progress-bar">
                <div 
                  className="progress-fill" 
                  style={{width: '0%'}}
                ></div>
              </div>
              <p>0/5 completed today</p>
            </div>
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="footer">
        <div className="status">
          <span className="indicator active"></span>
          System Active | 11 Email Checks Running
        </div>
        <div className="version">
          Zero-X Global Control Center v1.0
        </div>
      </footer>
    </div>
  );
};

export default Dashboard;
