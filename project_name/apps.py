{% extends "admin/base_site.html" %}
{% load static %}

{% block extrastyle %}
<style>
  :root {
    --primary-color: #623486;
    --title-color: #fff;
    --secondary-color: #ff6600;
    --secondary-dark-color: #ff6600;
    --highlight-color: #D8CCE1;
  }

  ::selection {
    background: var(--highlight-color);
    opacity: 1
  }
  ::-moz-selection {
    background: var(--highlight-color);
    opacity:1
  }

  body, td, th, input, textarea, select, .form-row p, form .button {
    font-family:
          -apple-system,
          BlinkMacSystemFont,
          'Segoe UI',
          Helvetica,
          Arial,
          sans-serif,
          'Apple Color Emoji',
          'Segoe UI Emoji',
          'Segoe UI Symbol';
  }
  #header {
    background: var(--primary-color);
    color: var(--title-color);
  }
  #branding h1, #branding h1 a:link, #branding h1 a:visited {
    color: var(--title-color);
    font-weight: bold;
  }
  #header a:link, #header a:visited {
    color: var(--title-color);
  }
  .login #header h1 a {
    color: var(--title-color) !important;
  }
  #user-tools a:focus, #user-tools a:hover {
    border-bottom-color: var(--secondary-dark-color);
    color: var(--secondary-dark-color);
  }
  .module h2, .module caption, .inline-group h2 {
    background-color: var(--secondary-color);
  }
  div.breadcrumbs {
    background: var(--secondary-color);
    color: var(--highlight-color);
  }
  div.breadcrumbs a:focus, div.breadcrumbs a:hover {
    color: var(--highlight-color);
  }
  a:link, a:visited {
    color: var(--secondary-color);
  }
  .selector-chosen h2 {
    background: var(--secondary-color) !important;
  }
  .button, input[type=submit], input[type=button], .submit-row input, a.button {
    background: var(--secondary-color);
  }
  .button.default, input[type=submit].default, .submit-row input.default {
    background: var(--primary-color);
    color: var(--secondary-color);
  }
  .button:active, input[type=submit]:active, input[type=button]:active, .button:focus, input[type=submit]:focus, input[type=button]:focus, .button:hover, input[type=submit]:hover, input[type=button]:hover {
    background: var(--secondary-color);
    opacity: 0.8;
  }
  .button.default:active, input[type=submit].default:active, .button.default:focus, input[type=submit].default:focus, .button.default:hover, input[type=submit].default:hover {
    background: var(--primary-color);
    color: var(--secondary-color);
    opacity: 0.8;
  }
  .object-tools a:focus, .object-tools a:hover {
    background-color: var(--secondary-color);
  }
</style>
{% endblock %}
