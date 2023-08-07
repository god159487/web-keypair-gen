import { createApp } from "vue";
import App from "./App.vue";
import Antd from "ant-design-vue";
import "ant-design-vue/dist/antd.css";
import router from "./router/index";
// import store from "./store";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import { LoadingPlugin } from "vue-loading-overlay";
import "vue-loading-overlay/dist/css/index.css";

const app = createApp(App);
app.use(Antd);
// app.use(store);
app.use(router);
app.use(LoadingPlugin);
app.mount("#app");
