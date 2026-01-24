---
layout: page
title: pwa
permalink: /notes/pwa/
---

# progressive web apps

websites that feel like apps.

used in: [pocket-arcade](/projects/pocket-arcade/)

---

## what you need

1. **manifest.json** – app metadata
2. **service worker** – offline capability
3. **HTTPS** – required for service workers

## manifest.json

```json
{
  "name": "My App",
  "short_name": "App",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#1a1a2e",
  "theme_color": "#1a1a2e",
  "icons": [
    { "src": "/icon-192.png", "sizes": "192x192" },
    { "src": "/icon-512.png", "sizes": "512x512" }
  ]
}
```

link in HTML:
```html
<link rel="manifest" href="/manifest.json">
```

## service worker (basics)

```javascript
// sw.js
const CACHE_NAME = 'v1';
const ASSETS = ['/', '/index.html', '/style.css', '/app.js'];

// install: fill cache
self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(ASSETS))
  );
});

// fetch: serve from cache, fallback to network
self.addEventListener('fetch', (e) => {
  e.respondWith(
    caches.match(e.request)
      .then(cached => cached || fetch(e.request))
  );
});
```

register:
```javascript
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js');
}
```

## caching strategies

**cache first (static assets):**
```javascript
caches.match(request) || fetch(request)
```

**network first (api calls):**
```javascript
fetch(request).catch(() => caches.match(request))
```

## cache invalidation

change version to invalidate:

```javascript
const CACHE_NAME = 'v2';  // bump this

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(
        keys.filter(k => k !== CACHE_NAME)
            .map(k => caches.delete(k))
      )
    )
  );
});
```

## what surprised me

- SW updates are tricky – new version waits until all tabs close
- `skipWaiting()` forces update but can cause issues
- debugging is annoying, DevTools > Application helps

---

## links

- [web.dev PWA guide](https://web.dev/progressive-web-apps/)
- [workbox](https://developer.chrome.com/docs/workbox/) – makes SW easier
