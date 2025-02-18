<!-- PerfectInput.vue -->
<template>
  <div class="input-group">
    <label :for="id">{{ label }}</label>
    <div class="input-wrapper">
      <input
        :id="id"
        :type="type"
        :placeholder="placeholder"
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
      />
      <span class="input-icon">
        <slot name="icon"></slot>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PerfectInput',
  props: {
    id: {
      type: String,
      required: true
    },
    label: {
      type: String,
      required: true
    },
    type: {
      type: String,
      default: 'text'
    },
    modelValue: {  // Изменили value на modelValue
      type: String,
      default: ''
    },
    placeholder: {
      type: String,
      default: ''
    }
  }
};
</script>

<style scoped>
.input-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-size: 14px;
}

.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
  border: none;
  border-bottom: 1px solid #ccc;
  padding-right: 30px; /* Отступ для иконки */
  font-size: 16px;
}

input:focus {
  outline: none;
  border-bottom-color: #327fd1;
}

.input-icon {
  position: absolute;
  right: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgb(91, 87, 87);
}

.input-wrapper:focus-within .input-icon {
  color: #327fd1; /* Цвет иконки при фокусе */
}

.input-icon ::v-deep i {
  font-size: 24px; /* Размер иконки */
}
</style>