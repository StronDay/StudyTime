<script setup>
const props = defineProps({
  startTime: String,
  endTime: String,
  title: String, // Добавляем проп title
  details: Object
})

const emit = defineEmits(['show-details'])

const handleClick = () => {
  emit('show-details', {
    subject: props.title, // Используем props.title
    time: `${props.startTime} - ${props.endTime}`,
    teacher: props.details.teacher,
    classroom: props.details.classroom,
    additionalInfo: props.details.additional_info
  })
}
</script>

<template>
  <div class="schedule-item" @click="handleClick">
    <div class="time">
      {{ startTime }} - {{ endTime }}
    </div>
    <div class="title">
      {{ title }} <!-- Используем переданный проп -->
    </div>
  </div>
</template>

<style scoped>
.schedule-item {
  padding: 15px;
  margin: 10px 0;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.schedule-item:hover {
  background-color: #f5f5f5;
}

.time {
  font-size: 14px;
  color: #666;
  margin-bottom: 5px;
}

.title {
  font-size: 16px;
  font-weight: 500;
}
</style>