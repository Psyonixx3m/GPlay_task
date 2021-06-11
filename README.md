# Gplay Crawler

Gplay Crawler is a scrapy crawler created for a task which requires:
- Navigating the sections "Hardware", "Peripherals".
- Scraping specific items with the following attributes:
- - Item cost must be less than 200BGN.
- - Item must be available.

Gplay Crawler also follows fullfils the following additional requirements:

Gather the following parameters of an item:

- category 
- subcategory
- title
- subtitle
- article number
- price

 

## Installation

Requires IDE

Python v3.6+

```bash
pip install scrapy
pip install jsonschema
```

## Usage

```python
import scrapy
import sqlite3

```

Crawler starts after executing the following command in the console:

scrapy crawl gp_items

