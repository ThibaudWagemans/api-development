<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/tibogeeraerts/api-development">
    <img src="images/logo.png" alt="Logo" width="200" height="150">
  </a>

  <h3 align="center">Basisproject API development</h3>

  <p align="center">
    Gemaakt door Tibo Geeraerts
    <br />
    <a href="https://github.com/tibogeeraerts/api-development"><strong>Bekijk de bestanden »</strong></a>
    <br />
    <br />
    <a href="https://geeraertstibo-api.netlify.app/">Front-end website</a>
    ·
    <a href="https://api-development-service-tibogeeraerts.cloud.okteto.net/docs">API docs website</a>
  </p>
</div>



<!-- Inhoudstafel -->
<details>
  <summary>Inhoudstafel</summary>
  <ol>
    <li>
      <a href="#gebouwd-met-">Gebouwd met</a>
    </li>
    <li>
      <a href="#over-dit-project">Over dit project</a>
      <ul>
        <li>
          <a href="#front-end-api">Front-end API</a>
          <ul>
             <li><a href="#get-random-quote-front-end">Get random quote front-end</li>
             <li><a href="#get-last-quote-front-end">Get last quote front-end</li>
             <li><a href="#create-quote-front-end">Create quote front-end</li>
             <li><a href="#get-all-quotes-front-end">Get all quotes front-end</li>
          </ul>
        </li>
        <li>
          <a href="#back-end-api">Back-end API</a>
          <ul>
             <li><a href="#post-custom-quote-back-end">Post custom quote back-end</li>
             <li><a href="#get-all-quotes-back-end">Get all quotes back-end</li>
             <li><a href="#get-random-quote-back-end">Get random quote back-end</li>
             <li><a href="#get-last-quote-back-end">Get last quote back-end</li>
          </ul>
        </li>
      </ul>
    </li>
    <li>
      <a href="#postman-requests">Postman requests</a>
      <ul>
             <li><a href="#get-random-quote-postman">Get random quote Postman</li>
             <li><a href="#get-last-quote-postman">Get last quote Postman</li>
             <li><a href="#get-all-quotes-postman">Get all quotes postman</li>
             <li><a href="#post-custom-quote-postman">Post custom quote Postman</li>
          </ul>
    </li>
    <li><a href="#contactgegevens">Contactgegevens</a></li>
  </ol>
</details>


## Gebouwd met :

[![FastAPI][FastAPI.py]][FastAPI-url]
[![Python][Python.py]][Python-url]
[![Html][Html.html]][Html-url]
[![AlpineJS][Alpine.js]][Alpine-url]
[![Javascript][Bootstrap.css]][Bootstrap-url]


<!-- Over dit project -->
## Over dit project

Ik heb voor dit project gekozen om quotes uit de serie 'The Office' aan de gebruiker weer te geven. Ik heb gekozen voor deze serie omdat dit één van mijn favoriete series is, en er enrom veel grappige dingen in worden gezegd. De ideale serie om dus grappige quotes uit weer te geven.

### Front-end API

[![screenshot van API front-end][frontend-screenshot]][frontend-url]

Dit is de home pagina van de front-end API. De layout van de pagina is gemaakt met Bootstrap en de inhoud wordt dynamisch weergegeven op basis van AlpineJS. Er zijn 3 knoppen aanwezig op de pagina.

#### Get random quote front-end
![Get random quote knop front-end][getrandomquote-frontend]

Als de gebruiker op deze knop drukt, wordt er een willekeurige quote uit de database gekozen en weergegeven. Er kan oneindig veel op de knop gedrukt worden er zal meestal een nieuwe quote verschijnen. Deze database met quotes bevat voor het grootste deel quotes uit 'The Office' zelf, maar er kunnen ook zelf quotes aan de database worden toegevoegd via de back-end API.

#### Get last quote front-end

![Get last quote knop front-end][getlastquote-frontend]

De get last quote knop kan worden ingedrukt om de laatste quote uit de database weer te geven aan de gebruiker. Deze knop is vooral bedoeld om te kijken of een zelf ingegeven quote in de database staat, aangezien deze helemaal als laatst in de database staat. Deze knop zal zonder aanpassing van de database altijd dezelfde quote weergeven.

#### Create quote front-end

![Create quote knop front-end][postquote-frontend]

De gebruiker kan ook zelf een quote opslaan in de database met de 'Create quote' knop. Er kan in het tekstveld boven de knop zelf een quote worden ingetoetst, en in de database worden opgeslagen door op de knop te drukken. Nadat er op de knop is gedrukt komt er onder de knop ook een bevestiging van welke quote er is opgeslagen in de database.

#### Get all quotes front-end

![Get all quotes knop front-end][getallquotes-frontend]

