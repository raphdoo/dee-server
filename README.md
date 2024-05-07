# A Voice Assistance server-side web app

Developed using Resuscitation Council; UK Guidelines

### Technologies

<div align="center">

  [![FastAPI](https://img.shields.io/badge/FastAPI-%2300BFA5.svg?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
  [![OpenAI](https://img.shields.io/badge/OpenAI-%23007ACC.svg?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
  
  
</div>

<div align="center">

  <a href="">![Git](https://img.shields.io/badge/git-%234ea94b.svg?style=for-the-badge&logo=git&logoColor=white)</a>
  [![Resuscitation Council; UK](https://img.shields.io/badge/Resuscitation_Council_UK-%230085AA.svg?style=for-the-badge&logo=&logoColor=white)](https://www.resus.org.uk/)
  
</div>



### Installation
 
First, you need to clone the repository into your local machine
```javascript
$ git clone https://github.com/raphdoo/dee-server.git
```

Then, you need to install the dependencies.
```javascript
$ python -m pip install -r .\setup.txt
```

Then, you need to create a virtual environment.
```javascript
$ touch .env
```

Then, you need to write your "OPEN_AI" key to .env file
```javascript
"OPEN_AI" = "YOURSECRETKEY"
```

Finally, you need to run the server.
```java
$ python -m uvicorn main:app --reload
```
### Base URL : 
