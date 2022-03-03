<template>
    <div class="group-social">
        <li class="group-social-item group-social-icon">
            <a href="https://pt-br.facebook.com/chacaraRecantodosPassaro/">
                <font-awesome-icon :icon="['fab', 'facebook-f']" />
            </a>
        </li>
        <li class="group-social-item group-social-icon">
            <a href="https://www.instagram.com/chacara_recantodospassaros/">
                <font-awesome-icon :icon="['fab', 'instagram']" />
            </a>
        </li>
        <li class="group-social-item group-social-icon">
            <a href="https://api.whatsapp.com/send?phone=5511998961438">
                <font-awesome-icon :icon="['fab', 'whatsapp']" />
            </a>

        </li>
    </div>
</template>

<style lang="scss">
    @import "./../../assets/style/colors.scss";

    .group-social {
        @apply flex items-center ml-4;
    }

    .group-social-item {
        @apply mr-4  font-medium;
        list-style-type: none;
    }

    .group-social-icon {
        border-radius: 100px;
        border: 1px solid $highGreen;
        height: 40px;
        width: 40px;
        text-align: center;
        padding: 8px;
    }

</style>