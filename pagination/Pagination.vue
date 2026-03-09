<template>
  <div class="pagination">
    <button class="page-btn" @click="$emit('prev')">‹</button>

    <button
      v-for="page in visiblePages"
      :key="page"
      class="page-btn"
      :class="{ active: page === modelValue }"
      @click="typeof page === 'number' && $emit('update:modelValue', page)"
    >
      {{ page }}
    </button>

    <button class="page-btn" @click="$emit('next')">›</button>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  modelValue: { type: Number, default: 1 },
  total:      { type: Number, default: 24 },
})
defineEmits(['update:modelValue', 'prev', 'next'])

const visiblePages = computed(() => {
  // Show first 3, ellipsis, then last page
  const pages = [1, 2, 3, '…', props.total]
  return pages
})
</script>

<style scoped>
.pagination {
  margin-top: 2.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
}

.page-btn {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  border: 1.5px solid var(--border);
  background: var(--card-bg);
  font-size: 0.85rem;
  cursor: pointer;
  transition: all 0.15s;
  color: var(--ink-light);
  font-family: 'DM Sans', sans-serif;
}
.page-btn:hover  { border-color: var(--accent); color: var(--accent); }
.page-btn.active { background: var(--ink); border-color: var(--ink); color: var(--cream); }
</style>