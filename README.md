
# json-into-html    [![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

json-2-html is a Python library that fetches data from APIs, allows users to define the structure of the JSON response, and generates responsive HTML pages to display the data in a user-friendly format.




## classes

#### ApiHandler

```http
  This class is responsible for managing communication with the API and
  retrieving JSON data.

  It takes the API URL as input during initialization.

  The fetch_data method sends a GET request to the API and returns the JSON
  data.

  It includes error handling for timeouts, connection errors, HTTP errors, and
  invalid JSON responses.
```

#### JsonDefinition

```http
  This class is used to define the structure of the JSON data and how each
  field should be displayed.

  It uses an Enum called DisplayType to represent the different display types
  (text, image, video, etc.).

  The add_field method allows you to add a field definition, specifying the
  field name, display type, and any additional options.

  It includes validation to ensure that required options are provided for
  certain display types (e.g., width and height for images).
```

#### HtmlGenerator

```http
  This class generates the HTML code based on the JSON data and definitions
  provided.

  It uses the BeautifulSoup library to create and manipulate HTML elements.
  
  The generate_html method iterates over the data and definitions, calling the
  appropriate method to generate the HTML for each field.

  It includes methods for adding the HTML head (with title and CSS links), and
  for generating the HTML for different field types (text, image, video, file,
  link).

  It uses a templating engine (Jinja2) to separate the HTML code from the
  Python code, making it easier to maintain and modify the HTML structure.
```


## example.py

You can use this example code!

```python
from json-into-html import ApiHandler, HtmlGenerator, JsonDefinition, DisplayType

# API address
api_url = "https://dog.ceo/api/breeds/image/random"

api_handler = ApiHandler(api_url)

data = api_handler.fetch_data()

if data:
    json_definition = JsonDefinition()

    json_definition.add_field("message", DisplayType.IMAGE)
    json_definition.add_field("status", DisplayType.TEXT)

    html_generator = HtmlGenerator(data, json_definition)

    html = html_generator.generate_html()

    html_generator.save_html("dog_image.html")
    print("HTML generated successfully!")
else:
    print("Failed to fetch data from API.")```
