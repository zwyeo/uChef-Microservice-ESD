<template>
  <nav class="navbar navbar-expand-lg my-0">
    <div class="container-fluid ms-5">
      <!-- Logo -->
      <router-link to="/"
        ><a class="nav-brand"
          ><img
            id="logo"
            src="../assets/logo.png"
            alt="uChef"
            style="width: 10em" /></a
      ></router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNavAltMarkup"
        aria-controls="navbarNavAltMarkup"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav mx-5">
          <!-- HOME NAV -->
          <router-link to="/"
            ><a
              v-if="this.$store.state.routeName == 'home'"
              class="nav-link active px-3 text-muted"
              aria-current="page"
              p
              >Home</a
            >
            <a v-else class="nav-link px-3 text-muted" aria-current="page" p
              >Home</a
            >
          </router-link>
          <!-- MY RECIPES NAV -->
          <router-link to="/my-recipes"
            ><a
              v-if="
                this.$store.state.userId &&
                this.$store.state.routeName == 'my-recipes'
              "
              class="nav-link active px-3 text-muted"
              aria-current="page"
              >MY RECIPES</a
            >
            <a
              v-if="
                this.$store.state.userId &&
                this.$store.state.routeName != 'my-recipes'
              "
              class="nav-link px-3 text-muted"
              aria-current="page"
              >MY RECIPES</a
            >
            <!-- TRIGGER LOGIN MODAL IF USER NOT LOGGED IN -->
            <a
              v-if="!this.$store.state.userId"
              class="nav-link px-3 text-muted"
              data-bs-toggle="modal"
              data-bs-target="#loginModal"
              aria-current="page"
              >MY RECIPES</a
            >
          </router-link>
          <!-- MY-BOOKMARKS NAVBAR -->
          <router-link to="/my-bookmarks"
            ><a
              v-if="
                this.$store.state.userId &&
                this.$store.state.routeName == 'my-bookmarks'
              "
              class="nav-link active px-3 text-muted"
              aria-current="page"
              >MY BOOKMARKS</a
            >
            <a
              v-if="
                this.$store.state.userId &&
                this.$store.state.routeName != 'my-bookmarks'
              "
              class="nav-link px-3 text-muted"
              aria-current="page"
              >MY BOOKMARKS</a
            >
            <!-- TRIGGER LOGIN MODAL IF USER NOT LOGGED IN -->
            <a
              v-if="!this.$store.state.userId"
              data-bs-toggle="modal"
              data-bs-target="#loginModal"
              class="nav-link px-3 text-muted"
              aria-current="page"
              >MY BOOKMARKS</a
            >
          </router-link>

          <!-- INSERT -->
          <!-- SEARCH BAR -->
          <div
            id="search-bar"
            class="d-flex text-center rounded-pill pe-2 border border-secondary px-2 mb-2 bg-white"
            style="width: 250px"
          >
            <div class="pt-2 icon">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-search mb-1"
                viewBox="0 0 16 16"
                @click="$store.dispatch('getRecipeBySearch')"
              >
                <path
                  d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"
                ></path>
              </svg>
            </div>

            <input
              type="text"
              :placeholder="$store.state.searchDesc"
              class="text-dark w-5 form-control rounded-pill input border-0 bg-white"
              v-model="searchQuery"
              style="background-color: #40ba37"
              @keyup.enter="onSearch"
            />
          </div>

          <!-- LOGIN IF GUEST -->
          <!-- Login Icon -->
          <div
            v-if="!this.$store.state.userId"
            @click="goToLoginPage"
            class="search-btn login-style ps-5 pt-2"
            style="color: #b6b6b6"
          >
            <i class="fa fa-user-plus"></i>
            <span> LOGIN <br> / SIGN UP</span>
          </div>

          <!-- PROFILE IF GUEST -->
          <!-- Search Icon -->
          <div
            v-if="!this.$store.state.userId"
            class="ps-5 pt-2 user-icon"
            style="color: #b6b6b6"
          >
            <i class="fa fa-user"></i>
            GUEST
          </div>

          <!-- LOGOUT USER IS AUTHENTICATED -->
          <!-- LOGOUT Icon -->
          <div
            id="icons-style"
            v-if="this.$store.state.userId"
            data-bs-toggle="modal"
            data-bs-target="#logoutModal"
            class="search-btn login-style ps-5 pt-2"
            style="color: #b6b6b6; bottom: 4.75rem;"
          >
            <i class="fa fa-rotate-right"></i>
            <span> LOGOUT</span>
          </div>

          <!-- PROFILE IF AUTHENTICATED -->
          <!-- USER Icon -->
          <div
            v-if="this.$store.state.userId"
            class="ps-5 text-success pt-2 user-icon"
            style="color: #b6b6b6; font-weight: bolder"
          >
            <i class="fa fa-user"></i>
            {{ this.$store.state.userName }}
          </div>
        </div>
      </div>
    </div>
  </nav>

  <!-- LOGIN Modal -->
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
          <h1 class="modal-title fs-5" id="exampleModalLabel">
            Authethication is required!
          </h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <img src="../assets/img/core-img/notLoggedIn.png" alt="" />
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
            class="btn btn-primary"
            @click="goToLoginPage"
            data-bs-dismiss="modal"
          >
            Login
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- LOGOUT Modal -->
  <div
    class="modal fade"
    id="logoutModal"
    tabindex="-1"
    aria-labelledby="ModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">
            Pressed wrong?
          </h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">Are you sure you want to log out?</div>
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
            class="btn btn-primary"
            @click="logOut"
            data-bs-dismiss="modal"
          >
            Yes
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getAuth, signOut } from "firebase/auth";
export default {
  name: "NavBarr",
  components: {},
  props: [],
  data() {
    return {
      isSearchExpand: false,
    };
  },
  computed: {
    // searchQuery is different from the usual computed because it required getter and setter
    searchQuery: {
      get() {
        return this.$store.state.queryParams;
      },
      // newValue is the user's search result
      set(newValue) {
        // console.log(newValue);
        this.$store.dispatch("setQueryParam", newValue);
      },
    },
  },
  methods: {
    // expand the search functionality when search icon is pressed
    openSearchBox() {
      this.isSearchExpand = true;
    },
    closeSearchBox() {
      this.isSearchExpand = false;
    },
    goToLoginPage() {
      this.$router.push("/login");
    },
    logOut() {
      // this.$store.state.userId = "";
      const auth = getAuth();
      signOut(auth)
        .then(() => {
          this.$store.state.userId = null;
          this.$store.state.userName = null;
          window.location.assign("/");
        })
        .catch((err) => console.log(err));
    },
    onSearch() {
      this.$store.dispatch("getRecipeBySearch");
      this.$store.dispatch("getCommunityRecipeBySearch");
      console.log("COMM", this.$store.state.commsearchrecipes);
      this.$router.push("/search-results");
    },
  },
  created() {},
};
</script>

