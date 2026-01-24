---
layout: page
title: tauri
permalink: /notes/tauri/
---

# tauri

desktop apps with web frontend and rust backend.

used in: [readmeo](/projects/readmeo/)

---

## why tauri over electron?

- **smaller:** ~5MB vs ~150MB
- **faster:** rust backend instead of node
- **more secure:** no node.js in the bundle

downside: need to learn rust if you want backend logic.

## setup

```bash
# new project with svelte
npm create tauri-app@latest
# → select svelte

# dev
npm run tauri dev

# build
npm run tauri build
```

## project structure

```
my-app/
├── src/              # frontend (svelte/react/vue)
├── src-tauri/        # rust backend
│   ├── src/
│   │   └── main.rs
│   ├── Cargo.toml
│   └── tauri.conf.json
└── package.json
```

## frontend ↔ backend communication

**rust side (define command):**

```rust
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

**frontend side (call command):**

```javascript
import { invoke } from '@tauri-apps/api/core';

const greeting = await invoke('greet', { name: 'Max' });
// → "Hello, Max!"
```

---

## links

- [tauri docs](https://v2.tauri.app/)
- [tauri + svelte guide](https://v2.tauri.app/start/frontend/svelte/)
