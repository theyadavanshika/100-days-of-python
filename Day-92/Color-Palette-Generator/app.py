from flask import Flask, render_template, request
from PIL import Image, UnidentifiedImageError

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    hex_colors = []
    error = None

    if request.method == "POST":

        image = request.files.get("image")

        if not image or image.filename == "":
            error = "Please select an image."

        else:
            try:
                img = Image.open(image)
                img = img.convert("RGB")

                quantized_img = img.quantize(colors=10, method=Image.Quantize.MEDIANCUT)

                color_counts = quantized_img.getcolors()
                palette = quantized_img.getpalette()

                if color_counts and palette:

                    top_colors = sorted(color_counts, reverse=True)

                    for count, color_index in top_colors:

                        r, g, b = palette[color_index * 3 : color_index * 3 + 3]

                        hex_code = "#{:02X}{:02X}{:02X}".format(r, g, b)

                        hex_colors.append(hex_code)

            except (UnidentifiedImageError, OSError):
                error = "Invalid image. Please upload a valid image."

    return render_template("index.html", hex_colors=hex_colors, error=error)


if __name__ == "__main__":
    app.run(debug=True)
