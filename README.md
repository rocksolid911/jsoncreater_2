# JSON Generator
JSON Generator has a simple and convenient syntax. JSON Generator allowing users to generate fake data based on a template. It has been designed for simplicity. For this reason we do not follow JSON schema standard! 


## Table of Contents
- [Usage](#usage)
- [API](#api)
- [Localization](#localization)
- [ToDo](#todo)
- [Licence](#licence)

## Usage
Using of JSON Generator is straightforward. First, you must define your JSON template by our simple API. This template is in JSON format. Then, you must call generate function with your JSON template as input. Generate function makes a random JSON object based on your JSON template as the return value. 

##Implemantation
run with ```python main.py ``` ```path/to/jsonfiletobegenerate``` ```path/to/jsonoutput```
###for windows

 For windows path use double \\ after each directory 

 like C:\\user\\Documents\\any_folder\\file_name.json


For your convenience, we provide a script (main.py) that load template from file and generate random JSON object. There is multiple template file in this repository.

## API

| Name | Description | Usage | Params | Returns |
| --- | --- | --- | --- | --- |
| Bool | Random boolean | ```{{bool}}``` | | Boolean |
| Choice | Returns random item from passed arguments list. | ```{{choice([list])}}``` | ```list``` List of string items | String |
| City | Random city name | ```{{city}}``` | | String |
| Company | Random company name | ```{{company}}``` | | String |
| Country | Random country name | ```{{country}}``` | | String |
| Email | Randim email | ```email()``` | | String |
| First name | Random first name | ```{{first_name}}``` | | String |
| Floating | Random float number in specified range. | ```{{floating([min], [max])}}``` | ```min``` Minimum number of in the range, ```max``` Maximum number in the range | Float |
| GUID | Random globally unique identifier (UUID4). | ```{{guid()}}``` | | String |
| Integer | Random integer in specified range. | ```integer([min=0], [max=10])``` | ```min``` Minimum number in the range, ```max``` Maximum number in the range. |
| Name | Random first name and last name | ```name()``` | | String |
| Object ID | MongoDB's globally unique identifier for objects. | ```object_id()``` | | String |
| Phone | Generates random phone number.  | ```Phone()``` | | String |
| Repeat | Clones next item in specified range of repeats to make an array. Repeatable object must come exactly after repear command in template | ```"{{repeat(min, [max])}}",  'this object will be repeated'``` | ```min``` Minimum number of repeats, ```max``` Maximum number of repeats | Array |
| State | Random state name. | ```state()``` | | String |
| Last name | Random last name | ```last_name()``` | | String |
| date | Random date | ```dategen()```| if want to change interval change it in /method/dategen.py|String|

Using this syntax ```"field_name|optional"``` in a field name you can make a field as an optional field.

## Localization
JSON Generator use [Faker](https://github.com/joke2k/faker) package. Faker can take locale as and argument, to return localized data. You can change it with LOCALE variable in locale.py. Default value for LOCALE is ```en_US```.

## ToDo
- Time Zone
- Gender for first name
- Format for floating
- Custom function
- Clone object (index)
- Negative random number
- Lorem Ipsum!
- Phone based on locale and format
- Random street
- Performance Analysis
- Setup script

#Author :  Siddhant Saraf