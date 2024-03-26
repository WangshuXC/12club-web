<template>
    <h1>hello administrator</h1>

    <div class="add-container">
        <div class="add-box">
            <v-btn prepend-icon="mdi-movie" @click="toggleShow('add', 'Anime')" size="x-large"
                :color="addForm.type === 'Anime' ? 'blue' : ''">Add Anime</v-btn>
            <v-btn prepend-icon="mdi-music" @click="toggleShow('add', 'Music')" size="x-large"
                :color="addForm.type === 'Music' ? 'blue' : ''">Add Music</v-btn>
        </div>
        <div class="add-editor" v-if="showAddEditor">
            <div>
                <v-img v-if="uploadCoverUrl" :src="uploadCoverUrl" alt="Cover Image" max-height="20vw"
                    style="margin-bottom: 20px ;" />
                <v-file-input accept="image/*" label="Cover" v-model="addForm.coverImage" prepend-icon="mdi-paperclip"
                    variant="solo-filled" @change="uploadCover($event, 'upload')"></v-file-input>
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
                        <v-chip color="deep-purple-accent-4" size="small" label>
                            {{ fileName }}
                        </v-chip>
                    </template>
                </template>
            </v-file-input>

            <v-dialog v-model="uploadDialog" max-width="50%" persistent>
                <template v-slot:activator="{ props: addActivatorProps }">
                    <v-btn v-bind="addActivatorProps" style="width: 50%; margin: auto;" color="success" size="large"
                        @click="sortFile(this.addForm.addFiles)">
                        Add
                    </v-btn>
                </template>

                <v-card v-if="uploadFlag">
                    <v-card-title class="text-h4" style="margin: auto;margin-top: 20px;">
                        确认上传文件的顺序
                    </v-card-title>
                    <v-spacer></v-spacer>
                    <div v-for="(file, index) in addForm.addFiles" :key="index" style="margin: auto;">
                        {{ file.name }} => {{ index + 1 }}.{{ file.name.split('.').pop() }}
                        <v-spacer></v-spacer>
                    </div>
                    <template v-slot:actions>
                        <v-spacer></v-spacer>

                        <v-btn @click="uploadDialog = false">
                            Cancel
                        </v-btn>
                        <v-btn @click="this.addUpload()">
                            I am sure
                        </v-btn>
                    </template>
                </v-card>

                <v-card v-if="!uploadFlag">
                    <v-progress-linear color="light-blue" height="20" v-model="uploadProgress"
                        striped></v-progress-linear>
                </v-card>
            </v-dialog>
        </div>
    </div>

    <div class="edit-container">
        <div class="edit-box">
            <v-btn prepend-icon="mdi-movie" @click="toggleShow('edit', 'Anime')" size="x-large"
                :color="editForm.type === 'Anime' ? 'blue' : ''">Edit Anime</v-btn>
            <v-btn prepend-icon="mdi-music" @click="toggleShow('edit', 'Music')" size="x-large"
                :color="editForm.type === 'Music' ? 'blue' : ''">Edit Music</v-btn>
        </div>
        <div class="edit-editor" v-if="showEditEditor">
            <!-- 表格 -->
            <!-- <v-card flat>
                <template v-slot:text>
                    <v-text-field v-model="search" label="Search" prepend-inner-icon="mdi-magnify" variant="outlined"
                        hide-details single-line></v-text-field>
                </template>

                <v-data-table :headers="headers" :items="animeList" :search="search">
                    <template v-slot:item="{ item }">
                        <tr @click="editItemClick(item)" class="tableItem">
                            <td>{{ item.title }}</td>
                            <td>{{ item.title_anothor }}</td>
                            <td>{{ item.update_date }}</td>
                            <td>{{ item.release_date }}</td>
                        </tr>
                    </template>
                </v-data-table>
            </v-card> -->
            <!-- 表格 -->
            <v-select v-model="selectedItem" :item-props="itemProps" item-value="id" :items="animeList"
                label="Selector">
            </v-select>
            <div v-if="selectedItem">
                <v-img v-if="selectedItem" :src="`${DATA_URL}/${editForm.type}/${editForm.title}/Cover.jpg`"
                    alt="Cover Image" max-height="20vw" style="margin-bottom: 20px ;" />
                <v-file-input accept="image/*" label="Update Cover" v-model="editForm.coverImage"
                    prepend-icon="mdi-paperclip" variant="solo-filled" @change="uploadCover"></v-file-input>
                <v-text-field v-model="editForm.title" label="Edit Title" placeholder="输入动漫标题" prepend-icon="mdi-pencil"
                    variant="solo" clearable></v-text-field>
                <v-text-field v-if="editForm.type === 'Anime'" v-model="editForm.anotherTitle" label="Edit AnotherTitle"
                    placeholder="输入动漫别名" prepend-icon="mdi-pencil" variant="solo" clearable></v-text-field>
                <v-text-field v-if="editForm.type === 'Anime'" v-model="editForm.japaneseTitle"
                    label="Edit JapaneseTitle" placeholder="输入动漫日文标题" prepend-icon="mdi-pencil" variant="solo"
                    clearable></v-text-field>
                <v-textarea v-model="editForm.description" label="Edit Description" placeholder="输入动漫简介"
                    prepend-icon="mdi-pencil" variant="solo" clearable></v-textarea>
            </div>

            <div :style="{ background: '#f5f5f5', padding: '30px', marginBlock: '20px', borderRadius: '10px' }"
                v-if="selectedItem">
                <v-file-input :label="'第 ' + item + ' 集'" variant="outlined" v-for="item in editForm.episode"
                    :key="item" v-model="editForm.editFiles[item]" :show-size="1024"></v-file-input>
            </div>

            <v-file-input v-model="editForm.addFiles" :show-size="1024" label="新项上传" placeholder="按住Ctrl再点击实现多选"
                prepend-icon="mdi-paperclip" variant="solo-filled" counter multiple v-if="selectedItem">
                <template v-slot:selection="{ fileNames }">
                    <template v-for="fileName in fileNames" :key="fileName">
                        <v-chip color="deep-purple-accent-4" size="small" label>
                            {{ fileName }}
                        </v-chip>
                    </template>
                </template>
            </v-file-input>

            <v-dialog v-model="editDialog" max-width="50%" persistent v-if="selectedItem">
                <template v-slot:activator="{ props: editActivatorProps }">
                    <v-btn v-bind="editActivatorProps" style="width: 50%; margin: auto;" color="success" size="large"
                        @click="sortFile(this.editForm.addFiles)">
                        Edit
                    </v-btn>

                    <v-btn @click="deleteItem(this.editForm.id)" style="width: 50%; margin: auto;margin-top: 30px;"
                        color="error" size="large">
                        Delete
                    </v-btn>
                </template>

                <v-card v-if="editFlag">
                    <v-card-title class="text-h4" style="margin: auto;margin-top: 20px;">
                        确认要更改的内容是否正确
                    </v-card-title>
                    <v-spacer></v-spacer>
                    <div v-for="(file, index) in editForm.addFiles" :key="index" style="margin: auto;">
                        {{ file.name }} => {{ editForm.episode + index + 1 }}.{{ file.name.split('.').pop() }}
                        <v-spacer></v-spacer>
                    </div>
                    <template v-slot:actions>
                        <v-spacer></v-spacer>

                        <v-btn @click="editDialog = false">
                            Cancel
                        </v-btn>
                        <v-btn @click="editDialog = false, editUpload()">
                            I am sure
                        </v-btn>
                    </template>
                </v-card>

                <v-card v-if="!editFlag">
                    <v-progress-linear color="light-blue" height="10" model-value="uploadProgress"
                        striped></v-progress-linear>
                </v-card>
            </v-dialog>
        </div>
    </div>

