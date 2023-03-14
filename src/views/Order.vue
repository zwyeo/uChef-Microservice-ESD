<template>
  <h1 class="text-center mt-5">Order page</h1>

  <button class="btn btn-primary">Proceed to Payment</button>

  <div v-for="ingredient in ingredient_list" :key="ingredient" class="col-sm-3">
    <ingredient-card :ing="ingredient"></ingredient-card>
  </div>
</template>

<script>
import axios from "axios";
import IngredientCard from "../components/IngredientCard.vue";
export default {
  name: "Order",
  components: {
    IngredientCard,
  },
  props: ["id"],
  data() {
    return {
      ingredient_list: [],
    };
  },
  created() {
    this.ingredient_list = this.$store.state.ingredient_list;
    console.log(this.ingredient_list);
  },
  methods: {},
};
</script>

<style></style>
