<template>
    <div class="w-full h-screen header">
        <div class="box-screen header pt-10">
            <div class="navbar">
               
                <LogoComponent/>
                <ul class="flex items-center">
                    <li class="navbar-item">Sobre a chácara</li>
                    <li class="navbar-item">Galeria</li>
                    <li class="navbar-item">Parceiros</li>
                    <li class="navbar-item">Eventos</li>
                    <li class="navbar-item">Contato</li>
                    <a href="#" class="navbar-button">Ver disponibilidade</a>

                    <SocialIconsComponent> </SocialIconsComponent>
                </ul>
            </div>

            <div class="content">
                <div class="text">
                    <p class="title">Chácara recanto dos pássaros</p>
                    <p class="subtitle">
                        O local ideal para você festejar
                    </p>
                    <button class="btn-green">Conheça a chácara</button>
                </div>
                
                <galery-component />
            </div>
        </div>
    </div>
</template>

<script>
import SocialIconsComponent from './SocialIconsComponent.vue'
import LogoComponent from './LogoComponent.vue'
import GaleryComponent from './GaleryComponent.vue'
export default {
    components: {
        SocialIconsComponent,
        LogoComponent,
        GaleryComponent,
    }
}
</script>

<style lang="scss">
@import "./style.scss";
</style>
