---
layout: page
title: Svelte
permalink: /notizen/svelte/
---

# Svelte

Mein Frontend-Framework der Wahl. Weniger Boilerplate als React.

Benutzt für: [Readmeo](/projekte/readmeo/)

---

## Basics

```svelte
<script>
  let count = 0;

  // Reactive: wird neu berechnet wenn count sich ändert
  $: doubled = count * 2;

  function increment() {
    count += 1;
  }
</script>

<button on:click={increment}>
  {count} × 2 = {doubled}
</button>

<style>
  /* Scoped by default */
  button {
    padding: 1rem;
  }
</style>
```

## Props

```svelte
<!-- Child.svelte -->
<script>
  export let name;
  export let count = 0;  // mit Default
</script>

<!-- Parent.svelte -->
<Child name="Max" count={5} />
```

## Stores

Global state:

```javascript
// stores.js
import { writable } from 'svelte/store';

export const user = writable(null);
export const theme = writable('dark');
```

```svelte
<script>
  import { user } from './stores.js';

  // $ prefix = auto-subscribe
  $: console.log($user);
</script>

{#if $user}
  <p>Hi {$user.name}</p>
{/if}
```

## Each & If

```svelte
{#each items as item, index (item.id)}
  <li>{index}: {item.name}</li>
{/each}

{#if loading}
  <p>Loading...</p>
{:else if error}
  <p>Error: {error}</p>
{:else}
  <p>Done!</p>
{/if}
```

---

## Svelte 5 (Runes)

Neu seit Ende 2024. Anderes Reactivity-System:

```svelte
<script>
  let count = $state(0);           // statt let count = 0
  let doubled = $derived(count * 2); // statt $: doubled = ...
</script>
```

Hab ich in Readmeo benutzt. Gewöhnungsbedürftig aber macht Sinn.

---

## Links

- [Svelte Tutorial](https://learn.svelte.dev/) – interaktiv, sehr gut
- [Svelte 5 Docs](https://svelte.dev/docs/svelte/overview)
