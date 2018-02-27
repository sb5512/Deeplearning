from image_list_creator import ImageListCreator
from feature_extraction import FeatureExtraction
from EnumModels import Models

# First we need to create a image list of all the images in a folder. 
# Creates image.txt listing the location of all images 
il = ImageListCreator()
il.make_list_image_filenames("images")


# Now we have the images.txt file with all images
# We extract features from theses images on various models

obj_fe = FeatureExtraction()
# Param 1 : Takes model name from EnumModels.
# Param 2 : expected that models is the folder that contains this model and prototxt file. 
#           But if it doesnot exist it will create a folder models and download necessary files
obj_fe.extract_features(Models.bvlc_alexnet.name , "models")
obj_fe.extract_features(Models.bvlc_googlenet.name , "models")
# Can do other models as given in Enum Models class

