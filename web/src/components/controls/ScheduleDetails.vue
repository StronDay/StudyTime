<template>
  <div class="schedule-details" v-if="details">
    <h3>{{ details.title }}</h3>
    <p><strong>Время:</strong> {{ details.startTime }} - {{ details.endTime }}</p>
    <p><strong>Преподаватель:</strong> {{ details.teacher }}</p>
    <p><strong>Аудитория:</strong> {{ details.room }}</p>
    <PerfectButton @click="closeDetails">Закрыть</PerfectButton>
  </div>
</template>

<script>
import PerfectButton from './PerfectButton.vue';

export default {
  name: 'ScheduleDetails',
  components: {
    PerfectButton
  },
  props: {
    details: {
      type: Object,
      required: false
    }
  },
  methods: {
    closeDetails() {
      this.$emit('close-details');
    }
  }
};
</script>

<style scoped>
.schedule-details {
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px; /* Скругление обводки */
  margin-top: 20px;
  background-color: #fff;
}

button {
  margin-top: 10px;
  padding: 5px 10px;
  cursor: pointer;
}
</style>