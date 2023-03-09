<template>
  <div class="container-fluid px-5">
    <nav-bar></nav-bar>
    <!-- START OF TAB -->
    <div class="text-center">
      <div class="btn-group">
        <a
          class="btn"
          @click="setsearchp"
          id="probtn"
          style="background-color: green; color: white"
          >Professional</a
        >
        <a class="btn" @click="setsearchc" id="cbtn">uChef Community</a>
      </div>
    </div>
    <!-- END OF TAB -->
    <h2 class="text-center p-5">
      <span v-if="$store.state.queryParam.length > 0">
        You searched for:"{{ this.$store.state.queryParam }}"</span
      >
    </h2>

    <!-- FOR PROFESSIONAL TAB -->
    <div
      v-if="this.$store.state.setsearch == 'professional'"
      class="row d-flex justify-content-center"
    >
      <div
        v-for="recipe in $store.state.recipes.meals"
        :key="recipe.idMeal"
        class="col-xl-4 col-md-6"
      >
        <router-link
          :to="{ name: 'recipe-details', params: { id: recipe.idMeal } }"
        >
          <recipe-card
            :title="recipe.strMeal"
            :img="recipe.strMealThumb"
            :id="recipe.idMeal"
            class="mb-5"
          ></recipe-card>
        </router-link>
      </div>
    </div>
    <div
      v-if="
        this.$store.state.setsearch == 'professional' &&
        this.$store.state.recipes.meals == null
      "
      class="row d-flex justify-content-center"
    >
      <div class="col d-flex justify-content-center">
        <img
          src="../assets/img/core-img/noSearchResults.png"
          style="width: 500px; height: 500px"
          alt=""
        />
      </div>
    </div>

    <!-- FOR COMMUNITY TAB -->
    <div
      v-if="this.$store.state.setsearch == 'community'"
      class="row d-flex justify-content-center"
    >
      <div
        v-for="recipe in $store.state.commsearchrecipes"
        :key="recipe.id"
        class="col-xl-4 col-md-6"
      >
        <router-link
          :to="{ name: 'recipe-details', params: { id: recipe.id } }"
        >
          <recipe-card
            :title="recipe.title"
            :img="recipe.image"
            :id="recipe.id"
            class="mb-5"
          ></recipe-card>
        </router-link>
      </div>
    </div>
    <div
      v-if="
        this.$store.state.setsearch == 'community' &&
        Object.keys(this.$store.state.commsearchrecipes).length === 0
      "
      class="row d-flex justify-content-center"
    >
      <div class="col d-flex justify-content-center">
        <img
          src="../assets/img/core-img/noSearchResults.png"
          style="width: 500px; height: 500px"
          alt=""
        />
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import RecipeCard from "@/components/RecipeCard.vue";
export default {
  name: "SearchResults",
  components: {
    NavBar,
    RecipeCard,
  },
  data() {
    return {};
  },
  created() {},
  methods: {
    // getRecipe() {
    //   //   console.log(this.$store.state.recipes);
    //   //   for (let recipe of this.$store.state.recipes) {
    //   //     console.log(recipe);
    //   //     console.log(recipe.id, recipe.title, recipe.image);
    //   //   }
    //   console.log(this.$store.state.commsearchrecipes);
    //   for (let recipe of this.$store.state.commsearchrecipes) {
    //     console.log(recipe);
    //     console.log(recipe.id, recipe.title, recipe.image);
    //   }
    // },
    setsearchc() {
      this.$store.state.setsearch = "community";
      console.log(this.$store.state.setsearch);
      //   console.log(event.target);
      event.target.style.backgroundColor = "green";
      event.target.style.color = "white";
      document.getElementById("probtn").style.backgroundColor = "white";
      document.getElementById("probtn").style.color = "black";

      // if (this.$store.state.queryParam)
      //   this.$store.dispatch("getCommunityRecipeBySearch");
    },
    setsearchp() {
      this.$store.state.setsearch = "professional";
      console.log(this.$store.state.setsearch);
      event.target.style.backgroundColor = "green";
      event.target.style.color = "white";
      document.getElementById("cbtn").style.backgroundColor = "white";
      document.getElementById("cbtn").style.color = "black";

      // this.$store.dispatch("getRecipeBySearch");
    },
  },
};
</script>

<style lang="scss" scoped>
.recipe-card-style {
  padding-left: 5em;
  padding-right: 5em;
}

/* Start */

@media (max-width: 768px) {
  .recipe-card-style {
    padding: 0;
  }
}
</style>
