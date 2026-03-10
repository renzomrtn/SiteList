<template>
  <aside>
    <!-- Categories -->
    <div class="aside-section">
      <div class="aside-title">Categories</div>
      <ul class="category-list">
        <li
          v-for="cat in categories"
          :key="cat.label"
          :class="{ active: cat.label === activeCategory }"
          @click="$emit('update:activeCategory', cat.label)"
        >
          <span>
            <span class="cat-icon">{{ cat.icon }}</span>{{ cat.label }}
          </span>
          <span class="cat-count">{{ cat.count.toLocaleString() }}</span>
        </li>
      </ul>
    </div>

    <!-- Tags -->
    <div class="aside-section">
      <div class="aside-title">Tags</div>
      <div class="tags-wrap">
        <div
          v-for="tag in tags"
          :key="tag"
          class="tag"
        >
          {{ tag }}
        </div>
      </div>
    </div>
  </aside>
</template>

<script setup>
import { categories, tags} from '~/data/categories.js'

defineProps({
  activeCategory: { type: String, default: 'All Sites' },
})
defineEmits(['update:activeCategory'])
</script>

<style scoped>
aside {
  animation: fadeUp 0.6s 0.15s ease both;
}

.aside-section {
  margin-bottom: 2.2rem;
}

.aside-title {
  font-family: 'DM Mono', monospace;
  font-size: 0.65rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--ink-muted);
  margin-bottom: 0.9rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px solid var(--border);
}

.category-list {
  list-style: none;
}
.category-list li {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 7px 10px;
  border-radius: 6px;
  cursor: pointer;
  transition: background 0.15s;
  font-size: 0.875rem;
  color: var(--ink-light);
}
.category-list li:hover { background: var(--tag-bg); }
.category-list li.active {
  background: var(--ink);
  color: var(--cream);
  font-weight: 500;
}

.cat-count {
  font-family: 'DM Mono', monospace;
  font-size: 0.7rem;
  color: var(--ink-muted);
  background: var(--border);
  padding: 1px 6px;
  border-radius: 100px;
}
.category-list li.active .cat-count {
  background: rgba(255,255,255,0.15);
  color: rgba(255,255,255,0.6);
}

.cat-icon {
  margin-right: 0.5rem;
  font-size: 0.9rem;
}

.tags-wrap {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}
/* Slightly smaller tags in sidebar */
.tags-wrap .tag {
  font-size: 0.72rem;
  padding: 4px 10px;
}
</style>