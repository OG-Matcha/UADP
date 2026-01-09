#!/usr/bin/env python3
"""
UADP Framework Setup Script
動態流式安裝器 - 從 GitHub 獲取最新版本的核心資產

此腳本會自動從 GitHub 下載最新的 UADP 框架檔案，確保版本同步。

版本: 2.0 (動態流式安裝器)
最後更新: 2026-01-09
"""

import os
import json
import sys
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime

# 專案根目錄
PROJECT_ROOT = Path.cwd()
UADP_DIR = PROJECT_ROOT / ".uadp"
CURSOR_RULES_DIR = PROJECT_ROOT / ".cursor" / "rules"

# GitHub Raw URL
REPO_RAW_URL = "https://raw.githubusercontent.com/OG-Matcha/UADP/main/"

# 當前日期（ISO 8601 格式）
CURRENT_DATE = datetime.now().strftime("%Y-%m-%dT00:00:00Z")
CURRENT_DATE_SHORT = datetime.now().strftime("%Y-%m-%d")

# 需要從 GitHub 下載的檔案清單（MANIFEST）
MANIFEST = [
    # 核心規則檔案
    ".cursor/rules/uadp-core.mdc",
    ".cursor/rules/uadp-agent-roles.mdc",
    ".cursor/rules/uadp-qa-standard.mdc",
    ".cursor/rules/uadp-task-runner.mdc",
    # 適配器模板
    ".uadp/adapters/README.md",
    ".uadp/adapters/mobile-flutter.mdc",
    ".uadp/adapters/web-modern.mdc",
    ".uadp/adapters/backend-api.mdc",
    # JSON Schema
    ".uadp/schemas/state.schema.json",
    ".uadp/schemas/contract.schema.json",
    # 外部引導協議
    ".uadp/UADP_EXTERNAL_PILOT.md",
]


def ensure_dir(path: Path):
    """確保目錄存在"""
    path.mkdir(parents=True, exist_ok=True)
    return path


def write_file(path: Path, content: str):
    """寫入檔案"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ {path.relative_to(PROJECT_ROOT)}")


def download_file(remote_path: str, local_path: Path) -> bool:
    """
    從 GitHub 下載檔案
    
    Args:
        remote_path: GitHub 上的檔案路徑（相對於倉庫根目錄）
        local_path: 本地儲存路徑
    
    Returns:
        bool: 下載是否成功
    """
    url = REPO_RAW_URL + remote_path
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            content = response.read().decode('utf-8')
            write_file(local_path, content)
            return True
    except urllib.error.URLError as e:
        print(f"  ❌ 下載失敗: {remote_path}")
        print(f"     錯誤: {e}")
        return False
    except Exception as e:
        print(f"  ❌ 下載失敗: {remote_path}")
        print(f"     錯誤: {e}")
        return False


def setup_directories():
    """建立目錄結構"""
    print("\n[1/5] 建立目錄結構...")
    
    ensure_dir(UADP_DIR / "adapters")
    ensure_dir(UADP_DIR / "schemas")
    ensure_dir(UADP_DIR / "logs")
    ensure_dir(CURSOR_RULES_DIR)
    
    print("  ✓ 目錄結構建立完成")


def setup_state_json():
    """建立 state.json（本地生成，包含正確的時間戳記）"""
    state_content = {
        "current_phase": "PLANNING",
        "phase_history": [
            {
                "phase": "PLANNING",
                "entered_at": CURRENT_DATE,
                "status": "in_progress"
            }
        ],
        "last_updated": CURRENT_DATE,
        "contract_file": ".uadp/contract.json",
        "amendments_file": ".uadp/amendments.md",
        "completed_steps": [],
        "blocking_issues": []
    }
    
    write_file(UADP_DIR / "state.json", json.dumps(state_content, ensure_ascii=False, indent=2))


def setup_amendments_md():
    """建立 amendments.md（本地生成，包含正確的時間戳記）"""
    content = """# UADP 自主修正紀錄

> 此檔案記錄所有在 [IMPLEMENTATION] 階段中，未經使用者預先核准的技術變更與修正決策。

---

## 格式說明

每筆修正紀錄應遵循以下格式：

```
[AMENDMENT] 原因: <描述> | 做法: <方案> | 影響: <對功能的改變>
```

---

## 修正紀錄

_目前尚無修正紀錄_
"""
    write_file(UADP_DIR / "amendments.md", content)


def setup_decisions_md():
    """建立 decisions.md（本地生成，包含正確的時間戳記）"""
    content = """# UADP 技術決策紀錄

