<script setup>
defineProps(['details'])
defineEmits(['close-details'])
</script>

<template>
  <div class="details-overlay">
    <div class="details-content">
      <div class="header">
        <h3>{{ details.subject }}</h3>
        <button @click="$emit('close-details')" class="close-btn">
          <i class='bx bx-x'></i>
        </button>
      </div>
      
      <div class="detail-item">
        <label>Время:</label>
        <span>{{ details.time }}</span>
      </div>
      
      <div class="detail-item">
        <label>Преподаватель:</label>
        <span>{{ details.teacher }}</span>
      </div>
      
      <div class="detail-item">
        <label>Аудитория:</label>
        <span>{{ details.classroom }}</span>
      </div>
      
      <div v-if="details.additionalInfo" class="additional-info">
        <label>Дополнительная информация:</label>
        <p>{{ details.additionalInfo }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.details-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.details-content {
  background: white;
  padding: 25px;
  border-radius: 10px;
  width: 90%;
  max-width: 500px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.close-btn {
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
  padding: 5px;
}

.detail-item {
  margin: 10px 0;
}

.detail-item label {
  font-weight: 500;
  margin-right: 10px;
}

.additional-info {
  margin-top: 20px;
  padding-top: 15px;
  border-top: 1px solid #eee;
}
</style>