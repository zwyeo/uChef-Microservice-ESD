<template>
    <div class="container-fluid px-5">
        <nav-bar></nav-bar>

        <h2 class="text-center pb-5">Update Recipe</h2>

        <div class="row">
            <div class="col-10 text-center">
                <table class="table">
                    <tr>
                        <th><label for="newRecipeName">Recipe Name</label></th>
                        <td><input id="newRecipeName" name="newRecipeName" type="text" class="form-control" v-model="newRecipeName" /></td>
                    </tr>
                    <tr>
                        <th><label for="newRecipeCategory">Recipe Category</label></th>
                        <td>
                            <select
                                id="newRecipeCategory"
                                class="form-control"
                                v-model="newRecipeCategory"
                            >
                                <option
                                    v-for="category in $store.state.foodCategories"
                                    :value="category"
                                >
                                    {{ category }}
                                </option>
                            </select>
                        </td>
                    </tr>
                    <tr>
                        <th><label for="newRecipeInstructions">Instructions (Steps)</label></th>
                        <td>
                            <div id="newRecipeInstructions">
                                <input v-for="i in noOfSteps" class="form-control" type="text" :placeholder="i" v-model="newRecipeInstructions[i-1]">
                                <br>
                                <button class="btn btn-small btn-primary" @click="this.noOfSteps++">Add Step</button>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <th><label for="newRecipeIngredients">Ingredients Required</label></th>
                        <td class="d-flex justify-content-center">
                            <table id="newRecipeIngredients">
                                <tr><td>Ingredient</td><td>Amount</td></tr>
                                <tr v-for="i in noOfIngredients">
                                    <td><input class="form-control ingredient" type="text" placeholder="e.g. salt" v-model="this.newRecipeIngredients[i-1]"></td>
                                    <td><input class="form-control measure" type="text" placeholder="e.g. 1 tbsp" v-model="this.newRecipeIngredientsMeasure[i-1]"></td>
                                </tr>
                                <br>
                                <tr><td colspan="2" class="text-center"><button class="btn btn-small btn-primary" @click="this.noOfIngredients++">Add Ingredient</button></td></tr>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <th><label for="newRecipeImage">Upload Image</label></th>
                        <td>
                            <div v-if="newRecipeImagePreview == null">
                                Preview:<br>
                                <img :src="newRecipeImagePath" height="268" width="356" alt="">
                            </div>
                            <div v-else>
                                Preview:<br>
                                <img :src="newRecipeImagePreview" height="268" width="356" alt="">
                            </div>
                            <input type="file" class="form-control" @change="previewImage">
                            <br>
                        </td>
                    </tr>
                    <tr>
                        <td></td>
                        <td class="text-center d-grid gap-2">
                            <button type="button" class="btn btn-primary" @click="updateDatabase">Update</button>
                        </td>
                    </tr>
                </table>
            </div>
        </div>
        

        <div class="row d-flex justify-content-center">
            <div class="col">
                <div class="form-group">
                    
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import NavBar from "../components/NavBar.vue"
import { getDatabase, ref, get, remove } from '@firebase/database';
import defaultExport, * as storage from "firebase/storage";
import { uploadBytes } from "firebase/storage";
import axios from "axios";

