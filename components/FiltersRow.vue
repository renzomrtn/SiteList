<template>
  <div class="filters-row">
    <span class="filter-label">Filter</span>

    <div
      v-for="tab in filterTabs"
      :key="tab.label"
      class="tag"
      :class="{ active: tab.label === activeFilter }"
      @click="$emit('update:activeFilter', tab.label)"
    >
      <template v-if="tab.icon">{{ tab.icon }} </template>{{ tab.label }}
    </div>

  </div>
</template>

<script setup>
import { filterTabs } from '~/data/categories.js'

</script>

<style scoped>
.filters-row {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 2.5rem 1.5rem;
  display: flex;
  align-items: center;
  gap: 0.6rem;
  flex-wrap: wrap;
  border-bottom: 1px solid var(--border);
}

.filter-label {
  font-size: 0.73rem;
  font-weight: 600;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  color: var(--ink-muted);
  margin-right: 0.4rem;
}

.sort-wrap {
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.sort-wrap label {
  font-size: 0.78rem;
  color: var(--ink-muted);
}
.sort-wrap select {
  font-family: 'DM Sans', sans-serif;
  font-size: 0.8rem;
  padding: 5px 10px;
  border: 1.5px solid var(--border);
  border-radius: 6px;
  background: var(--card-bg);
  color: var(--ink);
  outline: none;
  cursor: pointer;
}
</style>