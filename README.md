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