from PIL import Image

image = Image.open("test.jpg")

def resized_image(size1, size2):
    print(f"Current size:  {image.size}")

    resized_image = image.resize((size1,size2))

    resized_image.save('resized-image-.jpg')

    # resized_image.save('resized-image-' + str(size1) + 'x' + str(size2) '.jpg')

size1 = int(input('Enter Width:'))
size2 = int(input('Enter Length:'))