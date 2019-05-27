# Air Checker

![air checker](./docs/demo.jpeg)

This is the repo for the air checker app that is displaying on the cusur's web page.

## Context

On the [Cusur Website](http://www.cusur.udg.mx/) they want to display a component that will render the air quality each day.

The component should get the information updated from a database that will need to be administrable from another app.

This repo holds this two apps.

### Air Checker component (acc)

* the file `air_checker.php` has all the code that renders the component (via ajax)

* it exports a function that recieves the dom element where the component should be mounted.

### Air Checker admin (aca)

* The `admin/` folders holds the app that works as the `cms` for the component. 


## Deploy

The deploy for the `acc` app is pretty straigforward, just put the code that's inside the `air_checker.php` file within the Drupal code editor.