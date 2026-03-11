<template>
  <div class="hero">
    <div class="hero-eyebrow">The Web, Catalogued</div>

    <h1>My list of <em>Awesome Websites</em><br />in the internet</h1>

    <p class="hero-sub">
      Who needs a bookmark?
    </p>

    <div class="search-wrap">
      <span class="search-icon">🔍</span>
      <input
        type="text"
        :value="modelValue"
        placeholder="Search by name, category, or keyword…"
        @input="$emit('update:modelValue', $event.target.value)"
      />
      <span class="search-kbd">Search</span>
    </div>

    <div class="hero-stats">
      <div><strong>4,218</strong> websites</div>
      <div class="divider">|</div>
      <div><strong>139</strong> categories</div>
    </div>
  </div>
</template>

<script setup>
defineProps({ modelValue: String })
defineEmits(['update:modelValue'])
</script>

<style scoped>
.hero {
  padding: 5rem 2.5rem 3.5rem;
  max-width: 900px;
  margin: 0 auto;
  text-align: center;
  animation: fadeUp 0.6s ease both;
}

.hero-eyebrow {
  font-family: 'DM Mono', monospace;
  font-size: 0.72rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 1.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.6rem;
}
.hero-eyebrow::before,
.hero-eyebrow::after { content: '—'; color: var(--border); }

h1 {
  font-family: 'DM Serif Display', serif;
  font-size: clamp(2.8rem, 6vw, 4.5rem);
  line-height: 1.07;
  letter-spacing: -0.02em;
  color: var(--ink);
  margin-bottom: 1.2rem;
}
h1 em { color: var(--accent); font-style: italic; }

.hero-sub {
  font-size: 1.05rem;
  color: var(--ink-light);
  max-width: 540px;
  margin: 0 auto 2.5rem;
  line-height: 1.7;
  font-weight: 300;
}

/* ── SEARCH ── */
.search-wrap {
  position: relative;
  max-width: 580px;
  margin: 0 auto 1.5rem;
}
.search-wrap input {
  width: 100%;
  padding: 1rem 1.2rem 1rem 3.2rem;
  font-family: 'DM Sans', sans-serif;
  font-size: 1rem;
  background: var(--card-bg);
  border: 1.5px solid var(--border);
  border-radius: 8px;
  color: var(--ink);
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.search-wrap input::placeholder { color: var(--ink-muted); }
.search-wrap input:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px rgba(200,75,47,0.12);
}
.search-icon {
  position: absolute;
  left: 1.1rem;
  top: 50%;
  transform: translateY(-50%);
  color: var(--ink-muted);
  font-size: 1rem;
  pointer-events: none;
}
.search-kbd {
  position: absolute;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  font-family: 'DM Mono', monospace;
  font-size: 0.68rem;
  color: var(--ink-muted);
  border: 1px solid var(--border);
  padding: 2px 6px;
  border-radius: 3px;
  background: var(--tag-bg);
}

.hero-stats {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2.5rem;
  font-size: 0.8rem;
  color: var(--ink-muted);
  margin-top: 0.5rem;
}
.hero-stats strong {
  color: var(--ink);
  font-weight: 600;
  font-size: 1rem;
}
.divider { color: var(--border); }
</style>