#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script để trích xuất tất cả text cần dịch từ E4_IRO.rpy
Xuất ra file CSV dễ dễ dịch
"""

import re
import csv
from pathlib import Path

def extract_dialogues(rpy_file):
    """Trích xuất tất cả dialogue từ file .rpy"""
    
    with open(rpy_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    dialogues = []
    lines = content.split('\n')
    
    # Danh sách nhân vật trong game
    characters = [
        'iroha', 'hachiman', 'yukino', 'yui', 'kaori', 'haruno',
        'saki', 'keika', 'hayama', 'yumiko', 'mystery', 'orimoto'
    ]
    
    for i, line in enumerate(lines):
        # Bỏ qua các dòng command
        if any(cmd in line for cmd in ['scene ', 'show ', 'hide ', 'play ', 'stop ', 'with', 'call ', 'jump ', 'label ']):
            continue
        
        # Tìm dialogue: character "text"
        for char in characters:
            pattern = rf'{char}\s+"([^"]+)"'
            match = re.search(pattern, line)
            if match:
                text = match.group(1)
                # Bỏ qua dòng quá ngắn
                if len(text) > 3 and not text.startswith('audio/') and not text.startswith('movies/'):
                    dialogues.append({
                        'line_number': i + 1,
                        'character': char,
                        'original': text,
                        'vietnamese': ''
                    })
                break
        
        # Narrator dialogue (chỉ "text" trong ngoặc kép, indent 4 spaces)
        if re.match(r'^    "[^"]+$', line) and not any(line.strip().startswith(x) for x in ['voice', 'play', 'stop', 'scene']):
            match = re.search(r'^    "([^"]+)"', line)
            if match:
                text = match.group(1)
                if len(text) > 5 and not text.startswith('audio/'):
                    dialogues.append({
                        'line_number': i + 1,
                        'character': 'NARRATOR',
                        'original': text,
                        'vietnamese': ''
                    })
    
    return dialogues

def save_to_csv(dialogues, output_file):
    """Lưu dialogues vào CSV file"""
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['line_number', 'character', 'original', 'vietnamese'])
        writer.writeheader()
        writer.writerows(dialogues)
    
    print(f"✅ Đã lưu {len(dialogues)} dòng text vào: {output_file}")

def main():
    # Đường dẫn file
    script_dir = Path(__file__).parent
    rpy_file = script_dir / 'game' / 'scripts' / 'E4' / 'E4_IRO.rpy'
    output_file = script_dir / 'DICH_IROHA_ROUTE.csv'
    
    if not rpy_file.exists():
        print(f"❌ Không tìm thấy file: {rpy_file}")
        return
    
    print(f"📖 Đang trích xuất text từ: {rpy_file}")
    
    # Trích xuất dialogues
    dialogues = extract_dialogues(rpy_file)
    
    # Lưu vào CSV
    save_to_csv(dialogues, output_file)
    
    print(f"\n📋 Hướng dẫn sử dụng:")
    print(f"1. Mở file: {output_file}")
    print(f"2. Điền cột 'vietnamese' với bản dịch Tiếng Việt")
    print(f"3. Chạy script: python3 generate_translation.py")
    print(f"4. File dịch sẽ được generate tự động")

if __name__ == '__main__':
    main()
