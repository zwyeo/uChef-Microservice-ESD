import { createStore } from "vuex";
import axios from "axios";

export default createStore({
  state: {
    recipes: {},
    foodCategories: [
      "Beef",
      "Breakfast",
      "Chicken",
      "Dessert",
      "Goat",
      "Lamb",
      "Miscellaneous",
      "Pasta",
      "Pork",
      "Seafood",
      "Side",
      "Starter",
      "Vegan",
      "Vegetarian",
    ],
    selectedCategory: "",
    queryParam: "",
    searchDesc: "Search food recipe",
    // This will store all the popular recipe from DB
    popularRecipe: {},
    // This will store all the community recipe from db
    communityRecipe: {},
    //for reviews posting
    starrating: "0",
    activerecipeid: "",
    reviewsubject: "",
    reviewcomments: "",
    reviewlist: [],
    setsearch: "professional",
    // To track user session
    userId: "",
    userName: "",
    // To get the current route name
    routeName: "",
    prevRouteName: "", // To bypass the signup/name bug
    commsearched: false,
    commsearchrecipes: {},
  },
  mutations: {
    getRecipes(state, payload) {
      state.recipes = payload;
      console.log(state.recipes);
      // console.log(state.recipes[0].id);
      // console.log(state.queryParam);
      console.log(state.selectedCategory);
    },
    getCommRecipes(state, payload) {
      state.commsearchrecipes = payload;
    },
    // set the query param based on user search
    setQueryParam(state, newValue) {
      state.queryParam = newValue;
    },

    // To populate popularRecipe
    setPopularRecipe(state, setPopularRecipe) {
      state.popularRecipe = setPopularRecipe;
    },
    // To populate communityRecipe
    setCommunityRecipe(state, setCommunityRecipe) {
      state.communityRecipe = setCommunityRecipe;
    },

    // For user authetication
    set_userId(state, data) {
      state.userId = data;
    },
    set_userName(state, data) {
      state.userName = data;
    },
    setReviews(state, data) {
      state.reviewlist = data;
    },
    setRouteName(state, data) {
      state.routeName = data;
    },
  },
  actions: {
    // This fn is to retrive recipe data from themealdb API TO BE REPLACEEDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
    getRecipes({ commit }) {
      let userQuery = this.state.queryParam;
      // console.log(userQuery.includes(","));
      let selectedCat = this.state.selectedCategory;
      console.log("userQuery: " + userQuery);
      console.log("selectedCat:" + selectedCat);
      if (
        this.state.setsearch == "professional" ||
        this.state.setsearch == ""
      ) {
        if (selectedCat.length == 0 && !userQuery.includes(",")) {
          //vanilla search
          let url = "https://themealdb.com/api/json/v2/9973533/search.php";
          axios
            .get(url, {
              params: {
                s: userQuery,
              },
            })
            .then((res) => {
              const data = res.data.meals;
              // console.log(data);
              commit("getRecipes", data); // This will pass data into getRecipe mutation as payload
            });
        } else if (selectedCat.length != 0 && !userQuery.includes(",")) {
          //search + category fitler
          let commonrecipes = [];
          let url = "https://themealdb.com/api/json/v2/9973533/search.php";
          axios
            .get(url, {
              params: {
                s: userQuery,
              },
            })
            .then((res) => {
              const data = res.data.meals;
              let curl = "https://themealdb.com/api/json/v2/9973533/filter.php";
              axios
                .get(curl, { params: { c: selectedCat } })
                .then((response) => {
                  const catdata = response.data.meals;
                  // console.log(data, catdata);
                  for (let searchobj in data) {
                    for (let catobj in catdata) {
                      if (catdata[catobj].strMeal == data[searchobj].strMeal) {
                        // console.log(data[searchobj].strMeal);
                        commonrecipes.push(data[searchobj]);
                      }
                    }
                  }
                  // console.log(commonrecipes);
                  commit("getRecipes", commonrecipes);
                });
            });
        } else if (userQuery.includes(",")) {
          //multi ingredient search
          let url = "https://themealdb.com/api/json/v2/9973533/filter.php";
          userQuery = userQuery.replace(" ", "_");
          axios.get(url, { params: { i: userQuery } }).then((response) => {
            let data = response.data.meals;
            commit("getRecipes", data);
          });
        }
      } else if (this.state.setsearch == "community") {
        let commrecipes = [];
        let url =
          "https://wad-proj-22042-default-rtdb.asia-southeast1.firebasedatabase.app/community.json";
        axios.get(url).then((response) => {
          // console.log(response.data);
          let alldata = response.data;
          for (let recipeobj in alldata) {
            let commtitle = alldata[recipeobj].title.toLowerCase();
            commtitle = commtitle.split(" ");
            // console.log(commtitle);
            for (let word of commtitle) {
              if (userQuery.includes(word)) {
                // console.log(alldata[recipeobj]);
                commrecipes.push(alldata[recipeobj]);
              }
            }
          }
          // console.log(commrecipes);
          this.state.commsearched = true;
          commit("getCommRecipes", commrecipes);
        });
      }
    },
    // REDO SEARCH API------------------------------------------------
    getRecipeBySearch({ commit }) {
      const userQuery = this.state.queryParam;
      const url = "https://themealdb.com/api/json/v2/9973533/search.php";

      axios
        .get(url, {
          params: {
            s: userQuery,
          },
        })
        .then((res) => {
          const data = res.data;
          commit("getRecipes", data);
        });
    },
    // FOR BANNER
    getRecipeByCategory({ commit }) {
      const category = this.state.selectedCategory;
      const url = "https://themealdb.com/api/json/v2/9973533/filter.php";
      axios.get(url, { params: { c: category } }).then((res) => {
        const data = res.data;
        commit("getRecipes", data);
      });
    },
    // FOR SEARCHING COMMUNITY RECIPES
    getCommunityRecipeBySearch({ commit }) {
      const url =
        "https://wad-proj-22042-default-rtdb.asia-southeast1.firebasedatabase.app/community.json";

      axios.get(url).then((res) => {
        let commrecipes = [];
        let userQuery = this.state.queryParam;
        const data = res.data;
        console.log(data);

        for (let recipeObj in data) {
          let commTitle = data[recipeObj].title.toLowerCase();
          commTitle = commTitle.split(" ");
          for (let word of commTitle) {
            if (userQuery.includes(word)) {
              commrecipes.push(data[recipeObj]);
            }
          }
        }
        this.state.commsearched = true;
        commit("getCommRecipes", commrecipes);
        console.log(this.state.commsearchrecipes);
      });
    },

    getCommunityRecipeByCategory({ commit }) {
      const url =
        "https://wad-proj-22042-default-rtdb.asia-southeast1.firebasedatabase.app/community.json";

      axios.get(url).then((res) => {
        let commrecipes = [];
        let userQuery = this.state.queryParam;
        const category = this.state.selectedCategory;
        const data = res.data;

        for (let recipeObj in data) {
          let cat = data[recipeObj].category.toLowerCase();
          if (cat === category) {
            commrecipes.push(data[recipeObj]);
          }
        }
        this.state.commsearched = true;
        commit("getCommRecipes", commrecipes);
        console.log("THIS", this.state.commsearchrecipes);
      });
    },

    // TO BE REPLACEEDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
    filterCategory({ commit }) {
      //if search query is empty
      let selectedCat = this.state.selectedCategory;
      let url = "https://themealdb.com/api/json/v2/9973533/filter.php";
      let commonrecipes = [];
      if (this.state.queryParam.length == 0) {
        axios.get(url, { params: { c: selectedCat } }).then((response) => {
          const data = response.data.meals;
          // console.log(data);
          commit("getRecipes", data);
        });
      } else if (this.state.recipes.length != 0) {
        //search query present and searched then filter
        axios.get(url, { params: { c: selectedCat } }).then((response) => {
          const data = response.data.meals;
          // console.log(data);
          for (let obj in data) {
            for (let robj in this.state.recipes) {
              if (data[obj].strMeal == this.state.recipes[robj].strMeal) {
                commonrecipes.push(this.state.recipes[robj]);
              }
            }
          }
          // console.log(commonrecipes);
          commit("getCategoryRecipe", commonrecipes);
        });
      }
      this.state.selectedCategory = "";
    },
    postReview({ commit }) {
      console.log(
        this.state.activerecipeid,
        this.state.starrating,
        this.state.reviewsubject,
        this.state.reviewcomments,
        this.state.userName
      );
      let date = new Date();
      const month = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
      ];
      let wordmonth = month[date.getMonth()];
      let year = date.getFullYear();
      let day = date.getDate();
      let formatdate = `${day} ${wordmonth} ${year}`;
      axios.post(
        `https://wad-proj-22042-default-rtdb.asia-southeast1.firebasedatabase.app/recipes/${this.state.activerecipeid}/reviews.json`,
        {
          user: this.state.userName,
          rating: this.state.starrating,
          subject: this.state.reviewsubject,
          message: this.state.reviewcomments,
          date: formatdate,
        }
      );
      //reset fields
      this.state.reviewsubject = "";
      this.state.reviewcomments = "";
      this.state.starrating = "0";
      // this.state.dispatch("getReviews");
      // console.log(this.state.reviewlist);
      location.reload(); //to reload page
      // window.scrollTo(0, document.querySelector("#reviewSection").scrollHeight);
    },
    getReviews({ commit }) {
      //trying to use axios call to refresh page
      //review card population
      let review_list = [];
      let rurl = `https://wad-proj-22042-default-rtdb.asia-southeast1.firebasedatabase.app/recipes/${this.state.activerecipeid}/reviews.json`;
      axios.get(rurl).then((response) => {
        // console.log(response.data);
        let reviewsObj = response.data;
        for (let review in reviewsObj) {
          review_list.push(reviewsObj[review]);
        }
        review_list = review_list.reverse();
        commit("setReviews", review_list);
      });
    },
    // This fn receive user input from searchbar and pass payload to mutation
    setQueryParam({ commit }, newValue) {
      commit("setQueryParam", newValue);
    },

    setPopularRecipe({ commit }) {
      const url = `https://wad-proj-22042-default-rtdb.asia-southeast1.firebasedatabase.app/popularRecipe.json`;
      axios.get(url).then((res) => {
        const data = res.data;
        commit("setPopularRecipe", data);
      });
    },
    setCommunityRecipe({ commit }) {
      const url = `https://wad-proj-22042-default-rtdb.asia-southeast1.firebasedatabase.app/community.json`;
      axios.get(url).then((res) => {
        const data = res.data;
        commit("setCommunityRecipe", data);
      });
    },
  },

  getters: {
    user(state) {
      return state.user;
    },
    commuityRecipe(state) {
      return state.commuityRecipe;
    },
  },
  modules: {},
});
