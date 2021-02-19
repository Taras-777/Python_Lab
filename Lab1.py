class Camera:
    name = ""
    memory = 0
    zoom = 0
    number_of_pixels = 0
    color = ""
    photo_quality = ""

    def __init__(self, name, memory, zoom, number_of_pixels, color, photo_quality):
        self.name = name
        self.memory = memory
        self.zoom = zoom
        self.number_of_pixels = number_of_pixels
        self.color = color
        self.photo_quality = photo_quality
        # print("Конструктор")

    def __str__(self):
        return "Name: " + str(self.name) + "\nMemory: " + str(self.memory) + "GB" + "\nZoom: " + str(self.zoom) + "X" \
          "\nNumber of pixels: " + str(self.number_of_pixels) + "\nColor: " + str(self.color) + "\nPhoto quality: " \
               + str(self.photo_quality)

    def __del__(self):
        print('Деструктор')


out = Camera("Canon ", 128, 15, 12, "Black", "Good")
print(out.__str__())



