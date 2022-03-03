<template>
    <div class="galery">
        <div class="img-content">
            <img :src="selectedPhoto" class="img" />
            <div class="button-group">
                <button 
                    v-for="(src, index) in getPhotosUrl" 
                    :key="index" 
                    class="button"
                    :class="index == selectedPhotoIndex  ? 'button-selected' : ''"
                    @click="changePhoto(index)"
                />
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import GoogleApiService from '@/store/services/googleApi/googleApiService'
import GoogleDriveItem from '@/store/services/googleApi/models/googleDriveItem'
const secondsToWaitToChangePhoto = 5000

let timer = 0

import { Vue } from "vue-class-component";


export default class GaleryComponent extends Vue {
    selectedPhotoIndex = 0;
    photos: GoogleDriveItem[] = []

    created(): void{
        timer = setInterval(() => this.getNextImage(), secondsToWaitToChangePhoto)
    }

    mounted(): void{
        const albumGaleryId = "17GtfhCifpBSSyEZjFBILnn9_FLsN0-Pr"
        const googleService = new GoogleApiService()
        googleService.getAlbumFiles(albumGaleryId)
            .then((result) => {
                this.photos = result.files
            })
    }

    changePhoto(index: number): void {
        this.selectedPhotoIndex = index
        clearInterval(timer)
        timer = setInterval(() => this.getNextImage(), secondsToWaitToChangePhoto)
    }
    
    getNextImage():void {
        if(this.selectedPhotoIndex+2 > this.getPhotosUrl.length){
            this.selectedPhotoIndex = 0
        } else {
            this.selectedPhotoIndex+=1
        }
    }

    get selectedPhoto() : string {
        return this.getPhotosUrl ? this.getPhotosUrl[this.selectedPhotoIndex] : ''
    }

    get getPhotosUrl() : string[] {
        return this.photos.map(photo => (
            `https://drive.google.com/uc?export=view&id=${photo.id}`
        )).sort(() => Math.random() > Math.random() ? 1 : -1)
    }
}
</script>