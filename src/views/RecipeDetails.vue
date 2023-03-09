<template>
  <div class="px-5">
    <nav-bar></nav-bar>
  </div>
  <!-- Receipe Slider -->
  <div class="container animate__animated animate__backInLeft animate__fast">
    <div class="row mb-5">
      <div class="col-12">
        <div class="parent">
          <div
            class="background-image"
            :style="{ backgroundImage: 'url(' + image + ')' }"
          ></div>
          <div
            class="hero-image"
            :style="{ backgroundImage: 'url(' + image + ')' }"
          ></div>
        </div>
      </div>
    </div>
  </div>

  <!-- Receipe Content Area -->
  <div>
    <div class="container">
      <div class="row">
        <div class="col-12 col-md-8">
          <div class="receipe-headline my-5">
            <h2>{{ title }}</h2>
            <!-- IF VIDEO EXISTS -->
            <div v-if="videoExist == true">
              <!-- video button -->
              <button
                class="btn video-btn"
                data-bs-toggle="modal"
                :data-src="video"
                data-bs-target="#myModal"
                @click="open()"
              >
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
                  <path
                    d="M549.655 124.083c-6.281-23.65-24.787-42.276-48.284-48.597C458.781 64 288 64 288 64S117.22 64 74.629 75.486c-23.497 6.322-42.003 24.947-48.284 48.597-11.412 42.867-11.412 132.305-11.412 132.305s0 89.438 11.412 132.305c6.281 23.65 24.787 41.5 48.284 47.821C117.22 448 288 448 288 448s170.78 0 213.371-11.486c23.497-6.321 42.003-24.171 48.284-47.821 11.412-42.867 11.412-132.305 11.412-132.305s0-89.438-11.412-132.305zm-317.51 213.508V175.185l142.739 81.205-142.739 81.201z"
                  />
                </svg>
                Watch Video
              </button>

              <!-- Modal -->
              <div
                class="modal fade"
                id="myModal"
                tabindex="-1"
                role="dialog"
                aria-labelledby="exampleModalLabel"
                aria-hidden="true"
              >
                <div class="modal-dialog" role="document">
                  <div class="modal-content">
                    <div class="modal-body">
                      <button
                        type="button"
                        class="btn-close"
                        @click="close()"
                        data-bs-dismiss="modal"
                        aria-label="Close"
                      ></button>
                      <!-- 16:9 aspect ratio -->
                      <div class="ratio ratio-16x9">
                        <iframe
                          class="embed-responsive-item"
                          :src="video2"
                          allowscriptaccess="always"
                          allow="autoplay"
                        ></iframe>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- END of v-if-->
            <div v-else>
              <button class="btn video-btn disabled">No Video Available</button>
            </div>
          </div>
        </div>

        <div class="col-12 col-md-4">
          <div class="receipe-ratings my-5 float-end">
            <div
              class="ratings animate__animated animate__delay-1s animate__pulse animate__fast"
            >
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

            <a
              v-if="!bookmarked && !this.$store.state.userId"
              href="#"
              class="btn delicious-btn animate__animated animate__rubberBand animate__delay-1s animate__fast"
              data-bs-toggle="modal"
              data-bs-target="#loginModal"
              >Bookmark</a
            >
            <a
              v-if="!bookmarked && this.$store.state.userId"
              href="#"
              class="btn delicious-btn animate__animated animate__rubberBand animate__delay-1s animate__fast"
              @click="bookmark()"
              data-bs-toggle="modal"
              data-bs-target="#bookmarkModal"
              >Bookmark</a
            >
            <a
              v-if="bookmarked && this.$store.state.userId"
              href="#"
              class="btn delicious-btn animate__animated animate__rubberBand animate__delay-1s animate__fast"
              @click="unbookmark()"
              data-bs-toggle="modal"
              data-bs-target="#unbookmarkModal"
              >Bookmarked!</a
            >
          </div>
        </div>
      </div>

      <!-- Instructions -->
      <div class="row">
        <div
          class="col-12 col-lg-9 animate__animated animate__backInUp animate__delay-1s animate__fast"
        >
          <!-- Single Preparation Step -->
          <ul class="list-group list-group-light">
            <li
              v-for="(item, index) in instructions"
              :key="item"
              class="list-group-item px-3 border-0 rounded-3 list-group-item-light mb-2 d-flex"
            >
              <h4 v-if="index < 9">0{{ index + 1 }}</h4>
              <h4 v-else>{{ index + 1 }}</h4>
              <p class="ms-3 instruction-text">{{ item }}</p>
            </li>
          </ul>
        </div>

        <!-- Ingredients -->
        <div
          class="col-12 col-lg-3 animate__animated animate__backInRight animate__delay-1s animate__fast"
        >
          <h4 class="">Ingredients</h4>

          <!-- Ingredient list -->
          <div
            v-for="(item, index) in ingredient_list"
            :key="index"
            :id="index"
          >
            <ul class="list-group text-white ingredient-group">
              <li
                class="list-group-item d-flex justify-content-between align-content-center"
              >
                <h6 class="mb-0">
                  <img
                    src="../assets/img/core-img/salad.png"
                    class="ingredient-img"
                  />
                  &nbsp;<span class="item">{{ item }}</span>
                </h6>
              </li>
            </ul>

            <!-- End of ingredient list -->
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-12">
          <div
            class="section-heading text-left m-0 animate__animated animate__fadeInBottomLeft animate__delay-1s animate__fast"
            id="review-section"
          >
            <h3>Reviews</h3>
            <p>See what others have to say</p>
          </div>
          <div
            v-if="review_list.length > 0"
            class="animate__bounceInUp animate__animated animate__delay-1s animate__fast"
          >
            <review-card
              v-for="(review, index) of review_list"
              :key="index"
              :id="id"
              :user="review.user"
              :date="review.date"
              :rating="review.rating"
              :subject="review.subject"
              :message="review.message"
            >
            </review-card>
          </div>
          <div v-else>
            <p
              class="text-center pt-5 pb-5 animate__animated animate__fadeInBottomLeft animate__delay-1s animate__fast"
            >
              No reviews yet.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <review-btn></review-btn>
  <!-- ##### Follow Us Instagram Area End ##### -->

  <!-- Login Modal -->
  <div
    class="modal fade"
    id="loginModal"
    tabindex="-1"
    aria-labelledby="ModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5 mx-auto" id="exampleModalLabel">
            Login is required!
          </h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body m-3 mx-auto">
          <img src="../assets/img/core-img/notLoggedIn.png" alt="" />
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-success mx-auto"
            data-bs-dismiss="modal"
          >
            Ok
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- Bookmark Modal -->
  <div
    class="modal fade"
    id="bookmarkModal"
    tabindex="-1"
    aria-labelledby="ModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5 mx-auto" id="exampleModalLabel">
            Item bookmarked! 🥳
          </h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body m-3 mx-auto">
          Awesome! {{ title }} will be in your bookmark page!
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-success mx-auto"
            data-bs-dismiss="modal"
          >
            Ok
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- Unbookmark Modal -->
  <div
    class="modal fade"
    id="unbookmarkModal"
    tabindex="-1"
    aria-labelledby="ModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5 mx-auto" id="exampleModalLabel">
            Awww 😥... Item unbookmarked!
          </h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body m-3 mx-auto">
          {{ title }} will be removed your bookmark page!
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-success mx-auto"
            data-bs-dismiss="modal"
          >
            Ok
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from "../components/NavBar.vue";
import axios from "axios";
import {
  getDatabase,
  ref,
  child,
  get,
  onValue,
  remove,
  update,
  updates,
  set,
} from "firebase/database";
import ReviewBtn from "../components/ReviewButton.vue";
import ReviewCard from "../components/ReviewCard.vue";
export default {
  components: { NavBar, ReviewBtn, ReviewCard },
  props: ["id"],
  data() {
    return {
      title: null,
      image: null,
      videoExist: true,
      video: null,
      video2: null,
      instructions: [],
      ingredient_list: [],
      bookmarked: false,
      review_list: [],
      foodcategory: null,
      ratings: null,
    };
  },
  created() {
    //to link active id to store
    this.$store.state.activerecipeid = this.id;
    //filling up the recipe details
    console.log(this.id);
    let url = "https://themealdb.com/api/json/v1/1/lookup.php";

    if (isNaN(this.id)) {
      axios
        .get(
          `https://wad-proj-22042-default-rtdb.asia-southeast1.firebasedatabase.app/community.json`
        )
        .then((response) => {
          // console.log(response.data)
          for (let entry in response.data) {
            // console.log(response.data[entry].id)
            if (response.data[entry].id == this.id) {
              var obj = response.data[entry];
              this.videoExist = false;
              this.title = obj.title;
              this.image = obj.image;
              this.foodCategory = obj.strCategory;

              //formatting instructions
              let instruction = obj.instructions.split("\r\n");
              for (let i of instruction) {
                if (!i == "" && i.length > 1) {
                  this.instructions.push(i);
                }
              }

              // formatting ingredients and the measurements
              for (let i = 1; i < 21; i++) {
                let str_i = "strIngredient" + i;
                let str_m = "strMeasure" + i;
                if (obj[str_i] == "" || obj[str_i] == null) break;
                else {
                  let final = obj[str_m] + " " + obj[str_i];
                  this.ingredient_list.push(final);
                }
              }
            }
          }
        });
    }
    //
    else {
      axios
        .get(url, {
          params: {
            i: this.id,
          },
        })
        .then((response) => {
          console.log(response.data);
          let obj = response.data.meals[0];
          this.title = obj.strMeal;
          this.image = obj.strMealThumb;
          this.foodCategory = obj.strCategory;
          console.log(obj.strYoutube);
          if (obj.strYoutube === "") {
            this.videoExist = false;
            console.log(this.videoExist);
          }
          this.video = obj.strYoutube.replace("watch?v=", "embed/");

          //formatting instructions
          let instruction = obj.strInstructions.split("\r\n");
          for (let i of instruction) {
            if (!i == "" && i.length > 1) {
              this.instructions.push(i);
            }
          }
          // formatting ingredients and the measurements
          for (let i = 1; i < 21; i++) {
            let str_i = "strIngredient" + i;
            let str_m = "strMeasure" + i;
            if (obj[str_i] == "" || obj[str_i] == null) break;
            else {
              let final = obj[str_m] + " " + obj[str_i];
              this.ingredient_list.push(final);
            }
          }
        });
    }

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

    //Dictate the state of the bookmark button
    axios
      .get(
        `https://wad-proj-22042-default-rtdb.asia-southeast1.firebasedatabase.app/users/${this.$store.state.userId}/bookmarks.json`
      )
      .then((response) => {
        // console.log(response.data)
        for (let bookmark in response.data) {
          // console.log(bookmark);
          if (bookmark == this.id) {
            this.bookmarked = true;
          }
        }
      })
      .catch((error) => {
        console.log(error);
      });

    //review card population
    let rurl = `https://wad-proj-22042-default-rtdb.asia-southeast1.firebasedatabase.app/recipes/${this.id}/reviews.json`;
    axios.get(rurl).then((response) => {
      // console.log(response.data);
      let reviewsObj = response.data;
      for (let review in reviewsObj) {
        this.review_list.push(reviewsObj[review]);
      }

      this.review_list = this.review_list.reverse();
    });
  },
  methods: {
    // bookmarking functions
    bookmark() {
      let userId = this.$store.state.userId;

      if (this.$store.state.userId == "") {
        alert("Please login to bookmark!");
        window.location.assign("/login");
      } else {
        axios.post(
          `https://wad-proj-22042-default-rtdb.asia-southeast1.firebasedatabase.app/users/${userId}/bookmarks/${this.id}.json`,
          {
            title: this.title,
            image: this.image,
          }
        );
        this.bookmarked = true;

        //add category to user's preference in firebase db
        //get current instances of the catogory in user's preferences
        var current = null;
        var str_id = null;

        axios
          .get(
            `https://wad-proj-22042-default-rtdb.asia-southeast1.firebasedatabase.app/users/${this.$store.state.userId}/preferences.json`
          )
          .then((response) => {
            console.log(response.data);
            for (let bookmark in response.data) {
              str_id = bookmark;
              current = response.data[bookmark][this.foodCategory];
              console.log(current);
            }
            var final = current + 1;

            const db = getDatabase();
            set(
              ref(
                db,
                `users/${this.$store.state.userId}/preferences/${str_id}/${this.foodCategory}`
              ),
              final
            );
          });
      }
    },
    unbookmark() {
      const db = getDatabase();
      var userId = this.$store.state.userId;
      var bookmarkRef = ref(db, `users/${userId}/bookmarks/${this.id}`);
      remove(bookmarkRef).then(() => {
        this.bookmarked = false;
        console.log("location removed");
      });

      // reduce food category by 1 from user's preferences
      var current = null;
      var str_id = null;
      axios
        .get(
          `https://wad-proj-22042-default-rtdb.asia-southeast1.firebasedatabase.app/users/${this.$store.state.userId}/preferences.json`
        )
        .then((response) => {
          console.log(response.data);
          for (let bookmark in response.data) {
            str_id = bookmark;
            current = response.data[bookmark][this.foodCategory];
            console.log(current);
          }
          if (current > 0) {
            var final = current - 1;
          } else {
            var final = 0;
          }

          const db = getDatabase();
          set(
            ref(
              db,
              `users/${this.$store.state.userId}/preferences/${str_id}/${this.foodCategory}`
            ),
            final
          );
        });
    },
    //Video Modal Functions
    open() {
      console.log("it works");
      this.video2 = this.video.replace("watch?v=", "embed/");
    },
    close() {
      console.log("close");
      this.video2 = null;
    },
  },
};
</script>
<!-- CSS files
  ============== -->
