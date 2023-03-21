<template>
  <h1 class="text-center mt-5">Order page</h1>

  <div class="container mx-auto row">
    <div
      v-for="ingredient in ingredient_list"
      :key="ingredient"
      class="col-sm-6"
    >
      <ingredient-card
        class="text-center mx-5 my-3"
        :ing="ingredient"
      ></ingredient-card>
    </div>
  </div>

  <!-- Modal component to checkout -->
  <!-- Button trigger modal -->
  <div class="text-center">
    <button
      type="button"
      class="btn btn-primary btn-lg my-3"
      data-bs-toggle="modal"
      data-bs-target="#exampleModal"
    >
      Deliver Now!
    </button>
  </div>

  <!-- Modal -->
  <div
    class="modal fade"
    id="exampleModal"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Confirm Cart</h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <h3>Ingredient list</h3>
          <!-- <div
            v-for="ingredient in ingredient_list"
            class="d-flex justify-content-around"
            :key="ingredient"
          >
            {{ ingredient }}
            <div>Qty:1</div>
          </div> -->
          <table class="table table-striped-columns">
            <tr v-for="ingredient in ingredient_list" :key="ingredient">
              <td class="fw-bold ms-2">{{ ingredient }}</td>
              <td>Qty:1</td>
            </tr>
          </table>

          <hr />
          <form>
            <div class="mb-3">
              <label for="exampleInputEmail1" class="form-label">Address</label>
              <input
                type="text"
                class="form-control mb-2"
                placeholder="Street Address"
              />
              <div class="d-flex">
                <input
                  type="text"
                  class="form-control mb-2"
                  placeholder="City"
                />
                <input
                  type="number"
                  class="form-control mb-2"
                  placeholder="Postal Code"
                />
              </div>
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
          >
            Close
          </button>
          <button
            type="button"
            @click="connectSupermarket()"
            class="btn btn-primary"
          >
            Connect to Supermarket!
          </button>
        </div>
      </div>
    </div>
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
  methods: {
    connectSupermarket() {
      // talk to the backend
      // pass the ingredients data to the backend
      // **backend will check which supermarket to use (FP or CS)
      // **backend will return the supermarket and the price of each ingredient
      // ** backend will return stock status
      // if got stock, then return supermarket and price
      // if no stock, error handling from error microservice
      // With the price data, will route to another page (Payment) for customer to confirm payment
    },
  },
};
</script>

<style></style>
