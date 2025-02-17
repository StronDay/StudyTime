<template>
  <div class="user-profile">
    <i :class="iconClass" :style="{ fontSize: iconSize + 'px' }" class="user-icon"></i>
    <span class="user-name">{{ name }}</span>
  </div>
</template>

<script>
export default {
  name: 'UserProfile',
  props: {
    name: {
      type: String,
      required: true
    },
    iconClass: {
      type: String,
      default: 'bx bx-user'
    },
    iconSize: {
      type: Number,
      default: 24
    }
  }
};
</script>

<style scoped>
.user-profile {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.user-icon {
  margin-right: 10px;
  color: rgb(91, 87, 87); /* Цвет иконки по умолчанию */
}

.user-name {
  font-size: 18px;
  font-weight: bold;
}
</style>