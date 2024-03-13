<template>
    <h1>hello administrator</h1>

    <div class="add-container">
        <div class="add-box">
            <button class="add-anime" @click="showAddEditor('Anime')">Add Anime</button>
            <button class="add-music" @click="showAddEditor('Music')">Add Music</button>
        </div>
        <div class="add-editor" v-if="showEditor">
            <div>
                <v-img v-if="coverUrl" :src="coverUrl" alt="Cover Image" max-height="20vw"
                    style="margin-bottom: 20px ;" />
                <v-file-input accept="image/*" label="Cover" v-model="addForm.coverImage" prepend-icon="mdi-image"
                    variant="solo" @change="handleFileUpload"></v-file-input>
                <v-text-field v-model="addForm.title" label="Title" placeholder="Title" prepend-icon="mdi-pencil"
                    variant="solo" clearable></v-text-field>
                <v-textarea v-model="addForm.description" label="Description" placeholder="Description"
                    prepend-icon="mdi-pencil" variant="solo" clearable></v-textarea>
            </div>
            <v-file-input v-model="addForm.addFiles" :show-size="1024" label="File input" placeholder="按住Ctrl再点击实现多选"
                prepend-icon="mdi-paperclip" variant="solo" counter multiple>
                <template v-slot:selection="{ fileNames }">
                    <template v-for="fileName in fileNames" :key="fileName">
                        <v-chip class="me-2" color="deep-purple-accent-4" size="small" label>
                            {{ fileName }}
                        </v-chip>
                    </template>
                </template>
            </v-file-input>
            <v-btn @click="addUpload" style="width: 50%;margin: auto;" color="success" size="large">Add</v-btn>
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
                description: '',
                type: '',
                addFiles: [],
                // ... 其他字段
            },
            coverUrl: null,
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
            // 根据类型处理逻辑，这里简单示例
            // 如果是动画类型，设置 showEditor 为 true
            this.showEditor = true;
        },
        addUpload() {
            console.log('addUpload:', this.addForm);
            const formData = new FormData();
            formData.append('coverImage', this.addForm.coverImage);
            formData.append('title', this.addForm.title);
            formData.append('description', this.addForm.description);
            formData.append('type', this.addForm.type);
            for (let i = 0; i < this.addForm.addFiles.length; i++) {
                formData.append('files', this.addForm.addFiles[i]);
            }

            if (formData) {
                axios.post(`${this.API_URL}/upload`, formData)
                    .then(response => {
                        console.log('Upload successful:', response.data);
                        this.showEditor = false;
                        this.addForm.coverImage = null;
                        this.addForm.title = '';
                        this.addForm.description = '';
                        this.addForm.addFiles = [];
                        this.coverUrl = null;
                    })
                    .catch(error => {
                        console.error('Error uploading the file:', error);
                    });
            }

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
        width: 100%;
        height: 10vh;

        .add-anime {
            flex: 1;
            padding: 20px;
            margin-right: 30px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #fff;
        }

        .add-music {
            flex: 1;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #fff;
        }
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