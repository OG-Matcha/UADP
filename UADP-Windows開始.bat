@echo off
chcp 65001 >nul
echo ========================================
echo UADP Framework - Windows 啟動腳本
echo ========================================
echo.

REM 檢查 Python 是否安裝
echo [1/4] 檢查 Python 環境...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo    Python 未安裝，正在嘗試自動安裝...
    echo    這可能需要幾分鐘，請稍候...
    echo.
    
    REM 嘗試使用 winget 安裝 Python
    winget install -e --id Python.Python.3.10 --silent --accept-package-agreements --accept-source-agreements
    
    if %errorlevel% neq 0 (
        echo.
        echo    ⚠️  自動安裝失敗，請手動安裝 Python 3.10 或更新版本
        echo    下載連結: https://www.python.org/downloads/
        echo.
        pause
        exit /b 1
    )
    
    echo.
    echo    ✓ Python 安裝完成，請重新啟動此腳本
    echo    或手動將 Python 加入 PATH 環境變數
    echo.
    pause
    exit /b 0
)

python --version
echo    ✓ Python 已安裝

REM 檢查 pip 是否可用
echo.
echo [2/4] 檢查 pip...
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo    ⚠️  pip 不可用，請檢查 Python 安裝
    pause
    exit /b 1
)
echo    ✓ pip 可用

REM 安裝 jsonschema（如果需要）
echo.
echo [3/4] 安裝依賴項（jsonschema）...
python -m pip install jsonschema --quiet --disable-pip-version-check
if %errorlevel% neq 0 (
    echo    ⚠️  依賴項安裝失敗，但將繼續執行
) else (
    echo    ✓ jsonschema 已安裝
)

REM 執行 UADP 初始化腳本
echo.
echo [4/4] 執行 UADP 初始化...
echo.
python scripts/uadp-setup.py

if %errorlevel% neq 0 (
    echo.
    echo    ❌ 初始化失敗，請檢查錯誤訊息
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo ✅ 初始化完成！
echo ========================================
echo.
echo 📋 下一步：
echo    1. 關閉此視窗
echo    2. 在 Cursor IDE 中開啟此專案
echo    3. 告訴 AI: "[MODE: ARCHITECT] 我想做一個 [你的專案想法]"
echo.
echo 💡 提示：
echo    - 詳細文件請參考: https://github.com/OG-Matcha/UADP
echo    - 如有問題，請查看 README.md
echo.
pause

