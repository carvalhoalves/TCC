from csv import writer
from PIL import Image
from skimage.metrics import adapted_rand_error as are
from skimage.metrics import mean_squared_error as mse
from skimage.metrics import structural_similarity as mssim
from skimage.metrics import peak_signal_noise_ratio as psnr
import numpy as np


def write(csv, row):
    with open(csv, 'a') as f_object:
        writer_object = writer(f_object)

        writer_object.writerow(row)

        f_object.close()


def GIF(image_name, csv):
    path = 'Images/Lossy/'

    bmp = Image.open('Images/Standard Test Images .BMP/' + image_name + '.bmp')

    reference = np.array(bmp)

    # GIF
    bmp.save(path + image_name + '.gif', save_all=True, append_images=[bmp])

    gif = Image.open(path + image_name + '.gif')

    gif = gif.convert('RGB')

    test = np.array(gif)

    if csv == 'Tables/Lossy/ARE.csv':
        error, precision, recall = are(reference, test)
        return format(error, '.3f')
    else:
        if csv == 'Tables/Lossy/MSE.csv':
            return format(mse(reference, test), '.3f')
        else:
            if csv == 'Tables/Lossy/MSSIM.csv':
                return format(mssim(reference, test, data_range=reference.max() - reference.min(), multichannel=True),
                              '.3f')
            else:
                return format(psnr(reference, test), '.3f')


def JPEG(image_name, csv):
    path = 'Images/Lossy/'

    # JPEG
    bmp = Image.open('Images/Standard Test Images .BMP/' + image_name + '.bmp')

    reference = np.array(bmp)

    bmp.save(path + image_name + '.jpeg', optmize=True)

    jpeg = Image.open(path + image_name + '.jpeg')

    test = np.array(jpeg)

    if csv == 'Tables/Lossy/ARE.csv':
        error, precision, recall = are(reference, test)
        return format(error, '.3f')
    else:
        if csv == 'Tables/Lossy/MSE.csv':
            return format(mse(reference, test), '.3f')
        else:
            if csv == 'Tables/Lossy/MSSIM.csv':
                return format(mssim(reference, test, data_range=reference.max() - reference.min(), multichannel=True),
                              '.3f')
            else:
                return format(psnr(reference, test), '.3f')


def JPEG2000(image_name, csv):
    path = 'Images/Lossy/'

    # JPEG 2000
    bmp = Image.open('Images/Standard Test Images .BMP/' + image_name + '.bmp')

    reference = np.array(bmp)

    bmp.save(path + image_name + '.jp2', quality_layers=[17])

    jp2 = Image.open(path + image_name + '.jp2')

    test = np.array(jp2)

    if csv == 'Tables/Lossy/ARE.csv':
        error, precision, recall = are(reference, test)
        return format(error, '.3f')
    else:
        if csv == 'Tables/Lossy/MSE.csv':
            return format(mse(reference, test), '.3f')
        else:
            if csv == 'Tables/Lossy/MSSIM.csv':
                return format(mssim(reference, test, data_range=reference.max() - reference.min(), multichannel=True),
                              '.3f')
            else:
                return format(psnr(reference, test), '.3f')


def WebP(image_name, csv):
    path = 'Images/Lossy/'

    bmp = Image.open('Images/Standard Test Images .BMP/' + image_name + '.bmp')

    reference = np.array(bmp)

    # WebP
    bmp.save(path + image_name + '.webp')

    webp = Image.open(path + image_name + '.webp')

    test = np.array(webp)

    if csv == 'Tables/Lossy/ARE.csv':
        error, precision, recall = are(reference, test)
        return format(error, '.3f')
    else:
        if csv == 'Tables/Lossy/MSE.csv':
            return format(mse(reference, test), '.3f')
        else:
            if csv == 'Tables/Lossy/MSSIM.csv':
                return format(mssim(reference, test, data_range=reference.max() - reference.min(), multichannel=True),
                              '.3f')
            else:
                return format(psnr(reference, test), '.3f')


images = ['airplane', 'arctichare', 'cat', 'fruits', 'lena_color', 'mandril_color', 'monarch', 'tulips']

tables = ['Tables/Lossy/ARE.csv', 'Tables/Lossy/MSE.csv', 'Tables/Lossy/MSSIM.csv', 'Tables/Lossy/PSNR.csv']

print('\nPlease, wait. The results are being collected.')

for table in tables:
    for image in images:
        results = [image, GIF(image, table), JPEG(image, table), JPEG2000(image, table), WebP(image, table)]
        write(table, results)
        results.clear()

print('\nThe results were collected!')

print('\nYou can find them through the path Tables/Lossy in the folder of this project.')
