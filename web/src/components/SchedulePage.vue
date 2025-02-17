<script setup>
import NavigationPanel from './panels/NavigationPanel.vue';
import ScheduleItem from './controls/ScheduleItem.vue';
import ScheduleDetails from './controls/ScheduleDetails.vue';
import { ref } from 'vue';

const selectedDetails = ref(null);

function showDetails(details) {
  selectedDetails.value = details;
}

function closeDetails() {
  selectedDetails.value = null;
}
</script>

<template>
  <div class="profile-page">
    <!-- Панель навигации -->
    <NavigationPanel class="navigation" />

    <!-- Основной контент -->
    <div class="main-content">
      <h2>Расписание</h2>

      <div class="schedule-list">
        <ScheduleItem
          v-for="(item, index) in schedule"
          :key="index"
          :startTime="item.startTime"
          :endTime="item.endTime"
          :title="item.title"
          @show-details="showDetails"
        />
      </div>

      <ScheduleDetails :details="selectedDetails" @close-details="closeDetails" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'SchedulePage',
  data() {
    return {
      schedule: [
        { startTime: '08:00', endTime: '09:30', title: 'Математика', teacher: 'Иванов И.И.', room: '101' },
        { startTime: '09:45', endTime: '11:15', title: 'Физика', teacher: 'Петров П.П.', room: '102' },
        { startTime: '11:30', endTime: '13:00', title: 'Химия', teacher: 'Сидоров С.С.', room: '103' },
        { startTime: '13:15', endTime: '14:45', title: 'Информатика', teacher: 'Кузнецов К.К.', room: '104' }
      ]
    };
  }
};
</script>

<style scoped>
/* Общая оболочка */
.profile-page {
  display: flex;
  width: 100%;
  height: 100vh;
}

/* Панель навигации */
.navigation {
  width: 260px;
}

/* Основной контент */
.main-content {
  flex-grow: 1;
  padding-top: 20px;
  margin-left: 40px;
}

/* Список расписания */
.schedule-list {
  margin-top: 20px;
}
</style>