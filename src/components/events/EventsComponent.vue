<template>
  <div class="w-full h-screen events">
    <div class="box-screen">
        <div class="box-title">
            <p>Espaço para eventos</p>
        </div>
        <div class="events-galery">
            <div
                v-for="(event, index) in events"
                :key="index"
                class="events-galery-card"
            >
                <div class="events-galery-card-img">
                    <img
                        src="@/assets/imgs/header/escada.jpg"
                        class="img"
                    />
                </div>
                <p class="events-galery-card-title">
                    {{ event.title }}
                </p>
                <p class="events-galery-card-text">
                    Lorem ipsum dolor sit amet, consectetur adipiscing
                    elit. In aliquam libero sit amet finibus
                    scelerisque.
                </p>
                <button
                    class="focus:outline-none events-galery-card-btn"
                >
                    Mais fotos
                </button>
            </div>
        </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue } from "vue-class-component";

export default class EventsComponent extends Vue {
  events = [
      { title: "Casamentos" },
      { title: "Festas" },
      { title: "Confraternizações" },
      { title: "Happy hour" },
  ]
}
</script>

<style lang="scss">
@import "style.scss";
</style>
