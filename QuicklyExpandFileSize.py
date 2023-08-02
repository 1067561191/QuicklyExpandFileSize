import sys
import os

def append_zeros_to_match_size(file_path_a, file_path_b):
    size_a = os.path.getsize(file_path_a)
    size_b = os.path.getsize(file_path_b)

    if size_a <= size_b:
        print("Error: File A should be larger than File B.")
        return

    difference = size_a - size_b

    with open(file_path_b, 'ab') as file_b:
        chunk_size = 1024
        bytes_written = 0

        while bytes_written < difference:
            remaining_bytes = difference - bytes_written
            chunk = b'\x00' * min(chunk_size, remaining_bytes)
            file_b.write(chunk)
            bytes_written += len(chunk)

    print(f"File B is now equal in size to File A.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py file_path_a file_path_b")
    else:
        file_path_a = sys.argv[1]
        file_path_b = sys.argv[2]

        append_zeros_to_match_size(file_path_a, file_path_b)
