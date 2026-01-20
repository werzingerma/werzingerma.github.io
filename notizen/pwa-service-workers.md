---
layout: page
title: PWAs & Service Workers
permalink: /notizen/pwa-service-workers/
---

<p class="pill">Notes · Web · Offline</p>

Progressive Web Apps can be installed on devices and work offline. The key pieces are a manifest and a service worker.

### Web App Manifest

The manifest tells the browser how to install your app:

```json
{
  "name": "My App",
  "short_name": "App",
  "description": "A description of my app",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#4a90d9",
  "icons": [
    {
      "src": "/icons/icon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/icons/icon-512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}
```

Link it in your HTML:

```html
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#4a90d9">
```

### Display modes

- `fullscreen` - No browser UI at all
- `standalone` - Looks like a native app (most common)
- `minimal-ui` - Some browser controls visible
- `browser` - Normal browser tab

---

## Service Workers

A service worker is a script that runs in the background, separate from your web page. It can intercept network requests and cache responses.

### Registering a Service Worker

```javascript
// In your main.js
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js')
      .then(reg => console.log('SW registered'))
      .catch(err => console.log('SW registration failed', err));
  });
}
```

### Basic Service Worker

```javascript
// sw.js
const CACHE_NAME = 'my-app-v1';
const ASSETS = [
  '/',
  '/index.html',
  '/styles.css',
  '/app.js',
  '/icons/icon-192.png'
];

// Install - cache assets
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(ASSETS))
      .then(() => self.skipWaiting())
  );
});

// Activate - clean old caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys
          .filter(key => key !== CACHE_NAME)
          .map(key => caches.delete(key))
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch - serve from cache, fallback to network
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(cached => cached || fetch(event.request))
  );
});
```

### Caching strategies

**Cache First** - Fast, good for static assets:

```javascript
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(cached => cached || fetch(event.request))
  );
});
```

**Network First** - Fresh data, good for API calls:

```javascript
self.addEventListener('fetch', event => {
  event.respondWith(
    fetch(event.request)
      .catch(() => caches.match(event.request))
  );
});
```

**Stale While Revalidate** - Fast and fresh:

```javascript
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.open(CACHE_NAME).then(cache => {
      return cache.match(event.request).then(cached => {
        const fetched = fetch(event.request).then(response => {
          cache.put(event.request, response.clone());
          return response;
        });
        return cached || fetched;
      });
    })
  );
});
```

### Updating the Service Worker

When you change `sw.js`, browsers detect the new version:

1. New SW installs in background
2. Old SW keeps running until all tabs closed
3. New SW activates on next visit

Force update with version in cache name:

```javascript
const CACHE_NAME = 'my-app-v2';  // Change this to force update
```

---

### Offline page

Show a custom offline page when network unavailable:

```javascript
// In install handler, also cache offline page
cache.addAll([...ASSETS, '/offline.html']);

// In fetch handler
self.addEventListener('fetch', event => {
  event.respondWith(
    fetch(event.request)
      .catch(() => {
        if (event.request.mode === 'navigate') {
          return caches.match('/offline.html');
        }
        return caches.match(event.request);
      })
  );
});
```

### PWA requirements for installation

For the install prompt to appear:
- HTTPS (or localhost)
- Valid manifest with name, icons, start_url, display
- Registered service worker with fetch handler

### Resources

- [web.dev - Learn PWA](https://web.dev/learn/pwa/)
- [Service Worker API](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)
- [Workbox](https://developer.chrome.com/docs/workbox/) - Library for easier SW development
