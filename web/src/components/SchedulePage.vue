<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import Cookies from 'js-cookie'
import NavigationPanel from './panels/NavigationPanel.vue'
import ScheduleItem from './controls/ScheduleItem.vue'
import ScheduleDetails from './controls/ScheduleDetails.vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const selectedDetails = ref(null)
const schedule = ref([])
const loading = ref(true)
const error = ref(null)
const selectedDay = ref('MON')

const daysOfWeek = [
  { value: 'MON', label: 'Понедельник' },
  { value: 'TUE', label: 'Вторник' },
  { value: 'WED', label: 'Среда' },
  { value: 'THU', label: 'Четверг' },
  { value: 'FRI', label: 'Пятница' },
  { value: 'SAT', label: 'Суббота' }
]

// Создаем экземпляр axios
const api = axios.create({
  baseURL: 'http://0.0.0.0:5010/api'
})

// Флаг и очередь для обработки одновременного обновления токена
let isRefreshing = false
const failedQueue = []

const processQueue = (error, token = null) => {
  failedQueue.forEach(promise => {
    if (error) {
      promise.reject(error)
    } else {
      promise.resolve(token)
    }
  })
  failedQueue.length = 0
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
        })
          .then(token => {
            originalRequest.headers['Authorization'] = `Bearer ${token}`
            return api(originalRequest)
          })
          .catch(err => Promise.reject(err))
      }

      originalRequest._retry = true
      isRefreshing = true

      try {
        const refreshToken = Cookies.get('refresh_token')
        if (!refreshToken) throw new Error('No refresh token')

        const { data } = await axios.post('http://0.0.0.0:5010/api/token/refresh/', {
          refresh: refreshToken
        })

        Cookies.set('access_token', data.access, { expires: 7, secure: true, sameSite: 'Strict' })
        Cookies.set('refresh_token', data.refresh, { expires: 7, secure: true, sameSite: 'Strict' })

        api.defaults.headers.common['Authorization'] = `Bearer ${data.access}`
        originalRequest.headers['Authorization'] = `Bearer ${data.access}`

        processQueue(null, data.access)
        return api(originalRequest)
      } catch (refreshError) {
        Cookies.remove('access_token')
        Cookies.remove('refresh_token')
        router.push('/auth')
        processQueue(refreshError, null)
        return Promise.reject(refreshError)
      } finally {
        isRefreshing = false
      }
    }

    return Promise.reject(error)
  }
)

const fetchSchedule = async () => {
  loading.value = true
  try {
    const response = await api.get('/schedules/get/', {
      headers: {
        Authorization: `Bearer ${Cookies.get('access_token')}`
      },
      params: { day: selectedDay.value }
    })
    schedule.value = response.data
  } catch (err) {
    error.value = 'Ошибка загрузки расписания'
    console.error('Ошибка при загрузке расписания:', err)
  } finally {
    loading.value = false
  }
}

const showDetails = (details) => {
  selectedDetails.value = details
}

const closeDetails = () => {
  selectedDetails.value = null
}

onMounted(fetchSchedule)
</script>

<template>
  <div class="profile-page">
    <!-- Боковая панель навигации -->
    <NavigationPanel class="navigation" />

    <!-- Основной контент -->
    <div class="main-content">
      <h2>Расписание</h2>

      <!-- Выбор дня недели -->
      <div class="day-selector">
        <select 
          v-model="selectedDay" 
          @change="fetchSchedule"
          class="custom-select"
        >
          <option 
            v-for="day in daysOfWeek" 
            :key="day.value" 
            :value="day.value"
          >
            {{ day.label }}
          </option>
        </select>
      </div>

      <!-- Состояние загрузки -->
      <div v-if="loading" class="loading-state">
        <i class='bx bx-loader-circle bx-spin'></i>
        <span>Загрузка расписания...</span>
      </div>

      <!-- Ошибка -->
      <div v-else-if="error" class="error-state">
        <i class='bx bx-error-circle'></i>
        {{ error }}
      </div>

      <!-- Список занятий -->
      <div v-else class="schedule-list">
        <ScheduleItem
          v-for="(item, index) in schedule"
          :key="index"
          :start-time="item.start_time"
          :end-time="item.end_time"
          :title="item.subject"
          :details="item"
          @show-details="showDetails"
        />
      </div>

      <!-- Модальное окно с деталями -->
      <ScheduleDetails 
        v-if="selectedDetails"
        :details="selectedDetails" 
        @close-details="closeDetails"
      />
    </div>
  </div>
</template>

<style scoped>
/* Общая оболочка */
.profile-page {
  display: flex;
  width: 100%;
  min-height: 100vh;
  background: #ffffff;
}

/* Боковая панель */
.navigation {
  width: 260px;
  height: 100vh;
  position: fixed;
  left: 0;
  top: 0;
}

/* Основной контент */
.main-content {
  flex-grow: 1;
  margin-left: 260px;
  padding: 20px 40px;
  min-height: 100vh;
}

h2 {
  margin-bottom: 60px;
  font-weight: 600;
}

/* Стилизация выпадающего списка */
.custom-select {
  width: 200px;
  padding: 12px 20px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  background: white;
  font-size: 16px;
  color: #2c3e50;
  appearance: none;
  background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right 12px center;
  background-size: 16px;
  transition: border-color 0.2s;
}

.custom-select:focus {
  outline: none;
  border-color: #327fd1;
}

/* Список занятий */
.schedule-list {
  margin-top: 30px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

/* Состояния загрузки и ошибки */
.loading-state,
.error-state {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 20px;
  background: white;
  border-radius: 8px;
  margin-top: 30px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.loading-state i {
  font-size: 24px;
  color: #327fd1;
}

.error-state i {
  font-size: 24px;
  color: #e74c3c;
}

.error-state {
  color: #e74c3c;
}
</style>