<style scoped>
body {
  font-family: "Open Sans", sans-serif;
  font-size: 14px;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  color: #000000;
  line-height: 1.3;
  font-weight: 600;
}

p {
  color: #9b9b9b;
  font-size: 14px;
  line-height: 2;
  font-weight: 400;
}

a,
a:hover,
a:focus {
  -webkit-transition-duration: 500ms;
  transition-duration: 500ms;
  text-decoration: none;
  outline: 0 solid transparent;
  color: #000000;
  font-weight: 600;
  font-size: 14px;
  color: #474747;
}

ul,
ol {
  margin: 0;
}

ul li,
ol li {
  list-style: none;
}

.parent {
  position: relative;
  height: 600px;
  /* */
}

.background-image {
  background-size: cover;
  display: block;
  filter: blur(5px);
  -webkit-filter: blur(7px);
  width: 100%;
  height: 600px;
  top: 200px;
  left: 0;
  /* position: fixed; */
  z-index: -100;
}

.hero-image {
  background-size: cover;
  width: 400px;
  height: 400px;
  border-radius: 50%;
  display: block;
  position: absolute;
  top: 50%;
  left: 50%;
  z-index: 10;
  transform: translate(-50%, -50%);
  background-position: center;
}

/* Section Heading */
.section-heading {
  position: relative;
  z-index: 1;
  margin-bottom: 80px;
  text-align: center;
}

