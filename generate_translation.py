#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script để convert CSV file sang .rpy translation file
Tự động generate file E4_IRO_vietnamese.rpy từ CSV đã dịch
"""

import csv
from pathlib import Path

def generate_translation_file(csv_file, output_rpy):
    """Generate .rpy translation file từ CSV"""
    
    # Đọc CSV
    translations = {}
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            original = row['original'].strip()
            vietnamese = row['vietnamese'].strip()
            
            # Bỏ qua nếu chưa dịch
            if vietnamese:
                translations[original] = vietnamese
    
    # Header file .rpy
    rpy_content = """# -*- coding: utf-8 -*-
# Iroha Route - Tiếng Việt Translation
# Oregairu Zoku PC - Vietnamese Patch
# Auto-generated from CSV

translate vietnamese strings:
"""
    
    # Thêm tất cả translation
    for original, vietnamese in sorted(translations.items()):
        # Escape quotes
        original_escaped = original.replace('"', '\\"')
        vietnamese_escaped = vietnamese.replace('"', '\\"')
        
        rpy_content += f'''
    old "{original_escaped}"
    new "{vietnamese_escaped}"
'''
    
    # Lưu file
    with open(output_rpy, 'w', encoding='utf-8') as f:
        f.write(rpy_content)
    
    print(f"✅ Đã generate: {output_rpy}")
    print(f"📊 Tổng cộng: {len(translations)} dòng dịch")

def main():
    script_dir = Path(__file__).parent
    csv_file = script_dir / 'DICH_IROHA_ROUTE.csv'
    output_rpy = script_dir / 'game' / 'scripts' / 'E4' / 'E4_IRO_vietnamese_AUTO.rpy'
    
    if not csv_file.exists():
        print(f"❌ Không tìm thấy file CSV: {csv_file}")
        print(f"\n💡 Hãy chạy trước: python3 extract_text.py")
        return
    
    print(f"📝 Đang generate translation file từ: {csv_file}")
    generate_translation_file(csv_file, output_rpy)
    
    print(f"\n✨ Hoàn tất! File dịch: {output_rpy}")
    print(f"\n📌 Tiếp theo:")
    print(f"1. Copy file vào game/scripts/E4/")
    print(f"2. Chạy game và chọn Tiếng Việt")

if __name__ == '__main__':
    main()
