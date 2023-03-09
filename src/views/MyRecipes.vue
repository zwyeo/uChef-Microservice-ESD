<template>
  <div class="container-fluid px-5">
    <nav-bar></nav-bar>
    <h2 class="text-center p-5">My Recipes</h2>
    <div v-if="recipes.length != 0" class="row d-flex justify-content-center">
      <div v-for="recipe in recipes" :key="recipe.id" class="col-xl-4 col-md-6">
        <router-link :to="{ name: 'recipe-details', params: { id: recipe.id } }">

          <recipe-card-special
            :title="recipe.title"
            :img="recipe.image"
            :id="recipe.id"
            class="mb-5"
          ></recipe-card-special>
          
        </router-link>
      </div>
    </div>
    <div v-else class="row">
      <div class="col d-flex justify-content-center">
        <img style="width: 500px; height: 500px;" src="../assets/img/core-img/noRecipes.png" alt="">
      </div>
    </div>
    <router-link :to="{ name: 'add-recipe-page'}">
      <button
        class="btn btn-primary btn-circle btn-xl"
        style="padding: 0.1%; position: fixed; bottom: 20px; right: 20px"
      >
        +
      </button>
    </router-link>
  </div>
  <h4 class="mt-5 mx-5"></h4>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import RecipeCard from "@/components/RecipeCard.vue";
import RecipeCardSpecial from "../components/RecipeCardSpecial.vue";
import RemoveRecipe from "../components/RemoveRecipe.vue";
import { getDatabase, ref, onValue } from "firebase/database";
import AddRecipePage from "./AddRecipePage.vue";

export default {
  name: "MyRecipes",
  data() {
    return {
      recipes: []
    }
  },
  components: {
    NavBar,
    RecipeCard,
    RecipeCardSpecial,
    RemoveRecipe,
    AddRecipePage
  },
  methods: {
    getRecipes() {
      let userId = this.$store.state.userId;
      const db = getDatabase();
      // console.log(db);
      const usersRef = ref(db, `users/${userId}/recipes`);

      onValue(usersRef, (snapshot) => {
        if (snapshot.exists()) {
          const data = snapshot.val();
          this.recipes = data;
          console.log(this.recipes);
        } else {
          console.log("no data exists");
        }
      })
    }
  },
  mounted() {
    // console.log("mounted");
    this.getRecipes();
  }

};
</script>

<style>
.btn-circle {
  width: 30px;
  height: 30px;
  padding: 6px 0px;
  border-radius: 15px;
  text-align: center;
  font-size: 12px;
  line-height: 1.42857;
}

.btn-circle.btn-xl {
  width: 70px;
  height: 70px;
  padding: 10px 16px;
  border-radius: 35px;
  font-size: 24px;
  line-height: 1.33;
}

a {
  text-decoration: none;
}
</style>