</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            showAddEditor: false,
            showEditEditor: false,
            addForm: {
                coverImage: null,
                title: '',
                anotherTitle: '',
                japaneseTitle: '',
                description: '',
                type: '',
                addFiles: [],
            },
            uploadCoverUrl: null,
            editCoverUrl: null,
            uploadDialog: false,
            uploadFlag: true,
            editDialog: false,
            editFlag: true,
            search: '',
            headers: [
                {
                    align: 'start',
                    key: 'title',
                    sortable: true,
                    title: '名称',
                },
                { key: 'title_anothor', title: '别名' },
                { key: 'update_date', title: '上传时间' },
                { key: 'release_date', title: '最近更新时间' },
            ],
            animeList: [
                {
                    id: 1,
                    title: 'Frozen Yogurt',
                    title_anothor: 'Frozen Yogurt',
                    update_date: null,
                    release_date: null,
                },
            ],
            selectedItem: null,
            editForm: {
                id: -1,
                coverImage: null,
                title: '',
                anotherTitle: '',
                japaneseTitle: '',
                description: '',
                type: '',
                editFiles: [],
                addFiles: [],
                episode: 0,
            },
            uploadProgress: 0,
        };
    },
    watch: {
        selectedItem(newVal) {
            this.selectItem(newVal);
        },
    },
    mounted() {
        this.loadAnimeTable();
    },
    methods: {
        itemProps(item) {
            return {
                title: item.title,
                subtitle: item.update_date,
            }
        },
        toggleShow(addOrEdit, type) {
            if (addOrEdit === 'add') {
                if (this.showAddEditor === false) {
                    this.showAdd(type);
                } else {
                    this.addForm.type = '';
                    this.showAddEditor = !this.showAddEditor;
                }
            }

            if (addOrEdit === 'edit') {
                if (this.showEditEditor === false) {
                    this.showEdit(type)
                } else {
                    this.editForm.type = '';
                    this.showEditEditor = !this.showEditEditor;
                }
            }

        },
        uploadCover(event, type) {
            const file = event.target.files[0];
            if (file) {
                if (type === 'upload') this.uploadCoverUrl = URL.createObjectURL(file);
                if (type === 'edit') this.uploadCoverUrl = URL.createObjectURL(file);
            }
        },
        showAdd(type) {
            this.addForm.type = type;
            this.showAddEditor = true;
            this.editForm.type = '';
            this.showEditEditor = false;
        },
        showEdit(type) {
            this.editForm.type = type;
            this.showEditEditor = true;
            this.addForm.type = '';
            this.showAddEditor = false;
        },
        sortFile(list) {
            list.sort((a, b) => a.name.localeCompare(b.name));
        },
        // editItemClick(item) {
        //     this.editForm.id = item.id;
        //     this.editForm.title = item.title;
        //     this.editForm.anotherTitle = item.anotherTitle;
        //     this.editForm.japaneseTitle = item.japaneseTitle;
        //     this.editForm.description = item.description;
        // },
        selectItem(item) {
            for (const i of this.animeList) {
                if (i.id === item) {
                    this.editForm.id = item;
                    this.editForm.title = i.title;
                    this.editForm.anotherTitle = i.anotherTitle;
                    this.editForm.japaneseTitle = i.japaneseTitle;
                    this.editForm.description = i.description;
                    this.editForm.episode = i.episode;
                    this.editForm.editFiles = new Array(i.episode).fill(null);
                    break;
                }
            }
        },
        deleteItem(id) {
            const type = this.editForm.type;
            axios.delete(`${this.API_URL}/delete?id=${id}&type=${type}`)
                .then(response => {
                    console.log(response.data);
                })
                .catch(error => {
                    console.error(error.response.data);
                });
        },
        addUpload() {
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

            this.uploadFlag = false;

            // 发送 POST 请求
            axios.post(`${this.API_URL}/upload`, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
                onUploadProgress: progressEvent => {
                    // 计算上传进度
                    let percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
                    // 更新uploadProgress的数值
                    this.uploadProgress = percentCompleted;
                    console.log(this.uploadProgress);
                }
            })
                .then(() => {
                    this.showAddEditor = false;
                    this.uploadCoverUrl = null;
                    this.addForm = {
                        coverImage: null,
                        title: '',
                        anotherTitle: '',
                        japaneseTitle: '',
                        description: '',
                        type: '',
                        addFiles: [],
                    }
                    this.uploadProgress = 0;
                    this.uploadDialog = false;
                    this.loadAnimeTable();
                })
                .catch(error => {
                    console.error(error);
                });
        },
        editUpload() {
            const formData = new FormData();
            if (this.editForm.coverImage) formData.append('coverImage', new Blob(this.editForm.coverImage, { type: "image/jpeg" }), "Cover.jpg");
            formData.append('id', this.editForm.id);
            formData.append('title', this.editForm.title);
            formData.append('anotherTitle', this.editForm.anotherTitle);
            formData.append('japaneseTitle', this.editForm.japaneseTitle);
            formData.append('description', this.editForm.description);
            formData.append('type', this.editForm.type);

            for (let i = 0; i < this.editForm.editFiles.length; i++) {
                const file = this.editForm.editFiles[i];
                if (file && file !== undefined) {
                    const blob = new Blob([file[0]], { type: file[0].type });
                    const originalFileExtension = file[0].name.split('.').pop();
                    const fileName = i + '.' + originalFileExtension;
                    formData.append('editFiles', blob, fileName);
                    console.log('editFiles:', fileName);
                    formData.append('editEpisode', i)
                }
            }
            for (let i = 0; i < this.editForm.addFiles.length; i++) {
                const file = this.editForm.addFiles[i];
                const blob = new Blob([file], { type: file.type });
                const originalFileExtension = file.name.split('.').pop();
                const fileName = (this.editForm.episode + i + 1) + '.' + originalFileExtension;
                formData.append('addFiles', blob, fileName);
                console.log('addFiles:', fileName);
            }
            console.log('Printing formData entries:');
            for (let pair of formData.entries()) {
                console.log(pair[0] + ': ' + pair[1]);
            }
            this.uploadFlag = false;

            // 发送 POST 请求
            axios.post(`${this.API_URL}/update`, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
                onUploadProgress: progressEvent => {
                    // 计算上传进度
                    let percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
                    // 更新uploadProgress的数值
                    this.uploadProgress = percentCompleted;
                    console.log(this.uploadProgress);
                }
            })
                .then(() => {
                    this.showAddEditor = false;
                    this.uploadCoverUrl = null;
                    this.addForm = {
                        coverImage: null,
                        title: '',
                        anotherTitle: '',
                        japaneseTitle: '',
                        description: '',
                        type: '',
                        addFiles: [],
                    }
                    this.uploadProgress = 0;
                    this.uploadDialog = false;
                    this.loadAnimeTable();
                })
                .catch(error => {
                    console.error(error);
                });
        },
        loadAnimeTable() {
            axios.get(`${this.API_URL}/update`)
                .then(response => {
                    this.animeList = response.data;
                })
                .catch(error => {
                    console.error(error);
                });
        },
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

.edit-container {
    display: flex;
    flex-direction: column;
    width: 80vw;
    margin-inline: auto;
    margin-top: 20px;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f5f5f5;

    .edit-box {
        display: flex;
        justify-content: space-around;
        width: 100%;
        height: auto;
    }

    .edit-editor {
        display: flex;
        flex-direction: column;
        margin-top: 20px;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        background-color: #fff;

        .tableItem:hover {
            background-color: #ccc;
        }
    }
}
</style>