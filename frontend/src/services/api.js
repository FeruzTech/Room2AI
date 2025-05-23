import axios from 'axios';

export async function submitPrompt(ageGroup, prompt) {
  try {
    const res = await axios.post('/api/summarize', {
      age_group: ageGroup,
      prompt
    });
    return res.data.summary;
  } catch (e) {
    return e.response?.data?.detail || 'Error summarizing prompt.';
  }
}
