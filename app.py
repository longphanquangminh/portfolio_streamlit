import streamlit as st
from PIL import Image

def txt(a):  # 1 column - paragraph
    _, col, _ = st.columns((1,3,1))
    with col:
        st.markdown(a)

def txt1(a, b):  # 2 columns with offset to the left (2:1)
  _, col1, col2, _ = st.columns([1,2,1,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):  # 2 columns with offset to the right (1:2)
  _, col1, col2, _ = st.columns([1,1,2,1])
  with col1:
    st.markdown(f'`{a}`')  # highlight text
  with col2:
    st.markdown(b)

def txt3(a, b):  # 2 columns with offset to the right (1:2)
  _, col1, col2, _ = st.columns([1,1,2,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c): # 3 columns
  _, col1, col2, _, col3, _ = st.columns([1,0.65,1.5, 0.1,0.75,1])
  with col1:
    st.markdown(f'`{a}`')  # highlight text
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

st.set_page_config(page_title='Phan Quang Minh Long - Portfolio',page_icon="./image/logoML.png", layout="wide")

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

image = Image.open('./image/MinhLong-modified.png')
_, img_column, _ = st.columns((2,1,2))
img_column.image(image, use_column_width  = True)

st.write('''
# PHAN QUANG MINH LONG
##### A future Front-end Developer from [Vietnam](https://en.wikipedia.org/wiki/Vietnam) 🇻🇳  
''')
txt('## Summary')
# col.markdown('## Summary')
_, col, _ = st.columns((1,3,1))
col.success('''
💫  About Me: I'm Phan Quang Minh Long. I was born in 2001 and I'm a final year Management Information System student at the Faculty of Information Systems of the University of Economics & Law at VNU HCMC.
Throughout my university years, I've participated in various competitions, activities, and was a collaborator of numerous academic organizations in school in order to gain more knowledge and experience for my future career.

- 🌱 I’m currently learning ReactJS 😄
- 💬 Ask me about everything 🤔
- 📫 Contact me via email [here](mailto:longpqm19406c@st.uel.edu.vn)
- ⚡ I love to watch Japanese anime.
''')

#####################
txt('''
## Contact Infomation
''')
txt2('Phone', '[0852197589](tel:+84852197589)')
txt2('Zalo', '[0852197589](https://zalo.me/0852197589)')
txt2('Address', '[District 10, Ho Chi Minh City, Vietnam](https://www.google.com/maps/place/District+10,+Ho+Chi+Minh+City/@10.7727179,106.669428,15z/data=!3m1!4b1!4m5!3m4!1s0x31752edc7bd9fd65:0x7500396cc3a60d04!8m2!3d10.7745965!4d106.6679542)')
txt2('Email', '[longpqm19406c@st.uel.edu.vn](mailto:longpqm19406c@st.uel.edu.vn)')
txt2('LinkedIn', '[phanquangminhlong](https://www.linkedin.com/in/phanquangminhlong)')
txt2('GitHub', '[longphanquangminh](https://github.com/longphanquangminh)')
txt2('Leetcode', '[longphanquangminh](https://leetcode.com/longphanquangminh)')
txt2('Facebook', '[pqmlong265](https://www.facebook.com/pqmlong265)')
txt2('Instagram', '[minhlong909](https://www.instagram.com/minhlong909)')

#####################
txt('## Education')
# col.markdown('## Education')
txt1('**Final Year Student**,  *[VNUHCM-University of Economics and Law](https://en.wikipedia.org/wiki/University_of_Economics_and_Law)*, Vietnam',
'08/2019 - Present')
txt('''
- Management Information System
- Current GPA: `7.5 / 10`
- Scholarship for High performance student - 05/2021
- Student with 5 Merits - Faculty Level - 11/2021
''')

txt1('**Business Analysis & Product Design**,  *[Business Analyst Training Center](https://www.bacs.vn)*, Vietnam',
'08/2021 - 10/2022')
txt('''
- Final Project: [Online Reservation System](https://www.figma.com/file/DGwoWZ1yyR8WQ77YrrTyx6/Online-Reservation-System?node-id=0%3A1)
''')

txt1('**AI Developer Course**,  *[ISC Quang Trung](https://www.iscquangtrung.edu.vn)*, Vietnam',
'11/2021 - 03/2022')
txt('''
- Final Project: [Beverage Recognition](https://github.com/longphanquangminh/streamlit-beverage-recognition)
''')

#####################
txt('''
## Work Experience
''')
txt1('**Organizer, content creator & designer of Media Department**, *[ITB Club](https://www.facebook.com/itbclub.uel)*, Vietnam',
'09/2019 - 12/2020')
txt1('**Internship Trainee**, *[ISC Quang Trung](https://www.iscquangtrung.edu.vn)*, Vietnam',
'11/2021 - 03/2022')
txt1('**Academic Management Collaborator**, *[iGen Group](https://igen.world)*, Vietnam',
'05/2022 - 07/2022')
txt1('**Apprenticeship**, *[CrossTech](https://crosstechhub.com)*, Vietnam',
'06/2022 - 07/2022')
txt1('**Bootcamp''s Participant**, *[KMS Technology, Inc.](https://www.linkedin.com/company/kms-technology)*, Vietnam',
'07/2022')

#####################
txt('''
## Project
''')
txt4('Vehicle Detection', 'The website is used to identify vehicles, assess and visualize traffic conditions in Ho Chi Minh City, Vietnam. Using `SSD Object Detection` and real camera data from Ho Chi Minh', 'https://share.streamlit.io/lenguyengiabao/vehicle_detection/app.py')


#####################
txt('''
## Skills
''')
txt3('Programming', '`Basic C# (Unity AR)`')
txt3('Python Library (Basic)', '`numpy`, `pandas`, `matplotlib`, ...')
# txt3('Web development', '`Angular`, `HTML`, `CSS`, `Javascript`, `Typescript`')
txt3('Back-end', '`Javascript`, `Node.JS`, `Express.JS`, `MongoDB`')
txt3('Front-end', '`HTML`, `CSS`, `Javascript`, `Typescript`')
txt3('Framework', '`Angular`, `Bootstrap`')
txt3('Database', '`SQL Server`')
txt3('Tool', '`SQL Server`, `Postman`')
txt3('Design (Basic)', '`Adobe Photoshop`, `Adobe Illustrator`')
txt3('Version Control', '`Git`')