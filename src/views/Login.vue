<template>
  <div class="mx-auto" style="width: 400px">
    <img src="../assets/logo.png" alt="uChef Logo" />
    <!-- Pills navs -->
    <ul class="nav nav-pills nav-justified mb-3" id="ex1" role="tablist">
      <li class="nav-item" role="presentation">
        <router-link to="/login">
          <a
            class="nav-link nav-style active"
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
            class="nav-link"
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
          <!-- Email input -->
          <div class="form-outline mb-4">
            <input
              type="email"
              id="loginName"
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
            @click="authethicate()"
            type="submit"
            class="btn btn-primary btn-block mb-4 w-100"
          >
            Sign in
          </button>
          <button
            v-if="isLoading"
            @click="authethicate()"
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
</template>

<script>
import { getAuth, signInWithEmailAndPassword } from "firebase/auth";

export default {
  data() {
    return {
      email: "",
      password: "",
      errorMsg: "",
      isLoading: false,
    };
  },
  methods: {
    authethicate() {
      event.preventDefault();

      // sign in with email and password
      const auth = getAuth();
      this.isLoading = true;
      signInWithEmailAndPassword(auth, this.email, this.password)
        .then((userCredential) => {
          // Signed in
          const user = userCredential.user;
          console.log(user);
          console.log(this.$store.state.userName);
          this.$store.commit("set_userName", user.displayName);
          this.$store.commit("set_userId", user.uid);
          this.$router.push("/");
          console.log(this.$store.state.userId);
        })
        .catch((error) => {
          const errorCode = error.code;
          const errorMessage = error.message;
          switch (errorCode) {
            case "auth/invalid-email":
              this.errorMsg = "Invalid email!";
              this.isLoading = false;
              break;
            case "auth/user-not-found":
              this.errorMsg = "No account with that email was found!";
              this.isLoading = false;
              break;
            case "auth/wrong-password":
              this.errorMsg = "Incorrect password!";
              this.isLoading = false;
              break;
            default:
              this.errorMsg = "Email or password was incorrect";
              this.isLoading = false;
              break;
          }
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
</style>
