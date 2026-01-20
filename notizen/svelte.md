---
layout: page
title: Svelte
permalink: /notizen/svelte/
---

<p class="pill">Notes · Frontend · JavaScript</p>

Svelte is a frontend framework that compiles to vanilla JavaScript at build time. No virtual DOM, just efficient code.

### Why Svelte?

- No runtime library shipped to browser
- Less boilerplate than React/Vue
- True reactivity without hooks
- Scoped CSS by default
- Great performance

### Project setup

```bash
# Create new project with SvelteKit
npm create svelte@latest my-app
cd my-app
npm install
npm run dev
```

---

## Components

### Basic component

```svelte
<!-- Button.svelte -->
<script>
  export let text = "Click me";
  let count = 0;

  function handleClick() {
    count += 1;
  }
</script>

<button on:click={handleClick}>
  {text}: {count}
</button>

<style>
  button {
    background: #4a90d9;
    color: white;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 4px;
  }
</style>
```

### Using components

```svelte
<script>
  import Button from './Button.svelte';
</script>

<Button text="Counter" />
```

---

## Reactivity

Variables are reactive by default:

```svelte
<script>
  let count = 0;

  // Reactive statement - runs when dependencies change
  $: doubled = count * 2;

  // Reactive block
  $: {
    console.log('count changed to', count);
  }

  // Reactive if
  $: if (count > 10) {
    alert('Count is high!');
  }
</script>

<button on:click={() => count++}>
  Count: {count}, Doubled: {doubled}
</button>
```

### Arrays and objects

```svelte
<script>
  let items = ['a', 'b', 'c'];

  function addItem() {
    // Must reassign for reactivity
    items = [...items, 'd'];
    // or
    items.push('d');
    items = items;
  }
</script>
```

---

## Logic

### Conditionals

```svelte
{#if condition}
  <p>True</p>
{:else if otherCondition}
  <p>Other</p>
{:else}
  <p>False</p>
{/if}
```

### Loops

```svelte
<script>
  let items = [
    { id: 1, name: 'Apple' },
    { id: 2, name: 'Banana' }
  ];
</script>

<ul>
  {#each items as item (item.id)}
    <li>{item.name}</li>
  {/each}
</ul>

<!-- With index -->
{#each items as item, index}
  <li>{index}: {item.name}</li>
{/each}
```

### Await

```svelte
{#await fetchData()}
  <p>Loading...</p>
{:then data}
  <p>{data}</p>
{:catch error}
  <p>Error: {error.message}</p>
{/await}
```

---

## Props and events

### Props

```svelte
<!-- Child.svelte -->
<script>
  export let name;
  export let age = 18;  // default value
</script>

<p>{name} is {age}</p>

<!-- Parent.svelte -->
<Child name="Max" age={25} />
```

### Events

```svelte
<!-- Child.svelte -->
<script>
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();

  function handleClick() {
    dispatch('message', { text: 'Hello!' });
  }
</script>

<button on:click={handleClick}>Send</button>

<!-- Parent.svelte -->
<Child on:message={(e) => console.log(e.detail.text)} />
```

---

## Bindings

```svelte
<script>
  let name = '';
  let selected = 'a';
  let checked = false;
</script>

<!-- Two-way binding -->
<input bind:value={name} />

<select bind:value={selected}>
  <option value="a">A</option>
  <option value="b">B</option>
</select>

<input type="checkbox" bind:checked />
```

---

## Stores

Share state between components:

```javascript
// stores.js
import { writable, derived } from 'svelte/store';

export const count = writable(0);

export const doubled = derived(count, $count => $count * 2);
```

```svelte
<script>
  import { count, doubled } from './stores.js';
</script>

<!-- Auto-subscribe with $ prefix -->
<p>Count: {$count}, Doubled: {$doubled}</p>

<button on:click={() => $count++}>Add</button>

<!-- Or manually -->
<button on:click={() => count.update(n => n + 1)}>Add</button>
```

---

## Lifecycle

```svelte
<script>
  import { onMount, onDestroy, beforeUpdate, afterUpdate } from 'svelte';

  onMount(() => {
    console.log('Component mounted');
    return () => console.log('Cleanup on unmount');
  });

  onDestroy(() => {
    console.log('Component destroyed');
  });
</script>
```

### Resources

- [Svelte Docs](https://svelte.dev/docs)
- [Svelte Tutorial](https://svelte.dev/tutorial)
- [SvelteKit Docs](https://kit.svelte.dev/docs)
- [Svelte REPL](https://svelte.dev/repl) - Try in browser
