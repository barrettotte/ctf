import PyPDF2

with open('chall.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    print('metadata:', pdf_reader.metadata)

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        print(page)
        print('found', len(page.extract_text()), 'word(s)')

    # using hex viewer to find stream ranges

    # stream 1 /Length 4726>> stream
    with open('stream_1', 'w+') as f:
        pdf_file.seek(0xBA)
        s = pdf_file.read(4726)
        f.write(s.hex())

    # stream 2 /Length 20763>> stream
    with open('stream_2', 'w+') as f:
        pdf_file.seek(0x14C7)
        s = pdf_file.read(20763)
        f.write(s.hex())

    # stream 3 /Length 316>> stream
    with open('stream_3', 'w+') as f:
        pdf_file.seek(0x695D)
        s = pdf_file.read(316)
        f.write(s.hex())

    # stream 4 /Length 9272>> stream
    with open('stream_4', 'w+') as f:
        pdf_file.seek(0x6B7B)
        s = pdf_file.read(9272)
        f.write(s.hex())
    
    # stream 5 /Length 263>> stream
    with open('stream_5', 'w+') as f:
        pdf_file.seek(0x9220)
        s = pdf_file.read(263)
        f.write(s.hex())

    # stream 6 /Length 2932>> stream
    with open('stream_6', 'w+') as f:
        pdf_file.seek(0x95C1)
        s = pdf_file.read(2932)
        f.write(s.hex())

    pdf_file.seek(0)
    pdf_data = bytearray(pdf_file.read())
    print('pdf is', len(pdf_data), 'bytes')

