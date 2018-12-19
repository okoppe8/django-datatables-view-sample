-- heroku-postgresの場合、デフォルトでは正しく日本語のソートができない。
-- カラムごとにソート順の設定を変更する必要がある。
ALTER TABLE sample_item ALTER COLUMN name TYPE VARCHAR COLLATE "ja_JP.utf8";
ALTER TABLE sample_item ALTER COLUMN address TYPE VARCHAR COLLATE "ja_JP.utf8";
ALTER TABLE sample_item ALTER COLUMN furigana TYPE VARCHAR COLLATE "ja_JP.utf8";

