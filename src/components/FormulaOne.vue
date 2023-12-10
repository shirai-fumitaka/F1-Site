<template>
  <v-app id="inspire">
    <v-system-bar>
      <v-spacer></v-spacer>
      <v-icon>mdi-square</v-icon>
      <v-icon>mdi-circle</v-icon>
      <v-icon>mdi-triangle</v-icon>
    </v-system-bar>

    <v-container fluid>
      <v-row>
        <!-- サイドバー -->
        <v-col>
          <v-navigation-drawer v-model="drawer" class="mt-4">
            <v-sheet color="grey-lighten-4" class="pa-4">
              <v-avatar class="mb-4" color="grey-darken-1" size="64"></v-avatar>
              <div style="margin-top: -100px;">F1サイトメニュー</div>
            </v-sheet>

            <v-divider></v-divider>

            <v-list-item v-for="[icon, text] in links" :key="icon" link style="margin-top: -2px;">
              <router-link :to="{name: 'Qualifying'}"></router-link>
               <v-list-item-icon>
                <v-icon>{{ icon }}</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>{{ text }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-navigation-drawer>
        </v-col>

        <!-- メインエリア -->
        <v-col>
          <v-main>
            <v-container class="py-8 px-6" fluid align-start style="margin-left: -400px; margin-top: -50px;">
              <p>お知らせ</p>
              
              <!-- messagesをループして表示 -->
              <v-row v-for="(item, index) in messages" :key="index" justify="start">
                <v-col>
                  <v-card>
                    <v-card-text>
                      <p>{{ item.message }}</p>
                    </v-card-text>
                    
                  </v-card>
                </v-col>
              </v-row>
            </v-container>
          </v-main>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script setup>
import { ref } from 'vue';
// メッセージデータを保持するリファレンス
const messages = ref([
  { message: '2023/12/1予選情報を更新しました' },
]);

// サイドバーの状態を管理するリファレンス
const drawer = ref(null);

// ナビゲーションリンクのデータ
const links = [
  ['mdi-trophy', '予選結果'],
  ['mdi-trophy-variant', '決勝結果'],
  ['mdi-crown', 'ポイントランキング'],
  ['mdi-account', '選手情報'],
];

</script>
