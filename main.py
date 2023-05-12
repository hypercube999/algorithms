import random


def apply_hamming_control_bits(input_array):
    output_array = input_array.copy()
    for hamming_bit_number in _iter_hamming_bits_numbers(len(output_array)):
        output_array.insert(hamming_bit_number - 1, 0)
    for hamming_bit_number in _iter_hamming_bits_numbers(len(output_array)):
        output_array[hamming_bit_number-1] = _calc_hamming_bit_for(output_array, hamming_bit_number)
    return output_array


def _iter_hamming_bits_numbers(array_len):
    hamming_bit_power = 0
    hamming_bit_pos = 2 ** hamming_bit_power
    while hamming_bit_pos < array_len:
        yield hamming_bit_pos
        array_len += 1
        hamming_bit_power += 1
        hamming_bit_pos = 2 ** hamming_bit_power


def _calc_hamming_bit_for(input_array, hamming_bit_number):
    bit_count = 0
    for i in range(hamming_bit_number - 1, len(input_array), 2 * hamming_bit_number):
        for j in range(min(len(input_array)-i, hamming_bit_number)):
            bit_count += input_array[i + j]
    return bit_count % 2


if __name__ == '__main__':
    src_arr = [1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1]
    print("Source array", src_arr)

    arr_with_hamming_code = apply_hamming_control_bits(src_arr)
    print("Array with hamming code", arr_with_hamming_code)
