<template>
  <br />
  Sort By:
  <br />
  <input
    type="radio"
    id="health"
    value="healthiness"
    name="sort"
    @click="sortSet"
  />
  <label for="health">Healthy✅</label>
  <br />
  <input
    type="radio"
    id="popul"
    value="popularity"
    name="sort"
    @click="sortSet"
  />
  <label for="popul">Popularity⭐️</label>
  <br />
  <input type="radio" id="price" value="price" name="sort" @click="sortSet" />
  <label for="price">Price💰</label>
  <br />
  <br />
  Filter by:
  <select v-model="selectedFilter">
    <option v-for="category of $store.state.categories" :value="category">
      {{ category }}
    </option>
  </select>

  <div v-if="$store.state.selectedCategory == 'Nutrition'">
    <br />
    Calories<input type="number" v-model="inputedCalories" />
    <br />
    <br />
    <button @click="$store.dispatch('nutritionFilterBlank')">
      Filter Calories for ALL food
    </button>
  </div>
  <div v-if="$store.state.selectedCategory == 'Prep Time'">
    <br />
    Max time taken to cook<input type="number" v-model="inputedMaxTime" />
  </div>
  <div v-if="$store.state.selectedCategory == 'Allergy'">
    <br />
    Exclude these foods:
    <button value="dairy" @click="allergyCheck">Dairy 🥛</button>
    <button value="egg" @click="allergyCheck">Eggs 🍳</button>
    <button value="seafood" @click="allergyCheck">Seafood 🐟</button>
    <button value="soy" @click="allergyCheck">Soy 🫘</button>
  </div>
  <br />
  <div>
    <h2>Build Your Meal</h2>
    <button @click="$store.commit('searchByIngredients')">Ingredients👨‍🍳</button>
    Idk how to compare both arrays and use filters
  </div>
  <h2>Preview</h2>
  {{ $store.state.previews }}
  <h2>Recipes</h2>
  {{ $store.state.recipes }}
</template>

<script>
export default {
  components: {},
  computed: {
    selectedFilter: {
      get() {
        // console.log(this.$store.state.selectedCategory);
        return this.$store.state.selectedCategory;
      },
      set(selectedCategory) {
        // console.log(selectedCategory);
        this.$store.dispatch("setCategory", selectedCategory);
      },
    },
    inputedCalories: {
      get() {
        return this.$store.state.calories;
      },
      set(setCalories) {
        this.$store.dispatch("setCalories", setCalories);
      },
    },
    inputedMaxTime: {
      get() {
        return this.$store.state.maxtime;
      },
      set(setMaxTime) {
        this.$store.dispatch("setMaxTime", setMaxTime);
      },
    },
  },
  methods: {
    allergyCheck() {
      this.$store.state.selectedAllergies.push(event.target.value);
      console.log(this.$store.state.selectedAllergies.join());
    },
    sortSet() {
      this.$store.state.sortBy = event.target.value;
    },
  },
};
</script>

<style></style>
