<template>
  <div class="container-fluid px-5">
    <nav-bar></nav-bar>
    <h2 class="text-center p-5">My Delivery</h2>
    <div v-if="!this.orderID" class="row">
      <div class="col d-flex justify-content-center">
        <img
          style="width: 500px; height: 500px"
          src="../assets/img/core-img/noDeliveries.png"
          alt=""
        />
      </div>
    </div>
    <div v-else class="row">
      <div class="d-flex justify-content-evenly mb-5">
        <div class=""><span class="fw-bold">OrderID: </span>{{ orderID }}</div>
        <div class="fw-bold">ETA: {{ eta }}</div>
        <div class=""><span class="fw-bold">Total Paid: </span>{{ price }}</div>
      </div>

      <div class="text-center d-flex justify-content-evenly mt-5">
        <div>
          <img src="../assets/pkg.png" alt="" width="50" />
          <p class="fw-bold text-success">
            {{ message }}
          </p>
        </div>

        <p class="mt-4 text-success fw-bold">{{ time }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import axios from "axios";

export default {
  name: "MyDelivery",
  components: {
    NavBar,
  },
  data() {
    return {
      orderID: null,
      price: null,
      eta: null,
      message: null,
      time: null,
    };
  },
  created() {
    // If there is data in firebase, it will retrieve, else no deliveries
    let url = `https://esd-uchef-restore-default-rtdb.asia-southeast1.firebasedatabase.app/order.json`;
    axios.get(url).then((res) => {
      const data = JSON.parse(res.data["101"]);
      console.log(data);
      this.orderID = data["orderID"];
      this.message = data["message"];
      this.price = data["price"];
      this.eta = data["eta"];
      this.time = data["time"];
    });
  },
};
</script>

<style></style>
