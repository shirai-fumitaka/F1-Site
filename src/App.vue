<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          message="F1"
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://f1-gate.com/media/2017/20171216-logo_4.jpg"
          width="100"
        />
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <FormulaOne/>
      <Qualifying/>
    </v-main>
  </v-app>
</template>

<script>
import FormulaOne from './components/FormulaOne';
import Qualifying from './components/Qualifying'
export default {
  name: 'App',

  components: {
    FormulaOne,
    Qualifying
  },

  data: () => ({
    //
  }),
};
</script>
