#!/usr/bin/env python3
"""
UADP Schema Validator - JSON Schema 驗證工具

此腳本驗證 state.json 與 contract.json 是否符合 JSON Schema。
"""

import json
import sys
from pathlib import Path

# 嘗試載入 jsonschema 庫
try:
    import jsonschema
    from jsonschema import validate, ValidationError
except ImportError:
    print("❌ 錯誤: 需要安裝 jsonschema 庫")
    print("   執行: pip install jsonschema")
    sys.exit(1)

PROJECT_ROOT = Path(__file__).parent.parent
UADP_DIR = PROJECT_ROOT / ".uadp"
SCHEMAS_DIR = UADP_DIR / "schemas"

STATE_SCHEMA = SCHEMAS_DIR / "state.schema.json"
CONTRACT_SCHEMA = SCHEMAS_DIR / "contract.schema.json"
STATE_FILE = UADP_DIR / "state.json"
CONTRACT_FILE = UADP_DIR / "contract.json"


def load_json(file_path: Path) -> dict:
    """載入 JSON 檔案"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ 檔案不存在: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ JSON 格式錯誤 ({file_path}): {e}")
        return None
    except Exception as e:
        print(f"❌ 載入檔案時發生錯誤 ({file_path}): {e}")
        return None


def validate_file(data: dict, schema: dict, file_name: str) -> bool:
    """驗證 JSON 資料是否符合 Schema"""
    try:
        validate(instance=data, schema=schema)
        print(f"✅ {file_name} 驗證通過")
        return True
    except ValidationError as e:
        print(f"❌ {file_name} 驗證失敗:")
        print(f"   錯誤路徑: {'.'.join(str(x) for x in e.path)}")
        print(f"   錯誤訊息: {e.message}")
        if e.context:
            for error in e.context:
                print(f"   上下文: {error.message}")
        return False
    except Exception as e:
        print(f"❌ 驗證時發生錯誤 ({file_name}): {e}")
        return False


def main():
    """主函式"""
    print("🔍 開始驗證 UADP JSON Schema...\n")

    # 載入 Schema
    state_schema = load_json(STATE_SCHEMA)
    contract_schema = load_json(CONTRACT_SCHEMA)

    if not state_schema or not contract_schema:
        print("\n❌ 無法載入 Schema 檔案，驗證終止")
        sys.exit(1)

    # 驗證 state.json
    print("📋 驗證 state.json...")
    state_data = load_json(STATE_FILE)
    state_valid = False
    if state_data:
        state_valid = validate_file(state_data, state_schema, "state.json")

    # 驗證 contract.json
    print("\n📋 驗證 contract.json...")
    contract_data = load_json(CONTRACT_FILE)
    contract_valid = False
    if contract_data:
        contract_valid = validate_file(contract_data, contract_schema, "contract.json")

    # 總結
    print("\n" + "=" * 50)
    if state_valid and contract_valid:
        print("✅ 所有檔案驗證通過")
        sys.exit(0)
    else:
        print("❌ 部分檔案驗證失敗")
        sys.exit(1)


if __name__ == "__main__":
    main()

