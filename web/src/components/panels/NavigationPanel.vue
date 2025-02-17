<script setup>
import PerfectButton from '../controls/PerfectButton.vue';
</script>

<template>
<div class="navigation-page">
  <div class="sidebar">

  <h2>Study Time</h2>

  <div class="column button-column">

    <PerfectButton style="width: 100%; height: 40px;">
      <template #icon>
      <i class='bx bx-user-circle'></i>
      </template>
      Профиль
    </PerfectButton>

    <PerfectButton style="width: 100%; height: 40px;">
      <template #icon>
      <i class='bx bx-calendar' ></i>
      </template>
      Расписание
    </PerfectButton>

  </div>

  </div>
</div>
</template>

<style scoped>

.button-column {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.sidebar {
  width: 260px;
  background-color: #f0f0f0;
  padding: 20px;
  position: fixed;
  left: 0;
  top: 0;
  bottom: 0;
}

.sidebar h2 {
  margin-bottom: 60px;
}

</style>