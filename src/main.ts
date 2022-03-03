import { createApp } from "vue"
import App from "./App.vue"
import router from "./router"
import store from "./store"
import './main.css'

import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import {
    faSwimmingPool,
    faArrowLeft,
    faArrowRight,
    faEnvelope,
    faPhone,
    faMapMarker,
} from "@fortawesome/free-solid-svg-icons";
import {
    faFacebookF,
    faWhatsapp,
    faInstagram,
} from "@fortawesome/free-brands-svg-icons";

library.add(faMapMarker);
library.add(faPhone);
library.add(faEnvelope);
library.add(faFacebookF);
library.add(faInstagram);
library.add(faWhatsapp);
library.add(faSwimmingPool);
library.add(faArrowLeft);
library.add(faArrowRight);

createApp(App)
    .use(store)
    .use(router)
    .component("font-awesome-icon", FontAwesomeIcon)
    .mount("#app");
