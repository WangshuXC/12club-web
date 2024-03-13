<template>
    <h1>hello administrator</h1>

    <div class="add-container">
        <div class="add-box">
            <button class="add-anime" @click="showAddEditor('anime')">Add Anime</button>
            <button class="add-music" @click="showAddEditor('music')">Add Music</button>
        </div>
        <div class="add-editor" v-if="showEditor">
            <div>
                <v-img v-if="coverUrl" :src="coverUrl" alt="Cover Image" max-height="250"
                    style="margin-bottom: 20px ;" />
                <v-file-input accept="image/*" label="Cover" v-model="coverImage" prepend-icon="mdi-image"
                    variant="solo" @change="handleFileUpload"></v-file-input>
                <v-text-field label="Title" placeholder="Title" prepend-icon="mdi-pencil" variant="solo"
                    clearable></v-text-field>
                <v-textarea label="Description" placeholder="Description" prepend-icon="mdi-pencil" variant="solo"
                    clearable></v-textarea>
            </div>
            <v-file-input v-model="addFiles" :show-size="1024" label="File input" placeholder="按住Ctrl再点击实现多选"
                prepend-icon="mdi-paperclip" variant="solo" counter multiple>
                <template v-slot:selection="{ fileNames }">
                    <template v-for="fileName in fileNames" :key="fileName">
                        <v-chip class="me-2" color="deep-purple-accent-4" size="small" label>
                            {{ fileName }}
                        </v-chip>
                    </template>
                </template>
            </v-file-input>
        </div>
    </div>
    <div class="edit-container"></div>
</template>

<script>
export default {
    data() {
        return {
            showEditor: false,
            addFiles: [],
            coverImage: null,
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
            // 根据类型处理逻辑，这里简单示例
            // 如果是动画类型，设置 showEditor 为 true
            this.showEditor = true;
        },
        addUpload() {
            // 点击添加按钮后增加一个上传栏
            this.uploads.push(this.uploads.length);
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