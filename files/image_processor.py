"""
Batch Image Processor
Author: Neeraj R Rugi
"""
from PIL import Image as image
from PIL import ImageFilter as filter
import sys, os

# data_folder_path: str = sys.argv[1]
# end_folder_path: str = sys.argv[2]
if __name__ == '__main__':
    print(f"Example of folder path: C:\\User\\Documents\\Folder_Name")
    data_folder_path: str = input("Enter the location of the folder from where you want all the images to edited: ")
    end_folder_path: str = input("Enter the location of the folder where you want store all the edited images: ")

filters = ["BLUR", "CONTOUR", "DETAIL", "EMBOSS", "SHARPEN", "SMOOTH", "RESIZE"]
to_gray_scale: bool = False

def image_processor(file_list: list | None = None, path: str | None = None) -> None:
    '''
    Process Images in a directory and outputs it to an output directory.
    :param file_list: List containing file Names
    :param path: Path of output directory
    :return: None
    '''
    global to_gray_scale

    if file_list is None:
        print("The Data Directory is Empty")
        exit(0)

    print("Do you want convert each image to grayscale?")
    gray_scale = input("Enter Yes to apply gray scale, anything else to not apply:\nEnter your Choice: ").lower()
    if gray_scale == 'yes':
        to_gray_scale = True
    print("#" * 50)

    print('Do You want to apply filter like: "BLUR", "CONTOUR", "DETAIL", "EMBOSS", "SHARPEN", "SMOOTH, "RESIZE')
    user_filter = (input("Enter the Options you want separated by a space as is to apply the filters, leave empty to not:\n").upper()).split()
    for item in user_filter:
        if item not in filters:
            print('One or more of the Filters you opted is not accepted.');exit(0)
    print("#" * 50)

    for file in file_list:
        end_img = None
        with image.open(os.path.join(data_folder_path, file)) as img:
            end_img = img
            if to_gray_scale:
                end_img = img.convert('L')
                end_img.save(os.path.join(path, (file.split('.')[0] + "_converted" + '.png')), 'png')

            if "RESIZE" in user_filter:
                x, y = map(int, input("enter the X and Y pixel values respectively separated by space to resize each image to: ").split())
                img.thumbnail((x, y))


            if len(user_filter) > 0:
                for item in user_filter:
                    match item:
                        case "BLUR":
                            end_img = img.filter(filter.BLUR)
                        case "CONTOUR":
                            end_img = img.filter(filter.CONTOUR)
                        case "DETAIL":
                            end_img = img.filter(filter.DETAIL)
                        case "EMBOSS":
                            end_img = img.filter(filter.EMBOSS)
                        case "SHARPEN":
                            end_img = img.filter(filter.SHARPEN)
                        case "SMOOTH":
                            end_img = img.filter(filter.SMOOTH)

            end_img.save(os.path.join(path, (file.split('.')[0] + "_converted" + '.png')), 'png')

    print("Processing Complete, Please Check Output Folder")

def data_input(end_path, data_path) -> list:
    '''
    Creates an output directory and returns a list of files in the input directory
    :return: List of file names
    '''
    os.makedirs(end_path, exist_ok=True)
    return [img for img in os.listdir(data_path) if os.path.isfile(os.path.join(data_path, img)) and img.split('.')[1] in ['png', 'jpeg', 'jpg', 'gif', 'bmp', 'tiff', 'tif', 'webp', 'heic', 'ico', 'svg', 'raw', 'cr2', 'nef', 'orf', 'arw', 'psd', 'ai', 'eps']
]

def dir_check(data_path, end_path) -> None:
    print('Paths:', data_path, end_path,)
    if os.path.isdir(data_path) and os.path.exists(data_path):

        try:
            print('Data Directory Found')
            if os.path.isdir(end_path) and os.path.exists(end_path):
                print('Output Directory Found\n')
                print("#"*50)
                file_list: list = data_input(end_path, data_path)
                # print(file_list)
                image_processor(file_list, end_path)
            else:
                print("No Such Output directory found. Do you want to create a new Directory. Type 'Yes' or 'No'")
                match input('Enter Your Choice: ').lower():
                    case 'yes':
                        print('Output Directory Found\n')
                        print("#" * 50)
                        file_list: list = data_input(end_path, data_path)
                        # print(file_list)
                        image_processor(file_list, end_path)
                    case 'no':
                        print('Program Closing')
                    case _ :
                        print('Invalid Input.')
        except:
            print("Error Occured")
    else:
        print("No Data Directory to read from, Please check file name and path")


if __name__ == '__main__':
    dir_check(data_folder_path, end_folder_path)







