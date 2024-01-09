<template>
  <v-app id="inspire">
    <v-main>
      <v-container class="py-8 px-6 text-left" fluid>
        
        <h1 class="my-message">{{ message }}</h1> <!-- 新しいクラス my-message を追加 -->
        <!-- messagesをループして表示 -->
        <v-row v-for="item in driverData" :key="item.id" justify="center" app>
          <v-col>
            <v-card class="my-card">
              <v-card-text class="my-card-text">
                <p>選手名：{{ item.driver_name }}</p>
                <p>年齢：{{ item.age }}</p>
                <p>誕生日：{{ item.birthplace }}</p>
                <p>チーム：{{ item.team }}</p>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
        
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      message: '選手情報',
      driverData: [],
    };
  },

  mounted() {
    // Djangoのビューからデータを取得
    this.fetchData();
  },
  methods: {
    fetchData() {
      axios.get('http://127.0.0.1:8000/f1homepage/api/data/')
        .then(response => {
          this.driverData = response.data.drivers;
        })
        .catch(error => console.error('Error:', error));
    },
  },
};
</script>

<style scoped>
.my-card {
  margin-left: -260px;
  margin-top: -200px; /* カードを左上にずらすマージン */
}

.my-card-text {
  margin-top:   200px;
  padding-left: 60px; /* カード内のテキストを左にずらすパディング */
}

.my-message {
  margin-left: -260px;
  margin-top: -90px; /* メッセージを左にずらすマージン */
}
</style>
