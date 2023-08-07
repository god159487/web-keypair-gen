<template>
  <div>
    <navbar></navbar>
    <main class="py-5">
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
import navbar from "@/components/Navbar.vue";
export default {
  components: {
    navbar
  }
};
</script>
