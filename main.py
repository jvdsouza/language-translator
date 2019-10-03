from googletrans import Translator

translator = Translator()

# try:
#     with open('./input/input.txt', mode='r') as input_file:
#         translation = [translator.translate(line.strip()).text for line in input_file.readlines()]
        
#         try:
#             with open('./output/output.txt', mode='a') as output_file:
#                 for line in translation:
#                     output_file.write(line)
#         except FileNotFoundError as err:
#             print('file does not exist')
#             raise err
#         except IOError as err:
#             print('IO error')
#             raise err

# except FileNotFoundError as err:
#     print('file does not exist')
#     raise err
# except IOError as err:
#     print('IO error')
#     raise err

def tryFileIO(func):
    def tryBlock(*args):
        try:
            func(*args)
        except FileNotFoundError as err:
            print('file does not exist')
            raise err
        except IOError as err:
            print('IO error')
            raise err

    return tryBlock

@tryFileIO
def writeTranslationToFile(translation, textFilePath):
    with open(textFilePath, mode='w') as output_file:
        output_file.writelines(translation)

@tryFileIO
def translateInputFromFile(textFilePath):
    with open(textFilePath, mode='r') as input_file:
        translation = [translator.translate(line.strip()).text for line in input_file.readlines()]
        writeTranslationToFile(translation, './output.txt')

translateInputFromFile('./input.txt')