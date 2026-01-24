---
layout: page
title: Rust
permalink: /notizen/rust/
---

# Rust

Lerne ich gerade. Memory safety ohne Garbage Collector, aber der Compiler ist streng.

Stand: Januar 2025

---

## Das hab ich verstanden

### Ownership

Jeder Wert hat genau einen Owner. Geht der aus dem Scope, wird der Wert gedroppt.

```rust
let s1 = String::from("hello");
let s2 = s1;        // s1 ist jetzt ungültig!
// println!("{}", s1);  // Compiler-Fehler
```

### Borrowing

Referenzen um Werte zu nutzen ohne Ownership zu übernehmen.

```rust
fn len(s: &String) -> usize {  // immutable borrow
    s.len()
}

fn append(s: &mut String) {    // mutable borrow
    s.push_str(" world");
}
```

Regel: Entweder viele immutable ODER ein mutable Borrow. Nicht beides.

### Error Handling

Kein try/catch. `Result` für Fehler, `Option` für "kann leer sein".

```rust
fn read_file(path: &str) -> Result<String, io::Error> {
    let mut file = File::open(path)?;  // ? propagiert Fehler
    let mut s = String::new();
    file.read_to_string(&mut s)?;
    Ok(s)
}

match read_file("config.txt") {
    Ok(content) => println!("{}", content),
    Err(e) => eprintln!("Error: {}", e),
}
```

## Cargo Commands

```bash
cargo new projekt     # Neues Projekt
cargo run             # Kompilieren und starten
cargo build --release # Optimiert kompilieren
cargo test            # Tests laufen lassen
cargo clippy          # Linter
```

---

## Das versteh ich noch nicht ganz

- [ ] Lifetimes (`'a`) – wann brauch ich die explizit?
- [ ] Traits – wie Interfaces, aber wann `impl Trait` vs `dyn Trait`?
- [ ] Async/Await – tokio vs async-std?
- [ ] Smart Pointers – `Box`, `Rc`, `Arc`, `RefCell` – wann was?

## Was mich nervt

- Compile-Zeiten sind lang
- Manchmal kämpft man mehr mit dem Borrow Checker als mit dem Problem
- Viele Wege zum gleichen Ziel (`.iter()`, `.into_iter()`, `&vec`, ...)

## Was cool ist

- Wenn's kompiliert, läuft's meistens
- `cargo` ist besser als npm/pip/etc.
- Pattern Matching ist super

---

## Links

- [The Rust Book](https://doc.rust-lang.org/book/)
- [Rustlings](https://rust-lang.github.io/rustlings/) – Übungen
- [Rust Cheat Sheet](https://cheats.rs/)
