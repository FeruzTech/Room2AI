<template>
  <div v-if="summary">{{ summary }}</div>
</template>
<script setup>
const props = defineProps(['summary']);
</script>
