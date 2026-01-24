---
layout: page
title: PWAs & Service Workers
permalink: /notizen/pwa-service-workers/
---

# PWAs & Service Workers

Apps die offline funktionieren. Das Wichtigste ist der Service Worker.

Benutzt für: [Pocket Arcade](/projekte/pocket-arcade/)

Stand: Januar 2025

---

## Manifest (das Einfache)

```json
{
  "name": "My App",
  "short_name": "App",
  "start_url": "/",
  "display": "standalone",
  "icons": [
    { "src": "/icon-192.png", "sizes": "192x192" },
    { "src": "/icon-512.png", "sizes": "512x512" }
  ]
}
```

```html
<link rel="manifest" href="/manifest.json">
```

## Service Worker (das Interessante)

```javascript
// main.js - SW registrieren
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js');
}
```

```javascript
// sw.js - Basis-Setup
const CACHE = 'v1';
const ASSETS = ['/', '/index.html', '/app.js', '/styles.css'];

// Bei Install: Assets cachen
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE).then(c => c.addAll(ASSETS))
  );
});

// Bei Fetch: Cache first, dann Network
self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(cached => cached || fetch(e.request))
  );
});
```

## Caching-Strategien

**Cache First** - Schnell, für statische Assets:
```javascript
caches.match(request).then(cached => cached || fetch(request))
```

**Network First** - Frisch, für API-Calls:
```javascript
fetch(request).catch(() => caches.match(request))
```

**Stale While Revalidate** - Beides:
```javascript
// Sofort aus Cache liefern, im Hintergrund updaten
```

## Was mich überrascht hat

- SW-Updates sind tricky. Neue Version wartet bis alle Tabs zu
- `skipWaiting()` forciert Update, kann aber Probleme machen
- Debugging ist nervig, DevTools > Application > Service Workers hilft

## Damit es installierbar wird

- HTTPS (localhost geht auch)
- Manifest mit name, icons, start_url, display
- SW mit fetch handler

---

## Links

- [web.dev PWA Guide](https://web.dev/learn/pwa/)
- [Workbox](https://developer.chrome.com/docs/workbox/) – macht vieles einfacher
