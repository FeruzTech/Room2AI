<template>
  <div>
    <AgeSelector v-model="ageGroup" />
    <PromptInput v-model="prompt" />
    <button @click="submitPrompt">Summarize</button>
    <SummaryDisplay :summary="summary" />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import AgeSelector from './components/AgeSelector.vue';
import PromptInput from './components/PromptInput.vue';
import SummaryDisplay from './components/SummaryDisplay.vue';
import { submitPrompt as apiSubmitPrompt } from './services/api';

const ageGroup = ref('');
const prompt = ref('');
const summary = ref('');

async function submitPrompt() {
  if (!ageGroup.value) {
    summary.value = 'Please select an age group.';
    return;
  }
  summary.value = await apiSubmitPrompt(ageGroup.value, prompt.value);
}
</script>
