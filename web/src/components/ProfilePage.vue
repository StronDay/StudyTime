<script setup>
import NavigationPanel from './panels/NavigationPanel.vue';
import DataView from './controls/DataView.vue';
import UserProfile from './controls/UserProfile.vue';
</script>

<template>
  <div class="profile-page">
    <!-- Панель навигации -->
    <NavigationPanel class="navigation" />

    <!-- Основной контент -->
    <div class="main-content">
      <h2>Профиль</h2>

      <div class="user-profile">
        <UserProfile name="Иван Иванов" iconClass="bx bxs-user-account" :iconSize="32" />
      </div>

      <div class="data-grid">
        <DataView label="Логин" text="@ivanov">
          <template #icon>
            <i class='bx bx-user-circle'></i>
          </template>
        </DataView>

        <DataView label="Статус" text="Студент">
          <template #icon>
            <i class='bx bx-group'></i>
          </template>
        </DataView>

        <DataView label="Группа" text="КМБО-05-20">
          <template #icon>
            <i class='bx bx-phone'></i>
          </template>
        </DataView>

        <DataView label="Курс" text="3">
          <template #icon>
            <i class='bx bx-map'></i>
          </template>
        </DataView>
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
</style>