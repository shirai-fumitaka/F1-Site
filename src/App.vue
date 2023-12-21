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
      <router-view></router-view>
    
      <v-navigation-drawer v-model="drawer" class="mt-4" justify="start" app top>
            <v-sheet color="grey-lighten-4" class="pa-4">
              <v-avatar class="mb-4" color="grey-darken-1" size="64"> </v-avatar>
              <div style="margin-top: -100px;">F1サイトメニュー</div>
            </v-sheet>

            <v-divider></v-divider>

           
            <v-list-item v-for="[icon, text] in links" :key="icon" link style="margin-top: -2px;">
              <router-link :to="Link(text)" class="mb-4" color="grey-darken-1" size="64" >
               <v-list-item-icon>
                <v-icon>{{ icon }}</v-icon>
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
 setup(){
  const drawer = (null);

// ナビゲーションリンクのデータ
  const links = [
  ['mdi-home', 'ホーム'],
  ['mdi-trophy', '予選結果'],
  ['mdi-trophy-variant', '決勝結果'],
  ['mdi-crown', 'ポイントランキング'],
  ['mdi-account', '選手情報'],
 ];

  const Link=(text) => {
    
          if (text === 'ホーム') {
            return { path: '/', name:' FormulaOne' };
          } else if (text === '予選結果') {
            return { path:'/qualifying',name:'FormulaOne_Qualifying' };
          }
            else if (text === '決勝結果') {
            return { path:'/final',name:'FormulaOne_Final' };
          } 
            else if (text === 'ポイントランキング') {
            return { path:'/point',name:'FormulaOne_Point' };
          }
            else if (text === '選手情報') {
            return { path:'/driver',name:'FormulaOne_Driver' };
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
