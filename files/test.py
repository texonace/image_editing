from image_processor import dir_check as processor

print(f"Example of folder path: C:\\User\\Documents\\Folder_Name")
data_folder_path: str = input("Enter the location of the folder from where you want all the images to edited: ")
end_folder_path: str = input("Enter the location of the folder where you want store all the edited images: ")

processor(data_folder_path, end_folder_path)