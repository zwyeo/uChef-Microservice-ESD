<template>
  
  <div class="container-fluid px-5">
    <nav-bar></nav-bar>
    <div v-if="supermarket == 'Cold Storage'">
      <div
        class="text-center my-3"
        animate__animated
        animate__backInLeft
        animate__fast
      >
        <img src="../assets/cold_storage.png" alt="" class="w-25" />
      </div>
    </div>
    <div v-if="supermarket == 'Fairprice'">
      <div
        class="text-center my-3 animate__animated animate__backInLeft animate__fast"
      >
        <img src="../assets/fairprice.png" alt="" class="w-25" />
      </div>
    </div>
    <div v-if="success == false">
      <div
        class="my-3 text-center animate__animated animate__backInLeft animate__fast"
      >
        <h2>
          Sorry. Both Fairprice and Cold Storage are out of stock of the items.
        </h2>

        <!-- RECOMMENDED FOR YOU SECTION -->
        <h3 class="text-center p-5 mt-4">
          You may try other recommended recipes below:
        </h3>
        <div class="row d-flex justify-content-center">
          <div
            v-for="recipe in recommendations"
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
              >
              </recipe-card>
            </router-link>
          </div>
        </div>
      </div>
    </div>

    <div class="container mx-auto row animate__animated animate__backInLeft">
      <div v-for="order in order_info.order" :key="order.item" class="col-sm-6">
        <ingredient-card
          class="text-center mx-5 my-3"
          :ing="order.item"
          :price="order.price"
        ></ingredient-card>
      </div>
    </div>

    <!-- Modal component to checkout -->
    <!-- Button trigger modal -->
    <div v-if="supermarket == 'Cold Storage'" class="text-center">
      <button
        type="button"
        class="btn btn-primary btn-lg my-3"
        data-bs-toggle="modal"
        data-bs-target="#exampleModal"
      >
        Confirm Cart
      </button>
    </div>

    <div v-if="supermarket == 'Fairprice'" class="text-center">
      <button
        type="button"
        class="btn btn-primary btn-lg my-3"
        data-bs-toggle="modal"
        data-bs-target="#exampleModal"
      >
        Confirm Cart
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
            <h1 class="modal-title fs-5" id="exampleModalLabel">
              Confirm Cart
            </h1>
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
              <tr v-for="order in order_info.order" :key="order.item">
                <td class="fw-bold">{{ order.item }}</td>
                <td>Qty:1</td>
                <td>${{ order.price }}</td>
              </tr>
              <tr>
                <th class="text-success lead fw-bold">Total Price</th>
                <td></td>
                <th class="text-success lead fw-bold">${{ total_price }}</th>
              </tr>
            </table>
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              Close
            </button>
            <div>
              <stripe-checkout
                v-if="isStripe"
                ref="checkoutRef"
                :pk="publishableKey"
                :session-id="sessionId"
              />
              <button type="button" @click="checkout()" class="btn btn-primary">
                Checkout Now
                <span
                  v-if="loading"
                  class="spinner-border spinner-border-sm btn-spin"
                ></span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { StripeCheckout } from "@vue-stripe/vue-stripe";
import IngredientCard from "../components/IngredientCard.vue";
import NavBar from "../components/NavBar.vue";
import RecipeCard from "../components/RecipeCard.vue";

export default {
  name: "Order",
  components: {
    IngredientCard,
    StripeCheckout,
    NavBar,
    RecipeCard,
  },
  props: ["id"],
  data() {
    this.publishableKey =
      "pk_test_51MmDHTHHejWNjfqntLejqcMX51NluqXRdlSjEjvITvO2J14WdSXuxZVuv7Ftus56wnevZCTbchpqXXRwCNz8pxKZ00Xw45r97j";
    return {
      ingredient_list: [],
      order_info: {},
      recommendations: [],
      supermarket: null,
      total_price: null,
      loading: false,
      sessionId: null,
      success: false,
      isStripe: null,
      categorySelected: null,
    };
  },

  created() {
    this.ingredient_list = this.$store.state.ingredient_list;

    // this is to clean up the ingredient names
    var ingredientName = [];
    const filter_words = [
      "1lb",
      "tbs",
      "cup",
      "tsp",
      "tbsp",
      "1/2",
      "1/3",
      "1/4",
      "1/8",
      "cups",
      "oz",
      "100g",
      "300g",
      "500g",
      "bunch",
      "cloves",
      "Large",
    ];

    this.ingredient_list.forEach((ing) => {
      let word_arr = ing.split(" ");
      for (var i = 0; i < word_arr.length; i++) {
        if (!isNaN(word_arr[i])) {
          word_arr.splice(i, 1);
        }
        if (filter_words.includes(word_arr[i])) {
          word_arr.splice(i, 1);
        }
        if (word_arr[i] === "") {
          word_arr.splice(i, 1);
        }
        if (filter_words.includes(word_arr[i])) {
          word_arr.splice(i, 1);
        }
      }
      const str = word_arr.join(" ");
      ingredientName.push(str);
      this.ingredient_list = ingredientName;
    });
    this.$store.state.ingredient_list = this.ingredient_list = ingredientName;
    console.log(this.ingredient_list, "These are the ingredients");

    // Connect to the supermarket API and get the order info
    axios
      // .post("http://127.0.0.1:5001/delivery", {
        .post("http://localhost:8000/api/v1/delivery", {
        items: this.ingredient_list,
        category: this.$store.state.category,
        id: this.id,
        headers: {
          'Content-Type': 'application/json'
        }  
      })
      .then((res) => {
        this.order_info = res.data;
        console.log(this.order_info, "this is the returned data!!");
        if (res.data.success) {
          this.supermarket = res.data.supermarket;
          if (res.data.totalprice != null) {
            this.total_price = res.data.totalprice.toFixed(2);
          }

          this.success = res.data.success;
        } else {
          this.recommendations = res.data.recommended;
        }
      })
      .catch((err) => console.log(err));
  },
  methods: {
    checkout() {
      this.isStripe = true;
      this.loading = true;
      const orders = JSON.parse(JSON.stringify(this.order_info.order));
      const orderDict = { order: orders };
      // console.log({ orders: this.order_info.order });
      axios
        .post("http://127.0.0.1:5005/create-checkout-session", orderDict)
        // .post("http://localhost:8000/api/v1/create-checkout-session", orderDict)
        .then((response) => {
          console.log(response);
          this.sessionId = response.data.sessionId;
          this.$store.state.delivery = true;
          // console.log(this.sessionId);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  watch: {
    sessionId(newSession, oldSession) {
      this.$refs.checkoutRef.redirectToCheckout();
      this.loading = false;
    },
  },
};
</script>

<style></style>
