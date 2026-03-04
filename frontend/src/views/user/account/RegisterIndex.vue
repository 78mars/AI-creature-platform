<script setup>

import {ref} from "vue";
import api from "@/js/http/api.js";


import {useUserStore} from "@/stores/user.js";
import {useRouter} from "vue-router";
const user = useUserStore()
const router = useRouter()

const username = ref('')
const password = ref('')
const passwordDoubleCheck = ref('')
const errormessage = ref('')

async function handleRegister(){
  if(!username.value.trim()){
    errormessage.value='用户名不能为空'
  }else if(!password.value.trim()){
    errormessage.value='密码不能为空'
  }else if(password.value.trim() !== passwordDoubleCheck.value.trim()){
    errormessage.value='两次输入的密码不一致'
  }else{
    try {
      const res = await api.post('/api/user/account/register/', {
        username: username.value,
        password: password.value,
      })
      const data = res.data
      if (data.result === 'success') {
        user.setAccessToken(data.access)
        user.setUserInfo(data)
        await router.push({
          name: 'homepage-index'
        })
      } else {
        errormessage.value = data.result
      }
    } catch (err) {
      console.log(err)
    }
  }
}
</script>

<template>
  <div class="flex justify-center mt-12">
    <form @submit.prevent="handleRegister" class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
    <label class="label">用户名</label>
    <input v-model="username" type="text" class="input" placeholder="用户名" />

    <label class="label">密码</label>
    <input v-model="password" type="password" class="input" placeholder="密码" />

    <label class="label">再次确认密码</label>
    <input v-model="passwordDoubleCheck" type="password" class="input" placeholder="密码" />

      <p class="text-sm text-red-500">{{ errormessage }}</p>

    <button class="btn btn-neutral mt-4">注册</button>
      <div class="flex justify-end">
        <RouterLink :to="{name: 'user-account-login-index'}" class="btn btn-soft btn-primary ">
          登陆
        </RouterLink>
      </div>
  </form>
  </div>
</template>

<style scoped>

</style>