---
layout: page
title: Rust
permalink: /notizen/rust/
---

<p class="pill">Notes · Systems · Memory Safety</p>

Rust is a systems programming language focused on safety and performance. No garbage collector, no null, no data races.

### Why Rust?

- Memory safety without garbage collection
- Zero-cost abstractions
- Compiler catches bugs at compile time
- Great tooling (cargo, rustfmt, clippy)

### Ownership

Every value has exactly one owner. When the owner goes out of scope, the value is dropped.

```rust
fn main() {
    let s1 = String::from("hello");  // s1 owns the string
    let s2 = s1;                      // ownership moves to s2
    // println!("{}", s1);            // ERROR: s1 no longer valid

    let s3 = s2.clone();              // explicit copy
    println!("{} {}", s2, s3);        // both valid
}
```

### Borrowing

References let you use values without taking ownership.

```rust
fn main() {
    let s = String::from("hello");

    // Immutable borrow - can have multiple
    let len = calculate_length(&s);
    println!("{} has length {}", s, len);

    // Mutable borrow - only one at a time
    let mut s2 = String::from("hello");
    change(&mut s2);
}

fn calculate_length(s: &String) -> usize {
    s.len()
}

fn change(s: &mut String) {
    s.push_str(" world");
}
```

### Structs and impl

```rust
struct User {
    name: String,
    email: String,
    active: bool,
}

impl User {
    // Constructor
    fn new(name: String, email: String) -> Self {
        Self {
            name,
            email,
            active: true,
        }
    }

    // Method
    fn greeting(&self) -> String {
        format!("Hello, {}!", self.name)
    }

    // Mutable method
    fn deactivate(&mut self) {
        self.active = false;
    }
}
```

---

## Error handling

No exceptions. Use `Result` for recoverable errors, `panic!` for unrecoverable.

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_file(path: &str) -> Result<String, io::Error> {
    let mut file = File::open(path)?;  // ? propagates error
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    Ok(contents)
}

fn main() {
    match read_file("config.txt") {
        Ok(contents) => println!("{}", contents),
        Err(e) => eprintln!("Error: {}", e),
    }

    // Or with unwrap (panics on error)
    let contents = read_file("config.txt").unwrap();

    // Or with expect (panics with message)
    let contents = read_file("config.txt")
        .expect("Failed to read config");
}
```

### Option for nullable values

```rust
fn find_user(id: u32) -> Option<String> {
    if id == 1 {
        Some(String::from("Max"))
    } else {
        None
    }
}

fn main() {
    // Pattern matching
    match find_user(1) {
        Some(name) => println!("Found: {}", name),
        None => println!("Not found"),
    }

    // Or with if let
    if let Some(name) = find_user(1) {
        println!("Found: {}", name);
    }

    // Or with unwrap_or
    let name = find_user(1).unwrap_or_else(|| String::from("Anonymous"));
}
```

---

## Common patterns

### Iterators

```rust
let numbers = vec![1, 2, 3, 4, 5];

// Map and collect
let doubled: Vec<i32> = numbers.iter().map(|x| x * 2).collect();

// Filter
let evens: Vec<&i32> = numbers.iter().filter(|x| *x % 2 == 0).collect();

// Fold (reduce)
let sum: i32 = numbers.iter().fold(0, |acc, x| acc + x);

// Chaining
let result: i32 = numbers
    .iter()
    .filter(|x| *x % 2 == 0)
    .map(|x| x * 2)
    .sum();
```

### Enums

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(u8, u8, u8),
}

fn handle_message(msg: Message) {
    match msg {
        Message::Quit => println!("Quit"),
        Message::Move { x, y } => println!("Move to {}, {}", x, y),
        Message::Write(text) => println!("Write: {}", text),
        Message::ChangeColor(r, g, b) => println!("Color: {}, {}, {}", r, g, b),
    }
}
```

---

## Cargo commands

```bash
cargo new my-project      # Create new project
cargo build               # Compile
cargo build --release     # Compile optimized
cargo run                 # Build and run
cargo test                # Run tests
cargo check               # Fast syntax check
cargo clippy              # Linter
cargo fmt                 # Format code
cargo add serde           # Add dependency
cargo doc --open          # Generate and open docs
```

### Useful crates

| Crate | Purpose |
|-------|---------|
| serde | Serialization (JSON, etc.) |
| tokio | Async runtime |
| reqwest | HTTP client |
| clap | CLI argument parsing |
| anyhow | Easy error handling |
| thiserror | Custom error types |

### Resources

- [The Rust Book](https://doc.rust-lang.org/book/)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
- [Rustlings](https://rust-lang.github.io/rustlings/)
- [Rust Cheat Sheet](https://cheats.rs/)
