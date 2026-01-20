---
layout: page
title: Tauri
permalink: /notizen/tauri/
---

<p class="pill">Notes · Desktop · Rust</p>

Tauri lets you build desktop apps with web frontends (HTML/CSS/JS) and a Rust backend. Much smaller and faster than Electron.

### Why Tauri over Electron?

| | Tauri | Electron |
|---|---|---|
| Bundle size | ~3-10 MB | ~150+ MB |
| Memory usage | Lower | Higher |
| Backend | Rust | Node.js |
| Renderer | System WebView | Bundled Chromium |

### Project setup

```bash
# Create new project
npm create tauri-app@latest

# Or add to existing web project
cd my-web-app
npm install -D @tauri-apps/cli
npm run tauri init
```

### Project structure

```
my-app/
├── src/                    # Web frontend
│   ├── index.html
│   ├── main.js
│   └── styles.css
├── src-tauri/              # Rust backend
│   ├── src/
│   │   └── main.rs
│   ├── Cargo.toml
│   └── tauri.conf.json
└── package.json
```

### Configuration

`src-tauri/tauri.conf.json`:

```json
{
  "build": {
    "beforeDevCommand": "npm run dev",
    "beforeBuildCommand": "npm run build",
    "devPath": "http://localhost:5173",
    "distDir": "../dist"
  },
  "package": {
    "productName": "My App",
    "version": "1.0.0"
  },
  "tauri": {
    "windows": [
      {
        "title": "My App",
        "width": 800,
        "height": 600,
        "resizable": true
      }
    ]
  }
}
```

---

## Calling Rust from JavaScript

### Define a command in Rust

```rust
// src-tauri/src/main.rs

#[tauri::command]
fn greet(name: &str) -> String {
    format!("Hello, {}!", name)
}

#[tauri::command]
fn calculate(a: i32, b: i32) -> i32 {
    a + b
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![greet, calculate])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

### Call from JavaScript

```javascript
import { invoke } from '@tauri-apps/api/tauri';

// Call Rust function
const greeting = await invoke('greet', { name: 'Max' });
console.log(greeting);  // "Hello, Max!"

const sum = await invoke('calculate', { a: 5, b: 3 });
console.log(sum);  // 8
```

### Async commands

```rust
#[tauri::command]
async fn fetch_data(url: String) -> Result<String, String> {
    reqwest::get(&url)
        .await
        .map_err(|e| e.to_string())?
        .text()
        .await
        .map_err(|e| e.to_string())
}
```

---

## File system access

```rust
use std::fs;
use tauri::api::path::app_data_dir;

#[tauri::command]
fn save_file(content: String, filename: String, app_handle: tauri::AppHandle) -> Result<(), String> {
    let app_dir = app_data_dir(&app_handle.config())
        .ok_or("Could not get app data dir")?;

    let path = app_dir.join(filename);
    fs::write(path, content).map_err(|e| e.to_string())
}

#[tauri::command]
fn read_file(filename: String, app_handle: tauri::AppHandle) -> Result<String, String> {
    let app_dir = app_data_dir(&app_handle.config())
        .ok_or("Could not get app data dir")?;

    let path = app_dir.join(filename);
    fs::read_to_string(path).map_err(|e| e.to_string())
}
```

---

## Events

### Send events from Rust to JS

```rust
use tauri::Manager;

#[tauri::command]
fn start_process(window: tauri::Window) {
    std::thread::spawn(move || {
        for i in 0..100 {
            window.emit("progress", i).unwrap();
            std::thread::sleep(std::time::Duration::from_millis(50));
        }
    });
}
```

```javascript
import { listen } from '@tauri-apps/api/event';

await listen('progress', (event) => {
  console.log('Progress:', event.payload);
});
```

### Development

```bash
# Run in development
npm run tauri dev

# Build for production
npm run tauri build
```

### Resources

- [Tauri Docs](https://tauri.app/v1/guides/)
- [Tauri API Reference](https://tauri.app/v1/api/js/)
- [Awesome Tauri](https://github.com/tauri-apps/awesome-tauri)
