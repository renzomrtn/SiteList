<template>
  <div class="grid-area">
    <div class="grid-header">
      <h2>
        {{ activeCategory }}
        <span>({{ totalCount.toLocaleString() }})</span>
      </h2>
      <div class="view-toggle">
        <button
          class="view-btn"
          :class="{ active: viewMode === 'grid' }"
          title="Grid view"
          @click="viewMode = 'grid'"
        >⊞</button>
        <button
          class="view-btn"
          :class="{ active: viewMode === 'list' }"
          title="List view"
          @click="viewMode = 'list'"
        >☰</button>
      </div>
    </div>

    <div class="cards-grid" :class="{ 'list-mode': viewMode === 'list' }">
      <!-- Featured card always spans full width -->
      <FeaturedCard
        v-if="featuredSite"
        :site="featuredSite"
      />

      <!-- Regular cards -->
      <SiteCard
        v-for="site in regularSites"
        :key="site.id"
        :site="site"
      />

      <!-- Empty state -->
      <div v-if="sites.length === 0" class="empty-state">
        <span>🔍</span>
        <p>No sites found. Try a different search or filter.</p>
      </div>
    </div>

    <Pagination
      v-model="currentPage"
      :total="24"
      @prev="currentPage = Math.max(1, currentPage - 1)"
      @next="currentPage = Math.min(24, currentPage + 1)"
    />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  sites:          { type: Array,  default: () => [] },
  activeCategory: { type: String, default: 'All Sites' },
  totalCount:     { type: Number, default: 4218 },
})

const viewMode   = ref('grid')
const currentPage = ref(1)

const featuredSite  = computed(() => props.sites.find(s => s.featured))
const regularSites  = computed(() => props.sites.filter(s => !s.featured))
</script>

<style scoped>
.grid-area {
  animation: fadeUp 0.6s 0.1s ease both;
}

.grid-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.5rem;
}
.grid-header h2 {
  font-family: 'DM Serif Display', serif;
  font-size: 1.5rem;
  letter-spacing: -0.01em;
}
.grid-header h2 span { color: var(--accent); }

.view-toggle { display: flex; gap: 4px; }
.view-btn {
  background: none;
  border: 1.5px solid var(--border);
  padding: 6px 8px;
  border-radius: 5px;
  cursor: pointer;
  color: var(--ink-muted);
  transition: all 0.15s;
  font-size: 0.85rem;
}
.view-btn.active { background: var(--ink); border-color: var(--ink); color: var(--cream); }

/* ── GRID ── */
.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.25rem;
}

/* FeaturedCard spans full row regardless of column count */
.cards-grid > :first-child {
  grid-column: 1 / -1;
}

/* ── LIST MODE ── */
.list-mode {
  grid-template-columns: 1fr !important;
}

/* ── EMPTY STATE ── */
.empty-state {
  grid-column: 1 / -1;
  text-align: center;
  padding: 4rem 2rem;
  color: var(--ink-muted);
}
.empty-state span { font-size: 2.5rem; display: block; margin-bottom: 1rem; }
.empty-state p { font-size: 0.95rem; }
</style>