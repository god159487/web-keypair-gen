import { createRouter, createWebHistory } from "vue-router";
import Main from "@/views/Main.vue";
import Login from "@/views/Login.vue";


const routes = [
  {
    path: "/",
    name: "Main",
    component: Main,
    redirect: "/login",
    meta: {
      title: "Main",
    },
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
    meta: {
      title: "Login",
    },
  },
  {
    path: "/:pathMatch(.*)*",
    component: Main,
    redirect: "/login",
    meta: {
      title: "Main",
    },
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.URL),
  routes,
});

router.beforeEach((to, _, next) => {
  if (typeof to.meta.title === "string") {
    document.title = "Keypair Generator | " + to.meta.title;
  }
  next();
});

export default router;
