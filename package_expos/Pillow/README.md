# Pillows

## Presentation
You can find the video presentation [here](https://youtu.be/KL7dlMKavH4)

## Summary of support files
- `demo - Group04.ipynb`: the notebook containing this tutorial code
- `uga.jpg`: an image file used throughout the tutorial code

## Guide
[Pillow](https://pillow.readthedocs.io/en/stable/) is an Imaging Library that provides file format support, internal representation, and powerful image processing capabilities.

To install the Pillow package with basic installation, refer to the pip installation lines used in the `demo - Group04.ipynp` file. For more specific installation instructions for your device, refer to the Installation page on the package website.

### The Image Class
The Image class is the most important class in the Python Imaging Library. You are able to create instances of the Image class by loading images from a file, processing images, or creating images. 

To open an image from a file to create the Image instance, use the open() function. Once you have an instance of the image class, there are many methods provided by Pillow to manipulate the image.

To display the image, call the show() function. To learn the attributes of the image, call the format, size, and mode functions. The mode of an image is a string which defines the type and depth of a pixel in the image.

### Cutting, Pasting, and Merging
##### Cutting
To cut an image into a smaller portion, define a region by a 4-tuple. The coordinates of the tuple are (left, upper, right, lower) and refer to the positions between the pixels using a coordinate system with (0, 0) as the upper left corner. 

##### Pasting
To paste a region back onto an image, specify the image and the area that you would like to paste onto image instance. The image must be the exact same size as the area specified, and will raise an error if different sizes. Pasting will modify the Image instance.

##### Splitting and Merging
An image can consist of one or more bands of data. Images can be split between it's bands. The Python Imaging Library allows you to store several bands in a single image if they all have the same dimensions and depth. To get the number and names of bands in an image, use the getbands() method. 

If the image has multiple bands, the image can be split with the split() method. This split can then be stored in variables for each band. To merge the bands back into the image, call the Image.merge() function. You many store the bands in the original order to maintain the original format, or rearrange the bands to convert the image.

### Geometrical Transforms
##### Resize and Rotate
The PIL.Image.Image class contains methods resize() and rotate() an image. The resize() method takes a tuple giving the new size, and rotate() shifts the angle specified in degrees in a counterclockwise rotation.

##### Transpose
To rotate an image you can either use the rotate() method or the transpose() method. The transpose method allows you to flip an image on its horizontal and vertical axis. 

### Color Transformation
##### Color
The Python Imaging Library allows you to convert an images pixel representation using the convert() method. 

The mode of an image is a string which defines the type and depth of a pixel in the image. 
Pillow supports transformations between the “L” (grayscale) mode and the “RGB” (color) modes. Listed below are some additional modes. 
- `1` (1-bit pixels, black and white, stored with one pixel per byte)
- `L` (8-bit pixels, black and white)
- `P` (8-bit pixels, mapped to any other mode using a color palette)
- `RGB` (3x8-bit pixels, true color)
- `RGBA` (4x8-bit pixels, true color with transparency mask)
- `CMYK` (4x8-bit pixels, color separation)
- `YCbCr` (3x8-bit pixels, color video format)
-- Note that this refers to the JPEG, and not the ITU-R BT.2020, standard
- `LAB` (3x8-bit pixels, the L*a*b color space)
- `HSV` (3x8-bit pixels, Hue, Saturation, Value color space)
- `I` (32-bit signed integer pixels)
- `F` (32-bit floating point pixels)

##### Filter
The ImageFilter module contains various enhancement filters that can be used with the filter() method. The current version provides the following set of predefined image enhancement filters.
- BLUR
- CONTOUR
- DETAIL
- EDGE_ENHANCE
- EDGE_ENHANCE_MORE
- EMBOSS
- FIND_EDGES
- SHARPEN
- SMOOTH
- SMOOTH_MORE

##### Enhance
For more advanced image enhancement, you can use the classes in the ImageEnhance module. Using these tools you can adjust contrast, brightness, color balance and sharpness.

### Saving
To save a file, you can use the save() method. You can specify the format when saving and even change that format based on how you save it. 
