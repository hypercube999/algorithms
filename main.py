import random


def code_hamming(input_array):
    output_array = input_array.copy()
    for hamming_bit_number in _iter_hamming_bits_numbers_for_add(len(output_array)):
        output_array.insert(hamming_bit_number - 1, 0)
    for hamming_bit_number in _iter_hamming_bits_numbers_for_add(len(output_array)):
        output_array[hamming_bit_number-1] = _calc_hamming_bit_for(output_array, hamming_bit_number)
    return output_array


def _iter_hamming_bits_numbers_for_add(array_len):
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


def decode_hamming(input_array):
    temp_array = input_array.copy()
    bits_count = 0
    i = 0
    while 2**i < len(temp_array):
        temp_array[2**i-1] = 0
        bits_count += 1
        i += 1

    for hamming_bit_number in _iter_hamming_bits_numbers_for_add(len(temp_array) - bits_count):
        temp_array[hamming_bit_number - 1] = _calc_hamming_bit_for(temp_array, hamming_bit_number)

    diff_bit_position = _calc_dif_positions(input_array, temp_array)
    output_array = _fix_bits(diff_bit_position, input_array)
    output_array = _remove_hamming_bits(output_array)
    return output_array


def _fix_bits(diff_bit_position, input_array):
    output_array = input_array.copy()
    if len(diff_bit_position):
        bit_with_error = sum(diff_bit_position) - 1
        output_array[bit_with_error] = int(not output_array[bit_with_error])
    return output_array


def _calc_dif_positions(input_array, temp_array):
    diff_bit_position = []
    i = 0
    while 2 ** i < len(temp_array):
        if input_array[2 ** i - 1] != temp_array[2 ** i - 1]:
            diff_bit_position.append(2 ** i)
        i += 1
    return diff_bit_position


def _remove_hamming_bits(input_array):
    output_array = input_array.copy()
    i = 0
    bits_positions = []
    while 2 ** i < len(output_array):
        bits_positions.insert(0, 2 ** i - 1)
        i += 1
    for bits_pos in bits_positions:
        del output_array[bits_pos]
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
