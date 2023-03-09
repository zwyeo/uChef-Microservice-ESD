<template>
    <div class="container-fluid px-5">
        <nav-bar></nav-bar>

        <h2 class="text-center pb-5">Add New Recipe</h2>

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
                                <input v-for="i in noOfSteps" class="form-control" type="text" :placeholder="i">
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
                                    <td><input class="form-control ingredient" type="text" placeholder="e.g. salt"></td>
                                    <td><input class="form-control measure" type="text" placeholder="e.g. 1 tbsp"></td>
                                </tr>
                                <br>
                                <tr><td colspan="2" class="text-center"><button class="btn btn-small btn-primary" @click="this.noOfIngredients++">Add Ingredient</button></td></tr>
                                <br>
                            </table>
                        </td>
                    </tr>
                    <tr>
                        <th><label for="newRecipeImage">Upload Image</label></th>
                        <td>
                            <div v-if="newRecipeImagePreview != null">
                            Preview:<br>
                            <img
                                :src="newRecipeImagePreview"
                                height="268"
                                width="356"
                                alt=""
                            />
                            </div>
                            <input
                                type="file"
                                class="form-control"
                                @change="previewImage"
                            />
                            <br>
                        </td>
                    </tr>
                    <tr>
                        <td></td>
                        <td class="text-center d-grid gap-2">
                            <button type="button" class="btn btn-primary" @click="createNewRecipe">Create</button>
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

import NavBar from "../components/NavBar.vue";
import axios from "axios";
import { getStorage, ref, uploadBytes, getDownloadURL } from "firebase/storage";
import { uuidv4 } from "@firebase/util";

export default {
    name: "AddRecipePage",
    data() {
        return {
            newRecipeId: "",
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
    methods: {
        getRecipeInstructions() {
            let recipeInstructions = "";
            let instructions = document.getElementById("newRecipeInstructions");
            let steps = instructions.getElementsByTagName("input");
            for (let i of steps) {
                recipeInstructions += i.value + "\r\n";
            }
            // console.log(recipeInstructions);
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
            // console.log(this.newRecipeImage);
            this.newRecipeImagePreview = URL.createObjectURL(this.newRecipeImage);
        },
        createNewRecipe() {
            const storage = getStorage();
            if (this.newRecipeImage != null) {
                var storageRef = ref(storage, `${this.$store.state.userId}/${this.newRecipeImage.name}`);

                // Upload function for uploading image into firebase cloud storage
                // Note: anything that requires the data from inside this function needs to be written inside, as this is an async request
                uploadBytes(storageRef, this.newRecipeImage).then((snapshot) => {
                    console.log('Uploaded image successfully!');
                    getDownloadURL(storageRef).then(downloadURL => {
                        this.newRecipeImagePath = downloadURL;
                        console.log("Download URL:" + this.newRecipeImagePath);

                        this.newRecipeId = uuidv4();
                        // console.log(this.newRecipeId);
                        this.getRecipeInstructions();
                        this.getRecipeIngredients();

                        // console.log(this.newRecipeIngredients);
                        // console.log(this.newRecipeIngredientsMeasure);

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

                        axios.post(`https://wad-proj-22042-default-rtdb.asia-southeast1.firebasedatabase.app/users/${this.$store.state.userId}/recipes.json`, simpleFoodTemplate)
                        .then((response) => {
                            console.log(response.data);
                            axios.post(`https://wad-proj-22042-default-rtdb.asia-southeast1.firebasedatabase.app/community/${this.newRecipeId}.json`, fullFoodTemplate)
                            .then((response) => {
                                console.log(response.data);
                                window.location.href = "/my-recipes";
                            })
                            .catch(error => {
                                console.log(error);
                                this.error = error;
                            })
                        })
                        .catch(error => {
                            console.log(error);
                            this.error = error;
                        });
                        // clear inputs
                        this.newRecipeId = "";
                        this.newRecipeName = "";
                        this.newRecipeCategory = "Beef";
                        this.noOfSteps = 1;
                        this.newRecipeInstructions = "";
                        this.newRecipeIngredients = [];
                        this.newRecipeIngredientsMeasure = [];
                        this.noOfIngredients = 1;

                        this.newRecipeImage = null;
                        this.newRecipeImagePreview = null;
                        this.newRecipeImagePath = null;
                        
                        this.error = null;
                    })
                })
            } else {
                this.error = "Please upload an image!";
                console.log(this.error);
                alert(this.error);
            }
        }
    }
}
</script>

<style></style>