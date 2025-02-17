<template>
  <div class="schedule-item" @click="showDetails">
    <div class="time">{{ startTime }} - {{ endTime }}</div>
    <div class="title">{{ title }}</div>
  </div>
</template>

<script>
export default {
  name: 'ScheduleItem',
  props: {
    startTime: {
      type: String,
      required: true
    },
    endTime: {
      type: String,
      required: true
    },
    title: {
      type: String,
      required: true
    }
  },
  methods: {
    showDetails() {
      this.$emit('show-details', {
        startTime: this.startTime,
        endTime: this.endTime,
        title: this.title,
        teacher: this.teacher,
        room: this.room
      });
    }
  }
};
</script>

<style scoped>
.schedule-item {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 8px; /* Скругление обводки */
  margin-bottom: 10px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.schedule-item:hover {
  background-color: #f0f0f0;
}

.time {
  font-weight: bold;
}

.title {
  margin-top: 5px;
}
</style>