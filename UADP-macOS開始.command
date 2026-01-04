#!/bin/bash

# UADP Framework - macOS/Linux 啟動腳本
# 設定 UTF-8 編碼
export LANG=zh_TW.UTF-8

echo "========================================"
echo "UADP Framework - macOS/Linux 啟動腳本"
echo "========================================"
echo ""

# 檢查 python3 是否可用
echo "[1/5] 檢查 Python 環境..."
if ! command -v python3 &> /dev/null; then
    echo "   Python3 未安裝"
    echo ""
    
    # 檢查是否為 macOS
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "   ⚠️  檢測到 macOS 系統"
        echo "   macOS 通常會自動彈出「開發者工具安裝」視窗"
        echo "   請點擊「安裝」按鈕，安裝完成後重新執行此腳本"
        echo ""
        echo "   或手動安裝："
        echo "   1. 開啟終端機"
        echo "   2. 執行: xcode-select --install"
        echo ""
    else
        echo "   ⚠️  請先安裝 Python 3.10 或更新版本"
        echo "   Ubuntu/Debian: sudo apt-get install python3 python3-pip"
        echo "   Fedora: sudo dnf install python3 python3-pip"
        echo "   Arch: sudo pacman -S python python-pip"
        echo ""
    fi
    
    read -p "按 Enter 鍵退出..."
    exit 1
fi

python3 --version
echo "   ✓ Python3 已安裝"

# 檢查 pip3 是否可用
echo ""
echo "[2/5] 檢查 pip..."
if ! command -v pip3 &> /dev/null; then
    echo "   ⚠️  pip3 不可用，嘗試使用 python3 -m pip..."
    PIP_CMD="python3 -m pip"
else
    PIP_CMD="pip3"
    echo "   ✓ pip3 可用"
fi

# 安裝 jsonschema（如果需要）
echo ""
echo "[3/5] 安裝依賴項（jsonschema）..."
$PIP_CMD install jsonschema --quiet --disable-pip-version-check 2>/dev/null
if [ $? -eq 0 ]; then
    echo "   ✓ jsonschema 已安裝"
else
    echo "   ⚠️  依賴項安裝失敗，但將繼續執行"
fi

# 檢查並下載 uadp-setup.py（如果需要）
echo ""
echo "[4/5] 檢查 UADP 初始化引擎..."
if [ -f "scripts/uadp-setup.py" ]; then
    echo "   ✓ 找到本地初始化引擎"
    SETUP_SCRIPT="scripts/uadp-setup.py"
elif [ -f "uadp-setup.py" ]; then
    echo "   ✓ 找到本地初始化引擎"
    SETUP_SCRIPT="uadp-setup.py"
else
    echo "   正在從 GitHub 獲取 UADP 初始化引擎..."
    echo "   這可能需要幾秒鐘，請稍候..."
    echo ""
    
    # 嘗試下載腳本
    if curl -L -o uadp-setup.py https://raw.githubusercontent.com/OG-Matcha/UADP/main/scripts/uadp-setup.py; then
        echo "   ✓ 初始化引擎下載完成"
        SETUP_SCRIPT="uadp-setup.py"
    else
        echo ""
        echo "   ❌ 下載失敗，請檢查網路連線"
        echo "   或手動下載: https://raw.githubusercontent.com/OG-Matcha/UADP/main/scripts/uadp-setup.py"
        echo ""
        read -p "按 Enter 鍵退出..."
        exit 1
    fi
fi

# 執行 UADP 初始化腳本
echo ""
echo "[5/5] 執行 UADP 初始化..."
echo ""
python3 "$SETUP_SCRIPT"

if [ $? -ne 0 ]; then
    echo ""
    echo "   ❌ 初始化失敗，請檢查錯誤訊息"
    echo ""
    read -p "按 Enter 鍵退出..."
    exit 1
fi

echo ""
echo "========================================"
echo "✅ 初始化完成！"
echo "========================================"
echo ""
echo "📋 下一步："
echo "   1. 關閉此視窗"
echo "   2. 在 Cursor IDE 中開啟此專案"
echo "   3. 告訴 AI: \"[MODE: ARCHITECT] 我想做一個 [你的專案想法]\""
echo ""
echo "💡 提示："
echo "   - 詳細文件請參考: https://github.com/OG-Matcha/UADP"
echo "   - 如有問題，請查看 README.md"
echo ""
read -p "按 Enter 鍵退出..."

