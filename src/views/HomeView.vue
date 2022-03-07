<template>
    <div class="w-full mx-auto body">
        <title>Chácara Recanto dos Pássaros</title>
        <HomeComponent />
        <ComoditiesComponent />
        <AlbumComponent />
        <EventsComponent />
        <PartnersComponent />
        <FormComponent></FormComponent>
        <FooterComponent></FooterComponent>

    </div>
</template>

<script>
import HomeComponent from "./../components/home/HomeComponent.vue"
import FormComponent from "./../components/form/FormComponent.vue"
import FooterComponent from "./../components/footer/FooterComponent.vue"
import AlbumComponent from "./../components/album/AlbumComponent.vue"
import ComoditiesComponent from "./../components/comodities/ComoditiesComponent.vue"
import EventsComponent from "./../components/events/EventsComponent.vue"
import PartnersComponent from "./../components/partners/PartnersComponent.vue"

export default {
    components: {
        HomeComponent,
        FormComponent,
        FooterComponent,
        AlbumComponent,
        ComoditiesComponent,
        EventsComponent,
        PartnersComponent,
    },
}
</script>

<style lang="scss">
@import "@/assets/style/style.scss";
@import url("https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100&display=swap");
</style>


