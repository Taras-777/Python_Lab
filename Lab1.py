class Camera:
    camera = "Camera"

    @staticmethod
    def static():
        return Camera.camera

    def __init__(self, name ="", memory=0, zoom=0, number_of_pixels=0, color="", photo_quality=""):
        self.name = name
        self.memory = memory
        self.zoom = zoom
        self.number_of_pixels = number_of_pixels
        self.color = color
        self.photo_quality = photo_quality


    def __str__(self):
        return "Name: " + str(self.name) + "\nMemory: " + str(self.memory) + "GB" + "\nZoom: " + str(self.zoom) + "X" \
          "\nNumber of pixels: " + str(self.number_of_pixels) + "\nColor: " + str(self.color) + "\nPhoto quality: " \
               + str(self.photo_quality)

    def __del__(self):
        pass


def main():
    canon = Camera("Canon", 128, 15, 12, "Black", "Good")
    sony = Camera("SONY", 256, 18, 7, "Gold", "Good")
    xioami = Camera("XIAOMI", 64, 13, 8, "Green", "BAD")

    print(canon.__str__(),"\n","\n",sony.__str__(),"\n","\n",xioami.__str__())


if __name__ == '__main__':
    main()
