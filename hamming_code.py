import random


def code_hamming(input_array):
    output_array = input_array.copy()
    for bit_pos in _iter_hamming_bits_positions(len(input_array), increase_array_len=True):
        output_array.insert(bit_pos, 0)
    output_array_len = len(output_array)
    for hamming_bit_pos in _iter_hamming_bits_positions(output_array_len):
        bit_sum = 0
        for i in range(hamming_bit_pos, output_array_len, 2 * hamming_bit_pos + 2):
            for j in range(min(output_array_len - i, hamming_bit_pos)):
                bit_sum = (bit_sum + output_array[i + j]) % 2
        output_array[hamming_bit_pos] = bit_sum
    return output_array


def _iter_hamming_bits_positions(array_len, increase_array_len=False):
    hamming_bit_power = 0
    hamming_bit_pos = 2 ** hamming_bit_power
    while hamming_bit_pos < array_len:
        yield hamming_bit_pos - 1
        if increase_array_len:
            array_len += 1
        hamming_bit_power += 1
        hamming_bit_pos = 2 ** hamming_bit_power


def decode_hamming(input_array):
    temp_array = _remove_hamming_bits(input_array)
    temp_array = code_hamming(temp_array)
    syndrome_bits_positions = _calc_syndrome(input_array, temp_array)
    output_array = _fix_bits(syndrome_bits_positions, input_array)
    output_array = _remove_hamming_bits(output_array)
    return output_array


def _fix_bits(diff_bit_position, input_array):
    output_array = input_array.copy()
    if len(diff_bit_position):
        bit_with_error = sum(diff_bit_position) - 1
        output_array[bit_with_error] = int(not output_array[bit_with_error])
    return output_array


def _calc_syndrome(input_array, temp_array):
    diff_bit_numbers = []
    for bit_pos in _iter_hamming_bits_positions(len(input_array)):
        if input_array[bit_pos] != temp_array[bit_pos]:
            diff_bit_numbers.append(bit_pos+1)
    return diff_bit_numbers


def _remove_hamming_bits(input_array):
    output_array = input_array.copy()
    hamming_bits_positions = list(_iter_hamming_bits_positions(len(input_array)))
    for bit_pos in reversed(hamming_bits_positions):
        del output_array[bit_pos]
    return output_array


if __name__ == '__main__':
    src_arr = [1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1]
    print("Source array", src_arr)

    arr_with_hamming_code = code_hamming(src_arr)
    print("Array with hamming code", arr_with_hamming_code)

    error_bit_num = random.randint(0, len(arr_with_hamming_code)-1)
    print("Error bit is", error_bit_num)

    arr_with_error = arr_with_hamming_code.copy()
    arr_with_error[error_bit_num] = int(not arr_with_hamming_code[error_bit_num])
    print("Array with error", arr_with_error)

    decoded_array = decode_hamming(arr_with_error)
    print("Decoded array", decoded_array)

    assert src_arr == decoded_array
