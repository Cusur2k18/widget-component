# Widget

![info-widget](./docs/demo.jpeg)

This is the repo for the info-widget app that is displaying on the cusur's web page.

## Context

On the [Cusur Website](http://www.cusur.udg.mx/) they want to display a component that will render the air quality each day.

The component should get the information updated from a database that will need to be administrable from another app.

This repo holds this two apps.

### Widget component

* the file `widget.php` has all the code that renders the component (via ajax)

* it exports a function that recieves the dom element where the component should be mounted.

### Widget admin

* The `admin/` folders holds the app that works as the `cms` for the component.


## Deploy

The deploy for the `widget` app is pretty straigforward, just put the code that's inside the `widget.php` file within the Drupal code editor.


## Database structure

**Models**

| Name     |                          Fields                         |
|----------|---------------------------------------------------------|
| Event    | `name`, `is_active`, `level`, `created_at`, `updated_at`|
| User     | `django-admin-user`                                     |
| Measure  | `name`, `value`, `event_id`, `created_at`, `updated_at` |


## Usage

The `admin` system will serve the needed views so the admin is able to manage the `event` and the `measurements` as needed.

There's an endpoint from the `admin` that return you the active event and the latest measurment for that event:

```
GET /api/active_info
```

response object:

```
{
  statusCode: int,
  data: Event
  error: String | null
}
```