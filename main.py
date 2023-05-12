import random


def apply_hamming_control_bits(input_array):
    output_array = _insert_positions_for_hamming_bits(input_array)
    output_array = _add_hamming_bits(output_array)
    return output_array


def _insert_positions_for_hamming_bits(input_array):
    output_array = input_array.copy()
    hamming_bit_power = 0
    hamming_bit_pos = 2 ** hamming_bit_power - 1
    while hamming_bit_pos < len(output_array):
        output_array.insert(hamming_bit_pos, -1)
        hamming_bit_power += 1
        hamming_bit_pos = 2 ** hamming_bit_power - 1
    return output_array


def _add_hamming_bits(input_array):
    pass


if __name__ == '__main__':
    arr_len = 5

    src_arr = [random.randint(0, 1) for _ in range(arr_len)]
    print("Source array", src_arr)

    arr_with_hamming_code = apply_hamming_control_bits(src_arr)
    print("Array with hamming code", arr_with_hamming_code)

    bit_with_error = random.randint(0, len(arr_with_hamming_code) - 1)
    print("Bit with error", bit_with_error)
    arr_with_error = arr_with_hamming_code.copy()
    arr_with_error[bit_with_error] = int(not arr_with_error[bit_with_error])
    print("Array with error", arr_with_error)
