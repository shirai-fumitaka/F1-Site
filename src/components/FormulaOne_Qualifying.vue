<template>
  <div>
    <h1>{{ message }}</h1>
    <div v-for="(qualifyingDataPage, pageIndex) in paginatedData" :key="pageIndex">
      <h2>{{ qualifyingDataPage[0].gp }}</h2>
      <table class="title-text">
        <thead>
          <tr>
            <th class="header-text">順位</th>
            <th class="header-text">選手名</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in qualifyingDataPage" :key="item.id">
            <td>{{ item.rank }}</td>
            <td>{{ item.driver.name }}</td>
          </tr>
        </tbody>
      </table>
      <div class="pagination">
      {{ qualifyingDataPage[0].gp }}
        <ul class="page-numbers">
          <li v-for="pageNumber in pageCount" :key="pageNumber">
            <button @click="goToPage(pageNumber)" :class="{ 'active': pageNumber === currentPage }">
              {{ pageNumber }}
            </button>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      message: '予選結果',
      qualifyingData: [],
      currentPage: 1,
      itemsPerPage: 20,
    };
  },
  
  computed: {
    paginatedData() {
      const startIndex = (this.currentPage - 1) * this.itemsPerPage;
      const endIndex = startIndex + this.itemsPerPage;
      const slicedData = this.qualifyingData.slice(startIndex, endIndex);
      return this.groupDataByGP(slicedData);
    },
    pageCount() {
      return Math.ceil(this.qualifyingData.length / this.itemsPerPage);
    },
  },
  mounted() {
    // Djangoのビューからデータを取得
    this.fetchData();
  },
  methods: {
    fetchData() {
      axios.get('http://127.0.0.1:8000/f1homepage/api/data/')
        .then(response => {
          this.qualifyingData = response.data.qualifying;
        })
        .catch(error => console.error('Error:', error));
    },
    groupDataByGP(data) {
      // GPごとにデータをグループ化する
      const groupedData = {};
      data.forEach(item => {
        const gpName = item.gp;
        if (!groupedData[gpName]) {
          groupedData[gpName] = [];
        }
        groupedData[gpName].push(item);
      });
      return groupedData;
    },
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
        this.scrollToTop();
      }
    },
    nextPage() {
      if (this.currentPage < this.pageCount) {
        this.currentPage++;
        this.scrollToTop();
      }
    },
    goToPage(pageNumber) {
      if (pageNumber >= 1 && pageNumber <= this.pageCount) {
        this.currentPage = pageNumber;
        this.scrollToTop();
      }
    },
    scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    },
  },
};
</script>

<style scoped>
/* 他のスタイルは省略 */

.pagination {
  margin-top: 10px;
}

.pagination button {
  margin: 0 5px;
  cursor: pointer;
}

.pagination span {
  margin: 0 5px;
}

.page-numbers {
  list-style: none;
  display: flex;
  margin: 0;
  padding: 0;
}

.page-numbers li {
  margin-right: 5px;
}

.page-numbers button {
  cursor: pointer;
  padding: 5px 10px;
  border: 1px solid #ddd;
  border-radius: 3px;
}

.page-numbers button.active {
  background: linear-gradient(to right, #e079fc 0%, #7c44ff 100%);
  color: white;
}


.title-text {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.title-text th,
.title-text td {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
  background-color:#c01ee0, #4F9DFF;
}

.title-text th {
  background: linear-gradient(to right, #e079fc 0%, #7c44ff 100%);
  color: white;
}
</style>
