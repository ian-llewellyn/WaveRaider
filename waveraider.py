#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os

if len(sys.argv) == 1:
    sys.exit(os.EX_USAGE)

in_file = sys.argv[1]
#in_file = '/home/ian/06/06/rec_13-38-37.wav'
#in_file = '/home/ian/06/28/rec_14-57-24.wav'

wave_format = [
    {
        'name': 'ChunkID',
        'field_size': 4,
        'endianness': 'big'
    },{
        'name': 'ChunkSize',
        'field_size': 4,
        'endianness': 'little'
    },{
        'name': 'Format',
        'field_size': 4,
        'endianness': 'big'
    },{
        'name': 'SubChunk1ID',
        'field_size': 4,
        'endianness': 'big'
    },{
        'name': 'SubChunk1Size',
        'field_size': 4,
        'endianness': 'little'
    },{
        'name': 'AudioFormat',
        'field_size': 2,
        'endianness': 'little'
    },{
        'name': 'NumChannels',
        'field_size': 2,
        'endianness': 'little'
    },{
        'name': 'SampleRate',
        'field_size': 4,
        'endianness': 'little'
    },{
        'name': 'ByteRate',
        'field_size': 4,
        'endianness': 'little'
    },{
        'name': 'BlockAlign',
        'field_size': 2,
        'endianness': 'little'
    },{
        'name': 'BitsPerSample',
        'field_size': 2,
        'endianness': 'little'
    },{
        'name': 'SubChunk2ID',
        'field_size': 4,
        'endianness': 'big'
    },{
        'name': 'SubChunk2Size',
        'field_size': 4,
        'endianness': 'little'
    }
]

def swap_bytes(data_in):
    data_out = ''
    for byte in reversed(data_in):
        data_out += byte
    return data_out

def value_data(data):
    i = value_out = 0
    for byte in reversed(data):
        value_out += (ord(byte) * pow(256, i))
        i += 1
    return value_out

with file(in_file) as in_file:
    for item in wave_format:
        data = in_file.read(item['field_size'])
        if item['endianness'] == 'little':
            data = swap_bytes(data)
        if not data.isalnum():
            data = value_data(data)
        print item['field_size'], item['name'], data.__repr__()

    while 1:
        data = in_file.read(2)
        if not data:
            break
        print 'Left: ', value_data(swap_bytes(data)),
        data = in_file.read(2)
        if not data:
            break
        print 'Right: ', value_data(swap_bytes(data))
