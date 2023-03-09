<template>
  <!-- <div class="row">
    <div class="col-12">
      <div class="section-heading text-left">
        <h3>Leave a Review</h3>
      </div>
    </div>
  </div> -->

  <div class="row">
    <div class="col-12">
      <div class="contact-form-area">
        <div class="row">
          <div class="col-12">
            <input
              type="text"
              class="form-control"
              id="subject"
              placeholder="Subject"
              v-model="$store.state.reviewsubject"
              @keyup="validateForm"
            />
          </div>
          <div class="col-12">
            <textarea
              name="message"
              class="form-control"
              id="message"
              cols="30"
              rows="10"
              placeholder="Message"
              v-model="$store.state.reviewcomments"
              @keyup="validateForm"
            ></textarea>
          </div>
          <div class="col-12">
            <span v-if="!isValid"
              ><button
                class="btn delicious-btn mt-30"
                @click="$store.dispatch('postReview')"
                disabled
              >
                Post Review
              </button></span
            >
            <span v-else>
              <button
                class="btn delicious-btn mt-30"
                @click="$store.dispatch('postReview')"
                data-bs-dismiss="modal"
              >
                Post Review
              </button>
            </span>

            <span
              ><star-rating
                class="float-end mt-3"
                @change="validateForm"
              ></star-rating
            ></span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import StarRating from "../components/StarRating.vue";
export default {
  name: "ReviewForm",
  components: { StarRating },
  data() {
    return {
      isValid: false,
    };
  },
  methods: {
    validateForm() {
      if (
        this.$store.state.reviewsubject.length != 0 &&
        this.$store.state.reviewcomments.length != 0 &&
        this.$store.state.starrating != "0"
      ) {
        this.isValid = true;
      } else {
        this.isValid = false;
      }
    },
    closeModal() {},
  },
};
</script>

<style lang="scss" scoped>
* {
  margin: 0;
  padding: 0;
}

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

/* Spacing */

.mt-30 {
  margin-top: 30px !important;
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
  .receipe-post-search .col-12 {
    margin-bottom: 30px;
  }
}
@media only screen and (max-width: 767px) {
  .receipe-post-search .col-12 {
    margin-bottom: 15px;
  }
}

svg {
  width: 50px;
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
.receipe-headline .receipe-duration {
  border-left: 3px solid #40ba37;
  padding: 15px;
}
.receipe-headline .receipe-duration h6 {
  font-size: 15px;
  margin-bottom: 5px;
}
.receipe-headline .receipe-duration h6:last-child {
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

.single-preparation-step {
  position: relative;
  z-index: 1;
  margin-bottom: 50px;
}
.single-preparation-step h4 {
  color: #474747;
  -webkit-box-flex: 0;
  -ms-flex: 0 0 60px;
  flex: 0 0 60px;
  max-width: 60px;
  width: 60px;
  margin-bottom: 0;
}

@media only screen and (min-width: 768px) and (max-width: 991px) {
  .ingredients {
    margin-bottom: 80px;
  }
}
@media only screen and (max-width: 767px) {
  .ingredients {
    margin-bottom: 80px;
  }
}
.ingredients h4 {
  color: #7e2e2e;
  margin-bottom: 30px;
}
.ingredients .custom-checkbox .custom-control-label::before {
  border-radius: 0;
}
.ingredients .custom-control-label::before {
  width: 30px;
  height: 30px;
}
.ingredients .custom-control {
  padding-left: 2.5rem;
  margin-bottom: 30px;
  min-height: 35px;
}
.ingredients .custom-control-label {
  margin-bottom: 0;
  padding-top: 5px;
  font-size: 16px;
  font-weight: 600;
  color: #2f2f2f;
}
.ingredients .custom-control-label::after {
  top: 10px;
  left: 5px;
  width: 20px;
  height: 20px;
}

.ingredients
  .custom-checkbox
  .custom-control-input:checked
  ~ .custom-control-label::before {
  background-color: #40ba37;
}

img {
  width: 100%;
  height: auto;
  aspect-ratio: 2/1.4;
}
.outer {
  width: 750px;
}

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

.contact-form-area .form-control {
  height: 52px;
  width: 100%;
  background-color: #f3f5f8;
  font-size: 12px;
  font-style: italic;
  margin-bottom: 15px;
  border: none;
  border-left: 3px solid #f3f5f8;
  border-radius: 0;
  padding: 15px 30px;
  -webkit-transition-duration: 500ms;
  transition-duration: 500ms;
}
.contact-form-area .form-control:focus {
  border-left: 3px solid #40ba37;
  box-shadow: none;
}
.contact-form-area textarea.form-control {
  height: 200px;
  -webkit-transition-duration: 500ms;
  transition-duration: 500ms;
}
</style>
