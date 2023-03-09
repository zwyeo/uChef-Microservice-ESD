<template>
  <h1>Order page</h1>
  Need to pass ingredient props over
</template>

<script>
import axios from "axios";
export default {
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
