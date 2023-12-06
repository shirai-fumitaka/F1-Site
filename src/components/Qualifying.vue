<template>
  <div>
    <h1>{{ message }}</h1>
    <v-card>
      <v-card-text>
        <p>開催地：{{ qualifyingData.length > 0 ? qualifyingData[0].venue : 'No venue available' }}</p>
      </v-card-text>
    </v-card>
    <v-card v-for="item in qualifyingData" :key="item.id" v-if="item.id >= 1 && item.id <= 20">
        <v-card-text>
         <p> {{ item.rank }} {{ item.driver_name }}</p>
       </v-card-text>
    </v-card>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      message: '予選結果',
      qualifyingData: []
    };
  },
  mounted() {
    // Djangoのビューからデータを取得
    this.fetchData();
  },
  methods: {
    fetchData() {
      // Axiosを使用してDjangoのビューにリクエストを送信
      axios.get('http://127.0.0.1:8000/f1homepage/api/data/')
        .then(response => {
          // データをVue.jsのデータにセット
          this.qualifyingData = response.data.qualifying;
        })
        .catch(error => console.error('Error:', error));
    }
  }
};
</script>

<style scoped>
/* スタイルが必要な場合はここに記述 */
</style>
