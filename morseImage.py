from PIL import Image

class MorseImageDecoder:

    def __init__(self, filename):
        self.morse_image = None
        self.filename = filename
        self.bg_color = None
        self.morse_color = None
        self.MORSE_CODE_DICT = {'..-.': 'F', '-..-': 'X',
                                '.--.': 'P', '-': 'T', '..---': '2',
                                '....-': '4', '-----': '0', '--...': '7',
                                '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
                                '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
                                '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
                                '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
                                '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
                                '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}

        self.__read_image()


    def __read_image(self):
        try:
            self.morse_image = Image.open(self.filename)
            self.bg_color = self.morse_image.getpixel((0, 0))
            self.morse_color = self.morse_image.getpixel((1, 1))
            return self.morse_image
        except OSError as ex:
            print(ex)


    def __is_dot(self, row, column):
        rgb = self.morse_image.getpixel((column, row))
        rgb_next = self.morse_image.getpixel((column + 1, row))

        if (rgb == rgb_next and rgb == self.bg_color):
            return -1

        if (rgb != rgb_next):
            return 1
        else:
            return 0


    def __parse_image_morse(self):
        image_size = self.morse_image.size
        morse_code = ''
        morse_list = []
        for i in range(1, image_size[1]):
            if (i % 2 != 0):
                j = 1
                while j < image_size[0]:
                    is_dot = self.__is_dot(i, j)
                    if(is_dot == 1):
                        morse_code += '.'
                        j += 2
                    elif (is_dot == 0):
                        morse_code += '-'
                        j += 4
                    else:
                        morse_list.append(morse_code)
                        morse_code = ""
                        break

        return morse_list

    # TODO: Create an the encode method that creates a morse image
    # given an ascii text in capital
    def encode(self, text):
        pass

    def decode(self):
        message = ''
        morse = self.__parse_image_morse()
        for line in morse:
            message += self.MORSE_CODE_DICT[line]
        return message.lower()