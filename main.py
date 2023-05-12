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
        output_array.insert(hamming_bit_pos, 0)
        hamming_bit_power += 1
        hamming_bit_pos = 2 ** hamming_bit_power - 1
    return output_array


def _add_hamming_bits(input_array):
    output_array = input_array.copy()
    hamming_bit_power = 0
    hamming_bit_pos = 2 ** hamming_bit_power - 1
    while hamming_bit_pos < len(output_array):
        output_array[hamming_bit_pos] = _calc_hamming_bit_for(output_array, hamming_bit_power)
        hamming_bit_power += 1
        hamming_bit_pos = 2 ** hamming_bit_power - 1
    return output_array


def _calc_hamming_bit_for(input_array, hamming_bit_power):
    output_bit = 0
    step = 2 ** hamming_bit_power
    i = 2 ** hamming_bit_power - 1
    while i < len(input_array):
        j = 0
        while i + j < min(len(input_array), i + step):
            output_bit += input_array[i + j]
            j += 1
        i += 2 * step
    output_bit = output_bit % 2
    return output_bit


if __name__ == '__main__':
    src_arr = [1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1]
    print("Source array", src_arr)

    arr_with_hamming_code = apply_hamming_control_bits(src_arr)
    print("Array with hamming code", arr_with_hamming_code)
