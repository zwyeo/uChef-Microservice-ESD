<template>
  <div class="card card-style animate__animated animate__bounceIn">
    <img :src="img" class="img-style" :alt="title" />
    <div class="card-body">
      <div class="receipe-content">
        <h5>{{ title }}</h5>

        <div class="ratings">
          <div v-if="ratings == null || ratings == 4">
            <i class="fa fa-star" aria-hidden="true"></i>
            <i class="fa fa-star" aria-hidden="true"></i>
            <i class="fa fa-star" aria-hidden="true"></i>
            <i class="fa fa-star" aria-hidden="true"></i>
            <i class="fa fa-star-o" aria-hidden="true"></i>
          </div>

          <div v-if="ratings != null && ratings == 0">
            <i class="fa fa-star-o" aria-hidden="true"></i>
            <i class="fa fa-star-o" aria-hidden="true"></i>
            <i class="fa fa-star-o" aria-hidden="true"></i>
            <i class="fa fa-star-o" aria-hidden="true"></i>
            <i class="fa fa-star-o" aria-hidden="true"></i>
          </div>

          <div v-if="ratings != null && ratings == 1">
            <i class="fa fa-star" aria-hidden="true"></i>
            <i class="fa fa-star-o" aria-hidden="true"></i>
            <i class="fa fa-star-o" aria-hidden="true"></i>
            <i class="fa fa-star-o" aria-hidden="true"></i>
            <i class="fa fa-star-o" aria-hidden="true"></i>
          </div>

          <div v-if="ratings != null && ratings == 2">
            <i class="fa fa-star" aria-hidden="true"></i>
            <i class="fa fa-star" aria-hidden="true"></i>
            <i class="fa fa-star-o" aria-hidden="true"></i>
            <i class="fa fa-star-o" aria-hidden="true"></i>
            <i class="fa fa-star-o" aria-hidden="true"></i>
          </div>

          <div v-if="ratings != null && ratings == 3">
            <i class="fa fa-star" aria-hidden="true"></i>
            <i class="fa fa-star" aria-hidden="true"></i>
            <i class="fa fa-star" aria-hidden="true"></i>
            <i class="fa fa-star-o" aria-hidden="true"></i>
            <i class="fa fa-star-o" aria-hidden="true"></i>
          </div>

          <div v-if="ratings != null && ratings == 5">
            <i class="fa fa-star" aria-hidden="true"></i>
            <i class="fa fa-star" aria-hidden="true"></i>
            <i class="fa fa-star" aria-hidden="true"></i>
            <i class="fa fa-star" aria-hidden="true"></i>
            <i class="fa fa-star" aria-hidden="true"></i>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  // to add ratings props!!
  data() {
    return {
      ratings: null,
    }
  },
  props: ["title", "img", "id"],
  created() {
    //Rating
    //Rating
    axios
      .get(
        `https://wad-proj-22042-default-rtdb.asia-southeast1.firebasedatabase.app/recipes/${this.id}.json`
      )
      .then((response) => {
        if (response.data != null) {
          console.log(response.data);
          var total_rating = 0;
          var num_of_rating = 0;
          for (let review in Object.values(response.data)[0]) {
            // console.log(Object.values(response.data)[0][review].rating)
            total_rating += Number(
              Object.values(response.data)[0][review].rating
            );
            num_of_rating++;
          }
          var rating = total_rating / num_of_rating;
          var remainder = rating % 1;
          if (remainder == 0) {
            this.ratings = rating;
          } else if (remainder >= 0.5) {
            this.ratings = Math.ceil(rating);
          } else {
            this.ratings = Math.floor(rating);
          }
        }
      })
      .catch((error) => {
        console.log(error);
      });
  }
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

.card-style:hover {
  transform: scale(0.98);
  /* Scaling button to 0.98 to its original size */
  box-shadow: 3px 2px 22px 1px rgba(0, 0, 0, 0.24);
  /* Lowering the shadow */
  box-shadow: 70%;
}

/* Section Heading */

.best-receipe-area {
  position: relative;
  z-index: 1;
  padding-bottom: 50px;
}

.single-best-receipe-area {
  position: relative;
  z-index: 1;
}

.img-style {
  border-bottom: 3px solid #40ba37;
  width: 100%;
  height: 25em;
  object-fit: cover;
}

.receipe-content {
  padding-top: 30px;
  text-align: center;
}

.receipe-content h5 {
  font-size: 18px;
  margin-bottom: 10px;
  font-weight: 400;
  -webkit-transition-duration: 500ms;
  transition-duration: 500ms;
}

.receipe-content h5:hover,
.receipe-content h5:focus {
  color: #40ba37;
}

.ratings i {
  font-size: 11px;
  color: #fbb710;
  display: inline-block;
  padding: 0 1px;
}

/* remove padding from card-style class when in mobile view */
@media (max-width: 768px) {
  .card-style {
    padding: 0;
  }
}
</style>

<!-- <div class="card card-css p-2" style="width: 18rem">
  <img :src="img" class="card-img-top" :alt="title" />
  <div class="card-body">
    <h5 class="card-title">{{ title }}</h5>
    <p class="card-text">Delicious</p>
  </div>
</div> -->

<!-- .card-css {
  cursor: pointer;

  font-size: 16px;
  background-color: #808080;
  color: #fff;
  border-radius: 5px;
  box-shadow: 7px 6px 28px 1px rgba(0, 0, 0, 0.24);
  cursor: pointer;
  outline: none;
  transition: 0.2s all;
}
/* Adding transformation when the button is active */

.card-css:hover {
  transform: scale(0.98);
  /* Scaling button to 0.98 to its original size */
  box-shadow: 3px 2px 22px 1px rgba(0, 0, 0, 0.24);
  /* Lowering the shadow */
  box-shadow: 70%;
} -->
