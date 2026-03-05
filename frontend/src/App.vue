<script setup>

import NavBar from "@/components/navbar/NavBar.vue";
import {onMounted} from "vue";
import {useUserStore} from "@/stores/user.js";
import api from "@/js/http/api.js";
import {useRoute} from "vue-router";
import router from "@/router/index.js";

const user = useUserStore()
const route = useRoute()

onMounted(async () => {
  try {
    const res = await api.get('/api/user/account/get_user_info/')
    const data = res.data
    if (data.result === 'success') {
      user.setUserInfo(data)
    }
  } catch (err) {

  } finally {
    user.setHasPulledUserInfo(true)

    if (route.meta.needLogin && !user.isLogin()) {
      await router.replace({
        name: 'user-account-login-index'
      })
    }
  }
})
</script>

<template>
  <NavBar>
    <RouterView />
  </NavBar>
</template>

<style scoped>

</style>
