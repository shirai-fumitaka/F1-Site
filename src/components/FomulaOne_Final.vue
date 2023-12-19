<template>
    <div>
      <h1>{{ message }}</h1>
      <div v-for="(qualifyingDataPage, pageIndex) in paginatedData" :key="pageIndex">
        <h3>{{ qualifyingDataPage[0].gp }}/</h3>
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
          <button v-on:click="prevPage" :disabled="currentPage === 1">前へ</button>
          <span> {{ qualifyingDataPage[0].gp }} </span>
          <button v-on:click="nextPage" :disabled="currentPage === pageCount">次へ</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        message: '決勝結果',
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
        }
      },
      nextPage() {
        if (this.currentPage < this.pageCount) {
          this.currentPage++;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .header-text {
    letter-spacing: 20px; 
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
    padding: 6px;
  }
  
  .title-text th {
    background-color: rgb(31, 102, 202);
  }
  
  .pagination {
    margin-top: 10px;
  }
  
  .pagination button {
    margin: 0 5px;
    cursor: pointer;
  }
  
  .pagination span {
    margin: 0 10px;
  }
  </style>
  