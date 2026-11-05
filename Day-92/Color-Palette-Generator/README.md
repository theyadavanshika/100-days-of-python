# Color Palette Generator

A web application that extracts the 10 most representative colours from an uploaded image using Python and Pillow's Median Cut colour quantization algorithm.

## Features

- Upload JPG and PNG images.
- Preview uploaded images.
- Extract 10 representative colours.
- Convert RGB values into HEX codes.
- Display colours in a responsive grid.
- Copy HEX codes with a single click.
- Handle invalid image uploads with error messages.

## Technologies Used

- Python
- Flask
- Pillow
- HTML
- CSS
- JavaScript

## Installation

1. Clone the repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate into the project folder:

   ```bash
   cd Color-Palette-Generator
   ```

3. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

4. Activate it:

   ```bash
   source venv/bin/activate
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Run the application:

   ```bash
   python3 app.py
   ```

7. Open `http://127.0.0.1:5000/` in your browser.

## How It Works

1. The user uploads an image.
2. Pillow opens and processes the image.
3. Median Cut colour quantization reduces it to 10 representative colours.
4. The extracted RGB values are converted into HEX codes.
5. Flask passes the colours to the HTML template.
6. The website displays the palette.

## Author

Created as part of the 100 Days of Python course.