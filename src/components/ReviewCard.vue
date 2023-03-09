<template>
  <div class="container-fluid mx-auto">
    <div class="card">
      <div class="row d-flex">
        <div class="d-flex flex-column">
          <h3 class="mt-2 mb-0">
            {{ user }}<span class="fs-6 text-muted float-end">{{ date }}</span>
          </h3>
          <div>
            <p class="text-left">
              <span class="text-muted">{{ rating }}.0</span>
              <span v-if="rating == '5'"
                ><span class="fa fa-star star-active ml-3"></span>
                <span class="fa fa-star star-active"></span>
                <span class="fa fa-star star-active"></span>
                <span class="fa fa-star star-active"></span>
                <span class="fa fa-star star-active"></span
              ></span>
              <span v-if="rating == '4'"
                ><span class="fa fa-star star-active ml-3"></span>
                <span class="fa fa-star star-active"></span>
                <span class="fa fa-star star-active"></span>
                <span class="fa fa-star star-active"></span>
                <span class="fa fa-star star-inactive"></span
              ></span>
              <span v-if="rating == '3'"
                ><span class="fa fa-star star-active ml-3"></span>
                <span class="fa fa-star star-active"></span>
                <span class="fa fa-star star-active"></span>
                <span class="fa fa-star star-inactive"></span>
                <span class="fa fa-star star-inactive"></span
              ></span>
              <span v-if="rating == '2'"
                ><span class="fa fa-star star-active ml-3"></span>
                <span class="fa fa-star star-active"></span>
                <span class="fa fa-star star-inactive"></span>
                <span class="fa fa-star star-inactive"></span>
                <span class="fa fa-star star-inactive"></span
              ></span>
              <span v-if="rating == '1'"
                ><span class="fa fa-star star-active ml-3"></span>
                <span class="fa fa-star star-inactive"></span>
                <span class="fa fa-star star-inactive"></span>
                <span class="fa fa-star star-inactive"></span>
                <span class="fa fa-star star-inactive"></span
              ></span>
            </p>
          </div>
        </div>
      </div>
      <div class="row text-left">
        <h4 class="blue-text mt-3">"{{ subject }}"</h4>
        <p class="content">
          {{ message }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ReviewCard",
  props: ["id", "user", "rating", "date", "subject", "message"],
  data() {
    return {};
  },
};
</script>

<style lang="scss" scoped>
body {
  background-image: linear-gradient(#4a148c, #e53935);
  background-repeat: no-repeat;
  color: #000;
  overflow-x: hidden;
}

a {
  text-decoration: none !important;
  color: inherit;
}

a:hover {
  color: #455a64;
}

.card {
  border-radius: 5px;
  background-color: #fff;
  padding-left: 60px;
  padding-right: 60px;
  margin-top: 30px;
  padding-top: 30px;
  padding-bottom: 30px;
}

.star-active {
  color: #fbc02d;
  margin-top: 10px;
  margin-bottom: 10px;
}

.star-active:hover {
  color: #f9a825;
  cursor: pointer;
}

.star-inactive {
  color: #cfd8dc;
  margin-top: 10px;
  margin-bottom: 10px;
}

.blue-text {
  color: #0091ea;
}

.content {
  font-size: 18px;
}
</style>
