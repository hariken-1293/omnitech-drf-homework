# ■ OmnitechDynamics Django/DRFチュートリアル後の演習課題

## ■ 概要

課題の通り，簡易TODOアプリ(API群のみ)を作成した．

## ■ 機能の達成状況

| 達成状況     | 内容         |
| :---:  | ------------ |
| ✅ | ログイン機能(ログインというよりはトークン発行機能(Bearerトークン認証あたりで良いかと思います)) |
| ✅ | TODO登録機能 |
| ✅ | TODO編集機能 |
| ✅ | TODO削除機能(実装しなくても可) |
| ✅ | TODO詳細取得機能(1件取得) |
| ✅ | TODO一覧取得機能(複数件取得) |
| ✅ | Swagger UIでAPIドキュメントを確認できること |

一部ユニットテストを試しに記述しました．(models.py)


## ■ 使用技術
- Docker
- Django(v4.0)
- DjangoRestFramework(v3.13)
- View(ClassBasedView(Routersは利用しない))

> [!WARNING]
> Django・DRF・drf-spectacularの互換性に注意すること．
> 
> [DjangoとDRFの互換性リスト](https://www.django-rest-framework.org/community/release-notes/#313x-series)

## ■ Gitについて
### ■ コミットメッセージの分類
大まかに以下のように分類しています．
- fix: 修正
- add: 機能の追加
- docs: READMEなどのドキュメントの編集

### ■ ブランチ
- main: 課題提出時のマージ先
- dev: 開発の中心となるブランチ
