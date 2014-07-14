from alurinium.image.processor import ImageProcessor


class Backend(object):
    """
    This class is managed initial work with images

    :ivar keys_storage: Storage for cache result of image processing
    """
    def process_image(self, original_filename, output_filename, **options):
        processor = ImageProcessor()
        processor.initialize(**options)
        processor.process_file(original_filename, output_filename)
        return output_filename