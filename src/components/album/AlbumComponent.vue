<template>
    <div class="w-full h-screen">
        <div class="box-screen">
            <div class="box-title">
                <p class="mt-10">
                    Conheça mais sobre as nossas comodidades
                </p>
            </div>
            <div class="album">
                <div class="col-3 mr-5">
                    <ul class="album-selector">
                        <button
                            v-for="(album, index) in albuns"
                            :key="index"
                            class="album-selector-item"
                            :class="index === albumSelectedIndex ? 'album-selector-item-selected' : '' "
                            @click="getNextAlbum(index)"
                        >
                            {{ album.name }}
                        </button>
                    </ul>
                </div>
                <div class="col-8">
                    <div class="album-photos">
                        <div
                            class="flex flex-col items-center"
                            style="position: relative"
                        >
                            <div class="album-photos-photo">
                                <img :src="selectedPhoto" class="img" />
                            </div>
                            <div class="album-icons">
                                <div class="album-icons-icon">
                                    <button class="focus:outline-none">
                                        <font-awesome-icon
                                            icon="arrow-left"
                                            color="white"
                                            @click="previousPhoto"
                                        />
                                    </button>
                                </div>
                                <div class="album-icons-icon">
                                    <button class="focus:outline-none">
                                        <font-awesome-icon
                                            icon="arrow-right"
                                            color="white"
                                            @click="nextPhoto"
                                        />
                                    </button>
                                </div>
                            </div>
                        </div>
                        <div class="album-text">
                            <p class="album-text-title">{{ getAlbumName }}</p>
                            <p>{{ getAlbumDescription }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { Vue } from "vue-class-component";
import { Watch } from 'vue-property-decorator'

import GoogleApiService from '@/store/services/googleApi/googleApiService'
import GoogleDriveItem from '@/store/services/googleApi/models/googleDriveItem'

export default class AlbumComponent extends Vue {

  albumSelectedIndex = 0
  albumSelectedPhoto = 0
  albumPhotos: GoogleDriveItem[] = []
  albuns = [
    {
      name: 'A chácara',
      description: ' Todos os serviços que você precisa para uma ótima estadia ou para o evento que deseja. Veja as fotos dos nossos espaços e verifique a disponibilidade! ',
      googleDriveId: '1x_ndE4vQfnNkS--RCrKfiU7H7lFbrkLF',
    },
    {
      name: 'Piscina',
      description: ' Todos os serviços que você precisa para uma ótima estadia ou para o evento que deseja. Veja as fotos dos nossos espaços e verifique a disponibilidade! ',
      googleDriveId: '1yG1uUy-mCZZB9yby0_UINgk2Ngq3FuMw',
    },
    {
      name: 'Churrasqueira e fornos',
      description: ' Todos os serviços que você precisa para uma ótima estadia ou para o evento que deseja. Veja as fotos dos nossos espaços e verifique a disponibilidade! ',
      googleDriveId: '15e94TJUNZazPrF7C1fWkM_SL3CqYzc_Q',

    },
    {
      name: 'Salão de festas',
      description: ' Todos os serviços que você precisa para uma ótima estadia ou para o evento que deseja. Veja as fotos dos nossos espaços e verifique a disponibilidade! ',
      googleDriveId: '1IGmcxzqulX8RFOOrfTP471ikqSGeTG3e',
    },
    {
      name: 'Salão de jogos',
      description: ' Todos os serviços que você precisa para uma ótima estadia ou para o evento que deseja. Veja as fotos dos nossos espaços e verifique a disponibilidade! ',
      googleDriveId: '1UxdQI2CabOtw26nzqwPJdh5U-hgK-tWq',
    },
    {
      name: 'Quadra coberta',
      description: ' Todos os serviços que você precisa para uma ótima estadia ou para o evento que deseja. Veja as fotos dos nossos espaços e verifique a disponibilidade! ',
      googleDriveId: '1Mqp5XDQdxGOJvetzNHLgO1da7KhAonXk',
    }
  ]

  get getAlbumName(): string {
    return this.albuns[this.albumSelectedIndex].name
  }

  get getPhoto(): string {
    return this.albuns[this.albumSelectedIndex].name
  }

  get getAlbumDescription(): string {
    return this.albuns[this.albumSelectedIndex].description
  }
  
  getNextAlbum(index: number): void {
    this.albumSelectedIndex = index
  }

  previousPhoto(): void{
    this.updateAlbumSelectedPhoto(-1)
  }

  nextPhoto(): void {
    this.updateAlbumSelectedPhoto(+1)
  }

  updateAlbumSelectedPhoto(selectedIndex: number): void {
    const albumPhotosLength = this.albumPhotos.length
    let indexToGo = this.albumSelectedPhoto + selectedIndex
  
    if (indexToGo < 0) {
      this.albumSelectedPhoto = albumPhotosLength - 1
    } else if (indexToGo > albumPhotosLength - 1) {
      this.albumSelectedPhoto = 0
    } else {
      this.albumSelectedPhoto = indexToGo
    }

  }

  @Watch('albumSelectedIndex',{ immediate: true })
  getAlbumPhotos(albumSelectedIndex: number): void {
    const googleService = new GoogleApiService()
    const albumGoogleDriveId = this.albuns[albumSelectedIndex].googleDriveId
    googleService.getAlbumFiles(albumGoogleDriveId)
    .then((result) => {
      this.albumPhotos = result.files
    })
    .catch(() => 
      this.albumPhotos = []
    )
  }

  get selectedPhoto() : string {
      return this.getPhotosUrl ? this.getPhotosUrl[this.albumSelectedPhoto] : ''
  }

  get getPhotosUrl() : string[] {
      return this.albumPhotos.map(photo => (
          `https://drive.google.com/uc?export=view&id=${photo.id}`
      )).sort(() => Math.random() > Math.random() ? 1 : -1)
  }
}
</script>

<style lang="scss">
@import "style.scss";
</style>