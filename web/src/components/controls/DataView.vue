<template>
  <div class="data-view">
    <label class="data-label">{{ label }}</label>
    <div class="data-content">
      <slot name="icon">
        <i :class="iconClass" :style="{ fontSize: iconSize + 'px' }" class="data-icon"></i>
      </slot>
      <span :class="{ 'with-icon': $slots.icon }" class="data-text">{{ text }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DataView',
  props: {
    label: {
      type: String,
      required: true
    },
    text: {
      type: String,
      required: true
    },
    iconClass: {
      type: String,
      required: false
    },
    iconSize: {
      type: Number,
      default: 24
    }
  }
};
</script>

<style scoped>
.data-view {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}

.data-label {
  font-weight: bold;
  font-size: 14px;
  margin-bottom: 10px;
}

.data-content {
  display: flex;
  align-items: center;
}

.data-icon {
  margin-right: 10px;
  color: rgb(91, 87, 87); /* Цвет иконки по умолчанию */
}

.data-text.with-icon {
  margin-left: 20px;
}

.data-text {
  font-size: 16px;
}

.data-view ::v-deep i {
  font-size: 24px; /* Размер иконки по умолчанию */
  color: rgb(91, 87, 87); /* Цвет иконки по умолчанию */
}

.data-content:focus-within .data-icon {
  color: #327fd1; /* Цвет иконки при фокусе */
}
</style>