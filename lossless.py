from csv import writer
from PIL import Image
import os
import numpy as np
import tifffile as tiff
import time


def compression_factor(reference, test):
    return format(os.stat(reference).st_size / os.stat(test).st_size, '.3f')


def compression_ratio(reference, test):
    return format(os.stat(test).st_size / os.stat(reference).st_size, '.3f')


def percentage_ratio(reference, test):
    return format(((os.stat(reference).st_size - os.stat(test).st_size) / os.stat(reference).st_size) * 100, '.3f')


def write(csv, row):
    with open(csv, 'a') as f_object:
        writer_object = writer(f_object)

        writer_object.writerow(row)

        f_object.close()


def FORMAT(image, csv, extension):
    original_path = 'Images/Standard Test Images .BMP/' + image + '.bmp'

    # FORMAT
    bmp = Image.open(original_path)

    path_to_compress = 'Images/Lossless/' + image + extension

    start_time = time.time()
    bmp = bmp.convert('RGB')
    bmp.save(path_to_compress)
    tempo = format(1000 * (time.time() - start_time), '.3f')  # Compression Time

    if csv == 'Tables/Lossless/CFactor.csv':
        return compression_factor(original_path, path_to_compress)
    else:
        if csv == 'Tables/Lossless/CRatio.csv':
            return compression_ratio(original_path, path_to_compress)
        else:
            if csv == 'Tables/Lossless/CTime.csv':
                return tempo
            else:
                return percentage_ratio(original_path, path_to_compress)


def TIFF(image, csv):
    original_path = 'Images/Standard Test Images .BMP/' + image + '.bmp'

    # TIFF
    bmp = Image.open(original_path)

    reference = np.array(bmp)

    path_to_compress = 'Images/Lossless/' + image + '.tiff'

    start_time = time.time()
    tiff.imsave(path_to_compress, reference, compress=3, photometric='rgb')
    tempo = format(1000 * (time.time() - start_time), '.3f')  # Compression Time

    if csv == 'Tables/Lossless/CFactor.csv':
        return compression_factor(original_path, path_to_compress)
    else:
        if csv == 'Tables/Lossless/CRatio.csv':
            return compression_ratio(original_path, path_to_compress)
        else:
            if csv == 'Tables/Lossless/CTime.csv':
                return tempo
            else:
                return percentage_ratio(original_path, path_to_compress)


images = ['airplane', 'arctichare', 'cat', 'fruits', 'lena_color', 'mandril_color', 'monarch',
          'tulips']

tables = ['Tables/Lossless/CFactor.csv', 'Tables/Lossless/CRatio.csv', 'Tables/Lossless/CTime.csv',
          'Tables/Lossless/PRatio.csv']

print('\nPlease, wait. The results are being collected.')

for table in tables:
    for image in images:
        results = [image, FORMAT(image, table, '.pcx'), FORMAT(image, table, '.png'), FORMAT(image, table, '.tga'),
                   TIFF(image, table)]
        write(table, results)
        results.clear()

print('\nThe results were collected!')

print('\nYou can find them through the path Tables/Lossless in the folder of this project.')
