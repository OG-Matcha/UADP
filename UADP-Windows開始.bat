@echo off
chcp 65001 >nul
echo ========================================
echo UADP Framework - Windows 啟動腳本
echo ========================================
echo.

REM 檢查 Python 是否安裝
echo [1/5] 檢查 Python 環境...
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
echo [2/5] 檢查 pip...
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo    ⚠️  pip 不可用，請檢查 Python 安裝
    pause
    exit /b 1
)
echo    ✓ pip 可用

REM 安裝 jsonschema（如果需要）
echo.
echo [3/5] 安裝依賴項（jsonschema）...
python -m pip install jsonschema --quiet --disable-pip-version-check
if %errorlevel% neq 0 (
    echo    ⚠️  依賴項安裝失敗，但將繼續執行
) else (
    echo    ✓ jsonschema 已安裝
)

REM 檢查並下載 uadp-setup.py（如果需要）
echo.
echo [4/5] 檢查 UADP 初始化引擎...
if exist "scripts\uadp-setup.py" (
    echo    ✓ 找到本地初始化引擎
    set SETUP_SCRIPT=scripts\uadp-setup.py
) else if exist "uadp-setup.py" (
    echo    ✓ 找到本地初始化引擎
    set SETUP_SCRIPT=uadp-setup.py
) else (
    echo    正在從 GitHub 獲取 UADP 初始化引擎...
    echo    這可能需要幾秒鐘，請稍候...
    echo.
    
    REM 嘗試下載腳本
    curl -L -o uadp-setup.py https://raw.githubusercontent.com/OG-Matcha/UADP/main/scripts/uadp-setup.py
    
    if %errorlevel% neq 0 (
        echo.
        echo    ❌ 下載失敗，請檢查網路連線
        echo    或手動下載: https://raw.githubusercontent.com/OG-Matcha/UADP/main/scripts/uadp-setup.py
        echo.
        pause
        exit /b 1
    )
    
    echo    ✓ 初始化引擎下載完成
    set SETUP_SCRIPT=uadp-setup.py
)

REM 執行 UADP 初始化腳本
echo.
echo [5/5] 執行 UADP 初始化...
echo.
python %SETUP_SCRIPT%

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
echo    3. 強烈建議：上傳 .uadp/UADP_EXTERNAL_PILOT.md 給外部 AI（如 Gemini）作為溝通橋樑。
echo    4. 告訴 AI: "[MODE: ARCHITECT] 我想做一個 [你的專案想法]"
echo.
echo 💡 提示：
echo    - 詳細文件請參考: https://github.com/OG-Matcha/UADP
echo    - 如有問題，請查看 README.md
echo.
pause

