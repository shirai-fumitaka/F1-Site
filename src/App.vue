<template>
  <v-app>
    <v-app-bar app color="grey" dark class="gradient-background">
      <div class="d-flex align-center" style="width: 100%; position: absolute; z-index: 2;">
        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          message="F1サイト"
          src="https://f1-gate.com/media/2017/20171216-logo_4.jpg"
          width="100"
        />
        <span class="ml-4 custom-text">F1サイト</span>
      </div>
    </v-app-bar>

    <v-main class="main-content">
      <router-view></router-view>

      <v-navigation-drawer :style="{ background: 'linear-gradient(to right, #209077 0%, #1ae28a 100%)', 'z-index': 1 }" v-model="drawer" class="mt-4" height: =20px; app top>
        <v-divider></v-divider>

        <v-list-item v-for="[icon, text] in links" :key="icon" link style="margin-top: -2px;">
          <router-link :to="Link(text)" class="d-flex align-center" style="text-decoration: none; font-weight: bold; color: white;">
            <v-list-item-icon>
              <v-icon class="white--text mdi">{{ icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{ text }}</v-list-item-title>
            </v-list-item-content>
          </router-link>
        </v-list-item>
      </v-navigation-drawer>
    </v-main>
  </v-app>
</template>

<script>
export default {
  setup() {
    const drawer = null;

    const links = [
      ['mdi-home', 'ホーム'],
      ['mdi-trophy', '予選結果'],
      ['mdi-trophy-variant', '決勝結果'],
      ['mdi-crown', 'ポイントランキング'],
      ['mdi-account', '選手情報'],
    ];

    const Link = (text) => {
      if (text === 'ホーム') {
        return { path: '/', name: 'FormulaOne' };
      } else if (text === '予選結果') {
        return { path: '/qualifying', name: 'FormulaOne_Qualifying' };
      } else if (text === '決勝結果') {
        return { path: '/final', name: 'FormulaOne_Final' };
      } else if (text === 'ポイントランキング') {
        return { path: '/point', name: 'FormulaOne_Point' };
      } else if (text === '選手情報') {
        return { path: '/driver', name: 'FormulaOne_Driver' };
      }
    };

    return {
      drawer,
      links,
      Link,
    };
  },
};
</script>

<style>
.custom-font {
  font-family: 'Your Custom Font', sans-serif;
  text-decoration: none; /* 下線をなくす */
} 

.d-flex {
  display: flex;
}

.align-center {
  align-items: center;
}

.custom-text {
  font-size: 20px; /* フォントサイズの指定 */
  font-weight: bold; /* フォントウェイトの指定 */
  color: white; /* テキストの色指定 */
}

.gradient-background {
  background: linear-gradient(to right, #e079fc 0%, #7c44ff 100%);
}

/* v-app-barのテーマスタイルを変更 */
.v-application .v-app-bar {
  width: 100%;
}
</style>
