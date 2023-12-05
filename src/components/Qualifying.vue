<<template>
  <div>
    <p>{{ message }}</p>
    <ul>
      <li v-for="item in qualifyingData" :key="item.rank">
        {{ item.rank }} - {{ item.driver_name }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      message: 'Hello from Vue.js!',
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
