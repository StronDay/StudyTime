<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import Cookies from 'js-cookie'
import { useRouter } from 'vue-router'
import NavigationPanel from './panels/NavigationPanel.vue'
import DataView from './controls/DataView.vue'
import UserProfile from './controls/UserProfile.vue'

const router = useRouter()

const profileData = ref({
  user: {
    username: '',
    first_name: '',
    last_name: ''
  },
  group: { group: '' },
  course: { course: 0 }
})
const loading = ref(true)
const error = ref(null)

// Создаем кастомный экземпляр axios
const api = axios.create({
  baseURL: 'http://0.0.0.0:5010/api',
  withCredentials: true
})

let isRefreshing = false
let failedQueue = []

const processQueue = (error, token = null) => {
  failedQueue.forEach(prom => {
    if (error) {
      prom.reject(error)
    } else {
      prom.resolve(token)
    }
  })
  failedQueue = []
}

// Функция выхода из профиля
const logout = () => {
  Cookies.remove('access_token')
  Cookies.remove('refresh_token')
  router.push('/auth')
}

// Перехватчик ответов
api.interceptors.response.use(
  response => response,
  async error => {
    const originalRequest = error.config

    if (error.response?.status === 401 && !originalRequest._retry) {
      if (isRefreshing) {
        return new Promise((resolve, reject) => {
          failedQueue.push({ resolve, reject })
        }).then(() => {
          return api(originalRequest)
        }).catch(err => {
          return Promise.reject(err)
        })
      }

      originalRequest._retry = true
      isRefreshing = true

      try {
        const refreshToken = Cookies.get('refresh_token')
        if (!refreshToken) throw new Error('No refresh token')

        const { data } = await axios.post('http://0.0.0.0:5010/api/token/refresh/', {
          refresh: refreshToken
        })

        Cookies.set('access_token', data.access)
        Cookies.set('refresh_token', data.refresh)

        api.defaults.headers.common['Authorization'] = `Bearer ${data.access}`
        originalRequest.headers['Authorization'] = `Bearer ${data.access}`

        processQueue(null, data.access)
        return api(originalRequest)
      } catch (refreshError) {
        logout()
        processQueue(refreshError, null)
        return Promise.reject(refreshError)
      } finally {
        isRefreshing = false
      }
    }

    return Promise.reject(error)
  }
)

const fetchProfileData = async () => {
  try {
    const response = await api.get('/students/current/', {
      headers: {
        Authorization: `Bearer ${Cookies.get('access_token')}`
      }
    })

    profileData.value = response.data
  } catch (err) {
    if (err.response?.status === 401) {
      error.value = 'Требуется авторизация'
      logout()
    } else {
      error.value = 'Ошибка загрузки данных профиля'
      console.error(err)
    }
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  if (!Cookies.get('access_token')) {
    router.push('/auth')
    return
  }
  fetchProfileData()
})
</script>

<template>
  <div class="profile-page">
    <NavigationPanel class="navigation" />

    <div class="main-content">
      <div class="header">
        <h2>Профиль</h2>
        <button @click="logout" class="logout-button">Выйти</button>
      </div>

      <div v-if="loading" class="loading">
        Загрузка данных...
      </div>

      <div v-else-if="error" class="error">
        {{ error }}
      </div>

      <div v-else class="content">
        <div class="user-profile">
          <UserProfile 
            :name="`${profileData.user?.first_name || ''} ${profileData.user?.last_name || ''}`"
            iconClass="bx bxs-user-account" 
            :iconSize="32"
          />
        </div>

        <div class="data-grid">
          <DataView label="Логин" :text="profileData.user?.username || ''">
            <template #icon>
              <i class='bx bx-user-circle'></i>
            </template>
          </DataView>

          <DataView label="Статус" text="Студент">
            <template #icon>
              <i class='bx bxs-graduation'></i>
            </template>
          </DataView>

          <DataView 
            label="Группа" 
            :text="profileData.group?.group || 'Не указана'"
          >
            <template #icon>
              <i class='bx bx-group'></i>
            </template>
          </DataView>

          <DataView 
            label="Курс" 
            :text="profileData.course?.course?.toString() || 'Не указан'"
          >
            <template #icon>
              <i class='bx bxs-book-bookmark'></i>
            </template>
          </DataView>
        </div>
      </div>
    </div>
  </div>
</template>

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

/* Заголовок с кнопкой выхода */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Кнопка выхода */
.logout-button {
  padding: 10px 20px;
  font-size: 14px;
  border: none;
  border-radius: 8px;
  background-color: #e74c3c;
  color: white;
  cursor: pointer;
  transition: background-color 0.2s;
}

.logout-button:hover {
  background-color: #c0392b;
}

/* Профиль пользователя */
.user-profile {
  margin-top: 60px;
  margin-bottom: 40px;
}

/* Сетка данных */
.data-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  column-gap: var(--column-gap, 20px); /* Настраиваемый горизонтальный отступ */
  row-gap: 40px; /* Отступ между плитками по вертикали */
}

/* Состояние загрузки и ошибки */
.loading, .error {
  margin-top: 40px;
  font-size: 18px;
  color: #555;
}
</style>