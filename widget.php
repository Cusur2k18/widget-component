<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  
  <!-- Bulma css -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.5/css/bulma.min.css">

  <title>Calidad del aire</title>

  <style>
    #ac-component {
      margin-top: 20%;
    }

    #ac-component * {
      font-weight: bold;
    }

    #ac-component .container {
      max-width: 500px;
    }

    .traffic-light {
      
    }

    .traffic-light:nth-child(even) {
      margin: 0 .2rem;
    }

    .traffic-light:after {
      background: black;
      bottom: 70px;
      content: "";
      display: block;
      height: 48px;
      left: 79px;
      position: relative;
      width: 5px;
    }

    .traffic-light:last-child:after {
      background: transparent;
    }

    .heading {
      padding: 2rem;
      font-size: 30px;
      background: #140E49;
      color: white;
      font-weight: bold;
    }

    .measurer {
      max-height: 130px;
    }

    .measurer-content {
      background: rgb(213,213,213);
      background: linear-gradient(90deg, rgba(213,213,213,1) 0%, rgba(255,255,255,1) 100%);
    }

    .measurer-content:after {
      background: black;
      bottom: 0;
      content: "";
      display: block;
      height: 3px;
      left: 0;
      position: relative;
      width: 100%;
    }

    .measurer-footer {
      position: relative;
      bottom: 40px;
      left: 50px;
      text-align: center;
      font-size: 11px;
      font-weight: bold;
    }

    .measurer-footer .uipc {
      position: relative;
      top: 1.2rem;
      left: .8rem;
      font-size: 20px;
    }

    .sides-border {
      border-left: 3px solid #c5c5c5;
      border-right: 3px solid #c5c5c5;
    }

    .information h5 {
      font-size: 12px;
      text-align: left;
      margin-bottom: 10px;
    }
  </style>
</head>
<body>

<!-- Air Checker Component -->
<div id="ac-component">
  <div class="container has-text-centered">
    
    <!-- Heading -->
    <div class="heading">
      <h2>Calidad del Aire</h2>
    </div>

    <div class="measurer-content">
      <!-- Info -->
      <div class="columns information">
        <div class="column">
          <h5>Valoracion:</h5>
          <p>Bueno</p>
        </div>
        <div class="column sides-border">
          <h5>Particulas Suspendidas:</h5>
          <p>PM 2.5 46mcg/mt^3</p>
        </div>
        <div class="column">
          <h5>Monoxido de carbono:</h5>
          <p>CO=0ppm</p>
        </div>
      </div>

      <!-- Measurer -->
      <div class="columns is-centered measurer">
        <div class="traffic-light">
          <img src="/static/green-light-strong.png" alt="Gray" width="80">
        </div>
        <div class="traffic-light">
          <img src="/static/green-light-soft.png" alt="Gray" width="80">
        </div>
        <div class="traffic-light">
          <img src="/static/orange-light-strong.png" alt="Gray" width="80">
        </div>
        <div class="traffic-light">
          <img src="/static/orange-light-soft.png" alt="Gray" width="80">
        </div>
        <div class="traffic-light">
          <img src="/static/red-light-strong.png" alt="Gray" width="80">
        </div>
        <div class="traffic-light">
          <img src="/static/gray-light.png" alt="Gray" width="80">
        </div>
      </div>

      <!-- Footer -->
      <div class="columns measurer-footer">
        <p>Medicion realizada el 27 de Mayo del 2019, a las 9:00 horas en el CUSur</p>
        <p class="uipc">UIPC</p>
      </div>
    </div>

  </div>
</div>
  
</body>
</html>