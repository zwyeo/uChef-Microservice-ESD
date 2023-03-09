<template>
  <div
    id="carouselExampleCaptions"
    class="carousel slide carousel-fade"
    data-bs-ride="false"
  >
    <div class="carousel-indicators">
      <button
        type="button"
        data-bs-target="#carouselExampleCaptions"
        data-bs-slide-to="0"
        class="active"
        aria-current="true"
        aria-label="Slide 1"
      ></button>
      <button
        type="button"
        data-bs-target="#carouselExampleCaptions"
        data-bs-slide-to="1"
        aria-label="Slide 2"
      ></button>
      <button
        type="button"
        data-bs-target="#carouselExampleCaptions"
        data-bs-slide-to="2"
        aria-label="Slide 3"
      ></button>
      <button
        type="button"
        data-bs-target="#carouselExampleCaptions"
        data-bs-slide-to="3"
        aria-label="Slide 4"
      ></button>
      <button
        type="button"
        data-bs-target="#carouselExampleCaptions"
        data-bs-slide-to="4"
        aria-label="Slide 5"
      ></button>
      <button
        type="button"
        data-bs-target="#carouselExampleCaptions"
        data-bs-slide-to="5"
        aria-label="Slide 6"
      ></button>
    </div>
    <div class="carousel-inner">
      <div class="carousel-item active" data-bs-interval="2000">
        <img
          src="../assets/img/banner-img/chicken-category.jpg"
          class="d-block w-100"
          alt="..."
          style="height: 800px; object-fit: cover"
        />
        <div
          class="carousel-caption d-none d-md-block animate__animated animate__fadeInUp animate__delay-2 animate__slow carousel-label"
        >
          <h2
            class="animate__animated animate__fadeInUp animate__delay-4 animate__slower"
          >
            Chicken
          </h2>
          <p
            class="animate__animated animate__fadeInUp animate__delay-5 animate__slower carousel-text"
          >
            When it comes to both popularity and variety, there are few foods
            that can compete with chicken. As a staple in the diet of billions
            of people around the globe, chicken is enjoyed and revered primarily
            because of the many ways it can be cooked. Whether it be grilled,
            broiled, or fried, the possibilities are nearly endless when it
            comes to creating a mouth-watering serving of chicken.
          </p>
          <button class="text-btn" @click="searchCategory('chicken')">
            See Chicken Category
          </button>
        </div>
      </div>
      <div class="carousel-item" data-bs-interval="2000">
        <img
          src="../assets/img/banner-img/beef-category.jpg"
          class="d-block w-100"
          alt="..."
          style="height: 800px; object-fit: cover"
        />
        <div
          class="carousel-caption d-none d-md-block animate__animated animate__fadeInUp animate__delay-2 animate__slow carousel-label"
        >
          <h2
            class="animate__animated animate__fadeInUp animate__delay-4 animate__slower"
          >
            Beef
          </h2>
          <p
            class="animate__animated animate__fadeInUp animate__delay-5 animate__slower carousel-text"
          >
            When it comes to things you didn’t know about steak, one fun fact
            about this red meat that might surprise you is how much of it your
            average cattle can produce. If we assume that your beef animal
            weighs about 1,200 pounds and is doesn’t hold any excess weight in
            muscle, it should give you up to about 44% edible beef, or about 460
            pounds of meat. That’s a lot of delicious steak dinners.
          </p>
          <button class="text-btn" @click="searchCategory('beef')">
            See Beef Category
          </button>
        </div>
      </div>

      <div class="carousel-item" data-bs-interval="2000">
        <img
          src="../assets/img/banner-img/pork-category.jpg"
          class="d-block w-100"
          alt="..."
          style="height: 800px; object-fit: cover"
        />
        <div
          class="carousel-caption d-none d-md-block animate__animated animate__fadeInUp animate__delay-2 animate__slow carousel-label"
        >
          <h2
            class="animate__animated animate__fadeInUp animate__delay-4 animate__slower"
          >
            Pork
          </h2>
          <p
            class="animate__animated animate__fadeInUp animate__delay-5 animate__slower carousel-text"
          >
            Pork is a high-protein food and contains varying amounts of fats. To
            enjoy the healthiest pork benefits, it’s recommended to prioritize
            lean cuts – tenderloin, loin chops and sirloin roast. Lean cuts of
            pork are not just high in protein and lower in fat, but also contain
            more B-vitamins than many more other types of meat.
          </p>
          <button class="text-btn" @click="searchCategory('pork')">
            See Pork Category
          </button>
        </div>
      </div>
      <div class="carousel-item" data-bs-interval="2000">
        <img
          src="../assets/img/banner-img/pasta-category.jpg"
          class="d-block w-100"
          alt="..."
          style="height: 800px; object-fit: cover"
        />
        <div
          class="carousel-caption d-none d-md-block animate__animated animate__fadeInUp animate__delay-2 animate__slow carousel-label"
        >
          <h2
            class="animate__animated animate__fadeInUp animate__delay-4 animate__slower"
          >
            Pasta
          </h2>
          <p
            class="animate__animated animate__fadeInUp animate__delay-5 animate__slower carousel-text"
          >
            Pasta is a good source of carbohydrates. It also contains protein.
            Carbohydrates help fuel your body by providing energy that is
            released slowly over time. One cup of cooked spaghetti provides
            about 200 calories, 40 grams of carbohydrates, less than one gram of
            total fat, no cholesterol and only one gram of sodium when cooked
            without salt.
          </p>
          <button class="text-btn" @click="searchCategory('Pasta')">
            See Pasta Category
          </button>
        </div>
      </div>
      <div class="carousel-item" data-bs-interval="2000">
        <img
          src="../assets/img/banner-img/vegetarian-category.jpg"
          class="d-block w-100"
          alt="..."
          style="height: 800px; object-fit: cover"
        />
        <div
          class="carousel-caption d-none d-md-block animate__animated animate__fadeInUp animate__delay-2 animate__slow carousel-label"
        >
          <h2
            class="animate__animated animate__fadeInUp animate__delay-4 animate__slower"
          >
            Vegetarian
          </h2>
          <p
            class="animate__animated animate__fadeInUp animate__delay-5 animate__slower carousel-text"
          >
            Vegetarian diets are naturally low in saturated fat and cholesterol,
            and high in fiber, which may help to prevent heart disease,
            diabetes, kidney stones, and some cancers. Large studies even
            suggest that vegetarians have a 40% lower risk of developing cancer
            compared to meat eaters.
          </p>
          <button class="text-btn" @click="searchCategory('vegetarian')">
            See Vegetarian Category
          </button>
        </div>
      </div>
      <div class="carousel-item" data-bs-interval="2000">
        <img
          src="../assets/img/banner-img/desert-category.jpg"
          class="d-block w-100"
          alt="..."
          style="height: 800px; object-fit: cover"
        />
        <div
          class="carousel-caption d-none d-md-block animate__animated animate__fadeInUp animate__delay-2 animate__slow carousel-label"
        >
          <h2
            class="animate__animated animate__fadeInUp animate__delay-4 animate__slower"
          >
            Desserts
          </h2>
          <p
            class="animate__animated animate__fadeInUp animate__delay-5 animate__slower carousel-text"
          >
            Dessert is a course that concludes an evening meal. The course
            usually consists of sweet foods and beverages, but may include
            coffee, cheeses, nuts, or other savory items. In some parts of the
            world there is no tradition of dessert to conclude a meal.
          </p>
          <button class="text-btn" @click="searchCategory('dessert')">
            See Desserts Category
          </button>
        </div>
      </div>
    </div>
    <button
      class="carousel-control-prev"
      type="button"
      data-bs-target="#carouselExampleCaptions"
      data-bs-slide="prev"
    >
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button
      class="carousel-control-next"
      type="button"
      data-bs-target="#carouselExampleCaptions"
      data-bs-slide="next"
    >
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
</template>

<script>
export default {
  name: "Banner",
  methods: {
    searchCategory(cat) {
      this.$store.state.queryParam = "";
      this.$store.state.selectedCategory = cat;
      this.$store.dispatch("getRecipeByCategory");
      this.$store.dispatch("getCommunityRecipeByCategory");
      this.$router.push("/search-results");
    },
  },
};
</script>

<style scoped>
body,
html {
  height: 100%;
}
body,
html {
  height: 100%;
}
.active {
  color: #1c8314;
}
.carousel-label {
  /* position: absolute;
  top: 30%;
  bottom: 20%;
  left: 10%; */
  border-left: 3px solid #40ba37;
  background-color: rgba(24, 24, 24, 0.54);
  padding: 60px 10px;
  margin-bottom: 5%;
  color: white;
  width: 40%;
  text-align: center;
}
.carousel-text {
  font-size: larger;
  padding: 10%;
}
.text-btn {
  background: #40ba37;
  padding: 1em;
  color: white;
  border-left: 3px solid #1c8314;
  font-weight: bold;
}
</style>
