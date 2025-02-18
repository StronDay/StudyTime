<script setup>
import { ref } from 'vue'
import axios from 'axios'
import Cookies from 'js-cookie'
import PerfectInput from './controls/PerfectInput.vue'
import PerfectButton from './controls/PerfectButton.vue'

const login = ref('')
const password = ref('')
const errorMessage = ref('')
const serverResponse = ref(null)

const handleLogin = async () => {
  try {
    const loginData = {
      username: login.value,
      password: password.value
    };

    // Выводим данные в консоль перед отправкой
    console.log('Sending data:', loginData);
    const response = await axios.post('http://localhost:5010/api/token/', loginData, {
      withCredentials: true  // Это важно для отправки куки
    });

    serverResponse.value = response.data;
    const { access, refresh } = response.data;

    // Сохраняем токены в куки с настройками безопасности
    Cookies.set('access_token', access, { expires: 7, secure: true, sameSite: 'Strict' });
    Cookies.set('refresh_token', refresh, { expires: 7, secure: true, sameSite: 'Strict' });

    // Перенаправление или дальнейшие действия после успешного входа
    window.location.href = '/profile'; // Пример редиректа на страницу после авторизации

  } catch (error) {
    errorMessage.value = 'Неверный логин или пароль';
  }
}
</script>

<template>
  <div class="container">
    <div class="column main-column">

      <h1>Авторизация</h1>

      <div class="column side-column">

        <PerfectInput v-model="login" id="login" label="Логин" placeholder="Введите логин">
          <template #icon>
            <i class='bx bx-user-circle'></i>
          </template>
        </PerfectInput>
        
        <PerfectInput v-model="password" id="passwd" label="Пароль" placeholder="Введите пароль" type="password">
          <template #icon>
            <i class='bx bx-key'></i>
          </template>
        </PerfectInput>

      </div>

      <PerfectButton @click="handleLogin" style="width: 160px; height: 40px;">
        Войти
      </PerfectButton>

      <div v-if="errorMessage" class="error-message">
        {{ errorMessage }}
      </div>

      <!-- Вывод данных с сервера -->
      <div v-if="serverResponse" class="server-response">
        <h3>Ответ от сервера:</h3>
        <pre>{{ serverResponse }}</pre> <!-- Здесь выводятся данные от сервера -->
      </div>
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
