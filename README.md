# Color: Blue
by Diedre Brown

Final Project Files for Pratt Institute School of Information - Programming for Cultural Heritage (INFO664)

### Purpose
Though this project is a work in progress, the idea was to create a color reference dataset with images obtained from the Rijksmuseum API. This dataset lists the name of the image, the size and number of color channels it digitally displays, and an array of blue, green, and red mapping. To obtain this information, I used a number of Python libraries including:Pandas,CSV, OpenCV, Numpy, Requests, Urllib, and JSON. Information on the images was obtained by creating a RjksStudio account to obtain an API key. Once obtained, I selected for items that had blue in their description. Out of a possible 452 hits (according to the JSON I received), 370 of those records had images, and 66 were on display at the museum. However, of the two times that I fetched with the API, I only received 10 full records each time due to the API limits. From this JSON, I transposed the information into a list with a nested dictionary, and then into a CSV file. The CSV file was then used to find the image URL. The image was then retrieved from the web and stored locally. I then used OpenCV to analyze the image as an array.

### To Make the Code Work
1. Obtain an API key from the Rijksmuseum https://data.rijksmuseum.nl/object-metadata/api/

2. Follow the steps in Blue_GetRijksmuseum2.py to get the data from the Rijksmuseum website and store it into a CSV.

3. Use Blue_GetImage2.py to retrieve the images from the web.

4. Use OpenCV in Blue_ImgOpenCV2.py to get the separate color channel arrays for each image. 
