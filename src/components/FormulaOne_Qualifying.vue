<template>
  <div>
    <h1>{{ message }}</h1>
    <h3>{{ "バーレーンGP" }}</h3>
    <table class="title-text">
      <thead>
        <tr>
          <th class="header-text">順位</th>
          <th class="header-text">選手名</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in qualifyingData" :key="item.id">
          <td>{{ item.rank }}</td>
          <td>{{ item.driver.name }}</td>
        </tr>
      </tbody>
    </table>
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
.header-text {
  letter-spacing: 20px; /* 表題の文字と文字の間隔を広げる */
}

/* 以下のスタイルはVuetifyのデフォルトのテーブルスタイルを上書きする例です。 */
.title-text {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.title-text th, .title-text td {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 6px;
}

.title-text th {
  background-color: rgb(31, 102, 202);
}
</style>
