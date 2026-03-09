<template>
  <AppHeader />

  <HeroSection v-model="searchQuery" />

  <FiltersRow
    v-model:activeFilter="activeFilter"
    v-model:sort="sort"
  />

  <div class="main">
    <AppSidebar v-model:activeCategory="activeCategory" />

    <CardGrid
      :sites="filteredSites"
      :activeCategory="activeCategory"
      :totalCount="totalCount"
    />
  </div>

</template>

<script setup>
import { ref, computed } from 'vue'
import { sites }   from '~/data/sites.js'
import { categories } from '~/data/categories.js'


// ── Shared State ──────────────────────────────────────────────
const searchQuery    = ref('')
const activeFilter   = ref('All')
const sort           = ref('Most Popular')
const activeCategory = ref('All Sites')

// ── Derived Data ──────────────────────────────────────────────
const filteredSites = computed(() => {
  let result = [...sites]

  // Search
  if (searchQuery.value.trim()) {
    const q = searchQuery.value.toLowerCase()
    result = result.filter(s =>
      s.name.toLowerCase().includes(q) ||
      s.description.toLowerCase().includes(q) ||
      s.tags.some(t => t.toLowerCase().includes(q)) ||
      s.url.toLowerCase().includes(q)
    )
  }

  // Category filter (sidebar)
  if (activeCategory.value !== 'All Sites') {
    result = result.filter(s => s.category === activeCategory.value)
  }

  // Top tab filter
  if (activeFilter.value !== 'All') {
    const map = {
      'Trending':     s => s.meta === 'Trending',
      'Top Rated':    s => s.rating >= 4.8,
      'New Arrivals': s => s.metaIcon === '🆕',
      'Design':       s => s.category === 'Design & UI',
      'Dev Tools':    s => s.category === 'Dev Tools',
      'Learning':     s => s.category === 'Learning',
      'Writing':      s => s.category === 'Writing & Docs',
    }
    if (map[activeFilter.value]) {
      result = result.filter(map[activeFilter.value])
    }
  }

  // Sort
  if (sort.value === 'Top Rated') {
    result = [...result].sort((a, b) => b.rating - a.rating)
  } else if (sort.value === 'A–Z') {
    result = [...result].sort((a, b) => a.name.localeCompare(b.name))
  }

  return result
})

const totalCount = computed(() => {
  if (activeCategory.value === 'All Sites') return 4218
  return categories.find(c => c.label === activeCategory.value)?.count ?? filteredSites.value.length
})
</script>

<style scoped>
.main {
  max-width: 1100px;
  margin: 0 auto;
  padding: 2.5rem 2.5rem;
  display: grid;
  grid-template-columns: 220px 1fr;
  gap: 3rem;
}
</style>