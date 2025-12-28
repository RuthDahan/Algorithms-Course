import sys
import PIL.Image


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} image-filename")
        exit(-1)

    file_name = sys.argv[1]

    try:
        img = PIL.Image.open(file_name)
    except FileNotFoundError:
        print("Error: File not found.")
        return

    # שלב א': פירוק
    r, g, b = img.split()

    # שלב ב': יצירת "דף שחור"
    zero_band = PIL.Image.new("L", img.size, 0)

    # שלב ג': בנייה מחדש בצבע
    red_image = PIL.Image.merge("RGB", (r, zero_band, zero_band))
    green_image = PIL.Image.merge("RGB", (zero_band, g, zero_band))
    blue_image = PIL.Image.merge("RGB", (zero_band, zero_band, b))

    # 4. הצגת התמונות
    red_image.show()
    green_image.show()
    blue_image.show()


if __name__ == "__main__":
    main()
