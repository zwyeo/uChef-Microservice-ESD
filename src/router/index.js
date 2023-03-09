import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import MyRecipes from "../views/MyRecipes.vue";
import MyBookmarks from "../views/MyBookmarks.vue";
import RecipeDetails from "../views/RecipeDetails.vue";
import SearchResults from "../views/SearchResults.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import AddRecipePage from "../views/AddRecipePage.vue";
import UpdateRecipePage from "../views/UpdateRecipePage.vue";
import store from "@/store";

import * as firebase from "firebase/app";
import { getAuth, onAuthStateChanged } from "firebase/auth";

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/login",
    name: "login",
    component: Login,
  },
  {
    path: "/register",
    name: "register",
    component: Register,
  },
  {
    path: "/my-recipes",
    name: "my-recipes",
    component: MyRecipes,
    meta: { requriesAuth: true },
  },
  {
    path: "/my-bookmarks",
    name: "my-bookmarks",
    component: MyBookmarks,
    meta: { requriesAuth: true },
  },
  {
    path: "/recipe-details/:id",
    name: "recipe-details",
    component: RecipeDetails,
    props: true,
  },
  {
    path: "/search-results",
    name: "search-results",
    component: SearchResults,
  },
  {
    path: "/update-recipe-page/:id",
    name: "update-recipe-page",
    component: UpdateRecipePage,
    props: true,
  },
  {
    path: "/add-recipe-page",
    name: "add-recipe-page",
    component: AddRecipePage,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
    return savedPosition || { top: 0 };
  },
});

// NAVIGATION GAURDS
router.beforeEach((to, from, next) => {
  const requriesAuth = to.matched.some((record) => record.meta.requriesAuth);
  console.log(to, from);
  const isAuthenthicated = getAuth().currentUser;
  if (requriesAuth && !isAuthenthicated) {
  } else {
    next();
  }
});

router.afterEach((to, from, next) => {
  // console.log(to.name);
  // console.log(store.state.routeName);
  store.state.routeName = to.name;
});

export default router;
