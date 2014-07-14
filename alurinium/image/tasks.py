from PIL import Image
from alurinium.image.processor import ImageProcessor
from celery import task


# @task
# def process_image(input_filename, output_filename, **options):
#     processor = ImageProcessor()
#     processor.initialize(**options)
#     original = Image.open(input_filename)
#     result = processor.process_image(original)
#     result.save(output_filename, mode='PNG')