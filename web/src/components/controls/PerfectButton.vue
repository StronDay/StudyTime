<template>
  <button class="perfect-button">
    <slot name="icon"></slot>
    <span :class="{ 'with-icon': $slots.icon }"><slot></slot></span>
  </button>
</template>

<script>
export default {
  name: 'PerfectButton'
};
</script>

<style scoped>
.perfect-button {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px 20px;
  font-size: 16px;
  color: #fff;
  background-color: #327fd1;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  text-align: center;
  text-decoration: none;
}

.perfect-button:hover {
  background-color: #4a94e2;
}

.perfect-button span.with-icon {
  margin-left: 8px;
}

.perfect-button span {
  margin-left: 0;
}

.perfect-button ::v-deep i {
  font-size: 24px; /* Размер иконки */
}
</style>