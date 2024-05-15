#!/bin/bash

echo "Choose an option:"
echo "1) Client-Build"
echo "2) Management-Build"

# readコマンドを使ってユーザーの入力を取得
read -p "Enter the number of your choice: " choice

# ユーザーの選択に応じてアクションを実行
case $choice in
    1)
        echo "You chose Client-Build"
        python3 c-setup.py
        ;;
    2)
        echo "You chose Management-Build"
        python3 m-setup.py
        ;;
    *)
        echo "Invalid choice. Exiting."
        ;;
esac
