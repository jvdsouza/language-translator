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
    def tryBlock(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError as err:
            print('file does not exist')
            raise err
        except IOError as err:
            print('IO error')
            raise err

    return tryBlock

@tryFileIO
def writeTranslationToFile(translation, textFilePath):
    with open(textFilePath, mode='w', encoding='utf-8') as output_file:
        output_file.writelines(translation)

@tryFileIO
def translateInputFromFile(textFilePath):
    with open(textFilePath, mode='r', encoding='utf-8') as input_file:
        translation = [translator.translate(line.strip()).text for line in input_file.readlines()]
        return translation

writeTranslationToFile(translateInputFromFile('./input.txt'), './output.txt')