> 此檔案記錄專案開發過程中的重大技術決策與選擇理由。

---

## 決策紀錄

_目前尚無決策紀錄_
"""
    write_file(UADP_DIR / "logs" / "decisions.md", content)


def download_core_assets():
    """從 GitHub 下載所有核心資產"""
    print("\n[2/5] 從 GitHub 獲取最新核心資產...")
    print("  正在連線到 GitHub...")
    
    success_count = 0
    fail_count = 0
    
    # 顯示進度提示的對應表
    progress_messages = {
        ".cursor/rules/uadp-core.mdc": "正在獲取最新核心憲法...",
        ".cursor/rules/uadp-agent-roles.mdc": "正在獲取角色行為定義...",
        ".cursor/rules/uadp-qa-standard.mdc": "正在獲取 QA 標準...",
        ".cursor/rules/uadp-task-runner.mdc": "正在獲取鏈式執行協議...",
        ".uadp/adapters/README.md": "正在獲取適配器說明...",
        ".uadp/adapters/mobile-flutter.mdc": "正在獲取 Flutter 適配器...",
        ".uadp/adapters/web-modern.mdc": "正在獲取 Web 適配器...",
        ".uadp/adapters/backend-api.mdc": "正在獲取後端 API 適配器...",
        ".uadp/schemas/state.schema.json": "正在獲取狀態 Schema...",
        ".uadp/schemas/contract.schema.json": "正在獲取契約 Schema...",
        ".uadp/UADP_EXTERNAL_PILOT.md": "正在獲取外部引導協議...",
    }
    
    for remote_path in MANIFEST:
        local_path = PROJECT_ROOT / remote_path
        
        # 顯示進度提示
        message = progress_messages.get(remote_path, f"正在下載 {remote_path}...")
        print(f"  {message}")
        
        if download_file(remote_path, local_path):
            success_count += 1
        else:
            fail_count += 1
    
    print(f"\n  ✓ 下載完成: {success_count} 個檔案成功")
    if fail_count > 0:
        print(f"  ⚠️  下載失敗: {fail_count} 個檔案")
        print("\n  💡 提示：")
        print("     - 請檢查網路連線")
        print("     - 確認可以訪問 GitHub")
        print("     - 如果問題持續，請手動從以下連結下載：")
        print(f"       {REPO_RAW_URL}")
        return False
    
    return True


def main():
    """主函式"""
    print("=" * 60)
    print("UADP Framework Setup - 動態流式安裝器")
    print("=" * 60)
    print(f"\n專案根目錄: {PROJECT_ROOT}")
    print(f"初始化時間: {CURRENT_DATE_SHORT}")
    print(f"GitHub 倉庫: {REPO_RAW_URL}")
    
    try:
        # 建立目錄結構
        setup_directories()
        
        # 建立初始檔案（本地生成，包含正確的時間戳記）
        print("\n[3/5] 建立初始檔案...")
        setup_state_json()
        setup_amendments_md()
        setup_decisions_md()
        print("  ✓ 初始檔案建立完成")
        
        # 從 GitHub 下載核心資產
        download_success = download_core_assets()
        
        if not download_success:
            print("\n" + "=" * 60)
            print("⚠️  部分檔案下載失敗")
            print("=" * 60)
            print("\n📋 建議：")
            print("   1. 檢查網路連線")
            print("   2. 確認可以訪問 GitHub")
            print("   3. 重新執行此腳本")
            print(f"   4. 或手動從 {REPO_RAW_URL} 下載缺失的檔案")
            print("\n   即使部分檔案下載失敗，已下載的檔案仍可使用。")
            return 1
        
        # 完成訊息
        print("\n" + "=" * 60)
        print("✅ UADP 初始化成功！")
        print("=" * 60)
        print("\n📋 下一步：")
        print("   1. 在 Cursor IDE 中開啟此專案")
        print("   2. 告訴 AI: '[MODE: ARCHITECT] 我想做一個 [你的專案想法]'")
        print("   3. AI 會用蘇格拉底詰問法幫你釐清需求")
        print("\n💡 提示：")
        print("   - 所有核心資產已從 GitHub 獲取最新版本")
        print("   - 詳細文件請參考: https://github.com/OG-Matcha/UADP")
        print("\n")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  使用者中斷操作")
        return 1
    except Exception as e:
        print(f"\n❌ 初始化失敗: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
