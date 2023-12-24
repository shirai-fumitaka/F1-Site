<template>
    <div>
      <h1>{{ message }}</h1>
        <table class="title-text">
          <thead>
            <tr>
              <th class="header-text">順位</th>
              <th class="header-text">選手名</th>
              <th class="header-text">ポイント</th>

            </tr>
          </thead>
          <tbody>
            <tr v-for="item in pointDataPage" :key="item.id">
              <td>{{ item.rank }}</td>
              <td>{{ item.driver.name }}</td>
              <td>{{ item.point}}</td>
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
        message: 'ポイントランキング',
        pointData: [],
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
            this.pointData = response.data.point;
          })
          .catch(error => console.error('Error:', error));
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
  