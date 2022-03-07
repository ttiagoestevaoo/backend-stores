<template>
  <div class="w-full h-screen partners">
    <div class="box-screen flex items-center">
        <div class="flex-1">
            <p class="partners-title mb-10">
                Conheça os nossos parceiros
            </p>
            <p class="partners mb-10">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                In aliquam libero sit amet finibus scelerisque.
                Vestibulum et massa aliquam, mollis ligula auctor,
                fringilla nisl. Nam id iaculis lectus.
            </p>
            <button class="btn-green">Solicite um orçamento</button>
        </div>
        <div class="flex-1 flex flex-col">
            <div
                v-for="(partner, index) in partners"
                :key="index"
                class="partners-card"
            >
                <div class="mr-5">
                    <img :src="require(`@/assets/imgs/partners/${partner.img}.svg`)" class="img" />
                </div>
                <div class="">
                    <p class="partners-card-title">
                        {{ partner.title }}
                    </p>
                    <p class="">{{ partner.text }}</p>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue } from "vue-class-component";

export default class PartnersComponent extends Vue {
   partners = [
    {
        title: "Fotógrafo",
        img: "buffet",
        text: "Parceria com fotógrafo para registrar todos os momentos do seu evento.",
    },
    {
        title: "Buffet",
        img: "photographer",
        text: "Parceria com empresas de buffet para servir as melhores refeições para os seus convidados.",
    },
    {
        title: "Locação de utensílios",
        img: "chair",
        text: "Mesas, cadeiras, pratos, copos, talheres.",
    },
  ]
}
</script>

<style lang="scss">
@import "style.scss";
</style>
