# f1

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

1,vueのインストール
###
```
npm install -g @vue/cli
```
この時vueのバージョンは揃える。
うまくいかない場合はsudoを使う。




djangoとvueの連携方法

1、まずはCORS（CORSは、バックエンド用）からのリクエストを許可する仕組み）をインストール
###
```
pip install django-cors-headers
```

2、setting.pyに以下の内容を追記する。
###
```
# myproject/settings.py
INSTALLED_APPS = [
    # ...
    'corsheaders',
]

MIDDLEWARE = [
    # ...
    'corsheaders.middleware.CorsMiddleware',
    # ...
]
# myproject/settings.py
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",  # Vue.jsの開発サーバーのアドレス
    # 他の許可するオリジンもここに追加
]

```

3、axios（フロントエンド用）をインストールする
###
```
npm install axios
```

4、axiosをコードに反映させる
###
```
// myproject/myapp/static/myapp/vue_app.js
import axios from 'axios';

new Vue({
    el: '#app',
    data: {
        items: [],
    },
    mounted() {
        this.fetchData();
    },
    methods: {
        fetchData() {
            // DjangoのAPIエンドポイントからデータを取得
            axios.get('http://localhost:8000/api/mymodel/')
                .then(response => {
                    this.items = response.data;
                })
                .catch(error => {
                    console.error('Error fetching data', error);
                });
        },
    },
});
```
1,Routerの使用
Routerを使用して複数のページをAPP.vueから表示することができるようになる。
###
```
npm install vue-router
```

1,srcディレクトリにrouterディレクトリを作成し、その中にindex.jsファイルを作成します。
2,main.jsでvue-routerをインポートし、Vueインスタンスに適用します。
3,App.vue内でrouter-viewを使用して現在のルートに対応するコンポーネントを表示します。

表の表現
<thead>はHTMLで使用される要素で、HTML表のヘッダーグループを定義します。HTMLの表は通常、ヘッダー行（<thead>）、ボディ行（<tbody>）、およびフッター行（<tfoot>）の3つの部分に分かれます。それぞれの部分は、<th>（表のヘッダーセル）、<td>（表のデータセル）要素で構成されます。

