<template>
  <v-app id="inspire">

      <v-row justify="end">
        <!-- メインエリア -->
        <v-col>
          <v-main>
            <v-container class="py-8 px-6" fluid align-start style="margin-left: -100px; margin-top: -50px;">
              <p class="text-left">お知らせ</p>
              
              <!-- messagesをループして表示 -->
              <v-row v-for="(item, index) in messages" :key="index" justify="center" app center>
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
  </v-app>
</template>

<script>
 export default{
 data(){
  return{
    messages :[
  { message: '2023/12/1予選情報を更新しました' },
  { message: '2023/12/15予選情報を更新しました' },
   ],
  };
 },
};
</script>
