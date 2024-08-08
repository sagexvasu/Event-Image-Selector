# EVENT IMAGE SELECTOR

An Event Image Selector App makes it easy for people to pick and organize pictures for events like weddings, parties, and conferences. The app has a simple design, allowing users to upload images from their phone, computer, or social media accounts. It helps you find the right pictures by letting you sort them based on the type of event, theme, or color.

You can create groups of images, add tags to them, and even work together with others to make sure everyone involved in the event can see and choose the images. The app also lets you save the images in different formats, so they’re ready for printing, digital displays, or sharing online. Plus, it often comes with basic tools to edit the pictures, helping you make them look just right before the event.


# Installation Steps:

Note: Make sure to install python on your device through Homebrew (if using Mac)

1. Clone the repository: `git clone https://github.com/sagextitan/majorproject.git`

2. Setting up Python environment to execute python files and install the packages :

```python

# For creating and activating the virtual environment provided by Python for running commands

python3 -m venv venv
source venv/bin/activate

# For installing the packages

pip install -r requirements.txt

```

3. To start the server:

```bash

# After running this command you will get a url for starting the project on your local terminal that goes by this: http://127.0.0.1:5000


python3 app.py

```

4. If you want some new images to be added to local collection so that the API can process selfie and collect all similar images, add them to the `AllImages` folder and run this command so that on selfie submission the new images can be included if similarity is found:

```python

# This will create a new file `encoded_faces.npy` having details of all the faces. If there already exists a file then one can remove it and then run the above command

python3 preprocess_and_encode.py


```

[Do restart the server on which the application is running]
