---
layout: page
title: rust
permalink: /notes/rust/
---

# rust

learning this right now. basics + what i've understood so far.

last updated: january 2025 (still early)

---

## why rust?

- memory safety without garbage collector
- fast like C/C++
- compiler catches lots of bugs

need it for tauri backend and find the language interesting.

## ownership (the important part)

every value has exactly one owner. when owner goes out of scope, value is freed.

```rust
let s1 = String::from("hello");
let s2 = s1;  // ownership moved to s2
// println!("{}", s1);  // ERROR: s1 no longer valid

let s3 = s2.clone();  // explicit copy
println!("{} {}", s2, s3);  // both valid
```

## borrowing

with `&` borrow instead of taking ownership:

```rust
fn print_length(s: &String) {
    println!("Length: {}", s.len());
}

let s = String::from("hello");
print_length(&s);  // borrowed
println!("{}", s);  // still valid
```

rule: either N immutable borrows OR 1 mutable borrow. never both.

## error handling

no try/catch. instead `Result<T, E>`:

```rust
use std::fs::File;

// with match
let file = match File::open("data.txt") {
    Ok(f) => f,
    Err(e) => panic!("Error: {}", e),
};

// or short with ? (propagates error)
let file = File::open("data.txt")?;

// or with unwrap (panics on error)
let file = File::open("data.txt").unwrap();
```

## cargo commands

```bash
cargo new my-project    # new project
cargo build             # compile
cargo run               # compile + run
cargo test              # tests
cargo check             # fast syntax check
cargo clippy            # linter
cargo fmt               # format
```

---

## haven't figured out yet

- [ ] lifetimes (`'a`) – know it's important but haven't grokked it
- [ ] traits properly
- [ ] async/await in rust
- [ ] writing macros

## what's annoying

- compile times are long
- sometimes fighting the borrow checker more than the problem
- many ways to the same goal (`.iter()`, `.into_iter()`, `&vec`, ...)

## what's nice

- if it compiles, it usually works
- cargo is better than npm/pip/etc.
- pattern matching is great

---

## links

- [the rust book](https://doc.rust-lang.org/book/) – reading this now
- [rustlings](https://github.com/rust-lang/rustlings) – exercises
- [rust by example](https://doc.rust-lang.org/rust-by-example/)
