import os



POST_TITLE = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

POST_BODY = """This is a post test, where Im gonna put random things to test css such as h1, h2, p, colors, selector, borders, and such.
                            
                            space test

<h2>This is a h2, will be rendered as a h2? who nows</h2>
Can i affect the h2?
<p>This is a p, can i put css if is rendered as a p?</p> 
"""

user_id_folder = 'user-1' 
from flask import current_app
ADMIN_FOLDER = os.path.join(current_app.static_folder, 'images', user_id_folder, 'post'
        )

TEST_IMAGE =  'test_image.png'
SOURCE_IMAGE_PATH = os.path.join(current_app.static_folder, 'test')
ADMIN_AUTHOR = 'Admin'