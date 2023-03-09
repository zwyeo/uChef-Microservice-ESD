<template>
  <div class="container-fluid px-5">
    <nav-bar></nav-bar>
    <h2 class="text-center p-5">My Bookmarks</h2>
    <div v-if="bookmarks.length != 0" class="row d-flex justify-content-center">
      <div v-for="(recipe, id) in bookmarks" :key="recipe" class="col-xl-4 col-md-6">
        <router-link :to="{ name: 'recipe-details', params: { id: id } }">
          <recipe-card v-for="elements in recipe" :title="elements.title" :img="elements.image" :id="id"
            :key="elements.title" class="mb-5">
          </recipe-card>

        </router-link>
      </div>
      <!-- <button class="btn btn-primary" v-on:click="getBookmarks">Click me</button> -->
    </div>
    <div v-else class="row">
      <div class="col d-flex justify-content-center">
        <img style="width: 500px; height: 500px" src="../assets/img/core-img/noBookmarks.png" alt="" />
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import RecipeCard from "@/components/RecipeCard.vue";
import { getDatabase, ref, onValue } from "firebase/database";

export default {
  name: "MyBookmark",
  data() {
    return {
      bookmarks: [],
    };
  },
  components: {
    NavBar,
    RecipeCard,
  },
  methods: {
    getBookmarks() {
      let userId = this.$store.state.userId;
      const db = getDatabase();
      // console.log(db);
      const usersRef = ref(db, `users/${userId}/bookmarks`);

      onValue(usersRef, (snapshot) => {
        if (snapshot.exists()) {
          const data = snapshot.val();
          this.bookmarks = data;
          // console.log(this.bookmarks);
        } else {
          console.log("no data exists");
        }
      });
    },
  },
  mounted() {
    this.getBookmarks();
  },
};
</script>

<style>
  a {
    text-decoration: none;
  }
</style>
