<template>
    <button
      class="btn btn-danger"
      @click="warning"
    >
      Delete
    </button>
</template>

<script>
import { getDatabase, ref, get, remove } from "firebase/database";

export default {
  name: "RemoveRecipe",
  data() {
    return {};
  },
  props: ["recipe-id"],
  methods: {
    warning() {
      let confirmation = prompt(
        "Are you sure you want to delete this recipe? (Y/N)\nThis action cannot be undone.\nPlease type 'Y' to confirm."
      );
      if (confirmation == "Y") {
        this.removeRecipe();
      }
    },
    removeRecipe() {
      let userId = this.$store.state.userId;
      // console.log("remove recipe");
      // console.log(this.recipeId);

      const db = getDatabase();
      const recipesRef = ref(db, `community`);
      const usersRef = ref(db, `users/${userId}/recipes`);
      // console.log(recipesRef);
      // console.log(usersRef);

      get(recipesRef)
        .then((snapshot) => {
          let data = snapshot.val();
          // console.log(data);
          for (let i in data) {
            // console.log(data[i]);
            if (data[i].id == this.recipeId) {
              let deleteRef = ref(db, `community/${i}`);
              remove(deleteRef).then(() => {
                // console.log("Location removed");
                get(usersRef)
                  .then((snapshot) => {
                    let data = snapshot.val();
                    for (let i in data) {
                      // console.log(data[i]);
                      if (data[i].id == this.recipeId) {
                        let deleteRef = ref(db, `users/${userId}/recipes/${i}`);
                        remove(deleteRef).then(() => {
                          // console.log("Location removed");
                          window.location.href = "/my-recipes";
                        });
                      }
                    }
                  })
                  .catch((error) => {
                    console.log(error.message);
                  });
              });
            }
          }
        })
        .catch((error) => {
          console.log(error.message);
        });
    },
  },
  created() {},
};
</script>

<style></style>
