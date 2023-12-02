from PIL import Image

def image_to_ascii(image_path, output_width=100, ascii_chars='@%#*+=-:. '):
    # Open the image
    image = Image.open(image_path)
    
    # Resize the image while maintaining the aspect ratio
    aspect_ratio = image.height / image.width
    new_height = int(output_width * aspect_ratio)
    resized_image = image.resize((output_width, new_height))
    
    # Convert the image to grayscale
    grayscale_image = resized_image.convert('L')
    
    # Map pixel values to ASCII characters
    pixels = grayscale_image.getdata()
    ascii_str = ''.join([ascii_chars[pixel // len(ascii_chars)] for pixel in pixels])
    
    # Split the ASCII string into lines based on the output width
    ascii_lines = [ascii_str[i:i+output_width] for i in range(0, len(ascii_str), output_width)]
    
    # Join the lines to form the final ASCII art
    ascii_art = '\n'.join(ascii_lines)
    
    return ascii_art

# Example usage:
image_path = 'path/to/your/image.jpg'  # Replace with the path to your image file
output_width = 100  # Adjust the output width as needed
ascii_chars = '@%#*+=-:. '  # Customize the ASCII characters as needed

ascii_art = image_to_ascii(image_path, output_width, ascii_chars)
print(ascii_art)

