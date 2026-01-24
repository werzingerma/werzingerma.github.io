---
layout: page
title: svelte
permalink: /notes/svelte/
---

# svelte

my go-to frontend framework. less boilerplate than react.

used in: [readmeo](/projects/readmeo/)

---

## basics

```svelte
<script>
  let count = 0;

  // reactive: recalculates when count changes
  $: doubled = count * 2;

  function increment() {
    count += 1;
  }
</script>

<button on:click={increment}>
  {count} × 2 = {doubled}
</button>

<style>
  /* scoped by default */
  button {
    padding: 1rem;
  }
</style>
```

## props

```svelte
<!-- Child.svelte -->
<script>
  export let name;
  export let count = 0;  // with default
</script>

<!-- Parent.svelte -->
<Child name="Max" count={5} />
```

## stores

global state:

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

## each & if

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

## svelte 5 (runes)

new since late 2024. different reactivity system:

```svelte
<script>
  let count = $state(0);           // instead of let count = 0
  let doubled = $derived(count * 2); // instead of $: doubled = ...
</script>
```

used this in readmeo. takes getting used to but makes sense.

---

## links

- [svelte tutorial](https://learn.svelte.dev/) – interactive, very good
- [svelte 5 docs](https://svelte.dev/docs/svelte/overview)
