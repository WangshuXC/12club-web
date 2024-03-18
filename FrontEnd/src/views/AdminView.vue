<template>
    <h1>hello administrator</h1>

    <v-card title="Nutrition" flat>
        <template v-slot:text>
            <v-text-field v-model="search" label="Search" prepend-inner-icon="mdi-magnify" variant="outlined"
                hide-details single-line></v-text-field>
        </template>

        <v-data-table :headers="headers" :items="desserts" :search="search">
            <template v-slot:item="{ item }">
                <tr @click="handleItemClick(item)">
                    <td>{{ item.name }}</td>
                    <td>{{ item.calories }}</td>
                    <td>{{ item.fat }}</td>
                    <td>{{ item.carbs }}</td>
                    <td>{{ item.protein }}</td>
                </tr>
            </template>
        </v-data-table>
    </v-card>

    <div class="add-container">
        <div class="add-box">
            <v-btn prepend-icon="mdi-movie" @click="showAddEditor('Anime')" size="x-large"
                :color="addForm.type === 'Anime' ? 'blue' : ''">Add Anime</v-btn>
            <v-btn prepend-icon="mdi-music" @click="showAddEditor('Music')" size="x-large"
                :color="addForm.type === 'Music' ? 'blue' : ''">Add Music</v-btn>
        </div>
        <div class="add-editor" v-if="showEditor">
            <div>
                <v-img v-if="coverUrl" :src="coverUrl" alt="Cover Image" max-height="20vw"
                    style="margin-bottom: 20px ;" />
                <v-file-input accept="image/*" label="Cover" v-model="addForm.coverImage" prepend-icon="mdi-paperclip"
                    variant="solo-filled" @change="handleFileUpload"></v-file-input>
                <v-text-field v-model="addForm.title" label="Title" placeholder="输入动漫标题" prepend-icon="mdi-pencil"
                    variant="solo" clearable></v-text-field>
                <v-text-field v-if="addForm.type === 'Anime'" v-model="addForm.anotherTitle" label="AnotherTitle"
                    placeholder="输入动漫别名" prepend-icon="mdi-pencil" variant="solo" clearable></v-text-field>
                <v-text-field v-if="addForm.type === 'Anime'" v-model="addForm.japaneseTitle" label="japaneseTitle"
                    placeholder="输入动漫日文标题" prepend-icon="mdi-pencil" variant="solo" clearable></v-text-field>
                <v-textarea v-model="addForm.description" label="Description" placeholder="输入动漫简介"
                    prepend-icon="mdi-pencil" variant="solo" clearable></v-textarea>
            </div>
            <v-file-input v-model="addForm.addFiles" :show-size="1024" label="File input" placeholder="按住Ctrl再点击实现多选"
                prepend-icon="mdi-paperclip" variant="solo-filled" counter multiple>
                <template v-slot:selection="{ fileNames }">
                    <template v-for="fileName in fileNames" :key="fileName">
                        <v-chip class="me-2" color="deep-purple-accent-4" size="small" label>
                            {{ fileName }}
                        </v-chip>
                    </template>
                </template>
            </v-file-input>

            <v-dialog v-model="dialog" max-width="50%" persistent>
                <template v-slot:activator="{ props: activatorProps }">
                    <v-btn v-bind="activatorProps" style="width: 50%; margin: auto;" color="success" size="large"
                        @click="sortFile()">
                        Add
                    </v-btn>

                    <v-btn @click="showEditor = false; addForm.type = ''"
                        style="width: 50%; margin: auto;margin-top: 30px;" color="error" size="large">
                        Cancel
                    </v-btn>
                </template>

                <v-card>
                    <v-card-title class="text-h4" style="margin: auto;margin-top: 20px;">
                        Make sure your file-list's order is right
                    </v-card-title>
                    <v-spacer></v-spacer>
                    <div v-for="(file, index) in addForm.addFiles" :key="index" style="margin: auto;">
                        {{ file.name }} => {{ index + 1 }}.{{ file.name.split('.').pop() }}
                        <v-spacer></v-spacer>
                    </div>
                    <template v-slot:actions>
                        <v-spacer></v-spacer>

                        <v-btn @click="dialog = false">
                            Cancel
                        </v-btn>
                        <v-btn @click="dialog = false, this.addUpload()">
                            I am sure
                        </v-btn>
                    </template>
                </v-card>
            </v-dialog>
        </div>
    </div>
    <div class="edit-container"></div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            showEditor: false,
            addForm: {
                coverImage: null,
                title: '',
                anotherTitle: '',
                japaneseTitle: '',
                description: '',
                type: '',
                addFiles: [],
            },
            coverUrl: null,
            dialog: false,
            search: '',
            headers: [
                {
                    align: 'start',
                    key: 'name',
                    sortable: false,
                    title: 'Dessert (100g serving)',
                },
                { key: 'calories', title: 'Calories' },
                { key: 'fat', title: 'Fat (g)' },
                { key: 'carbs', title: 'Carbs (g)' },
                { key: 'protein', title: 'Protein (g)' },
                { key: 'iron', title: 'Iron (%)' },
            ],
            desserts: [
                {
                    name: 'Frozen Yogurt',
                    calories: 159,
                    fat: 6.0,
                    carbs: 24,
                    protein: 4.0,
                    iron: 1,
                },
                {
                    name: 'Ice cream sandwich',
                    calories: 237,
                    fat: 9.0,
                    carbs: 37,
                    protein: 4.3,
                    iron: 1,
                },
                {
                    name: 'Eclair',
                    calories: 262,
                    fat: 16.0,
                    carbs: 23,
                    protein: 6.0,
                    iron: 7,
                },
                {
                    name: 'Cupcake',
                    calories: 305,
                    fat: 3.7,
                    carbs: 67,
                    protein: 4.3,
                    iron: 8,
                },
                {
                    name: 'Gingerbread',
                    calories: 356,
                    fat: 16.0,
                    carbs: 49,
                    protein: 3.9,
                    iron: 16,
                },
                {
                    name: 'Jelly bean',
                    calories: 375,
                    fat: 0.0,
                    carbs: 94,
                    protein: 0.0,
                    iron: 0,
                },
                {
                    name: 'Lollipop',
                    calories: 392,
                    fat: 0.2,
                    carbs: 98,
                    protein: 0,
                    iron: 2,
                },
                {
                    name: 'Honeycomb',
                    calories: 408,
                    fat: 3.2,
                    carbs: 87,
                    protein: 6.5,
                    iron: 45,
                },
                {
                    name: 'Donut',
                    calories: 452,
                    fat: 25.0,
                    carbs: 51,
                    protein: 4.9,
                    iron: 22,
                },
                {
                    name: 'KitKat',
                    calories: 518,
                    fat: 26.0,
                    carbs: 65,
                    protein: 7,
                    iron: 6,
                },
            ],
        };
    },
    mounted() {
    },
    methods: {
        handleFileUpload(event) {
            const file = event.target.files[0];
            if (file) {
                this.coverUrl = URL.createObjectURL(file);
            }
        },
        showAddEditor(type) {
            this.addForm.type = type;
            this.showEditor = true;
        },
        sortFile() {
            console.log(this.addForm.addFiles);
            this.addForm.addFiles.sort((a, b) => a.name.localeCompare(b.name));
            console.log('-----------------');
            console.log(this.addForm.addFiles);
        },
        addUpload() {
            // this.addForm.addFiles.sort((a, b) => {
            //     const cleanFileName = (filename) => filename.replace(/\[.*?\]/g, '');
            //     return cleanFileName(a).localeCompare(cleanFileName(b));
            // });
            const formData = new FormData();
            formData.append('coverImage', new Blob(this.addForm.coverImage, { type: "image/jpeg" }), "Cover.jpg");
            formData.append('title', this.addForm.title);
            formData.append('anotherTitle', this.addForm.anotherTitle);
            formData.append('japaneseTitle', this.addForm.japaneseTitle);
            formData.append('description', this.addForm.description);
            formData.append('type', this.addForm.type);
            for (var i = 0; i < this.addForm.addFiles.length; i++) {
                const file = this.addForm.addFiles[i];
                const blob = new Blob([file], { type: file.type });
                const originalFileExtension = file.name.split('.').pop();
                const fileName = (i + 1) + '.' + originalFileExtension;
                formData.append('files', blob, fileName);
            }

            // 发送 POST 请求
            axios.post(`${this.API_URL}/upload`, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                }
            })
                .then(response => {
                    this.showEditor = false;
                    this.coverUrl = null;
                    this.addForm = {
                        coverImage: null,
                        title: '',
                        anotherTitle: '',
                        japaneseTitle: '',
                        description: '',
                        type: '',
                        addFiles: [],
                    }
                    console.log(response.data);
                })
                .catch(error => {
                    console.error(error);
                });
        }
    },
};
</script>

<style scoped>
.add-container {
    display: flex;
    flex-direction: column;
    width: 80vw;
    margin-inline: auto;
    margin-top: 20px;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f5f5f5;

    .add-box {
        display: flex;
        justify-content: space-around;
        width: 100%;
        height: auto;
    }

    .add-editor {
        display: flex;
        flex-direction: column;
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        background-color: #fff;
    }
}
</style>