Deze knop geeft de eerste 50 quotes in de database weer. Dit zijn normaal gezien al de quotes in de database aangezien er bij het opstarten maar 20 quotes in de database worden gezet. Via de back-end API kunnen er quotes worden toegevoegd, maar als er meer dan 50 quotes in totaal zijn worden deze niet meer weergegeven.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Back-end API

[![screenshot van API back-end][backend-screenshot]][backend-url]

Dit is de home pagina van de back-end API. Deze pagina is een interactieve API documentatie voorzien door Swagger UI. Deze interactieve pagina laat toe alle mogelijke eindpunten van de API aan te spreken op één plaats. Hier is te zien dat er 4 eindpunten zijn. 

#### Post custom quote back-end

![Post custom quote back-end][postquote-backend]

Via dit deel op de pagina kan er een nieuwe quote in de database worden gezet. Om dit te doen moet de gebruiker een POST request doen naar de API met in de body een "content" veld, waarachter een string moet komen, in JSON formaat. Wat de gebruiker in de string zet zal als quote gezien worden en zo in de database worden gezet. De API zal zelf de quote van een ID voorzien in de database.

#### Get all quotes back-end

![Get all quotes back-end][getallquotes-backend]

Via deze dropdown op de pagina kunnen alle quotes in de database worden opgevraagd. Er kan hier zelf worden gekozen bij welke quote er begonnen moet woren (skip), en hoeveel quotes er getoond moeten worden (limit). Als er vervolgens op de blauwe 'execute' knop wordt geklikt, dan zullen de quotes die binnen de geselecteerde parameters vallen weergegeven worden.

#### Get random quote back-end

![Get random quote back-end][getrandomquote-backend]

In dit deel van de docs pagina kan er een willekeurige quote worden gevraagd. Er zijn geen parameters nodig dus er moet enkel op de 'execute' knop worden gedrukt om een quote weer te geven. De quote zelf kan in de teruggestuurde body gelezen worden bij 'content'

#### Get last quote back-end

![Get last quote back-end][getlastquote-backend]

Ook bij deze request zijn er geen parameters nodig. Door hier op de 'execute' knop te drukken wordt de laatste quote uit de database opgevraagt. Als er dus een zelfgemaakte quote in de database is gezet, zal deze hier weergegeven worden.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Postman requests

Hier geef ik nog even een korte demonstratie hoe de 4 verschillende endpoints via Postman gebruikt kunnen worden.

### Get random quote Postman

![Get random quote with Postman][getrandom-postman]

### Get last quote Postman

![Get last quote with Postman][getlast-postman]

### Get all quotes Postman

![Get all quotes with Postman][getall-postman]

### Post custom quote Postman

![Post custom quote with Postman][postquote-postman]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contactgegevens

Tibo Geeraerts - [@geeraerts_tibo](https://twitter.com/geeraerts_tibo) - r0882113@student.thomasmore.be

Front-end link: [https://geeraertstibo-api.netlify.app/](https://geeraertstibo-api.netlify.app/)

Hosted API link: [https://api-development-service-tibogeeraerts.cloud.okteto.net/docs](https://api-development-service-tibogeeraerts.cloud.okteto.net/docs)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
[FastAPI.py]: https://img.shields.io/badge/-%F0%9F%97%B2%20FastAPI-019486?style=for-the-badge
[FastAPI-url]: https://fastapi.tiangolo.com/
[Python.py]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org/
[Html.html]: https://img.shields.io/badge/HTML-E54C21?style=for-the-badge&logo=html5&logoColor=white
[Html-url]: https://www.w3schools.com/html/
[Alpine.js]: https://img.shields.io/badge/Alpine.js-77C1D2?style=for-the-badge&logo=javascript&logoColor=white
[Alpine-url]: https://alpinejs.dev/
[Bootstrap.css]: https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com/

[frontend-screenshot]: images/front-end-screenshot.jpg
[frontend-url]: https://geeraertstibo-api.netlify.app/
[getrandomquote-frontend]: images/getrandomquote-front-end.jpg
[getlastquote-frontend]: images/getlastquote-front-end.jpg
[postquote-frontend]: images/postquote-front-end.jpg
[getallquotes-frontend]: images/getallquotes-front-end.jpg

[backend-screenshot]: images/back-end-screenshot.jpg
[backend-url]: https://api-development-service-tibogeeraerts.cloud.okteto.net/docs
[postquote-backend]: images/postquote-back-end.jpg
[getallquotes-backend]: images/getallquotes-back-end.jpg
[getrandomquote-backend]: images/getrandomquote-back-end.jpg
[getlastquote-backend]: images/getlastquote-back-end.jpg

[getrandom-postman]: images/postman-getrandom.jpg
[getlast-postman]: images/postman-getlast.jpg
[getall-postman]: images/postman-getall.jpg
[postquote-postman]: images/postman-postquote.jpg
