#!/usr/bin/env python3
"""验证 characters/*.md 角色档案的格式与内容质量。"""

import glob
import os
import re
import sys


REQUIRED_FM_FIELDS = {"id", "name", "faction", "rank", "status"}
VALID_STATUSES = {"active", "injured", "dead", "missing"}
REQUIRED_SECTIONS = [
    "一句话概括",
    "个性",
    "语言风格",
    "属性",
    "背景",
    "能力与限制",
    "人际关系",
    "对话与行动示例",
]
ATTRIBUTES = ["武力", "智力", "体力", "魅力", "政治"]
PLACEHOLDER_RE = re.compile(r"<[^>]*(?:简要|说明|描述|背景|段|填写|补充|待定|示例|TODO)[^>]*>", re.IGNORECASE)


def parse_frontmatter(lines):
    """解析 YAML frontmatter，返回 (fields_dict, end_line_index)。"""
    if not lines or lines[0].strip() != "---":
        return None, 0
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, 0
    fields = {}
    for line in lines[1:end]:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    return fields, end


def find_sections(text):
    """返回所有 ## 标题名的集合。"""
    return set(re.findall(r"^##\s+(.+?)(?:\s*（.*?）)?\s*$", text, re.MULTILINE))


def check_attributes(text):
    """检查属性表格，返回错误列表。"""
    errors = []
    table_match = re.search(
        r"##\s+属性.*?\n((?:.*\n)*?)(?=\n##|\Z)", text
    )
    if not table_match:
        errors.append("找不到属性表格")
        return errors

    table_text = table_match.group(1)
    found_attrs = {}
    for line in table_text.split("\n"):
        line = line.strip()
        if not line.startswith("|") or "---" in line or "属性" in line.split("|")[1:2]:
            continue
        cells = [c.strip() for c in line.split("|")]
        cells = [c for c in cells if c]
        if len(cells) >= 3:
            attr_name = cells[0]
            if attr_name in ATTRIBUTES:
                found_attrs[attr_name] = cells[1:]

    for attr in ATTRIBUTES:
        if attr not in found_attrs:
            errors.append(f"缺少属性: {attr}")
            continue
        val_str, *desc = found_attrs[attr]
        try:
            val = int(val_str)
            if not 1 <= val <= 100:
                errors.append(f"属性 {attr} 值 {val} 超出 1-100 范围")
        except ValueError:
            errors.append(f"属性 {attr} 值 '{val_str}' 不是有效数字")
        description = desc[0] if desc else ""
        if not description.strip():
            errors.append(f"属性 {attr} 缺少说明文字")

    return errors


def check_dialogue_examples(text):
    """检查对话示例，返回错误列表。"""
    errors = []
    section_match = re.search(
        r"##\s+对话与行动示例.*?\n((?:.*\n)*?)(?=\n##\s|\Z)", text
    )
    if not section_match:
        errors.append("找不到对话与行动示例章节内容")
        return errors

    section_text = section_match.group(1)
    examples = re.findall(r"###\s+示例", section_text)
    if not examples:
        errors.append("至少需要 1 个对话示例（### 示例）")
        return errors

    has_situation = bool(re.search(r"\*\*情境\*\*", section_text))
    has_action = bool(re.search(r"\*\*行动\*\*", section_text))
    has_dialogue = bool(re.search(r"\*\*台词\*\*", section_text))

    if not has_situation:
        errors.append("对话示例缺少 **情境**")
    if not has_action:
        errors.append("对话示例缺少 **行动**")
    if not has_dialogue:
        errors.append("对话示例缺少 **台词**")

    return errors


def check_file(filepath):
    """检查单个角色文件，返回 (errors, warnings) 列表。"""
    errors = []
    filename = os.path.basename(filepath)
    expected_id = filename.removesuffix(".md")

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.split("\n")

    # --- Frontmatter ---
    fm, _ = parse_frontmatter(lines)
    if fm is None:
        errors.append("缺少 YAML frontmatter（文件必须以 --- 开头和结尾）")
        return errors

    for field in REQUIRED_FM_FIELDS:
        if field not in fm:
            errors.append(f"frontmatter 缺少必填字段: {field}")

    if "status" in fm and fm["status"] not in VALID_STATUSES:
        errors.append(
            f"status 值 '{fm['status']}' 无效，必须是 {'/'.join(sorted(VALID_STATUSES))} 之一"
        )

    if "id" in fm and fm["id"] != expected_id:
        errors.append(f"id '{fm['id']}' 与文件名 '{filename}' 不一致（应为 '{expected_id}'）")

    # --- 必填章节 ---
    sections = find_sections(content)
    for sec in REQUIRED_SECTIONS:
        if sec not in sections:
            errors.append(f"缺少必填章节: ## {sec}")

    # --- 属性 ---
    errors.extend(check_attributes(content))

    # --- 占位符检测 ---
    for i, line in enumerate(lines, 1):
        placeholders = PLACEHOLDER_RE.findall(line)
        for ph in placeholders:
            errors.append(f"第 {i} 行发现模板占位符残留: {ph}")

    # --- 对话示例 ---
    errors.extend(check_dialogue_examples(content))

    return errors


def main():
    char_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "characters")
    files = sorted(glob.glob(os.path.join(char_dir, "*.md")))

    if not files:
        print("⚠ 未找到任何角色文件")
        sys.exit(0)

    total_errors = 0
    for filepath in files:
        filename = os.path.basename(filepath)
        errors = check_file(filepath)
        if errors:
            print(f"FAIL  {filename}")
            for err in errors:
                print(f"  ✗ {err}")
            total_errors += len(errors)
        else:
            print(f"PASS  {filename}")

    print(f"\n共检查 {len(files)} 个文件，{total_errors} 个错误")
    sys.exit(1 if total_errors > 0 else 0)


if __name__ == "__main__":
    main()
