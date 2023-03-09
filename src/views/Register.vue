<template>
  <div class="mx-auto" style="width: 400px">
    <img src="../assets/logo.png" alt="uChef Logo" />
    <!-- Pills navs -->
    <ul class="nav nav-pills nav-justified mb-3" id="ex1" role="tablist">
      <li class="nav-item" role="presentation">
        <router-link to="/login">
          <a
            class="nav-link"
            id="tab-login"
            data-mdb-toggle="pill"
            role="tab"
            aria-controls="pills-login"
            aria-selected="true"
            >Login</a
          >
        </router-link>
      </li>
      <li class="nav-item" role="presentation">
        <router-link to="/register">
          <a
            class="nav-link active"
            id="tab-register"
            data-mdb-toggle="pill"
            role="tab"
            aria-controls="pills-register"
            aria-selected="false"
            >Sign Up</a
          >
        </router-link>
      </li>
    </ul>
    <!-- Pills navs -->

    <!-- Pills content -->
    <div class="tab-content">
      <div
        class="tab-pane fade show active"
        id="pills-login"
        role="tabpanel"
        aria-labelledby="tab-login"
      >
        <form>
          <!-- Name input -->
          <div class="form-outline mb-4">
            <input
              type="text"
              id="name"
              class="form-control"
              placeholder="Name"
              v-model="name"
            />
            <!-- <label class="form-label" for="loginName">Email or username</label> -->
          </div>

          <!-- Email input -->
          <div class="form-outline mb-4">
            <input
              type="email"
              id="email"
              class="form-control"
              placeholder="Email"
              v-model="email"
            />
            <!-- <label class="form-label" for="loginName">Email or username</label> -->
          </div>

          <!-- Password input -->
          <div class="form-outline mb-4">
            <input
              type="password"
              id="loginPassword"
              class="form-control"
              placeholder="Password"
              v-model="password"
            />

            <div class="text-center text-danger mt-1" v-if="errorMsg">
              {{ errorMsg }}
            </div>
          </div>

          <!-- Submit button -->
          <button
            v-if="!isLoading"
            @click="createUser()"
            type="submit"
            class="btn btn-primary btn-block mb-4 w-100"
          >
            Sign Up
          </button>

          <button
            v-if="isLoading"
            @click="createUser()"
            type="submit"
            class="btn btn-primary btn-block mb-4 w-100"
          >
            <span class="spinner-border spinner-border-sm btn-spin"></span>
            Authethicating...
          </button>
        </form>
      </div>
      <div
        class="tab-pane fade"
        id="pills-register"
        role="tabpanel"
        aria-labelledby="tab-register"
      ></div>
    </div>
  </div>
  <!-- Pills content -->
</template>

<script>
import {
  getAuth,
  createUserWithEmailAndPassword,
  updateProfile,
} from "firebase/auth";
import axios from "axios";

export default {
  data() {
    return {
      name: "",
      email: "",
      password: "",
      isLoading: false,
      errorMsg: "",
    };
  },
  methods: {
    createUser() {
      this.isLoading = true;
      const auth = getAuth();
      // creating a user account
      event.preventDefault();

      createUserWithEmailAndPassword(auth, this.email, this.password)
        .then((userCredential) => {
          // Signed in
          const user = userCredential.user;
          // console.log(user);
          // console.log(this.name);
          updateProfile(user, { displayName: this.name });

          this.$store.commit("set_userName", user.displayName);
          this.$store.commit("set_userId", user.uid);
          this.$store.state.prevRouteName = "register";
          this.populateUserDB(user.uid);
          // this.$router.push("/");

          // reset the values
          this.email = "";
          this.password = "";
        })
        .catch((error) => {
          const errorCode = error.code;
          // const errorMessage = error.message;
          switch (errorCode) {
            case "auth/email-already-in-use":
              this.errorMsg = "Email is already in used!";
              this.isLoading = false;
              break;
            case "auth/invalid-email":
              this.errorMsg = "Email is invalid!";
              this.isLoading = false;
              break;
            case "auth/operation-not-allowed":
              this.errorMsg = "This email is is not enabled!";
              this.isLoading = false;
              break;
            default:
              this.errorMsg =
                "Your password is weak! Please try a different one!";
              this.isLoading = false;
              break;
          }
        });
    },
    populateUserDB(uid) {
      const url = `https://wad-proj-22042-default-rtdb.asia-southeast1.firebasedatabase.app/users/${uid}/preferences.json`;

      axios
        .post(url, {
          Beef: 0,
          Breakfast: 0,
          Chicken: 0,
          Dessert: 0,
          Goat: 0,
          Lamb: 0,
          Miscellaneous: 0,
          Pasta: 0,
          Pork: 0,
          Seafood: 0,
          Side: 0,
          Starter: 0,
          Vegan: 0,
          Vegetarian: 0,
        })
        .then((res) => {
          this.$router.push("/");
        });
    },
  },
};
</script>

<style scoped>
.btn-spin {
  padding: relative;
  top: -3px;
}

/* @media screen and (max-width: 1170px) {
  .login-style {
    width: 400px;
  }
}

@media screen and (min-width: 1170px) {
  .login-style {
    width: 600px;
  }
} */
</style>
