const { createClient } = require('/Users/julienuhlig/.openclaw/workspace/node_modules/@base44/sdk');

const base44 = createClient({
  apiKey: '8e72cea1a5da495b8a54016a261abbc2'
});

async function listApps() {
  try {
    console.log('Fetching available apps...');
    
    // Try to list all apps
    const apps = await base44.apps.list();
    console.log('Available apps:', JSON.stringify(apps, null, 2));
    
  } catch (error) {
    console.error('Error listing apps:', error.message);
    
    // Try alternative approach
    try {
      console.log('\nTrying to access specific app...');
      const app = await base44.apps.get('6989df145d41eebf80a51614');
      console.log('App found:', JSON.stringify(app, null, 2));
    } catch (e2) {
      console.error('Cannot access app:', e2.message);
    }
  }
}

listApps();
