<script setup>
import PerfectInput from './controls/PerfectInput.vue'
import PerfectButton from './controls/PerfectButton.vue'
</script>

<template>
  <div class="container">
    <div class="column main-column">

      <h1>Авторизация</h1>

      <div class="column side-column">

        <PerfectInput id="login" label="Логин" placeholder="Введите логин">
          <template #icon>
            <i class='bx bx-user-circle'></i>
          </template>
        </PerfectInput>
        
        <PerfectInput id="passwd" label="Пароль" placeholder="Введите пароль" type="password">
          <template #icon>
            <i class='bx bx-key'></i>
          </template>
        </PerfectInput>

      </div>

      <PerfectButton style="width: 160px; height: 40px;">
        Войти
      </PerfectButton>

    </div>
  </div>
</template>

<style scoped>

.main-column {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 120px;

  gap: 120px;
}

.side-column {
  display: flex;
  flex-direction: column;
  align-items: center;

  gap: 40px;
}

h1 {
  font-size: 24px;
}
</style>