export default {
    data() {
        return {
            newRecipeId: this.id,
            newRecipeName: "",
            newRecipeCategory: "Beef",
            noOfSteps: 1,
            newRecipeInstructions: "",
            newRecipeIngredients: [],
            newRecipeIngredientsMeasure: [],
            noOfIngredients: 1,

            newRecipeImage: null,
            newRecipeImagePreview: null,
            newRecipeImagePath: null,

            error: null
        }
    },
    components: {
        NavBar
    },
    props: ["id"],
    methods: {
        getRecipeInstructions() {
            let recipeInstructions = "";
            let instructions = document.getElementById("newRecipeInstructions");
            let steps = instructions.getElementsByTagName("input");
            for (let i of steps) {
                recipeInstructions += i.value + "\r\n";
            }
            console.log(recipeInstructions);
            this.newRecipeInstructions = recipeInstructions;
        },
        getRecipeIngredients() {
            let recipeIngredients = [];
            let recipeIngredientsMeasure = [];
            let tempRecipeIngredients = [];
            let tempRecipeIngredientsMeasure = [];
            let table = document.getElementById("newRecipeIngredients");
            let ingredients = table.getElementsByTagName("tr");
            for (let ingredient of ingredients) {
                let item = ingredient.getElementsByTagName("td")[0];
                let count = ingredient.getElementsByTagName("td")[1];
                // console.log(item);
                // console.log(count);
                tempRecipeIngredients.push(item);
                tempRecipeIngredientsMeasure.push(count);
            }
            tempRecipeIngredients.shift();
            tempRecipeIngredientsMeasure.shift();

            for (let i=0; i<this.noOfIngredients; i++) {
                let ingredient = tempRecipeIngredients[i].getElementsByTagName("input")[0].value;
                let measure = tempRecipeIngredientsMeasure[i].getElementsByTagName("input")[0].value;

                recipeIngredients.push(ingredient);
                recipeIngredientsMeasure.push(measure);
            }
            // console.log(recipeIngredients);
            // console.log(recipeIngredientsMeasure);

            this.newRecipeIngredients = recipeIngredients;
            this.newRecipeIngredientsMeasure = recipeIngredientsMeasure;
        },
        previewImage(event) {
            this.newRecipeImage = event.target.files[0];
            console.log(this.newRecipeImage);
            this.newRecipeImagePreview = URL.createObjectURL(this.newRecipeImage);
        },
        getRecipe() {
            // full parent function
            console.log("update Recipe")
            let userId = this.$store.state.userId;

            const db = getDatabase();
            const recipesRef = ref(db, `community`);
            const usersRef = ref(db, `users/${userId}/recipes`);

            get(recipesRef)
            .then((snapshot) => {
                let data = snapshot.val();
                // console.log(data);
                for (let i in data) {
                    if (data[i].id == this.id) {
                        let recipeDetails = data[i];
                        this.initaliseRecipeDetails(recipeDetails);
                        this.viewRecipeDetails();
                    }
                }
            })
            .catch((error) => {
                console.log(error.message);
            })
        },
        initaliseRecipeDetails(recipeDetails) {
            console.log(recipeDetails);
            // to turn instructions from a string to an array for processing
            let recipeInstructions = recipeDetails.instructions.split("\r\n");
            // console.log(recipeInstructions);
            let removeBlank = recipeInstructions.pop();
            if (removeBlank != "") {
                recipeInstructions.push(removeBlank);
            }

            // to turn ingredients and measures from 20 variables into 1 array
            let ingredientArray = [];
            let measureArray = [];

            for (let i=1; i<21; i++) {
                let ingredient = "strIngredient" + i;
                let measure = "strMeasure" + i;
                if (recipeDetails[ingredient] != "") {
                    // console.log(recipeDetails[ingredient]);
                    ingredientArray.push(recipeDetails[ingredient]);
                }
                if (recipeDetails[measure] != "") {
                    measureArray.push(recipeDetails[measure]);
                }
            }
            
            this.newRecipeName = recipeDetails.title;
            this.newRecipeImagePath = recipeDetails.image;
            this.newRecipeCategory = recipeDetails.category;
            this.newRecipeInstructions = recipeInstructions;
            this.noOfSteps = recipeInstructions.length;
            this.newRecipeIngredients = ingredientArray;
            this.newRecipeIngredientsMeasure = measureArray;
            this.noOfIngredients = this.newRecipeIngredients.length;

        },
        viewRecipeDetails() {
            console.log("newRecipeName: " + this.newRecipeName);
            console.log("newRecipeCategory: " + this.newRecipeCategory);
            console.log("noOfSteps: " + this.noOfSteps);
            console.log("newRecipeInstructions: " + this.newRecipeInstructions);
            console.log("newRecipeIngredients: " + this.newRecipeIngredients);
            console.log("newRecipeIngredientsMeasure: " + this.newRecipeIngredientsMeasure);
            console.log("noOfIngredients: " + this.noOfIngredients);
            console.log("newRecipeImage: " + this.newRecipeImage);
            console.log("newRecipeImagePreview: " + this.newRecipeImagePreview);
            console.log("newRecipeImagePath: " + this.newRecipeImagePath);
            console.log("error: " + this.error);
        },
        updateDatabase() {
            console.log("##### UPDATE DATABASE START #####");
            console.log("##### DATA COLLECTED START#####");
            console.log("newRecipeName: " + this.newRecipeName);
            console.log("newRecipeCategory: " + this.newRecipeCategory);
            console.log("noOfSteps: " + this.noOfSteps);
            console.log("newRecipeInstructions: " + this.newRecipeInstructions);
            console.log("newRecipeIngredients: " + this.newRecipeIngredients);
            console.log("newRecipeIngredientsMeasure: " + this.newRecipeIngredientsMeasure);
            console.log("noOfIngredients: " + this.noOfIngredients);
            console.log("newRecipeImage: " + this.newRecipeImage);
            console.log("newRecipeImagePreview: " + this.newRecipeImagePreview);
            console.log("newRecipeImagePath: " + this.newRecipeImagePath);
            console.log("error: " + this.error);
            console.log("##### DATA COLLECTED END #####");
            console.log("##### UPDATE DATABASE END #####");

            const store = storage.getStorage();
            if (this.newRecipeImage != null) {
                var storageRef = storage.ref(store, `${this.$store.state.userId}/${this.newRecipeImage.name}`);
                console.log(storageRef);
                storage.uploadBytes(storageRef, this.newRecipeImage).then((snapshot) => {
                    console.log('Uploaded image successfully!');
                    storage.getDownloadURL(storageRef).then(downloadURL => {
                        this.newRecipeImagePath = downloadURL;
                        console.log("Download URL:" + this.newRecipeImagePath);

                        this.getRecipeInstructions();
                        this.getRecipeIngredients();

                        let simpleFoodTemplate = {
                            id: this.newRecipeId,
                            title: this.newRecipeName,
                            image: this.newRecipeImagePath
                        }

                        let fullFoodTemplate = {
                            id: this.newRecipeId,
                            title: this.newRecipeName,
                            image: this.newRecipeImagePath,
                            category: this.newRecipeCategory,
                            instructions: this.newRecipeInstructions,
                            
                            "strIngredient1": "",
                            "strIngredient2": "",
                            "strIngredient3": "",
                            "strIngredient4": "",
                            "strIngredient5": "",
                            "strIngredient6": "",
                            "strIngredient7": "",
                            "strIngredient8": "",
                            "strIngredient9": "",
                            "strIngredient10": "",
                            "strIngredient11": "",
                            "strIngredient12": "",
                            "strIngredient13": "",
                            "strIngredient14": "",
                            "strIngredient15": "",
                            "strIngredient16": "",
                            "strIngredient17": "",
                            "strIngredient18": "",
                            "strIngredient19": "",
                            "strIngredient20": "",

                            "strMeasure1": "",
                            "strMeasure2": "",
                            "strMeasure3": "",
                            "strMeasure4": "",
                            "strMeasure5": "",
                            "strMeasure6": "",
                            "strMeasure7": "",
                            "strMeasure8": "",
                            "strMeasure9": "",
                            "strMeasure10": "",
                            "strMeasure11": "",
                            "strMeasure12": "",
                            "strMeasure13": "",
                            "strMeasure14": "",
                            "strMeasure15": "",
                            "strMeasure16": "",
                            "strMeasure17": "",
                            "strMeasure18": "",
                            "strMeasure19": "",
                            "strMeasure20": ""
                        }

                        for (let i=1; i<this.newRecipeIngredients.length + 1; i++) {
                            let ingredient = "strIngredient" + i
                            let measure = "strMeasure" + i
                            fullFoodTemplate[ingredient] = this.newRecipeIngredients[i-1]
                            fullFoodTemplate[measure] = this.newRecipeIngredientsMeasure[i-1]
                        }

                        // console.log(fullFoodTemplate)
                        let userId = this.$store.state.userId;
                        let db = getDatabase();
                        let recipesRef = ref(db, "community");
                        const usersRef = ref(db, `users/${userId}/recipes`);

                        get(recipesRef)
                        .then((snapshot) => {
                            let data = snapshot.val();
                            // console.log(data);
                            for (let i in data) {
                                // console.log(data[i]);
                                if (data[i].id == this.id) {
                                    let updateRef = ref(db, `community/${i}`);
                                    remove(updateRef).then(() => {
                                        console.log("location removed");
                                        axios.post(`https://wad-proj-22042-default-rtdb.asia-southeast1.firebasedatabase.app/community.json`,fullFoodTemplate);

                                        get(usersRef)
                                        .then((snapshot) => {
                                            let data = snapshot.val();
                                            for (let i in data) {
                                                // console.log(data[i]);
                                                if (data[i].id == this.id) {
                                                    let updateRef = ref(db, `users/${userId}/recipes/${i}`);
                                                    remove(updateRef).then(() => {
                                                        console.log("Location removed");
                                                        axios.post(`https://wad-proj-22042-default-rtdb.asia-southeast1.firebasedatabase.app/users/${this.$store.state.userId}/recipes.json`, simpleFoodTemplate)
                                                        .then((response) => {
                                                            // console.log(response);
                                                            window.location.reload();
                                                        });
                                                    })
                                                }
                                            }
                                        })
                                        .catch((error) => {
                                            console.log(error.message);
                                        })
                                    });
                                }
                            }
                        })
                        .catch((error) => {
                            console.log(error.message);
                        })
                    })
                })
            } else {
                
                this.getRecipeInstructions();
                this.getRecipeIngredients();

                let simpleFoodTemplate = {
                    id: this.newRecipeId,
                    title: this.newRecipeName,
                    image: this.newRecipeImagePath
                }

                let fullFoodTemplate = {
                    id: this.newRecipeId,
                    title: this.newRecipeName,
                    image: this.newRecipeImagePath,
                    category: this.newRecipeCategory,
                    instructions: this.newRecipeInstructions,
                    
                    "strIngredient1": "",
                    "strIngredient2": "",
                    "strIngredient3": "",
                    "strIngredient4": "",
                    "strIngredient5": "",
                    "strIngredient6": "",
                    "strIngredient7": "",
                    "strIngredient8": "",
                    "strIngredient9": "",
                    "strIngredient10": "",
                    "strIngredient11": "",
                    "strIngredient12": "",
                    "strIngredient13": "",
                    "strIngredient14": "",
                    "strIngredient15": "",
                    "strIngredient16": "",
                    "strIngredient17": "",
                    "strIngredient18": "",
                    "strIngredient19": "",
                    "strIngredient20": "",

                    "strMeasure1": "",
                    "strMeasure2": "",
                    "strMeasure3": "",
                    "strMeasure4": "",
                    "strMeasure5": "",
                    "strMeasure6": "",
                    "strMeasure7": "",
                    "strMeasure8": "",
                    "strMeasure9": "",
                    "strMeasure10": "",
                    "strMeasure11": "",
                    "strMeasure12": "",
                    "strMeasure13": "",
                    "strMeasure14": "",
                    "strMeasure15": "",
                    "strMeasure16": "",
                    "strMeasure17": "",
                    "strMeasure18": "",
                    "strMeasure19": "",
                    "strMeasure20": ""
                }

                for (let i=1; i<this.newRecipeIngredients.length + 1; i++) {
                    let ingredient = "strIngredient" + i;
                    let measure = "strMeasure" + i;
                    fullFoodTemplate[ingredient] = this.newRecipeIngredients[i-1];
                    fullFoodTemplate[measure] = this.newRecipeIngredientsMeasure[i-1];
                }

                let userId = this.$store.state.userId;
                let db = getDatabase();
                let recipesRef = ref(db, "community");
                const usersRef = ref(db, `users/${userId}/recipes`);

                get(recipesRef)
                .then((snapshot) => {
                    let data = snapshot.val();
                    // console.log(data);
                    for (let i in data) {
                        // console.log(data[i]);
                        if (data[i].id == this.id) {
                            let updateRef = ref(db, `community/${i}`);
                            remove(updateRef).then(() => {
                                //console.log("location removed");
                                axios.post(`https://wad-proj-22042-default-rtdb.asia-southeast1.firebasedatabase.app/community.json`,fullFoodTemplate);

                                get(usersRef)
                                .then((snapshot) => {
                                    let data = snapshot.val();
                                    for (let i in data) {
                                        // console.log(data[i]);
                                        if (data[i].id == this.id) {
                                            let deleteRef = ref(db, `users/${userId}/recipes/${i}`);
                                            remove(deleteRef).then(() => {
                                                // console.log("Location removed");
                                                axios.post(`https://wad-proj-22042-default-rtdb.asia-southeast1.firebasedatabase.app/users/${this.$store.state.userId}/recipes.json`, simpleFoodTemplate)
                                                .then((response) => {
                                                    // console.log(response.data)
                                                    window.location.reload();
                                                });
                                            })
                                        }
                                    }
                                })
                                .catch((error) => {
                                    console.log(error.message);
                                })
                            });
                        }
                    }
                })
                .catch((error) => {
                    console.log(error.message);
                })
            }
        }
    },
    created() {
        // console.log(this.id);
        this.$store.state.activerecipeid = this.id;
        this.getRecipe();
    }
}
</script>
    
<style></style>
  