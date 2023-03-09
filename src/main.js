import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import { initializeApp } from "firebase/app";
import { getAuth, onAuthStateChanged } from "firebase/auth";
import "animate.css";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: process.env.VUE_APP_FIREBASE_API,
  authDomain: process.env.VUE_APP_FIREBASE_AUTH_DOMAIN,
  databaseURL: process.env.VUE_APP_FIREBASE_URL,
  projectId: process.env.VUE_APP_FIREBASE_PROJECT_ID,
  storageBucket: process.env.VUE_APP_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.VUE_APP_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.VUE_APP_FIREBASE_APP_ID,
};

// Initialize Firebase
initializeApp(firebaseConfig);
const auth = getAuth();

let app;

onAuthStateChanged(auth, (user) => {
  // console.log("user", user);
  if (!app) {
    app = createApp(App).use(store).use(router).mount("#app");
    store.state.userId = user.uid;
    store.state.userName = user.displayName;
  }
});
