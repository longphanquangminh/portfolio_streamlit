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
##### [See My CV](https://drive.google.com/file/d/1t9LyC15nODKYXYYqHkbzFa3JVoMjP72_/view)
##### [See My Website](https://longphanquangminh.github.io/Long-Phan-Resume)
''')
txt('## Summary')
# col.markdown('## Summary')
_, col, _ = st.columns((1,3,1))
col.success('''
💫  About Me: I'm Phan Quang Minh Long. I was born in 2001 and I'm a final year Management Information System student at Faculty of Information Systems of the University of Economics & Law at VNU HCMC.
Throughout my university years, I've participated in various competitions, activities, and was a collaborator of numerous academic organizations in school in order to gain more knowledge and experience for my future career.

- 🌱 I’m currently learning ReactJS 😄
- 💬 Ask me about everything 🤔
- 📫 Contact me via email: [longpqm19406c@st.uel.edu.vn](mailto:longpqm19406c@st.uel.edu.vn?subject=HelloMinhLong).
- 📚 My manga app: [HERE](https://mangapqml.glideapp.io)
- 🇯🇵 I love anime:  `Dragon Ball`,  `One Piece`,  `Spy X Family`, ...
''')

#####################
txt('''
## Contact Infomation
''')
# txt2('Phone', '🇻🇳 [(+84) 852 197 589](tel:+84852197589)')
txt2('Zalo', '🇻🇳 [(+84) 852 197 589](https://zalo.me/0852197589)')
txt2('Address', '🇻🇳 [District 10, Ho Chi Minh City, Vietnam](https://www.google.com/maps/place/District+10,+Ho+Chi+Minh+City/@10.7727179,106.669428,15z/data=!3m1!4b1!4m5!3m4!1s0x31752edc7bd9fd65:0x7500396cc3a60d04!8m2!3d10.7745965!4d106.6679542)')
txt2('Email', '[longpqm19406c@st.uel.edu.vn](mailto:longpqm19406c@st.uel.edu.vn?subject=HelloMinhLong)')
txt2('LinkedIn', '[phanquangminhlong](https://www.linkedin.com/in/phanquangminhlong)')
txt2('GitHub', '[longphanquangminh](https://github.com/longphanquangminh)')
txt2('GitLab', '[longpqm19406c](https://gitlab.com/longpqm19406c)')
txt2('Google Developer', '[minhlong2605](https://developers.google.com/profile/u/minhlong2605)')
txt2('CH Play', '[Phan Quang Minh Long](https://play.google.com/store/apps/developer?id=Phan+Quang+Minh+Long)')
txt2('Leetcode', '[longphanquangminh](https://leetcode.com/longphanquangminh)')
txt2('Facebook', '[pqmlong265](https://www.facebook.com/pqmlong265)')
txt2('Instagram', '[minhlong909](https://www.instagram.com/minhlong909)')
txt2('Twitter', '[pqmlong](https://twitter.com/pqmlong)')
txt2('Discord', '[minhlong2605#4963](https://discord.com/channels/@me/995346151031197707)')
txt2('Codecademy', '[longPhanQuangMinh9567554876](https://www.codecademy.com/profiles/longPhanQuangMinh9567554876)')
txt2('Stack Overflow', '[17742483](https://stackoverflow.com/users/17742483)')
txt2('Kaggle', '[longphanquangminh](https://www.kaggle.com/longphanquangminh)')
txt2('Behance', '[longphanquangminh](https://www.behance.net/longphanquangminh)')
txt2('Pinterest', '[minhlong2605](https://www.pinterest.com/minhlong2605)')
txt2('Reddit', '[minhlong26052001](https://www.reddit.com/user/minhlong26052001)')
txt2('Youtube', '[Phan Quang Minh Long](https://www.youtube.com/channel/UC5oOhh4McMGJVAEDvRvDYGA)')
txt2('LmssPlus', '[G0D OF JUNGLE](https://lmssplus.com/profile/G0D%20OF%20JUNGLE)')
txt2('Website', '[Click to access](https://longphanquangminh.github.io/Long-Phan-Resume)')

#####################
txt('## Education')
# col.markdown('## Education')
txt1('**Senior Student**,  *[VNUHCM](https://en.wikipedia.org/wiki/Vietnam_National_University,_Ho_Chi_Minh_City)-[University of Economics and Law (UEL)](https://en.wikipedia.org/wiki/University_of_Economics_and_Law)*, Vietnam',
'`08/2019 - present`')
txt('''
- [Faculty of Information Systems](https://www.facebook.com/khoahttt.uel)
- Specialization: [Management Information System](https://is.uel.edu.vn/Resources/Docs/SubDomain/is/academy/Course-description-bachelor-of-management-information-system.pdf)
- Current Grade Point Average (GPA): `7.5 / 10`. Scores of specialized subjects: 
    - PROGRAMMING TECHNIQUES (`C#`) (3 credits): `7.5 / 10` (B+)
    - DIGITAL INFRASTRUCTURE FOR INFORMATION SYSTEM (3 credits): `8.0 / 10` (A)
    - APPLIED INFORMATICS (`MICROSOFT OFFICE`) (2 credits): `9.5 / 10` (A+)
    - INTRODUCTION TO DATABASE (3 credits): `9.0 / 10` (A+)
    - E-COMMERCE (3 credits): `8.5 / 10` (A)
    - SAFETY AND SECURITY INFORMATION SYSTEM (3 credits): `9.0 / 10` (A+)
    - MANAGEMENT INFORMATION SYSTEMS (`ERP`, `SCM`, `CRM`, ...) (3 credits): `9.5 / 10` (A+)
    - BUSINESS INFORMATION SYSTEM ([`SAP`](https://en.wikipedia.org/wiki/SAP)) (2 credits): `10 / 10` (A+)
    - ANALYSIS AND DESIGN OF MANAGEMENT INFORMATION SYSTEM (`BA`, `UI/UX`) (3 credits): `8.5 / 10` (A)
    - INTEGRATED BUSINESS PROCESSES WITH `ERP` SYSTEMS ([`SAP`](https://en.wikipedia.org/wiki/SAP)) (3 credits): `8.5 / 10` (A)
    - BUSINESS WEBSITE DEVELOPMENT (3 credits): `7.5 / 10` (B+)
    - DATABASE MANAGEMENT SYSTEM (3 credits): `9.0 / 10` (A+)
    - ADVANCED WEB DEVELOPMENT (3 credits): `7.5 / 10` (B+)
    - INFORMATION SYSTEM PROJECT MANAGEMENT (3 credits): `8.0 / 10` (A)
    - BUSINESS INTELLIGENCE AND DECISION SUPPORT SYSTEM (`BI` and `DSS`) (3 credits): `9.5 / 10` (A+)
- Scholarship for High performance student `05/2021`
- [Student with 5 Merits - Faculty Level](https://www.facebook.com/LCH.HTTT.UEL/photos/pcb.4923846807625977/4923844107626247) `11/2021`
- `Certificate of Merit` for completing `Student Scientific Research Project` in academic year `2021-2022`. Decision No.: `500/QĐ-ĐHKTL`, dated `April 20, 2022` of `Rector` of `UEL`.
''')

txt1('**AI Developer**,  *[ISC Quang Trung](https://www.iscquangtrung.edu.vn)*, Vietnam',
'`11/2021 - 03/2022`')
txt('''
- Final Project: [Beverage Recognition](https://github.com/longphanquangminh/streamlit-beverage-recognition)
- Our Presentation: [Youtube](https://www.youtube.com/watch?v=E11CZIF5GmI)
''')

txt1('**Business Analysis & Product Design**,  *[Business Analyst Training Center](https://www.bacs.vn)*, Vietnam',
'`08/2021 - 10/2022`')
txt('''
- Final Project: [Online Reservation System](https://www.figma.com/file/DGwoWZ1yyR8WQ77YrrTyx6/Online-Reservation-System?node-id=0%3A1)
- Certification: [Document](https://drive.google.com/file/d/1Gzsi4fSwXCHjklHNhpO0L-fr52UNX9Yk/view)
''')

txt1('**Full-stack Web Developer**,  *[R2S Academy](https://www.facebook.com/r2s.tuyendung)*, Vietnam',
'`07/2021`')
txt('''
- Final Project: [ABC Mobile Store](https://gitlab.com/abc334/abc-ms_abc-mobile-store)
- My role: Front-end Developer
- Our group presentation in the final part of the video: [Youtube](https://www.youtube.com/watch?v=ogapwDYKUOk)
- Powerpoint slide: [Document](https://drive.google.com/file/d/1KKqHWTMARa-nsxInlV14TuHig0hXehrN/view?usp=sharing)
- Certification: [Document](https://drive.google.com/file/d/1CntI2J04ecUAivct7m-ju-3-oXrsKio3/view?usp=sharing)
''')

txt1('**High school**,  *[Quang Trung Nguyen Hue Secondary and High School](https://qtnh.edu.vn)*, Vietnam',
'`08/2016 - 06/2019`')
txt('''
- 2-year `valedictorian`, `class vice discipline` and `class vice academic` (Grade 10 & 11).
- `Executive Committee` - Communist Youth Union of Quang Trung Nguyen Hue Secondary and High School.
- `Typical students` follow Uncle Ho's words on the occasion of the 12th traditional festival on January 9, 2018. Certification: [Document](https://drive.google.com/file/d/1Djt156NbAjUkGjS1xu7235gBxqYFcfIy/view?usp=sharing)
- `First-ever` ex-student to study at [VNUHCM-UEL](https://en.wikipedia.org/wiki/University_of_Economics_and_Law).
''')

#####################
txt('''
## Work Experience
''')
txt1('**Interim executive committee member of Youth Union class**, *K19406C UEL*',
'`08/2019 - 10/2019`')
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
## My Featured Projects
''')
txt4('ABC Mobile Store','Our team has built a website selling electronic devices such as mobile phones, tablets for ABC Mobile Store. Using `Angular` framework, `Bootstrap`, `Eclipse`, `MySQL`, ... to build this entire website system. My role: Front-end Developer.','https://gitlab.com/abc334/abc-ms_abc-mobile-store')
txt4('Reservation System (BA, UI/UX)','In order to comply with epidemic prevention regulations, help customers have a better experience and the restaurant can manage the number of customers more easily, our team has proposed and designed an online reservation system. Build responsive web-app system for user and admin roles. Specially, the mobile interface with CRO buttons provide a better experience for customers.','https://www.figma.com/file/DGwoWZ1yyR8WQ77YrrTyx6/Online-Reservation-System?node-id=0%3A1')
txt4('Beverage Recognition', 'The project is used to identify beverage brands in Vietnam. Based on data about photos of beverage products that the team collects themselves on [Kaggle](https://www.kaggle.com), [Google](https://www.google.com) and [VnExpress](https://vnexpress.net/), our team has built a model that can recognize logos of beverage brands in Vietnam using `SSD Object Detection` and `CNN`. Our presentation: [Youtube](https://www.youtube.com/watch?v=E11CZIF5GmI)', 'https://github.com/longphanquangminh/streamlit-beverage-recognition')
txt4('Unity AR UEL App','Build augmented reality applications by Unity for new college students to discover school information vividly (Faculty-level SCIENCE RESEARCH).','CH Play: https://play.google.com/store/apps/details?id=com.DefaultCompany.MyProjectCameraDemohihi')
txt4('MarPet Website','Our learning team has implemented a website that sells pet food and accessories, specifically dogs and cats, to provide online pet products and services for the spiritual well-being of people. Using `Angular` framework, `Bootstrap`, `MongoDB`, `Node.js` & `Express.js` to build this entire website system. Detail: Designing and deciding on the visual layout of a website; Changing the code, software or graphics of existing websites; Researching new technologies, software packages; CRUD products, administrators and users; Testing the website.','https://github.com/Pet-Shop-Dev')
txt4('BI Solution for HR Dept. in Adventure Works Cycles','Our learning team has found out, studied more about [Adventure Works Cycles](https://www.linkedin.com/pulse/adventure-work-cycles-jayant-velichety), especially the HR department, and used technology software such as `SQL Server` (`ETL`, `SSIS`, `SSAS`) and `Power BI` to serve project goals. Make raw data structured and analyzable, visualize them as dashboards for better and clearer reports, so that problems and advantages of employees, company can be discovered supporting more effective decision making.','https://drive.google.com/file/d/1_unqth-DUPpMG1mC-ED51Ye5j0EubE59/view?usp=sharing')
txt4('KMS ImageFinder','Our team won the `1st prize` (Technical Challenge Winner) of `KMS Fresher Bootcamp 2022 program` with the topic "Events: Pictures Finder": Build a website/tool to make it easier for marathon runners to collect their photos on `Google Drive` and `other sites` (in the future) based on their facial traits. My role: Front-end developer (`Angular`), logo design, support work related to using `API` on the interface.','https://fe-oql27hnv2q-as.a.run.app/home')


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
txt4('08/2019','[IELTS](https://en.wikipedia.org/wiki/International_English_Language_Testing_System) Academic 5.5 (Listening 5.5 Reading 5.5 Writing 6.0 Speaking 5.0)','[myuel.uel.edu.vn/Modules/UIS/images/chungchiNN/16_IELTS_K194060852.jpg](https://myuel.uel.edu.vn/Modules/UIS/images/chungchiNN/16_IELTS_K194060852.jpg)')
txt4('08/2021','[HackerRank](https://en.wikipedia.org/wiki/HackerRank) [SQL](https://en.wikipedia.org/wiki/SQL) (INTERMEDIATE)','[www.hackerrank.com/certificates/5c8725fc537b](https://www.hackerrank.com/certificates/5c8725fc537b)')
txt4('03/2022','[MOS WORD 2016](https://docs.microsoft.com/en-us/certifications/mos-word-2016) ([IIG Vietnam](https://iigvietnam.com/en))','https://drive.google.com/file/d/1B5P2I1EJ_YJWCGHgmL53J3URXifTgNNX/view')
txt4('04/2022','[Coursera](https://en.wikipedia.org/wiki/Coursera) FRONT-END WEB UI FRAMEWORKS AND TOOLS: [BOOTSTRAP](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework)) 4','https://coursera-certificate-images.s3.amazonaws.com/VPTQ5YLCBDMT')

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
