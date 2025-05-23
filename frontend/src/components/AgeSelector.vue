<template>
  <select v-model="modelValue">
    <option value="">Select Age Group</option>
    <option>Early Elementary [5-8]</option>
    <option>Late Elementary [9-11]</option>
    <option>Middle School [12-14]</option>
    <option>High School [15-18]</option>
  </select>
</template>
<script setup>
const props = defineProps(['modelValue']);
const emit = defineEmits(['update:modelValue']);
</script>