.section-heading h3 {
  font-size: 30px;
  margin-bottom: 0;
}

.section-heading.text-left {
  text-align: left !important;
}

.section-heading.white h3 {
  color: #ffffff;
}

/* Video button */
.video-btn {
  align-items: center;
  background-color: #40ba37;
  border: 2px solid #111;
  border-radius: 8px;
  box-sizing: border-box;
  color: #111;
  cursor: pointer;
  display: flex;
  font-family: Inter, sans-serif;
  font-size: 16px;
  height: 48px;
  justify-content: center;
  line-height: 24px;
  max-width: 100%;
  padding: 0 25px;
  position: relative;
  text-align: center;
  text-decoration: none;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

.video-btn:after {
  background-color: grey;
  border-radius: 8px;
  content: "";
  display: block;
  height: 48px;
  left: 0;
  width: 100%;
  position: absolute;
  top: -2px;
  transform: translate(8px, 8px);
  transition: transform 0.2s ease-out;
  z-index: -1;
}

.video-btn:hover:after {
  transform: translate(0, 0);
}

.video-btn:active {
  background-color: #ffdeda;
  outline: 0;
}

.video-btn:hover {
  outline: 0;
}

@media (min-width: 768px) {
  .video-btn {
    padding: 0 40px;
  }
}

/* Button */
.delicious-btn {
  display: inline-block;
  min-width: 160px;
  height: 60px;
  color: #ffffff;
  border: none;
  border-left: 3px solid #1c8314;
  border-radius: 0;
  padding: 0 30px;
  font-size: 16px;
  line-height: 58px;
  font-weight: 600;
  -webkit-transition-duration: 500ms;
  transition-duration: 500ms;
  text-transform: capitalize;
  background-color: #40ba37;
}

.delicious-btn.active,
.delicious-btn:hover,
.delicious-btn:focus {
  font-size: 16px;
  font-weight: 600;
  color: #ffffff;
  background-color: #1c8314;
  border-color: #40ba37;
}

.delicious-btn.btn-2 {
  background-color: #1c8314;
  border-color: #40ba37;
}

.delicious-btn.btn-2.active,
.delicious-btn.btn-2:hover,
.delicious-btn.btn-2:focus {
  background-color: #40ba37;
  border-color: #1c8314;
}

.delicious-btn.btn-3 {
  background-color: #474747;
  border-color: #1c8314;
}

.delicious-btn.btn-3.active,
.delicious-btn.btn-3:hover,
.delicious-btn.btn-3:focus {
  background-color: #40ba37;
  border-color: #1c8314;
}

.delicious-btn.btn-4 {
  background-color: transparent;
  border: 3px solid #40ba37;
  line-height: 53px;
  color: #40ba37;
}

@media only screen and (max-width: 767px) {
  .delicious-btn.btn-4 {
    height: 40px;
    line-height: 33px;
  }
}

.delicious-btn.btn-4.active,
.delicious-btn.btn-4:hover,
.delicious-btn.btn-4:focus {
  line-height: 53px;
  color: #ffffff;
  background-color: #40ba37;
}

@media only screen and (max-width: 767px) {
  .delicious-btn.btn-4.active,
  .delicious-btn.btn-4:hover,
  .delicious-btn.btn-4:focus {
    height: 40px;
    line-height: 33px;
  }
}

@media only screen and (max-width: 767px) {
  .delicious-btn {
    height: 40px;
    line-height: 39px;
  }
}

/* :: 8.0 Best Receipe Area */
.ratings i {
  font-size: 11px;
  color: #fbb710;
  display: inline-block;
  padding: 0 1px;
}

/* :: 15.0 Receipe Area */
@media only screen and (min-width: 768px) and (max-width: 991px) {
  .col-12 {
    margin-bottom: 30px;
  }
}

@media only screen and (max-width: 767px) {
  .col-12 {
    margin-bottom: 15px;
  }
}

svg {
  width: 35px;
}

.receipe-headline span {
  font-size: 14px;
  display: block;
  color: #a4a4a4;
  margin-bottom: 0;
}

.receipe-headline h2 {
  font-size: 36px;
  color: #474747;
  margin-bottom: 30px;
}

@media only screen and (max-width: 767px) {
  .receipe-headline h2 {
    font-size: 24px;
  }
}

.receipe-headline {
  border-left: 3px solid #40ba37;
  padding: 15px;
}

.receipe-headline {
  font-size: 15px;
  margin-bottom: 5px;
}

.receipe-headline {
  margin-bottom: 0;
}

.receipe-ratings .ratings {
  margin-bottom: 30px;
}

.receipe-ratings i {
  font-size: 18px;
  color: #fbb710;
  padding: 0 3px;
}

.instruction-text {
  font-size: 20px;
}

/* Ingredient list */
.ingredient-group {
  width: 300px !important;
}

.list-group-item {
  margin-top: 10px;
  border-radius: none;
  border: none;
  /* background: #40ba37; */
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.list-group-item:hover {
  transform: scaleX(1.1);
}

.list-group-item:hover .check {
  opacity: 1;
}

.ingredient-img {
  width: 50px;
  position: relative;
}

.item {
  position: absolute;
  top: 20px;
  left: 80px;
}

/* Video Modal */
.modal-dialog {
  max-width: 800px;
  margin: 30px auto;
}

.modal-body {
  position: relative;
  padding: 0px;
}

.btn-close {
  position: absolute;
  right: -30px;
  top: 0;
}
</style>