<style scoped>
@import url(../css/classy-nav.min.css);
@import url(../css/font-awesome.min.css);

.input:focus {
  box-shadow: none;
  text-decoration: none;
}
.login-style :hover {
  cursor: pointer;
  color: #42b983;
}
a .nav-link.active {
  background-color: #40ba37 !important;
  border-bottom: 3px solid #1c8314;
  color: white !important;
}
/* a .nav-link :hover {
  color: #40ba37 !important;
  font-weight: bold !important;
} */

a {
  text-decoration: none;
  text-transform: uppercase;
  color: black;
}

@media screen and (max-width: 992px) {
  .user-icon {
    display: none;
  }
}

@media screen and (max-width: 600px) {
  #search-bar {
    width: 200px;
  }
}

@media screen and (min-width: 992px) and (max-width: 1199px) {
  #search-bar {
    position: absolute;
    right: 0;
    bottom: 4rem;
    margin-top: 0.5rem;
    margin-right: 0.5rem;
  }
  .login-style {
    position: absolute;
    right: 8rem;
    top: 6rem;
    margin-top: 0.5rem;
    margin-right: 0.5rem;
  }
  .user-icon {
    position: absolute;
    right: 2rem;
    top: 6rem;
    margin-top: 0.5rem;
    margin-right: 0.5rem;
  }
}

@media screen and (min-width: 1200px) {
  .login-style {
    position: absolute;
    right: 5rem;
    bottom: 4rem;
    margin-top: 0.5rem;
    margin-right: 2rem;
  }
  .user-icon {
    position: absolute;
    right: 0;
    bottom: 4.75rem;
    margin-top: 0.5rem;
    margin-right: 0.5rem;
  }
  #search-bar {
    position: absolute;
    right: 13rem;
    bottom: 4rem;
    margin-top: 0.5rem;
    margin-right: 0.5rem;
  }
}
</style>
