# FastAPI テンプレート ドキュメント

このディレクトリには、FastAPIプロジェクトの理解に必要なすべてのドキュメントが含まれています。

## ドキュメント一覧

### 🏗️ アーキテクチャ設計
- **[directory-structure.md](./directory-structure.md)** - 詳細なディレクトリ構造と各層の責任
- **[architecture-diagram.md](./architecture-diagram.md)** - 視覚的なアーキテクチャ図とフロー

### 📋 開発ガイド
- **[development-guide.md](./development-guide.md)** - 開発環境のセットアップと運用方法
- **[api-guidelines.md](./api-guidelines.md)** - API設計のガイドライン
- **[testing-guide.md](./testing-guide.md)** - テスト戦略と実装方法

### 🔧 技術仕様
- **[database-design.md](./database-design.md)** - データベース設計とマイグレーション
- **[external-integrations.md](./external-integrations.md)** - 外部サービス統合の仕様

## 📖 読み始める順番

1. **新規参加者**: `directory-structure.md` → `architecture-diagram.md`
2. **開発環境構築**: `development-guide.md`
3. **API開発**: `api-guidelines.md` → `testing-guide.md`
4. **データベース作業**: `database-design.md`
5. **外部連携**: `external-integrations.md`

## 🚀 クイックスタート

```bash
# 開発環境の起動
docker-compose up -d

# データベースマイグレーション
docker-compose exec api alembic upgrade head

# テスト実行
docker-compose exec api pytest
```

## 💡 ヒント

- 実装に迷った時は `directory-structure.md` の各層の責任を確認
- 新機能追加時は `architecture-diagram.md` の依存関係を参考に
- 外部API統合時は `external-integrations.md` のアダプターパターンを活用

## 📝 ドキュメント更新

新機能を追加した際は、関連するドキュメントの更新も忘れずに行ってください。特に：
- 新しいエンドポイント: `api-guidelines.md` 
- 新しいサービス層: `directory-structure.md`
- 新しい外部連携: `external-integrations.md` 