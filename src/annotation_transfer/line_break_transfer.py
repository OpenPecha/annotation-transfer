from fast_antx.core import transfer


def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def write_text_file(file_path, text):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"File saved to: {file_path}")
    except Exception as e:
        print(f"Error writing file {file_path}: {e}")


def transfer_line_breaks(source_text, target_text, output_format="txt"):
    annotation_patterns = [
        ['line_break', r'(\r?\n)']
    ]

    try:
        result = transfer(
            source=source_text,
            patterns=annotation_patterns,
            target=target_text,
            output=output_format
        )
    except Exception as e:
        print(f"Error during transfer: {e}")
        result = ""

    return result


def process_file(source_file_path, target_file_path, output_file_path, output_format="txt"):
    source_text = read_text_file(source_file_path)
    target_text = read_text_file(target_file_path)

    if source_text is None or target_text is None:
        return
    result = transfer_line_breaks(source_text, target_text, output_format)
    write_text_file(output_file_path, result)


def main():
    source_file_path = '../../data/source_text/I768580E7.opf/base/I1PD106653.txt'
    target_file_path = '../../data/target_text/P000001.opf/base/v001.txt'
    output_file_path = "../../data/annotated_text/line_breaks_v001.txt"

    process_file(source_file_path, target_file_path, output_file_path, output_format="txt")


if __name__ == "__main__":
    main()
