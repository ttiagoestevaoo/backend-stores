<template>
    <div class="w-full mx-auto body">
        <title>Chácara Recanto dos Pássaros</title>
        <HomeComponent />

        <ComoditiesComponent />
        <AlbumComponent />
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
                                src="../assets/imgs/header/escada.jpg"
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

export default {
    components: {
        HomeComponent,
        FormComponent,
        FooterComponent,
        AlbumComponent,
        ComoditiesComponent,
    },
    data(){
        return {
            events: [
                { title: "Casamentos" },
                { title: "Festas" },
                { title: "Confraternizações" },
                { title: "Happy hour" },
            ],
            partners: [
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
            ],
        };
    },
}
</script>

<style lang="scss">
@import "./../assets/style/colors.scss";
@import url("https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100&display=swap");

.box-shadow {
    border-radius: 20px;
    box-shadow: 0px 10px 30px $ligthGray;
}

.body {
    font-family: "Roboto";
    color: $extraHighGreen;
    height: 100%;
}

.container {
    @apply w-full;
}

.box {
    position: relative;
    @apply w-4/5 mx-auto;

    &-screen {
        @extend .box;
        @apply h-screen;
    }
}

.header {
    background-color: $lightBrown;
    position: relative;
}

.content {
    top: 15%;
    left: 0;
    position: absolute;
    z-index: 0;
    @apply mt-20 w-full flex justify-between;
}

.content {
    .text,
    .galery {
        @apply w-1/2 mr-5 my-auto;
    }
}

.galery {
    position: relative;
    min-height: 500px;
    min-width: 700px;

    .img-content {
        @apply w-full;
        position: relative;
        padding-top: 30px;

        .img {
            border-radius: 50px 50px 0 50px;
            @apply object-cover;
            min-height: 500px;
            max-height: 500px;
            min-width: 700px;
            max-width: 700px;
        }

        .button-group {
            position: absolute;
            bottom: 0%;
            right: 0;
            margin-bottom: 0;

            @apply flex justify-start mr-3;

            .button {
                width: 12px;
                height: 12px;
                background-color: #fff;
                @apply box-shadow mr-4;

                &-selected {
                    background-color: $lightGreen;
                }
            }
        }
    }

    .img-content::after {
        content: "";
        width: 95%;
        height: 90%;
        top: 0;
        left: 5%;
        background-color: $lightGreen;
        position: absolute;
        opacity: 0.3;
        z-index: -1;
        border-radius: 50px 50px 0 50px;
    }
}

.content {
    * {
        @apply mb-5;
    }

    .title {
        color: $lightGreen;
        @apply text-lg font-bold;
        font-size: 70px;
        line-height: 90px;
    }

    .subtitle {
        color: $extraHighGreen;
    }
}

.btn {
    @apply py-2 px-6 mx-auto text-sm font-bold;
    font-size: 20px;
    border-radius: 20px;
}

.btn-green {
    @extend .btn;
    background-color: $lightGreen;
    color: #fff;
}

.navbar {
    @apply flex justify-between items-center;

    .navbar-social {
        @apply flex justify-between items-center ml-4;
    }
}

.navbar-item {
    @apply mr-4  font-medium;
}

.navbar-icon {
    border-radius: 100px;
    border: 1px solid $highGreen;
    height: 40px;
    width: 40px;
    text-align: center;
    padding: 8px;
}

.navbar-logo {
    height: 100%;
}
.navbar-logo-img {
    height: 80px;
}

.navbar-button {
    border-radius: 20px;
    border: 1px solid $highGreen;
    color: $highGreen;
    @apply px-3 py-2  mx-4  font-medium;
}

.comodities {
    position: relative;

    .comodities-icons {
        @apply flex justify-center w-full;
        position: absolute;
        top: -4em;

        .comodity {
            font-size: 14px;
            background-color: #fff;
            @apply mr-auto px-4 py-6 w-44 font-bold flex flex-col justify-center items-center box-shadow;
        }
    }
}

.comodity-img {
    @apply items-center text-center;
    max-height:60px;
    max-width: 60px;
}

.comodity-text{
    @apply mt-5 items-start text-center;
    height:40px;
    width: 140px;
}

.album {
    position: relative;
    height: auto;
    @apply flex justify-between mt-10;

    &-selector {
        @apply items-center text-center flex flex-col justify-between box-shadow;

        height: 100%;

        &-item {
            @apply py-2 my-5 px-20 w-full;

            &-selected {
                border-left: 2px solid $lightGreen;
                @apply font-bold;
                color: $lightGreen;
            }
        }
    }

    &-photos {
        position: relative;
        @apply p-10 items-center flex flex-col box-shadow;

        &-photo {
            img {
                border-radius: 20px;
                @apply object-cover;
                max-height: 400px;
                min-width: 800px;
            }
        }
    }

    &-text {
        color: $extraHighGreen;
        @apply flex flex-col mt-10;

        &-title {
            @apply font-bold text-lg mb-2;
        }
    }

    &-icons {
        position: absolute;
        bottom: -20px;

        @apply flex flex-row;

        &-icon {
            background-color: $lightGreen;
            border-radius: 50%;
            width: 20px;
            height: 20px;
            @apply p-5 flex items-center mx-2 justify-center;
        }
    }
}

.events {
    background-color: $extraLightGreen;
}

.events-galery-card {
    @apply p-10 w-1/4 mr-5 box-shadow;
    background-color: #fff;
    text-align: center;
}

.events-galery {
    @apply flex justify-around;
}

.events-galery-card-img {
    img {
        border-radius: 20px;
        @apply object-cover mx-auto;
    }
}

.box-title {
    color: $highGreen;
    font-size: 40px;
    @apply font-bold w-full text-center;

    p {
        padding-top: 2em;
        padding-bottom: 1em;
    }
}

.events-galery-card-title {
    color: $highGreen;
    font-size: 20px;
    @apply font-bold my-5;
}

.events-galery-card-text {
    @apply my-5;
}

.events-galery-card-btn {
    border-radius: 34px;
    background-color: $ligthGray;
    color: $hightGray;
    @apply my-5 py-4 px-10;
}

.partners {
    @apply flex;
}

.partners-card {
    @apply box-shadow flex w-3/4 my-6 p-10 items-center;
}

.partners-card:nth-child(odd) {
    @apply mr-auto;
}
.partners-card:nth-child(even) {
    @apply ml-auto;
}

.partners-title {
    @apply font-bold;
    color: $lightGreen;
    font-size: 70px;
    line-height: 80px;
}

.partners-card-title {
    @apply font-bold mb-2;
    color: $hightOrange;
    font-size: 20px;
}


</style>


