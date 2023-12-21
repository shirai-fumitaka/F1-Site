<template>
    <v-app id="inspire">
  
        <v-row>
            <h1>{{ message }}</h1>
          <!-- メインエリア -->
          <v-col>
            <v-main>
              <v-container class="py-8 px-6" fluid align-start style="margin-left: -100px; margin-top: -50px;">
                
                <!-- messagesをループして表示 -->
                <v-row v-for="item in driverData" :key="item.id" justify="center" app center>
                  <v-col>
                    <v-card>
                      <v-card-text>
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
          </v-col>
        </v-row>
    </v-app>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        message:'選手情報',
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
  
  