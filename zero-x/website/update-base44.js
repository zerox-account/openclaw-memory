const { createClient } = require('/Users/julienuhlig/.openclaw/workspace/node_modules/@base44/sdk');

const base44 = createClient({
  apiKey: '8e72cea1a5da495b8a54016a261abbc2'
});

const ZERO_X_CONTENT = {
  projectId: '6989df145d41eebf80a51614',
  sections: [
    {
      id: 'hero',
      title: 'Transforming Waste into Clean Energy',
      subtitle: 'Zero-X Group: Advanced Modular Gasification Systems. From waste to power in a single container.',
      cta: 'Explore Technology'
    },
    {
      id: 'technology',
      title: 'X-150 Modular Gasification',
      content: 'Containerized downdraft gasification system with integrated tar reformer. 650kW thermal output, 86% efficiency. Oxy-steam process for clean syngas production.'
    },
    {
      id: 'results',
      title: 'Proven Results: Project Cométha',
      content: '1,000+ operating hours validated by Fraunhofer Institute. Paris pilot with Syctom/SIAAP. Multifuel capability: wood, sewage sludge, agricultural waste.'
    },
    {
      id: 'use-cases',
      title: 'Applications',
      cases: [
        'Data Centers - COOLSTACK',
        'Mining Operations - MINEBASE',
        'Biogas Plants - DIGEST+',
        'Food Processing - FOODPOWER',
        'Breweries - BREWPOWER'
      ]
    },
    {
      id: 'about',
      title: '20 Years of Innovation',
      content: 'From Agnion (2007) to Entrade to Zero-X (2026). Red Herring Top 100, Inc. 5000 #12. Heatpipe Reformer technology by Prof. Dr. Jürgen Karl.'
    },
    {
      id: 'contact',
      title: 'Partner With Us',
      email: 'zerox@exventure.co',
      location: 'Spinlab, Leipzig, Germany'
    }
  ]
};

async function updateWebsite() {
  try {
    console.log('Connecting to Base44...');
    
    // Update app content
    const result = await base44.apps.update(ZERO_X_CONTENT.projectId, {
      content: ZERO_X_CONTENT.sections
    });
    
    console.log('✅ Website updated successfully!');
    console.log('Project: Zero-X Labs');
    console.log('URL: https://zero-x-speed.base44.app');
    
  } catch (error) {
    console.error('❌ Error:', error.message);
    console.log('Attempting alternative method...');
    
    // Try entities approach
    try {
      const pages = await base44.entities.pages.list({
        appId: ZERO_X_CONTENT.projectId
      });
      console.log('Current pages:', pages);
    } catch (e2) {
      console.error('Alternative also failed:', e2.message);
    }
  }
}

updateWebsite();
