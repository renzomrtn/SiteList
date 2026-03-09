<template>
  <header>
    <div class="logo">
      Web<span>Dict</span>
      <div class="logo-vol">VOL. I</div>
    </div>

    <nav>
      <a
        v-for="link in navLinks"
        :key="link.label"
        href="#"
        :class="{ active: link.label === activeNav }"
        @click.prevent="activeNav = link.label"
      >
        {{ link.label }}
      </a>
    </nav>

    <div class="header-actions">
      <button class="btn-ghost">Sign in</button>
      <button class="btn-accent">+ Add Site</button>
    </div>
  </header>
</template>

<script setup>
import { ref } from 'vue'

const navLinks = [
  { label: 'Browse' },
  { label: 'Collections' },
  { label: 'Submit' },
  { label: 'About' },
]
const activeNav = ref('Browse')
</script>

<style scoped>
header {
  background: var(--ink);
  color: var(--cream);
  padding: 0 2.5rem;
  position: sticky;
  top: 0;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 60px;
  border-bottom: 2px solid var(--accent);
}

.logo {
  font-family: 'DM Serif Display', serif;
  font-size: 1.4rem;
  letter-spacing: -0.02em;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.logo span { color: var(--accent); }

.logo-vol {
  font-family: 'DM Mono', monospace;
  font-size: 0.65rem;
  color: var(--ink-muted);
  border: 1px solid #444;
  padding: 2px 6px;
  border-radius: 3px;
  letter-spacing: 0.08em;
  margin-top: 2px;
}

nav {
  display: flex;
  align-items: center;
  gap: 1.8rem;
}
nav a {
  color: #BDB8B0;
  text-decoration: none;
  font-size: 0.82rem;
  font-weight: 500;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  transition: color 0.2s;
}
nav a:hover  { color: var(--cream); }
nav a.active { color: var(--accent-soft); }

.header-actions {
  display: flex;
  gap: 0.75rem;
  align-items: center;
}

.btn-ghost {
  background: transparent;
  border: 1px solid #444;
  color: #BDB8B0;
  padding: 6px 14px;
  border-radius: 4px;
  font-size: 0.78rem;
  font-weight: 500;
  cursor: pointer;
  font-family: 'DM Sans', sans-serif;
  letter-spacing: 0.03em;
  transition: all 0.2s;
}
.btn-ghost:hover { border-color: var(--accent); color: var(--accent-soft); }

.btn-accent {
  background: var(--accent);
  border: none;
  color: #fff;
  padding: 6px 16px;
  border-radius: 4px;
  font-size: 0.78rem;
  font-weight: 600;
  cursor: pointer;
  font-family: 'DM Sans', sans-serif;
  letter-spacing: 0.03em;
  transition: background 0.2s;
}
.btn-accent:hover { background: #B03D24; }
</style>