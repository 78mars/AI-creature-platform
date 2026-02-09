<script setup>

import MenuIcon from "@/components/navbar/icons/MenuIcon.vue";
import HomepageIcon from "@/components/navbar/icons/HomepageIcon.vue";
import FriendIcon from "@/components/navbar/icons/FriendIcon.vue";
import CreateIcon from "@/components/navbar/icons/CreateIcon.vue";
import SearchIcon from "@/components/navbar/icons/SearchIcon.vue";
</script>

<template>
  <div class="drawer lg:drawer-open">
    <input id="my-drawer-4" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content">
      <!-- Navbar -->
      <nav class="navbar w-full bg-base-100 shadow-sm">
        <div class = "navbar-start">
          <label for="my-drawer-4" aria-label="open sidebar" class="btn btn-square btn-ghost">
          <!-- Sidebar toggle icon -->
          <MenuIcon />
        </label>
        <div class="px-2 font-bold text-xl">AIcreatures</div>
        </div>
        <div class="navbar-center w-4/5 max-w-180">
          <div class="join w-4/5">
            <input class="input join-item rounded-l-full" placeholder="搜索你感兴趣的内容" />
            <button class="btn join-item rounded-r-full gap-0">
              <SearchIcon />
              搜索
            </button>
          </div>
        </div>
        <div class="navbar-end">
          <buttion class="btn btn-ghost text-lg">登陆</buttion>
        </div>
      </nav>
      <!-- Page content here -->
      <slot> </slot>
    </div>

    <div class="drawer-side is-drawer-close:overflow-visible">
      <label for="my-drawer-4" aria-label="close sidebar" class="drawer-overlay"></label>
      <div class="flex min-h-full flex-col items-start bg-base-200 is-drawer-close:w-16 is-drawer-open:w-44">
        <!-- Sidebar content here -->
        <ul class="menu w-full grow">
          <!-- List item -->
          <li>
            <button class="is-drawer-close:tooltip is-drawer-close:tooltip-right" data-tip="首页">
              <!-- Home icon -->
              <homepage-icon />
              <span class="is-drawer-close:hidden text-base ml-2 whitespace-nowrap py-3">首页</span>
            </button>
          </li>
          <li>
            <button class="is-drawer-close:tooltip is-drawer-close:tooltip-right" data-tip="好友">
              <!-- Home icon -->
              <friend-icon />
              <span class="is-drawer-close:hidden text-base ml-2 whitespace-nowrap py-3">好友</span>
            </button>
          </li>
          <li>
            <button class="is-drawer-close:tooltip is-drawer-close:tooltip-right" data-tip="创作">
              <!-- Home icon -->
              <CreateIcon />
              <span class="is-drawer-close:hidden text-base ml-2 whitespace-nowrap py-3">创作</span>
            </button>
          </li>

          <!-- List item -->
          <li>
            <button class="is-drawer-close:tooltip is-drawer-close:tooltip-right" data-tip="Settings">
              <!-- Settings icon -->
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" stroke-linejoin="round" stroke-linecap="round" stroke-width="2" fill="none" stroke="currentColor" class="my-1.5 inline-block size-4"><path d="M20 7h-9"></path><path d="M14 17H5"></path><circle cx="17" cy="17" r="3"></circle><circle cx="7" cy="7" r="3"></circle></svg>
              <span class="is-drawer-close:hidden">Settings</span>
            </button>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>