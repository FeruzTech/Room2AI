<template>
  <textarea v-model="modelValue" placeholder="Enter your subject prompt..."></textarea>
</template>
<script setup>
const props = defineProps(['modelValue']);
const emit = defineEmits(['update:modelValue']);
</script>
