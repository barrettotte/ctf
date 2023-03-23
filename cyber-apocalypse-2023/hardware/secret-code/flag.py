import csv
import math

# https://media.parallax.com/wp-content/uploads/2020/07/13155129/350-00027a.png.webp

# channel 0 -> D (2)
# channel 1 -> DP (5)
# channel 2 -> A (7)
# channel 3 -> G (10)
# channel 4 -> C (4)
# channel 5 -> B (6)
# channel 6 -> E (1)
# channel 7 -> F (9)

# https://hosteng.com/DmDHelp/Content/Instruction_Set/SEG_Hex_BCD_to_7_Segment_Display.htm
lut_common_cathode = {
    '0111111': '0',
    '0000110': '1',
    '1011011': '2',
    '1001111': '3',
    '1100110': '4',
    '1101101': '5',
    '1111101': '6',
    '0000111': '7',
    '1111111': '8',
    '1101111': '9',
    '1110111': 'A',
    '1111100': 'B', # b
    '0111001': 'C',
    '1011110': 'D', # d
    '1111001': 'E',
    '1110001': 'F',
}

def decode_7seg(signals):
    return lut_common_cathode[signals] if signals in lut_common_cathode else '?'
        
def remap_signals(signals):
    return ''.join([
        signals[3], # G
        signals[7], # F
        signals[6], # E
        signals[0], # D
        signals[4], # C
        signals[5], # B
        signals[2], # A
    ])

def update_segment_state(signals):
    return {
        'G': signals[3],
        'F': signals[7],
        'E': signals[6],
        'D': signals[0],
        'C': signals[4],
        'B': signals[5],
        'A': signals[2],
        'DP': signals[1],
    }

def check_segment_state_change(current, prev):
    return current['A'] != prev['A'] \
    or current['B'] != prev['B'] \
    or current['C'] != prev['C'] \
    or current['D'] != prev['D'] \
    or current['E'] != prev['E'] \
    or current['F'] != prev['F'] \
    or current['DP'] != prev['DP']

segment_state = update_segment_state(['0','0','0','0','0','0','0','0'])
prev_segment_state = update_segment_state(['0','0','0','0','0','0','0','0'])
last_known_dot_decoded = '?'

with open('7seg.csv') as signals_csv:
    signal_reader = csv.reader(signals_csv, delimiter=',')
    next(signal_reader)

    last_ts = 0
    flag_parts = []
    flag_idx = 0
    row_idx = 0
    dot_tick = 0

    for row in signal_reader:
        ts = math.trunc(float(row[0]))

        signals = ''.join(row[1:])
        mapped = remap_signals(signals)
        decoded = decode_7seg(mapped)

        prev_segment_state = segment_state
        segment_state = update_segment_state(signals)
        
        dot = signals[1] == '1'
        all_off = mapped == '0000000'
        time_advanced = ts != last_ts
        bad_decode = decoded == '?'

        if dot:
            dot_tick += 1
        
        print(f'[{row_idx}] ({ts}s) (tick={dot_tick})', signals, '->', mapped, '=', decoded, '.' if dot else '')

        if dot and not all_off:
            if bad_decode:
                raise Exception(f'bad decode?')
            else:
                flag_parts.append(decoded)
                print(f'\t\t\tadded flag[{flag_idx}] = ' + decoded)
                flag_idx += 1

        last_ts = ts
        row_idx += 1
    print()

    print(flag_parts, '\n')
    flag_parts = ''.join(flag_parts)
    print(flag_parts, '\n')

    flag = bytes.fromhex(flag_parts)
    print(flag)
