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

slide1 = Slide(
    Step(
        Config({"x": "Foo", "y": "Bar"}),
    )
)
story.add_slide(slide1)

slide2 = Slide(
    Step(
        Config({"color": "Foo", "x": "Baz", "geometry": "circle"}),
    )
)
story.add_slide(slide2)

story.play()
