<template>
    <h1>hello administrator</h1>
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
                <v-text-field v-if="addForm.type === 'Anime'" v-model="addForm.japansesTitle" label="JapansesTitle"
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
            <!-- <v-btn @click="dialog = !dialog" style="width: 50%;margin: auto;" color="success" size="large">Add</v-btn> -->
            <v-dialog v-model="dialog" max-width="50%" persistent>
                <template v-slot:activator="{ props: activatorProps }">
                    <v-btn v-bind="activatorProps" style="width: 50%; margin: auto;" color="success" size="large">
                        Add
                    </v-btn>

                    <v-btn @click="this.showEditor = false" style="width: 50%; margin: auto;margin-top: 30px;"
                        color="error" size="large">
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
                japansesTitle: '',
                description: '',
                type: '',
                addFiles: [],
            },
            coverUrl: null,
            dialog: false,
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
        addUpload() {
            // this.addForm.addFiles.sort((a, b) => {
            //     const cleanFileName = (filename) => filename.replace(/\[.*?\]/g, '');
            //     return cleanFileName(a).localeCompare(cleanFileName(b));
            // });
            const formData = new FormData();
            formData.append('coverImage', new Blob(this.addForm.coverImage, { type: "image/jpeg" }), "Cover.jpg");
            formData.append('title', this.addForm.title);
            formData.append('anotherTitle', this.addForm.anotherTitle);
            formData.append('japansesTitle', this.addForm.japansesTitle);
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
        height: 10vh;
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