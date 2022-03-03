<template>
  <div class="comodities">
    <div class="box">
        <div class="comodities-icons">
            <div
                v-for="(comodity_icon, index) in comodity_icons"
                :key="index"
                class="comodity"
            >
                  <div class="comodity-img" >
                    <img
                      :src="require(`@/components/comodities/svgs/${comodity_icon.icon}.svg`)"
                  />
                  </div>
                <p class="comodity-text">{{ comodity_icon.title }}</p>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      comodity_icons: [
          { title: "Piscina", icon: "nadador" },
          { title: "Churrasqueira", icon: "churrasco" },
          { title: "Forno e fogão a lenha", icon: "forno" },
          { title: "Salão de festas", icon: "champanhe" },
          { title: "Salão de jogos", icon: "snooker" },
          {
              title: "Quadra poliesportiva coberta",
              icon: "bola_de_futebol",
          },
      ],
    }
  },
}
</script>

