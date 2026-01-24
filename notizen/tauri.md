---
layout: page
title: Tauri
permalink: /notizen/tauri/
---

# Tauri

Desktop-Apps mit Web-Frontend und Rust-Backend.

Benutzt für: [Readmeo](/projekte/readmeo/)

---

## Warum Tauri statt Electron?

- **Kleiner:** ~5MB statt ~150MB
- **Schneller:** Rust Backend statt Node
- **Sicherer:** Kein Node.js im Bundle

Nachteil: Rust lernen wenn man Backend-Logik braucht.

## Setup

```bash
npm create tauri-app@latest
# → Svelte auswählen

npm run tauri dev    # Development
npm run tauri build  # Production Build
```

## Projekt-Struktur

```
my-app/
├── src/              # Frontend (Svelte/React/Vue)
├── src-tauri/        # Rust Backend
│   ├── src/
│   │   └── main.rs
│   ├── Cargo.toml
│   └── tauri.conf.json
└── package.json
```

## Frontend ↔ Backend

**Rust-Seite (Command definieren):**

```rust
// src-tauri/src/main.rs
#[tauri::command]
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![greet])
        .run(tauri::generate_context!())
        .expect("error while running");
}
```

**Frontend-Seite (Command aufrufen):**

```javascript
import { invoke } from '@tauri-apps/api/core';

const greeting = await invoke('greet', { name: 'Max' });
// → "Hello, Max!"
```

## Config

`src-tauri/tauri.conf.json`:

```json
{
  "productName": "My App",
  "version": "0.1.0",
  "build": {
    "frontendDist": "../dist"
  },
  "app": {
    "windows": [
      {
        "title": "My App",
        "width": 800,
        "height": 600
      }
    ]
  }
}
```

---

## Für Readmeo gebraucht

- File System API (Markdown speichern)
- Clipboard API (Copy to clipboard)

Alles in Tauri 2 eingebaut, muss nur in Config aktiviert werden.

---

## Links

- [Tauri Docs](https://v2.tauri.app/)
- [Tauri + Svelte Guide](https://v2.tauri.app/start/frontend/svelte/)
