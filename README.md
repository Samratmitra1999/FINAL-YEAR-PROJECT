<div align="center">

  <img src="static/logo.png" alt="logo" width="200" height="auto" />
  
  <h1>CAR NUMBER PLATE RECOGNITION</h1>
  
  <p>
    Car Number Plate Detection System Using Flask and OpenCV.
    <br />
    A Website for Car Number Plate Recognition and Rto information.
  </p>
  

<br />

<!-- Table of Contents -->
# :notebook_with_decorative_cover: Table of Contents

- [About the Project](#star2-about-the-project)
  * [Screenshots](#camera-screenshots)
  * [Tech Stack](#space_invader-tech-stack)
  * [Features](#dart-features)
- [Getting Started](#toolbox-getting-started)
  * [Prerequisites](#bangbang-prerequisites)
  * [Installation](#gear-installation)
  * [Run Locally](#running-run-locally)
  * [Deployment](#triangular_flag_on_post-deployment)
- [Usage](#eyes-usage)
- [Roadmap](#compass-roadmap)
- [Flow Of The Task](#grey_question-faq)
- [License](#warning-license)
- [Contact](#handshake-contact)
- [Acknowledgements](#gem-acknowledgements)

  

<!-- About the Project -->
## :star2: About the Project


<!-- Screenshots -->
### :camera: Screenshots

<div align="center"> 
  <img src="https://placehold.co/600x400?text=Your+Screenshot+here" alt="screenshot" />
</div>


<!-- TechStack -->
### :space_invader: Tech Stack

<details>
  <summary>Client</summary>
  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
    <li><a href="https://html.com/"></a>HTML</li>
    <li><a href="https://www.free-css.com/">CSS</a></li>
    <li><a href="https://www.javascript.com/">Javascript</a></li>
    <li><a href="https://getbootstrap.com/">Bootstrap</a></li>
  </ul>
</details>


<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://firebase.google.com/">Google Firebase</a></li>
  </ul>
</details>

<!-- Features -->
### :dart: Features

- 👉Create a model that will detect a car in an image and recognize characters on number plate of the car .
- 👉Secondly , it will use the characters and fetch the owners information using RTO API’s .
- 👉Create a Web portal where all this information will be displayed (using Html, Css, and Javascript).

<!-- Getting Started -->
## 	:toolbox: Getting Started

<!-- Prerequisites -->
### :bangbang: Prerequisites

<!-- Installation -->
### :gear: Installation

Install my-project


<!-- Run Locally -->
### :running: Run Locally
```bash
  open Anaconda
  cd myproject
```
Clone the project

```bash
  git clone https://github.com/Samratmitra1999/FINAL-YEAR-PROJECT
```


Install dependencies

```bash
  pip install requirements.txt
```



<!-- Deployment -->
### :triangular_flag_on_post: Deployment

To deploy this project run

```bash
  python main.py
```


<!-- Usage -->
## :eyes: Usage

This was a Final Year Project assigned to us by Biplab Mahapatra Sir.

In this task, we have created one Web UI in which you have to select and upload one of image of your car’s number plate and then our webpage will display all the details about that car like owner name, date of registration, insurance, etc. For doing this task we have used following tools and technologies:-

i) Python (Flask framework, OpenCV module, absl, re, json, etc)

ii) Web Technologies (HTML, CSS, JavaScript)

iii) PaddleOCR

iv) Haarcascade Russian number plate model for number plate detection.

v) RTO Car Registration API
  
vi) Google Firebase(To store and retrive rto information of vehicles in database)



```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
```

<!-- Roadmap -->
## :compass: Roadmap

* [1] First the code of flask will get run(app.py)
* [2] When user upload the image it get saved in S3 bucket.
* [3] When user upload the image it get saved in inputs folder.
* [4] The npr.py runs in backend and the number plate gets cropped and the ocr extracts the number plate in text and displays the result.
* [5] The result gets stored in json file and it is retrived to display in search history webpage.
* [6] The user can get details of the searched image from databse created in firebase in Rto information webpage.
* [2] The user can also add details of the car to database.



<!-- Flow Of The Task -->
## :grey_question: Flow Of The Task

- Question 1

  + Answer 1

- Question 2

  + Answer 2


<!-- License -->
## :warning: License

Distributed under the no License. See LICENSE.txt for more information.


<!-- Contact -->
## :handshake: Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - samratmitra1999@gmail.com

Project Link: (https://github.com/Samratmitra1999/FINAL-YEAR-PROJECT)


<!-- Acknowledgments -->
## :gem: Acknowledgements

Use this section to mention useful resources and libraries that you have used in your projects.

 - [Shields.io](https://shields.io/)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [Emoji Cheat Sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md#travel--places)
 - [Readme Template](https://github.com/othneildrew/Best-README-Template)
