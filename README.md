celestial-symphony-gatsby
=========================


# Overview

webサイト[Celestial Symphony](https://stfate.net)のGatsby+Netlifyによる実装．  
[こちらのテーマ](https://github.com/baobabKoodaa/blog)をベースにしている．


# Install log

## Prerequisites

- npm/node
- [gatsby-cli](https://www.gatsbyjs.com/docs/gatsby-cli/)


## Wordpressからの記事データ移行

[wordpress-article-extractor](https://github.com/stfate/wordpress-article-extractor)を用いる．  
抽出した記事データを`content/posts`に配置する．


## プロジェクト作成

```bash
gatsby new celestial-symphony-gatsby https://github.com/baobabKoodaa/blog
```


## カスタマイズ

- 事前にAlgoliaのアカウントを作成しておく ([ここ参照](https://dev.greglobinski.com/setup-algolia-account/))
- `.env`に以下の環境変数を設定
    - POSTS_FOLDER=posts
    - ALGOLIA_APP_ID={ALGOLIAのAPP_ID}
    - ALGOLIA_SEARCH_ONLY_API_KEY={ALGOLIAのSEARCH_ONLY_API_KEY}
    - ALGOLIA_ADMIN_API_KEY={ALGOLIAのADMIN_API_KEY}
    - ALGOLIA_INDEX_NAME=CONTENT
- `gatsby-config.js`にstyled-components&algoliaの設定を追加

```bash
{
  resolve: "gatsby-plugin-styled-components",
  options: {

  }
},
{
  resolve: `gatsby-plugin-algolia`,
  options: {
    appId: process.env.ALGOLIA_APP_ID ? process.env.ALGOLIA_APP_ID : "",
    apiKey: process.env.ALGOLIA_ADMIN_API_KEY ? process.env.ALGOLIA_ADMIN_API_KEY : "",
    indexName: process.env.ALGOLIA_INDEX_NAME ? process.env.ALGOLIA_INDEX_NAME : "",
    queries,
    chunkSize: 10000 // default: 1000
  }
},
```

- `content/meta/config.js`のauthor情報を編集
- `src/theme/theme.yaml`のcoloring設定を好みに応じて編集
- Headerのレイアウト変更する場合は`src/components/Header/Header.js`を編集
- `src/components/Menu/Menu.js`にてHeaderに表示するメニュー項目を編集

```javascript
this.items = [
  { to: "/", label: "Home", icon: FaHome },
  { to: "/tags/", label: "Tags", icon: FaTag },
  { to: "/search/", label: "Search", icon: FaSearch },
  // { to: "/follow/", label: "Follow", icon: FaRss },
  // { to: "/contact/", label: "Contact", icon: FaEnvelope },
  { to: "/about/", label: "About", icon: FaUser }
];
```

- 各メニューのフォントカラーなどを調整する場合は`src/components/Menu/Item.js`のCSSを編集する
- 各種画像差し替え
    - サイトアイコン：`src/images/app-icons/icon.png`
    - アバター(左上のサイト名横部に表示される画像): `src/images/jpg/avatar.jpg`
    - ヘッダー背景画像: `src/images/jpg/header.jpg`
- アイコン画像生成: `scripts/generate-app-icons.sh`


## ビルド

- develop: `gatsby develop`
- production: `gatsby build`


## サイトへのデプロイ

`git push`する．


# 記事投稿

`content/posts`に`yyyy-mm-dd--title`のディレクトリを追加し，その下に`index.md`を追加する．

- 記事カバー: `cover.png`で指定 (700x314)
- Twitter card用画像: `twitter_card.png`で指定 (600x314)
    - `cp_twitter_cards.py`で`static/twitter_cards`にコピー&`tyrfing.site`上にupload
    - Twitter card表示時は`tyrfing.site`上のファイルを参照する