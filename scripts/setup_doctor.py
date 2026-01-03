#!/usr/bin/env python3
"""
UADP Setup Doctor - 環境診斷工具

此腳本讀取 .uadp/contract.json 並執行環境診斷，
產出 Markdown 報告與 JSON 摘要。
"""

import json
import os
import sys
import hashlib
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

# 專案根目錄
PROJECT_ROOT = Path(__file__).parent.parent
UADP_DIR = PROJECT_ROOT / ".uadp"
CONTRACT_FILE = UADP_DIR / "contract.json"
DIAGNOSIS_REPORT = UADP_DIR / "diagnosis_report.md"
DIAGNOSIS_SUMMARY = UADP_DIR / "diagnosis_summary.json"


class SetupDoctor:
    """環境診斷工具主類別"""

    def __init__(self):
        self.contract: Dict[str, Any] = {}
        self.findings: Dict[str, List[str]] = {
            "passed": [],
            "warnings": [],
            "errors": [],
            "info": []
        }
        self.summary: Dict[str, Any] = {}

    def load_contract(self) -> bool:
        """載入 contract.json"""
        try:
            if not CONTRACT_FILE.exists():
                self.findings["errors"].append(
                    f"contract.json 不存在: {CONTRACT_FILE.relative_to(PROJECT_ROOT)}"
                )
                return False

            with open(CONTRACT_FILE, "r", encoding="utf-8") as f:
                self.contract = json.load(f)

            self.findings["passed"].append("contract.json 載入成功")
            return True
        except json.JSONDecodeError as e:
            self.findings["errors"].append(
                f"contract.json JSON 格式錯誤: {e}"
            )
            return False
        except Exception as e:
            self.findings["errors"].append(
                f"載入 contract.json 時發生錯誤: {e}"
            )
            return False

    def check_file_structure(self):
        """檢查檔案結構"""
        required_files = [
            (UADP_DIR / "state.json", "state.json"),
            (UADP_DIR / "contract.json", "contract.json"),
            (UADP_DIR / "amendments.md", "amendments.md"),
            (UADP_DIR / "logs" / "decisions.md", "logs/decisions.md"),
        ]

        for file_path, name in required_files:
            if file_path.exists():
                self.findings["passed"].append(f"{name} 存在")
            else:
                self.findings["warnings"].append(f"{name} 不存在")

    def check_dependencies(self):
        """檢查依賴項"""
        # 檢查 Python 版本
        try:
            result = subprocess.run(
                ["python", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                version = result.stdout.strip()
                self.findings["passed"].append(f"Python: {version}")
            else:
                self.findings["warnings"].append("Python 不可用")
        except Exception as e:
            self.findings["warnings"].append(f"檢查 Python 時發生錯誤: {e}")

        # 檢查 Node.js 版本
        try:
            result = subprocess.run(
                ["node", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                version = result.stdout.strip()
                self.findings["passed"].append(f"Node.js: {version}")
            else:
                self.findings["info"].append("Node.js 不可用（非必需）")
        except Exception:
            self.findings["info"].append("Node.js 不可用（非必需）")

        # 檢查 Git
        try:
            result = subprocess.run(
                ["git", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                version = result.stdout.strip()
                self.findings["passed"].append(f"Git: {version}")
            else:
                self.findings["warnings"].append("Git 不可用")
        except Exception:
            self.findings["warnings"].append("Git 不可用")

    def check_contract_structure(self):
        """檢查 contract.json 結構"""
        required_keys = [
            "contract_version",
            "metadata",
            "requirements",
            "milestones"
        ]

        for key in required_keys:
            if key in self.contract:
                self.findings["passed"].append(f"contract.json 包含 {key}")
            else:
                self.findings["errors"].append(
                    f"contract.json 缺少必要欄位: {key}"
                )

    def detect_adapter(self) -> Optional[str]:
        """自動偵測適配器"""
        adapters_dir = UADP_DIR / "adapters"

        # 檢查 Flutter
        if (PROJECT_ROOT / "pubspec.yaml").exists():
            return "mobile-flutter"

        # 檢查 React/Vite
        package_json = PROJECT_ROOT / "package.json"
        if package_json.exists():
            try:
                with open(package_json, "r", encoding="utf-8") as f:
                    pkg = json.load(f)
                    deps = pkg.get("dependencies", {})
                    dev_deps = pkg.get("devDependencies", {})
                    all_deps = {**deps, **dev_deps}

                    if "react" in all_deps and "vite" in all_deps:
                        return "web-modern"
                    elif "react" in all_deps or "express" in all_deps:
                        return "backend-api"
            except Exception:
                pass

        # 檢查 Python 後端
        if (PROJECT_ROOT / "requirements.txt").exists():
            return "backend-api"

        return None

    def check_adapter(self):
        """檢查適配器"""
        adapter = self.detect_adapter()
        if adapter:
            adapter_file = UADP_DIR / "adapters" / f"{adapter}.mdc"
            if adapter_file.exists():
                self.findings["passed"].append(
                    f"適配器已偵測: {adapter}，檔案存在"
                )
            else:
                self.findings["warnings"].append(
                    f"適配器已偵測: {adapter}，但檔案不存在"
                )
        else:
            self.findings["info"].append(
                "未偵測到技術棧（可能是框架專案本身）"
            )

    def validate_json_schema(self, data: Dict, schema_path: Path) -> bool:
        """驗證 JSON 是否符合 Schema（簡化版）"""
        if not schema_path.exists():
            return True  # Schema 不存在時跳過驗證

        try:
            with open(schema_path, "r", encoding="utf-8") as f:
                schema = json.load(f)
            # 這裡可以實作更完整的 JSON Schema 驗證
            # 目前僅檢查基本結構
            return True
        except Exception as e:
            self.findings["warnings"].append(
                f"JSON Schema 驗證失敗: {e}"
            )
            return False

    def generate_summary(self) -> Dict[str, Any]:
        """生成診斷摘要"""
        return {
            "diagnosis_timestamp": datetime.now().isoformat(),
            "phase": "DIAGNOSIS",
            "project_type": self.contract.get("project_type", "unknown"),
            "findings": {
                "passed_count": len(self.findings["passed"]),
                "warnings_count": len(self.findings["warnings"]),
                "errors_count": len(self.findings["errors"]),
                "info_count": len(self.findings["info"])
            },
            "adapter_detected": self.detect_adapter(),
            "contract_loaded": bool(self.contract),
            "file_structure": {
                "state_json_exists": (UADP_DIR / "state.json").exists(),
                "contract_json_exists": CONTRACT_FILE.exists(),
                "amendments_md_exists": (UADP_DIR / "amendments.md").exists()
            }
        }

    def generate_report(self) -> str:
        """生成 Markdown 報告"""
        report = f"""# UADP 環境診斷報告

> **生成時間：** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
> **階段：** DIAGNOSIS  
> **專案類型：** {self.contract.get("project_type", "unknown")}

---

## 1. 診斷結果摘要

- ✅ **通過項目：** {len(self.findings["passed"])} 項
- ⚠️ **警告項目：** {len(self.findings["warnings"])} 項
- ❌ **錯誤項目：** {len(self.findings["errors"])} 項
- ℹ️ **資訊項目：** {len(self.findings["info"])} 項

---

## 2. 詳細檢查結果

### 2.1 通過項目 ✅

"""
        for item in self.findings["passed"]:
            report += f"- {item}\n"

        if self.findings["warnings"]:
            report += "\n### 2.2 警告項目 ⚠️\n\n"
            for item in self.findings["warnings"]:
                report += f"- {item}\n"

        if self.findings["errors"]:
            report += "\n### 2.3 錯誤項目 ❌\n\n"
            for item in self.findings["errors"]:
                report += f"- {item}\n"

        if self.findings["info"]:
            report += "\n### 2.4 資訊項目 ℹ️\n\n"
            for item in self.findings["info"]:
                report += f"- {item}\n"

        adapter = self.detect_adapter()
        if adapter:
            report += f"\n---\n\n## 3. 適配器偵測\n\n**偵測結果：** {adapter}\n"

        report += "\n---\n\n**診斷完成時間：** " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"

        return report

    def run(self):
        """執行診斷"""
        print("[*] 開始執行 UADP 環境診斷...\n")

        # 載入 contract.json
        if not self.load_contract():
            print("[ERROR] 無法載入 contract.json，診斷終止")
            return False

        # 執行各項檢查
        print("[*] 檢查檔案結構...")
        self.check_file_structure()

        print("[*] 檢查依賴項...")
        self.check_dependencies()

        print("[*] 檢查 contract.json 結構...")
        self.check_contract_structure()

        print("[*] 檢查適配器...")
        self.check_adapter()

        # 生成報告
        print("\n[*] 生成診斷報告...")
        report = self.generate_report()
        summary = self.generate_summary()

        # 寫入檔案
        UADP_DIR.mkdir(parents=True, exist_ok=True)

        with open(DIAGNOSIS_REPORT, "w", encoding="utf-8") as f:
            f.write(report)

        with open(DIAGNOSIS_SUMMARY, "w", encoding="utf-8") as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)

        print(f"[OK] 診斷報告已生成: {DIAGNOSIS_REPORT}")
        print(f"[OK] 診斷摘要已生成: {DIAGNOSIS_SUMMARY}")

        # 顯示摘要
        print("\n" + "=" * 50)
        print("診斷結果摘要:")
        print(f"  [PASS] 通過: {len(self.findings['passed'])} 項")
        print(f"  [WARN] 警告: {len(self.findings['warnings'])} 項")
        print(f"  [ERROR] 錯誤: {len(self.findings['errors'])} 項")
        print(f"  [INFO] 資訊: {len(self.findings['info'])} 項")
        print("=" * 50)

        return len(self.findings["errors"]) == 0


def main():
    """主函式"""
    doctor = SetupDoctor()
    success = doctor.run()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

