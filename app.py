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
##### A Front-end Developer from [Vietnam](https://en.wikipedia.org/wiki/Vietnam) 🇻🇳  
''')
txt('## Summary')
# col.markdown('## Summary')
_, col, _ = st.columns((1,3,1))
col.success('''
💫  About Me: I'm Phan Quang Minh Long. I was born in 2001 and I'm a final year Management Information System student at [Faculty of Information Systems](https://www.facebook.com/khoahttt.uel) of the University of Economics & Law at VNU HCMC.
Throughout my university years, I've participated in various competitions, activities, and was a collaborator of numerous academic organizations in school in order to gain more knowledge and experience for my future career.

- 🌱 I’m currently learning ReactJS 😄
- 💬 Ask me about everything 🤔
- 📫 Contact me via email [here](mailto:longpqm19406c@st.uel.edu.vn)
- ⚡ I love to watch 🇯🇵 anime:  `Dragon Ball`,  `One Piece`,  `Spy X Family`, ...
''')

#####################
txt('''
## Contact Infomation
''')
txt2('Phone', '🇻🇳 [(+84) 852 197 589](tel:+84852197589)')
txt2('Zalo', '🇻🇳 [(+84) 852 197 589](https://zalo.me/0852197589)')
txt2('Address', '🇻🇳 [District 10, Ho Chi Minh City, Vietnam](https://www.google.com/maps/place/District+10,+Ho+Chi+Minh+City/@10.7727179,106.669428,15z/data=!3m1!4b1!4m5!3m4!1s0x31752edc7bd9fd65:0x7500396cc3a60d04!8m2!3d10.7745965!4d106.6679542)')
txt2('Email', '[longpqm19406c@st.uel.edu.vn](mailto:longpqm19406c@st.uel.edu.vn)')
txt2('LinkedIn', '[phanquangminhlong](https://www.linkedin.com/in/phanquangminhlong)')
txt2('GitHub', '[longphanquangminh](https://github.com/longphanquangminh)')
txt2('Leetcode', '[longphanquangminh](https://leetcode.com/longphanquangminh)')
txt2('Facebook', '[pqmlong265](https://www.facebook.com/pqmlong265)')
txt2('Instagram', '[minhlong909](https://www.instagram.com/minhlong909)')
txt2('Discord', '[minhlong2605#4963](https://discord.com/channels/@me/995346151031197707)')

#####################
txt('## Education')
# col.markdown('## Education')
txt1('**Senior Student**,  *[VNUHCM](https://en.wikipedia.org/wiki/Vietnam_National_University,_Ho_Chi_Minh_City)-[University of Economics and Law](https://en.wikipedia.org/wiki/University_of_Economics_and_Law)*, Vietnam',
'`08/2019 - present`')
txt('''
- Management Information System
- Current GPA: `7.5 / 10`
- Scholarship for High performance student `05/2021`
- Student with 5 Merits - Faculty Level `11/2021`
- `Certificate of Merit` for completing `Student Scientific Research Project` in academic year `2021-2022`. Decision No.: `500/QĐ-ĐHKTL`, dated `April 20, 2022` of `Rector` of `UEL`.
''')

txt1('**AI Developer Course**,  *[ISC Quang Trung](https://www.iscquangtrung.edu.vn)*, Vietnam',
'`11/2021 - 03/2022`')
txt('''
- Final Project: [Beverage Recognition](https://github.com/longphanquangminh/streamlit-beverage-recognition)
''')

txt1('**Business Analysis & Product Design**,  *[Business Analyst Training Center](https://www.bacs.vn)*, Vietnam',
'`08/2021 - 10/2022`')
txt('''
- Final Project: [Online Reservation System](https://www.figma.com/file/DGwoWZ1yyR8WQ77YrrTyx6/Online-Reservation-System?node-id=0%3A1)
''')

#####################
txt('''
## Work Experience
''')
txt1('**Organizer, content creator & designer of Media Department**, *[ITB Club](https://www.facebook.com/itbclub.uel)*, Vietnam',
'`09/2019 - 12/2020`')
txt1('**Organizer**, *[Ecommerce Unitour UEL](https://www.facebook.com/EcommerceUnitour)*, Vietnam',
'`12/2019`')
txt1('**Connector & part-time designer**, *[CCA UEL](https://www.facebook.com/cca.uel.edu.vn)*, Vietnam',
'`01/2020 - 11/2020`')
txt1('**Internship Trainee**, *[ISC Quang Trung](https://www.iscquangtrung.edu.vn)*, Vietnam',
'`11/2021 - 03/2022`')
txt1('**Academic Management Collaborator**, *[iGen Group](https://igen.world)*, Vietnam',
'`05/2022 - 07/2022`')
txt1('**Apprenticeship**, *[CrossTech](https://crosstechhub.com)*, Vietnam',
'`06/2022 - 07/2022`')
txt1('**Bootcamp Participant**, *[KMS Technology, Inc.](https://www.linkedin.com/company/kms-technology)*, Vietnam',
'`07/2022`')

#####################
txt('''
## My Finished Projects
''')
txt4('Reservation System (BA, UI/UX)','In order to comply with epidemic prevention regulations, help customers have a better experience and the restaurant can manage the number of customers more easily, our team has proposed and designed an online reservation system. Build responsive web-app system for user and admin roles. Specially, the mobile interface with CRO buttons provide a better experience for customers.','https://www.figma.com/file/DGwoWZ1yyR8WQ77YrrTyx6/Online-Reservation-System?node-id=0%3A1')
txt4('Beverage Recognition', 'The project is used to identify beverage brands in Vietnam. Based on data about photos of beverage products that the team collects themselves on [Kaggle](https://www.kaggle.com) and [Google](https://www.google.com), our team has built a model that can recognize logos of beverage brands in Vietnam using `SSD Object Detection` and `CNN`.', 'https://github.com/longphanquangminh/streamlit-beverage-recognition')
txt4('Unity AR UEL App','Build augmented reality applications by Unity for new college students to discover school information vividly (Faculty-level SCIENCE RESEARCH).','CH Play: https://play.google.com/store/apps/details?id=com.DefaultCompany.MyProjectCameraDemohihi')
txt4('MarPet Website','Our learning team has implemented a website that sells pet food and accessories, specifically dogs and cats, to provide online pet products and services for the spiritual well-being of people. Using `Angular` framework, `Bootstrap`, `MongoDB`, `Node.js` & `Express.js` to build this entire website system. Detail: Designing and deciding on the visual layout of a website; Changing the code, software or graphics of existing websites; Researching new technologies, software packages; CRUD products, administrators and users; Testing the website.','https://github.com/Pet-Shop-Dev')
txt4('KMS ImageFinder','Our team won the 1st prize (Technical Challenge Winner) of KMS Fresher Bootcamp 2022 program with the topic "Events: Pictures Finder": Build a website/tool to make it easier for marathon runners to collect their photos on `Google Drive` and `other sites` (in the future) based on their facial traits. My role: Front-end developer (`Angular`), logo design, support work related to using `API` on the interface.','https://fe-oql27hnv2q-as.a.run.app/home')


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
txt3('Database', '`Microsoft SQL Server`, `Microsoft Excel`')
txt3('Tool', '`Microsoft SQL Server`, `Postman`')
txt3('Design (Basic)', '`Figma`, `Adobe Photoshop`, `Adobe Illustrator`')
txt3('Version Control', '`Git`')
txt3('Office (Basic)', '`Microsoft Word`, `Microsoft Excel`, `Microsoft Powerpoint`')
txt3('Manual Testing','')

#####################
txt('''
## Highlighted Licenses & Certifications
''')
txt4('02/2020','2020 [Volunteer spring campaign](https://www.facebook.com/xuantinhnguyen.uel) – FIS UEL','')


#####################
txt('''
## Volunteering
''')
txt4('02/2020','2020 [Volunteer spring campaign](https://www.facebook.com/xuantinhnguyen.uel) – FIS UEL','')
txt4('03/2020','2020 [Earth Hour Campaign](https://www.facebook.com/giotraidatvn) Volunteer (Online)','https://drive.google.com/file/d/1Jnfg8SidPK-xSjTsDyju4Q7FZyrh7cy6/view?usp=sharing')
txt4('07/2020','2020 VIETNAM MAPPING EVENT BY [REDBULL](https://www.facebook.com/RedBullVN) X [HCM-SAC](https://www.facebook.com/hotrohssv) ([ASIAN RECORD](https://worldkings.org/news/asia-records-institute/worldkings-worldkings-news-asia-records-institute-asri-vietkings-red-bull-vietnam-achieved-asian-record-in-the-honor-of-positive-day-july-11-2020)) POSITIVE DAY','https://drive.google.com/file/d/1bwziixVCNJ_ZdnYisaAhVrLYXUIqzMsR/view?usp=sharing')
txt4('11/2020 - 12/2020','2020 [VNU Will Run](https://www.facebook.com/VNUWILLRun) Foundation','https://drive.google.com/file/d/1otQjq1TGZow889OSjplYBylpPBjhUfej/view?usp=sharing')
txt4('12/2020','2020 [VUG](https://www.facebook.com/VUG.vn) Running','https://drive.google.com/file/d/1z5GMc14W8vrSYAX6p4hL7vLnSD1zNC9i/view?usp=sharing')
txt4('03/2022','2022 Earth Hour Campaign Volunteer (Online)','https://drive.google.com/file/d/1oH5yFWcaUVLp83wxX6erCpg_YchFANcW/view?usp=sharing')
txt4('07/2022','2022 [National university entrance exam Support Campaign](https://www.facebook.com/tsmt.tphcm)','')
