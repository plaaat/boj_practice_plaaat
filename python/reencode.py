import os
import chardet

def convert_euckr_to_utf8(root_directory):
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith('.py'):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'rb') as file:
                    raw_data = file.read()
                    result = chardet.detect(raw_data)
                    original_encoding = result['encoding']
                
                if original_encoding is not None and original_encoding.lower() == 'euc-kr':
                    try:
                        decoded_data = raw_data.decode('euc-kr')
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(decoded_data)
                        print(f"Converted {file_path} from euc-kr to utf-8")
                    except Exception as e:
                        print(f"Failed to convert {file_path}: {e}")
                else:
                    print(f"{file_path} is already in utf-8 encoding or not euc-kr encoding")

# 사용 예시
convert_euckr_to_utf8('.')
