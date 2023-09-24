pip install ipyvizzu[streamlit]
pip install ipyvizzu-story[streamlit]

import streamlit as st
from ipyvizzu import Data, Config
from ipyvizzustory import Story, Slide, Step


st.title("Streamlit Tutorial App")
st.write("This is my new app")

button1 = st.button("Click me")
if button1:
    st.write("This is some text")

data = Data()
data.add_series("Foo", ["Alice", "Bob", "Ted"])
data.add_series("Bar", [15, 32, 12])
data.add_series("Baz", [5, 3, 2])

story = Story(data=data)

# create Slides and Steps and add them to the Story
slide1 = Slide(
    Step(
        Config({"x": "Foo", "y": "Bar"}),
        )
    )
story.add_slide(slide1)
slide2 = Slide(
    Step(Config({"color": "Foo", "x": "Baz", "geometry": "circle"}))
    )
story.add_slide(slide2)

# note: in Streamlit if you want to use the `play` method,
# you need to set the width and height in pixels
story.set_size(width="800px", height="480px")

# you can export the Story into a html file
story.export_to_html(filename="mystory.html")

# or you can get the html Story as a string
html = story.to_html()
print(html)

# you can display the Story with the `play` method
story.play()
