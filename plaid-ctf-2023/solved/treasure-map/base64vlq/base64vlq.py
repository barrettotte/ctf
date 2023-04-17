# try to decode mapping files
#
# https://www.murzwin.com/base64vlq.html

import os
import json
import sys
import traceback

##### ripped code #####

# base64 vlq from https://gist.github.com/mjpieters/86b0d152bb51d5f5979346d11005588b

"""Decode and encode Base64 VLQ encoded sequences
Base64 VLQ is used in source maps.
VLQ values consist of 6 bits (matching the 64 characters of the Base64
alphabet), with the most significant bit a *continuation* flag. If the
flag is set, then the next character in the input is part of the same
integer value. Multiple VLQ character sequences so form an unbounded
integer value, in little-endian order.
The *first* VLQ value consists of a continuation flag, 4 bits for the
value, and the last bit the *sign* of the integer:
  +-----+-----+-----+-----+-----+-----+
  |  c  |  b3 |  b2 |  b1 |  b0 |  s  |
  +-----+-----+-----+-----+-----+-----+
while subsequent VLQ characters contain 5 bits of value:
  +-----+-----+-----+-----+-----+-----+
  |  c  |  b4 |  b3 |  b2 |  b1 |  b0 |
  +-----+-----+-----+-----+-----+-----+
For source maps, Base64 VLQ sequences can contain 1, 4 or 5 elements.
"""

from typing import Callable, Final, List, Optional, Tuple

B64CHARS: Final[bytes] = (
    b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
)
B64TABLE: Final[list[Optional[int]]] = [None] * (max(B64CHARS) + 1)
for i, b in enumerate(B64CHARS):
    B64TABLE[b] = i

B64ENC: Callable[[int], str] = B64CHARS.decode().__getitem__
SHIFTSIZE: Final[int] = 5
FLAG: Final[int] = 1 << 5
MASK: Final[int] = (1 << 5) - 1

def base64vlq_decode(vlqval: str) -> Tuple[int]:
    """Decode Base64 VLQ value"""
    results: List[int] = []
    add = results.append
    shiftsize, flag, mask = SHIFTSIZE, FLAG, MASK
    shift = value = 0
    # use byte values and a table to go from base64 characters to integers
    for v in map(B64TABLE.__getitem__, vlqval.encode("ascii")):
        value += (v & mask) << shift  # type: ignore  # v is always int
        if v & flag:  # type: ignore  # v is always int
            shift += shiftsize
            continue
        # determine sign and add to results
        add((value >> 1) * (-1 if value & 1 else 1))
        shift = value = 0
    return tuple(results)

##### done rip #####

# https://www.murzwin.com/base64vlq.html
# https://stackoverflow.com/questions/19330344/how-to-read-base64-vlq-code
# https://medium.com/@trungutt/yet-another-explanation-on-sourcemap-669797e418ce

def parse_src_maps(map_dir):
    src_maps = {}
    for map_path in sorted(os.listdir(map_dir)):
        i = 0
        decoded_lines = {}

        try:
            with open(f"{map_dir}/{map_path}") as map_file:
                map_json = json.load(map_file)

                for mapping in map_json['mappings'].split(';'):
                    if mapping is None or len(mapping) == 0:
                        i += 1
                        continue

                    if ',' in mapping:
                        submappings = []
                        for submap in mapping.split(','):
                            submappings.append(list(base64vlq_decode(submap)))
                        decoded = submappings
                    else:
                        decoded = [list(base64vlq_decode(mapping))]

                    decoded_lines[i] = decoded
                    i += 1

        except Exception as e:
            print(f'failed to decode {i}) ' + map_path + ' mappings')
            print(map_json['mappings'])
            print(traceback.format_exc())
            exit(1)

        src_maps[map_path] = decoded_lines
    return src_maps

def interpret(target_line, segments, context):
    prev_target_col = 0

    for i, segment in enumerate(segments):
        target_col = prev_target_col + segment[0]
        prev_target_col = target_col
        
        src_idx = context['prev_src_col'] + segment[1]
        context['prev_src_col'] = src_idx

        src_line = context['prev_src_line'] + segment[2]
        context['prev_src_line'] = src_line

        src_col = context['prev_src_col'] + segment[3]
        context['prev_src_col'] = src_col

        # decoded                                ([from_position](source_index)=>[to_position])
        print(f"{target_line}) {segments}        [{src_line},{src_col}](#{src_idx})=>[{target_line},{target_col}]")
    return context

###

map_dir = '../maps'
parsed_maps = parse_src_maps(map_dir)

for map_path, decoded_lines in parsed_maps.items():
    print('\n\n---------------------------------')
    print(map_path)
    print('---------------------------------')

    context = {
        'prev_src_idx': 0,
        'prev_src_line': 0,
        'prev_src_col': 0
    }
    for line_num, line in decoded_lines.items():
        if line is list:
            for segment in line:
                context = interpret(line_num, segment, context)
        else:
            context = interpret(line_num, line, context)
