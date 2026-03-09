<template>
  <div class="card">
    <div
      class="card-thumb"
      :style="{ background: `linear-gradient(135deg, ${site.gradient[0]}, ${site.gradient[1]})` }"
    >
      <div class="favicon">{{ site.emoji }}</div>
      <div class="url-badge">{{ site.url }}</div>
      <div class="card-bookmark">🔖</div>
    </div>

    <div class="card-body">
      <div class="card-tags">
        <span v-for="tag in site.tags" :key="tag" class="card-tag">{{ tag }}</span>
      </div>
      <div class="card-title">{{ site.name }}</div>
      <div class="card-desc">{{ site.description }}</div>
    </div>

    <div class="card-footer">
      <div class="card-meta">{{ site.metaIcon }} {{ site.meta }}</div>
      <div class="rating">
        {{ starString(site.rating) }}
        <span class="rating-val">{{ site.rating.toFixed(1) }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  site: { type: Object, required: true },
})

function starString(rating) {
  const full  = Math.round(rating)
  const empty = 5 - full
  return '★'.repeat(full) + '☆'.repeat(empty)
}
</script>

<style scoped>
.card {
  background: var(--card-bg);
  border: 1.5px solid var(--border);
  border-radius: 10px;
  overflow: hidden;
  transition: box-shadow 0.2s, transform 0.2s, border-color 0.2s;
  cursor: pointer;
  display: flex;
  flex-direction: column;
}
.card:hover {
  box-shadow: 0 8px 28px rgba(0,0,0,0.1);
  transform: translateY(-2px);
  border-color: var(--accent-soft);
}

.card-thumb {
  height: 140px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.favicon {
  width: 42px;
  height: 42px;
  border-radius: 10px;
  background: rgba(255,255,255,0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.3rem;
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255,255,255,0.25);
}

.url-badge {
  position: absolute;
  bottom: 10px;
  left: 12px;
  font-family: 'DM Mono', monospace;
  font-size: 0.65rem;
  background: rgba(0,0,0,0.35);
  color: rgba(255,255,255,0.85);
  padding: 3px 8px;
  border-radius: 4px;
  letter-spacing: 0.04em;
  backdrop-filter: blur(4px);
}

.card-bookmark {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 30px;
  height: 30px;
  background: rgba(255,255,255,0.2);
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(255,255,255,0.7);
  font-size: 0.85rem;
  backdrop-filter: blur(6px);
  transition: background 0.15s;
}
.card-bookmark:hover { background: rgba(255,255,255,0.35); }

.card-body {
  padding: 1rem 1.1rem;
  flex: 1;
}

.card-tags {
  display: flex;
  gap: 5px;
  flex-wrap: wrap;
  margin-bottom: 0.6rem;
}
.card-tag {
  font-size: 0.68rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 2px 7px;
  border-radius: 3px;
  background: var(--tag-bg);
  color: var(--ink-muted);
}

.card-title {
  font-family: 'DM Serif Display', serif;
  font-size: 1.1rem;
  line-height: 1.3;
  margin-bottom: 0.35rem;
  color: var(--ink);
}

.card-desc {
  font-size: 0.82rem;
  color: var(--ink-muted);
  line-height: 1.6;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-footer {
  padding: 0.65rem 1.1rem;
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.card-meta {
  font-family: 'DM Mono', monospace;
  font-size: 0.68rem;
  color: var(--ink-muted);
}

.rating {
  display: flex;
  align-items: center;
  gap: 3px;
  font-size: 0.72rem;
  color: var(--gold);
}
.rating-val {
  color: var(--ink-muted);
  margin-left: 2px;
}
</style>