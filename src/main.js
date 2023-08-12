import "bootstrap/dist/css/bootstrap.css";
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import axiosInstance from "./utils/axios"

const app = createApp(App);

app.use(router);
app.config.globalProperties.$axios = axiosInstance;

app.mount("#app");
