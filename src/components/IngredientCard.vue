<template>
  <div class="card-style">
    <div class="fw-bold">
      <img
        src="../assets/img/core-img/salad.png"
        class="ingredient-img my-2 mx-2"
      />
      {{ ing }}
      <p>[Show FP logo and price]</p>
    </div>

    <div class="d-flex justify-content-center">
      <div class="me-2">Qty: {{ qty }}</div>
      <button class="btn btn-primary me-1 mb-3" @click="increaseQty()">
        +
      </button>
      <button class="btn btn-secondary me-2 mb-3" @click="decreaseQty()">
        -
      </button>
      <button class="btn btn-danger mb-3" @click="remove()">X</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      qty: 1,
    };
  },
  props: ["ing"],
  methods: {
    increaseQty() {
      this.qty++;
    },
    decreaseQty() {
      if (this.qty != 0) this.qty--;
    },
    remove() {},
  },
};
</script>

<style scoped>
.card-style {
  cursor: pointer;
  font-size: 16px;
  /* background-color: #f6f6c9; */
  color: #40ba37;
  border-radius: 5px;
  box-shadow: 7px 6px 28px 1px rgba(0, 0, 0, 0.24);
  cursor: pointer;
  outline: none;
  transition: 0.2s all;
}
.ingredient-img {
  width: 50px;
  position: relative;
}
</style>
