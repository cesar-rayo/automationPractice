from PIL import Image, ImageChops
import logging
import datetime

LOGGER = logging.getLogger(__name__)

class ImageAnalysis:
    DESIRED_SIZE = (1200, 3305)
    RESULTS_PATH = "./results"
    @staticmethod
    def differences(path_test_result, path_expected_result):
        response = False
        test_result = Image.open(path_test_result)
        expected_result = Image.open(path_expected_result)
        
        target_files = []
        for image in [test_result, expected_result]:
            LOGGER.info("> Loading image [ {} ]".format(image.filename))
            new_image = image.resize(ImageAnalysis.DESIRED_SIZE)
            file_name = '{}/pp_{}'.format(ImageAnalysis.RESULTS_PATH, image.filename.split("/")[-1])
            new_image.save(file_name)
            target_files.append(file_name)

        i1 = Image.open(target_files[0])
        i2 = Image.open(target_files[1])
        
        diff = ImageChops.difference(i1.convert('CMYK'), i2.convert('CMYK'))

        if diff.getbbox():
            response = True
            LOGGER.info("> Found differences")
            time = datetime.datetime.now()
            diff_path = "{}/difference_{}.jpg".format(ImageAnalysis.RESULTS_PATH, time.strftime("%Y%m%d_%H%M%S"))
            LOGGER.info("> Creating file [ {} ]".format(diff_path))
            diff.save(diff_path)
        return response
