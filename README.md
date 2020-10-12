# Download Images From Yandex using Python
These scripts here presented were a clone of the repository: https://github.com/bobokvsky/yandex-images-download.git 

I cloned and added another functionality so it can also search for similar pictures given one or more images as input. So go ahead and thank them as well!

# How to use it:

## (1)Example (1):
`$ python3 yandex_images_download.py Chrome -k "dog" -isd "0" --limit 10`
                       
                        **or**

`$ python3 yandex_images_download.py Chrome --keyword "dog" --image-same-directory "0" --limit 10`

This will open the browswer and search for the 'dog' keyword. From the image section it will grab the pictures that YandexEngine found and then download the ammount you specified with the --limit flag

*notice that the flag -isd is set to 0(cero)*


## (2)Example (2):
`$ python3 yandex_images_download.py Chrome -k "0" -isd "1" --limit 10`

                           **or**

`$ python3 yandex_images_download.py Chrome --keyword "0" --image-same-directory "1" --limit 10`

Executing this command will take all the pictures within the 'putYourImagesHere' folder and will open the browswer and search for similar images. From the image section it will grab the pictures that YandexEngine found and then download the ammount you specified with the --limit flag

*notice that the flag -k is set to 0(cero)*

This was the part I added myself and worked in.

**Note**
you can pass multiple words to search as well as passing several pictures in the 'putYourImagesHere' folder

**Disclaimer**
I know there were more options (flags) in the repository from which I took part of this code, but I didnt have time to add support for those :) 





