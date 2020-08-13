---
title: "WordpressからGatsby+Netlifyに転生した話"
path: "/posts/2020-08-13--wordpress-to-gatsby"
date: "2020-08-13"
cover: "Gatsby_Logo.png"
author: "stfate"
tags: ["tech", "web技術", "gatsby"]
---

<style type="text/css">
<!--
p {white-space: pre-wrap};
-->
</style>

<re-img
    src="Gatsby_Logo.png"
    title="Gatsby.js"
    href="https://www.gatsbyjs.com"
    >
</re-img>


当ブログは長らくWordpressで構築してきましたが，時代も令和になりWeb周りの情勢も大きく変わった中で不満点もいろいろ出てきていました．
具体的には，

- (ページ遷移が)重い
- HTTPS対応していない (これはWordpressがダメなんじゃなくてサーバ側の問題)
- (管理画面が)重い
- 管理画面で記事編集するのめんどくさい．できればテキストエディタでやりたい
- (検索が)重い
- 令和らしく記事もgitでバージョン管理したい

上記を改善できるサイト構築フレームワークとして[Gatsby.js](https://www.gatsbyjs.com/)があることに気づき，
[Netlify](https://www.netlify.com/)と併用すればGithubベースの管理ができて，かつドメインやDNS管理も非常に簡単になり，
さらにHTTPS対応も簡単にできるのでとてもちょうど良い！ということで移行することにしました．
参考にしたのはこのあたりの情報源．

- [ブログをWordpressからGatsbyに移行したので、その手順とハマったポイントを解説する](https://qiita.com/akashixi/items/9653d0a6522117618e0f)
- [GatsbyとNetlifyで簡単にブログを作成](https://qiita.com/k-penguin-sato/items/7554e5e7e90aa10ae225)
- [WordPressやめます Gatsbyに移行しました](https://tech-blog.s-yoshiki.com/entry/192)

過去の記事はCD感想&ライヴ感想は全て移行済みです．
(かつてニュースサイトだった時代の)古のニュース記事はタグの関係でimportに失敗して対応がめんどくさそうだったので
テキストでバックアップ取った上でこのブログにはimportしないことにしました．

Wordpress時代と比べて，ロード時間は圧倒的に減ったと思います．さすが静的生成．
Algoliaによる検索も高速なので，検索も効率よくできるようになったんじゃないかと．
何より記事執筆->投稿までテキストエディタ上で完結できる(記事をpullした時点でサイトにデプロイされる)のが非常に楽．
令和らしいサイトになったのではないかと思います(？)

ブログ書くモチベをツール変更により上げたところで，音源感想など再び精力的に上げていきたいと思います．
よろしくお願いします．
