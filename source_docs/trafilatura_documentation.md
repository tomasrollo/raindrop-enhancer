================
CODE SNIPPETS
================
TITLE: Bash: Command-line URL Extraction
DESCRIPTION: Provides an example of using Trafilatura directly from the command-line to extract main content and comments from a given URL.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/quickstart

LANGUAGE: Bash
CODE:
```
trafilatura -u "https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/"
```

--------------------------------

TITLE: Install Trafilatura with Optional Modules
DESCRIPTION: Installs the cchardet package for faster encoding detection or installs Trafilatura with all additional functionality.

SOURCE: https://trafilatura.readthedocs.io/en/latest/installation

LANGUAGE: bash
CODE:
```
$ pip install cchardet  # single package only
$ pip install trafilatura[all]  # all additional functionality
```

--------------------------------

TITLE: Install Trafilatura from GitHub
DESCRIPTION: Installs the latest development version of Trafilatura directly from its GitHub repository. This is useful for testing or using the most recent code changes.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/installation

LANGUAGE: bash
CODE:
```
pip install --force-reinstall -U git+https://github.com/adbar/trafilatura
```

--------------------------------

TITLE: Install Latest Trafilatura from GitHub
DESCRIPTION: This command installs the absolute latest code base of Trafilatura directly from its GitHub repository, useful for testing development versions or contributing to the project.

SOURCE: https://trafilatura.readthedocs.io/en/latest/installation

LANGUAGE: bash
CODE:
```
pip install --force-reinstall -U git+https://github.com/adbar/trafilatura
```

--------------------------------

TITLE: Setup Epsilla Docker and Install Libraries
DESCRIPTION: This snippet shows how to pull the Epsilla Docker image, run a container, and install the necessary Python libraries: pyepsilla for database interaction and langchain with sentence-transformers for embedding models.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial-epsilla

LANGUAGE: bash
CODE:
```
$ docker pull epsilla/vectordb
$ docker run --pull=always -d -p 8888:8888 epsilla/vectordb

$ pip install -U pyepsilla

$ pip install -U langchain sentence_transformers
```

--------------------------------

TITLE: Install Trafilatura using pip
DESCRIPTION: Installs the Trafilatura library and its dependencies using the pip package manager. This is the primary method for setting up Trafilatura.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/installation

LANGUAGE: bash
CODE:
```
pip install trafilatura
```

--------------------------------

TITLE: Install Optional Modules for Trafilatura
DESCRIPTION: Installs additional Python packages that enhance Trafilatura's functionality, such as faster encoding detection (cchardet) or comprehensive feature support (all).

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/installation

LANGUAGE: bash
CODE:
```
pip install cchardet
pip install trafilatura[all]
```

--------------------------------

TITLE: Bash: Command-line File Input
DESCRIPTION: Demonstrates how to pipe HTML content from a file or standard input to the Trafilatura command-line tool for extraction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/quickstart

LANGUAGE: Bash
CODE:
```
cat myfile.html | trafilatura
```

LANGUAGE: Bash
CODE:
```
< myfile.html trafilatura
```

--------------------------------

TITLE: Python: Basic HTML Extraction
DESCRIPTION: Demonstrates the fundamental process of fetching a URL and extracting the main text content using Trafilatura's `fetch_url` and `extract` functions.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/quickstart

LANGUAGE: Python
CODE:
```
from trafilatura import fetch_url, extract

downloaded = fetch_url('https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/')
result = extract(downloaded)
print(result)
```

--------------------------------

TITLE: Install Trafilatura and SoMaJo
DESCRIPTION: Installs the latest version of Trafilatura and the SoMaJo tokenizer using pip. These are essential for text extraction and tokenization.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial1

LANGUAGE: bash
CODE:
```
pip install -U trafilatura
pip install -U SoMaJo
```

--------------------------------

TITLE: Bash: Command-line Extraction Options
DESCRIPTION: Shows how to combine command-line options for Trafilatura, such as specifying JSON output and disabling table extraction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/quickstart

LANGUAGE: Bash
CODE:
```
< myfile.html trafilatura --json --no-tables
```

--------------------------------

TITLE: Upgrade Trafilatura to Latest Version
DESCRIPTION: Updates the Trafilatura installation to the most recent version available on PyPI. This ensures access to the latest features and bug fixes.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/installation

LANGUAGE: bash
CODE:
```
pip install --upgrade trafilatura
```

--------------------------------

TITLE: Install Specific Trafilatura Version
DESCRIPTION: This command allows you to install a specific version of Trafilatura, which is useful for compatibility with older Python versions or specific project requirements.

SOURCE: https://trafilatura.readthedocs.io/en/latest/installation

LANGUAGE: bash
CODE:
```
pip install trafilatura==1.12.2
```

--------------------------------

TITLE: Python: Customize Output Format
DESCRIPTION: Shows how to customize the output format of extracted data from HTML, including options for XML, JSON, and Markdown, with or without metadata.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/quickstart

LANGUAGE: Python
CODE:
```
result = extract(downloaded, output_format="xml")
```

LANGUAGE: Python
CODE:
```
extract(downloaded, output_format="json", include_comments=False)
```

LANGUAGE: Python
CODE:
```
extract(downloaded, output_format="markdown", with_metadata=True)
```

--------------------------------

TITLE: Python: Fast Mode Extraction
DESCRIPTION: Illustrates how to use Trafilatura in a faster mode by bypassing fallback algorithms, which can improve performance at the potential cost of accuracy.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/quickstart

LANGUAGE: Python
CODE:
```
result = extract(downloaded, no_fallback=True)
```

--------------------------------

TITLE: Install Trafilatura with Pip
DESCRIPTION: This command installs the Trafilatura library and its dependencies using pip, the Python package installer. It's the primary method for adding Trafilatura to your Python environment.

SOURCE: https://trafilatura.readthedocs.io/en/latest/installation

LANGUAGE: bash
CODE:
```
pip install trafilatura
```

--------------------------------

TITLE: Check Python Version
DESCRIPTION: Verifies if a compatible Python version (3.6 or higher) is installed on the system. This is a prerequisite for installing Trafilatura.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/installation

LANGUAGE: bash
CODE:
```
$ python3 --version
Python 3.10.12
```

--------------------------------

TITLE: Upgrade Trafilatura to Latest Version
DESCRIPTION: This command upgrades an existing Trafilatura installation to the latest available version from PyPI, ensuring you have the most recent features and bug fixes.

SOURCE: https://trafilatura.readthedocs.io/en/latest/installation

LANGUAGE: bash
CODE:
```
pip install --upgrade trafilatura
```

--------------------------------

TITLE: Install Trafilatura
DESCRIPTION: Installs or updates the Trafilatura library to the latest version using pip.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial0

LANGUAGE: bash
CODE:
```
pip install -U trafilatura
```

--------------------------------

TITLE: Build Documentation with Sphinx
DESCRIPTION: Instructions for building the documentation using Sphinx. This involves installing dependencies and running the sphinx-build command.

SOURCE: https://trafilatura.readthedocs.io/en/latest/index

LANGUAGE: Shell
CODE:
```
pip install -r requirements.txt
sphinx-build -b html . _build/
```

--------------------------------

TITLE: Install Python Dependencies
DESCRIPTION: Installs the pyepsilla client for interacting with the Epsilla database, and langchain with sentence-transformers for text embedding.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial-epsilla

LANGUAGE: bash
CODE:
```
pip install -U pyepsilla
pip install -U langchain sentence_transformers
```

--------------------------------

TITLE: Using Sitemaps for Website Crawling with Command-Line
DESCRIPTION: This resource explains how to use sitemaps to crawl websites directly from the command-line. It's a practical guide for efficient website data collection.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorials

LANGUAGE: Shell
CODE:
```
# Example command using a hypothetical tool that processes sitemaps
# Assume 'sitemap-crawler' is a command-line tool
# sitemap-crawler --sitemap-url https://example.com/sitemap.xml --output-dir ./crawled_data
```

--------------------------------

TITLE: Reproduce Trafilatura Tests
DESCRIPTION: Instructions on how to reproduce the benchmark tests for Trafilatura. This involves cloning the project repository, installing necessary packages, and running the evaluation script with provided data.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/evaluation

LANGUAGE: bash
CODE:
```
git clone https://github.com/adbar/trafilatura.git
cd trafilatura
pip install -r requirements.txt
python tests/run_tests.py
```

--------------------------------

TITLE: Tokenize XML File with Somajo
DESCRIPTION: Demonstrates how to tokenize an XML file using the somajo-tokenizer command-line tool. It shows the basic tokenization command and an example of piping the output to sed to remove XML tags and empty lines.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial1

LANGUAGE: bash
CODE:
```
# tokenize a file
$ somajo-tokenizer --xml xmlfiles/filename.xml
```

LANGUAGE: bash
CODE:
```
# remove tags
$ somajo-tokenizer --xml xmlfiles/filename.xml | sed -e "s|</*.*>||g" -e "/^$/d"
```

--------------------------------

TITLE: Advanced token filtering examples
DESCRIPTION: Provides examples of advanced filtering techniques for tokens, including removing stopwords from a file and converting text to lowercase using uconv.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial1

LANGUAGE: bash
CODE:
```
  * with a list of stopwords: `egrep -vixFf stopwords.txt`
  * alternative to convert to lower case: `uconv -x lower`
```

--------------------------------

TITLE: Install Trafilatura
DESCRIPTION: This snippet shows the command to install or update the Trafilatura library using pip. It ensures you have the latest version for optimal performance.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial0

LANGUAGE: bash
CODE:
```
pip install -U trafilatura
```

--------------------------------

TITLE: Install Trafilatura with GUI support
DESCRIPTION: Installs Trafilatura version 1.8.1 with graphical user interface support using pip. This command ensures that all necessary dependencies for the GUI are included.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-gui

LANGUAGE: bash
CODE:
```
pip3 install -U trafilatura==1.8.1[gui]
```

--------------------------------

TITLE: Python: Extract All Text Content
DESCRIPTION: Demonstrates the `html2txt` function for extracting all text content from an HTML document in a manner similar to converting HTML to plain text.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/quickstart

LANGUAGE: Python
CODE:
```
from trafilatura import html2txt
html2txt(downloaded)
```

--------------------------------

TITLE: Add User Bin Directory to PATH (Unix)
DESCRIPTION: This command adds the user-specific binary directory to your system's PATH environment variable on Unix-like systems. This is necessary if the Trafilatura command-line tool is not recognized after installation.

SOURCE: https://trafilatura.readthedocs.io/en/latest/installation

LANGUAGE: bash
CODE:
```
export PATH="$HOME/.local/bin:$PATH"
```

--------------------------------

TITLE: Download and Process with Trafilatura
DESCRIPTION: This command-line example shows how to use Trafilatura to download web pages from a list of URLs, save extracted text to an output directory, and back up the downloaded HTML sources. It specifies input file, output directory, and backup directory.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial-dwds

LANGUAGE: bash
CODE:
```
trafilatura --input-file linkliste.txt --output-dir ausgabe/ --backup-dir html-quellen/
```

--------------------------------

TITLE: Trafilatura Citation Example
DESCRIPTION: An example of how to cite the Trafilatura project in academic work, formatted as a BibTeX entry.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/index

LANGUAGE: bibtex
CODE:
```
@inproceedings{barbaresi-2021-trafilatura,
  title = {{Trafilatura: A Web Scraping Library and Command-Line Tool for Text Discovery and Extraction}},
  author = "Barbaresi, Adrien",
  booktitle = "Proceedings of the Joint Conference of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing: System Demonstrations",
  pages = "122--131",
  publisher = "Association for Computational Linguistics",
  url = "https://aclanthology.org/2021.acl-demo.15",
  year = 2021,
}
```

--------------------------------

TITLE: Build Trafilatura Documentation
DESCRIPTION: Instructions for building the Trafilatura documentation using Sphinx. This involves installing dependencies and running the Sphinx build command.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/index

LANGUAGE: shell
CODE:
```
pip install -r requirements.txt
sphinx-build -b html . _build/
```

--------------------------------

TITLE: Initialize web crawl
DESCRIPTION: Initializes the crawl process by setting up `CrawlParameters`, copying values to the URL store, and retrieving the initial page if the crawl starts without pre-defined URLs. It handles adding known URLs and setting up the starting point.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/spider

LANGUAGE: Python
CODE:
```
def init_crawl(
    start: str,
    lang: Optional[str] = None,
    rules: Optional[RobotFileParser] = None,
    todo: Optional[List[str]] = None,
    known: Optional[List[str]] = None,
    prune_xpath: Optional[str] = None,
) -> CrawlParameters:
    """Initialize crawl by setting variables, copying values to the
    URL store and retrieving the initial page if the crawl starts."""
    params = CrawlParameters(start, lang, rules, prune_xpath)

    # todo: just known or also visited?
    URL_STORE.add_urls(urls=known or [], visited=True)
    URL_STORE.add_urls(urls=params.filter_list(todo))
    URL_STORE.store_rules(params.base, params.rules)

    # visiting the start page if necessary
    if not todo:
        URL_STORE.add_urls(urls=[params.start], visited=False)
        params = crawl_page(params, initial=True)
    else:
        params.update_metadata(URL_STORE)

    return params
```

--------------------------------

TITLE: Install Trafilatura GUI (Python)
DESCRIPTION: Installs Trafilatura version 1.8.1 with GUI support using pip. This command ensures that all necessary dependencies for the graphical interface are included.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-gui

LANGUAGE: bash
CODE:
```
pip3 install -U trafilatura==1.8.1[gui]
```

--------------------------------

TITLE: Python: Extract Metadata
DESCRIPTION: Shows how to use the `extract_metadata` function to specifically extract metadata such as title, author, or publication date from a web page.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/quickstart

LANGUAGE: Python
CODE:
```
from trafilatura import fetch_url, extract_metadata
downloaded = fetch_url('https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/')
extract_metadata(downloaded)
```

--------------------------------

TITLE: Python: Perform first iteration of focused crawler
DESCRIPTION: This example demonstrates how to set up a focused crawler to extract internal links from a given website. It performs the first iteration of the crawler, starting from a specified URL and limiting the number of seen URLs.

SOURCE: https://trafilatura.readthedocs.io/en/latest/crawls

LANGUAGE: Python
CODE:
```
>>> from trafilatura.spider import focused_crawler

# perform the first iteration (will not work with this website, there are no internal links)
>>> to_visit, known_links = focused_crawler("https://example.org", max_seen_urls=1)
```

--------------------------------

TITLE: Launch Trafilatura GUI (Command-line)
DESCRIPTION: Launches the Trafilatura graphical user interface from the terminal. This command assumes Trafilatura has been successfully installed.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-gui

LANGUAGE: bash
CODE:
```
trafilatura_gui
```

--------------------------------

TITLE: Check Python Version
DESCRIPTION: This snippet demonstrates how to check your installed Python version using the command line. Trafilatura requires Python 3.6 or higher.

SOURCE: https://trafilatura.readthedocs.io/en/latest/installation

LANGUAGE: bash
CODE:
```
$ python3 --version
Python 3.10.12
```

--------------------------------

TITLE: Install Trafilatura with Python
DESCRIPTION: Instructions for installing Trafilatura using pip, the Python package installer. This is the primary method for integrating Trafilatura into Python projects.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage

LANGUAGE: bash
CODE:
```
pip install trafilatura
```

--------------------------------

TITLE: Connect to Epsilla and Setup Database
DESCRIPTION: Python code to establish a connection to a local Epsilla server, load a database named 'TrafilaturaDB', and create a table named 'Trafilatura' with specified fields for document ID, content, and vector embeddings.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial-epsilla

LANGUAGE: python
CODE:
```
from pyepsilla import vectordb
client = vectordb.Client(
    # replace with a production server if not running a local docker container
    host='localhost',
    port='8888'
)

status_code, response = client.load_db(
    db_name="TrafilaturaDB",
    db_path="/tmp/trafilatura_store"
)
print(response)

client.use_db(db_name="TrafilaturaDB")

# creates a table called Trafilatura
client.drop_table('Trafilatura')
client.create_table(
  table_name="Trafilatura",
  table_fields=[
    {"name": "ID", "dataType": "INT"},
    {"name": "Doc", "dataType": "STRING"},
    {"name": "Embedding", "dataType": "VECTOR_FLOAT", "dimensions": 384}
  ]
)
```

--------------------------------

TITLE: Install Trafilatura using pip
DESCRIPTION: The primary installation method for Trafilatura is using a Python package manager like pip. This command installs the latest version of the library, making it available for use in your Python projects.

SOURCE: https://trafilatura.readthedocs.io/en/latest/index

LANGUAGE: bash
CODE:
```
pip install trafilatura
```

--------------------------------

TITLE: Troubleshoot Trafilatura GUI on Linux (Debian/Ubuntu)
DESCRIPTION: Installs the GTK development library required for the Trafilatura GUI on Debian/Ubuntu systems. Optionally, it suggests using a wxPython wheel for faster compilation.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-gui

LANGUAGE: bash
CODE:
```
sudo apt install libgtk-3-dev
```

--------------------------------

TITLE: Install GTK Development Files on Debian/Ubuntu
DESCRIPTION: Installs the GTK+ 3 development files required for the Trafilatura GUI on Debian-based Linux distributions like Ubuntu.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-gui

LANGUAGE: bash
CODE:
```
sudo apt install libgtk-3-dev
```

--------------------------------

TITLE: Trafilatura XML Module Initialization
DESCRIPTION: This snippet shows the initial setup of the trafilatura.xml module, including necessary imports for HTML parsing, version checking, file handling, JSON operations, and XML processing using lxml. It also defines constants for XML validation and formatting.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
# pylint:disable-msg=E0611,I1101
"""
All functions related to XML generation, processing and validation.
"""

import csv
import logging

from html import unescape
from importlib.metadata import version
from io import StringIO
from json import dumps as json_dumps
from pathlib import Path
from typing import List, Optional

from lxml.etree import (_Element, Element, SubElement, XMLParser,
                        fromstring, tostring, DTD)

from .settings import Document, Extractor
from .utils import sanitize, sanitize_tree, text_chars_test


LOGGER = logging.getLogger(__name__)
PKG_VERSION = version("trafilatura")

# validation
TEI_SCHEMA = str(Path(__file__).parent / "data" / "tei_corpus.dtd")
TEI_VALID_TAGS = {'ab', 'body', 'cell', 'code', 'del', 'div', 'graphic', 'head', 'hi', \
                  'item', 'lb', 'list', 'p', 'quote', 'ref', 'row', 'table'}
TEI_VALID_ATTRS = {'rend', 'rendition', 'role', 'target', 'type'}
TEI_DTD = None  # to be downloaded later if necessary
TEI_REMOVE_TAIL = {"ab", "p"}
TEI_DIV_SIBLINGS = {"p", "list", "table", "quote", "ab"}

CONTROL_PARSER = XMLParser(remove_blank_text=True)

NEWLINE_ELEMS = {'code', 'graphic', 'head', 'lb', 'list', 'p', 'quote', 'row', 'table'}
SPECIAL_FORMATTING = {'del', 'head', 'hi', 'ref'}
WITH_ATTRIBUTES = {'cell', 'row', 'del', 'graphic', 'head', 'hi', 'item', 'list', 'ref'}
NESTING_WHITELIST = {"cell", "figure", "item", "note", "quote"}

META_ATTRIBUTES = [
    'sitename', 'title', 'author', 'date', 'url', 'hostname',
    'description', 'categories', 'tags', 'license', 'id',
    'fingerprint', 'language'
]

HI_FORMATTING = {'#b': '**', '#i': '*', '#u': '__', '#t': '`'}


MAX_TABLE_WIDTH = 1000

```

--------------------------------

TITLE: Extract with Optimized Settings
DESCRIPTION: Provides an example of combining settings for faster processing, including disabling comments and tables, and bypassing fallbacks.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
>>> result = extract(downloaded, include_comments=False, include_tables=False, no_fallback=True)
```

--------------------------------

TITLE: Perform focused web crawling on the command-line
DESCRIPTION: This snippet shows how to execute a web crawl directly from the command-line using Trafilatura. It allows users to specify starting URLs and other parameters to discover and retrieve links, facilitating efficient exploration of websites without writing Python scripts.

SOURCE: https://trafilatura.readthedocs.io/en/latest/crawls

LANGUAGE: Shell
CODE:
```
# Example: Crawl a specific website from the command-line
# trafilatura --crawl <url> --output-file crawled_links.txt

# To crawl a single URL and extract links:
# trafilatura --url http://example.com --links

# For more advanced crawling, you might use:
# trafilatura --crawl http://example.com --depth 2 --output-file crawl_output.jsonl

# Note: The exact command-line arguments might vary based on Trafilatura version and specific needs.
# Consult the Trafilatura documentation for the most up-to-date options.

```

--------------------------------

TITLE: Wget Download and Trafilatura XML/TEI Processing
DESCRIPTION: This example demonstrates an alternative workflow: first, download HTML files from a list of URLs using wget with specified delays to avoid overwhelming servers. Then, process the downloaded HTML files using Trafilatura, outputting in XML TEI format and excluding comments.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial0

LANGUAGE: bash
CODE:
```
wget --directory-prefix=download/ --wait 5 --input-file=mylist.txt
trafilatura --input-dir download/ --output-dir corpus/ --xmltei --no-comments
```

--------------------------------

TITLE: Setup Epsilla Docker Container
DESCRIPTION: This bash script pulls the latest Epsilla vector database Docker image and runs it in detached mode, exposing port 8888.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial-epsilla

LANGUAGE: bash
CODE:
```
docker pull epsilla/vectordb
docker run --pull=always -d -p 8888:8888 epsilla/vectordb
```

--------------------------------

TITLE: Install Trafilatura using Pip
DESCRIPTION: Installs the Trafilatura Python package using the pip package manager in the terminal.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-r

LANGUAGE: bash
CODE:
```
$ pip install trafilatura
```

--------------------------------

TITLE: Configure SOCKS Proxy for Downloads
DESCRIPTION: Explains how to route all Trafilatura downloads through a SOCKS proxy by setting the http_proxy environment variable. It shows examples for basic proxy configuration and for proxies requiring user authentication.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/downloads

LANGUAGE: bash
CODE:
```
# set socks proxy
export http_proxy=socks5://PROXYHOST:PROXYPORT

# with user and password
export http_proxy=socks5://USER:PASSWORD@PROXYHOST:PROXYPORT
```

--------------------------------

TITLE: Install Trafilatura using Pip
DESCRIPTION: Installs the Trafilatura Python package using the pip package manager in a terminal.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-r

LANGUAGE: Shell
CODE:
```
$ pip install trafilatura

```

--------------------------------

TITLE: Run Evaluation with Latest Data - Trafilatura
DESCRIPTION: To run the evaluation with the latest data and packages, refer to the corresponding README file on GitHub. This provides instructions and necessary setup for conducting the evaluation.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/evaluation

LANGUAGE: text
CODE:
```
To run the evaluation with the latest data and packages see the `corresponding readme <https://github.com/adbar/trafilatura/blob/master/tests/README.rst>`_ .
```

--------------------------------

TITLE: Shell: Crawl a website using trafilatura CLI
DESCRIPTION: This command-line example shows how to use the `trafilatura` tool to crawl a website and save the extracted links to a file. It uses the `--crawl` option to specify the target URL.

SOURCE: https://trafilatura.readthedocs.io/en/latest/crawls

LANGUAGE: Shell
CODE:
```
$ trafilatura --crawl "https://www.example.org" > links.txt
```

--------------------------------

TITLE: Get robots.txt rules
DESCRIPTION: Fetches and parses the robots.txt file for a given base URL. It constructs the full robots.txt URL and uses `fetch_url` to get the data, then passes it to `parse_robots`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/spider

LANGUAGE: Python
CODE:
```
def get_rules(base_url: str) -> Optional[RobotFileParser]:
    """Attempt to fetch and parse robots.txt file for a given website."""
    robots_url = base_url + ROBOTS_TXT_URL
    data = fetch_url(robots_url)
    return parse_robots(robots_url, data) if data else None
```

--------------------------------

TITLE: Perform focused web crawling with Python
DESCRIPTION: This snippet demonstrates how to initiate a focused web crawl using Trafilatura in Python. It involves setting up the crawler with a starting URL and potentially other configuration options to discover and retrieve links within a specific website, adhering to politeness and efficiency.

SOURCE: https://trafilatura.readthedocs.io/en/latest/crawls

LANGUAGE: Python
CODE:
```
from trafilatura import WebParser

parser = WebParser()

# Example: Crawl a specific website
# You would typically provide a starting URL and potentially other parameters
# For demonstration, let's assume you have a list of URLs to process
urls_to_crawl = ['http://example.com']

# In a real scenario, you would use a more sophisticated crawling mechanism
# that manages the frontier, handles politeness, etc.
# For instance, using the main trafilatura.fetch_url function or a dedicated crawler class

# Example of fetching a single URL (part of crawling)
# from trafilatura import fetch_url
# html = fetch_url(urls_to_crawl[0])
# if html:
#     links = parser.links(html, url=urls_to_crawl[0])
#     print(f"Found {len(links)} links on {urls_to_crawl[0]}")

```

--------------------------------

TITLE: Reinstall Trafilatura Package
DESCRIPTION: This command reinstalls the Trafilatura package locally after modifying the settings.py file. It uses pip to install from the current directory without installing dependencies, ensuring the local changes are applied.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/settings

LANGUAGE: bash
CODE:
```
pip install --no-deps -U .
```

--------------------------------

TITLE: Crawl Websites Using Sitemaps with Trafilatura
DESCRIPTION: This section explains how to use Trafilatura to crawl websites by processing their sitemaps. It provides examples for discovering links from a sitemap, saving them to a file, and filtering by target language.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
# run link discovery through a sitemap for sitemaps.org and store the resulting links in a file
$ trafilatura --sitemap "https://www.sitemaps.org/" --list > mylinks.txt

# using an already known sitemap URL
$ trafilatura --sitemap "https://www.sitemaps.org/sitemap.xml" --list

# targeting webpages in German
$ trafilatura --sitemap "https://www.sitemaps.org/" --list --target-language "de"
```

--------------------------------

TITLE: Extract Text from Links using Trafilatura
DESCRIPTION: This command-line instruction uses the 'trafilatura' tool to process a list of links from an input file. It can output the extracted content either as raw text files or in XML format, storing the results in a specified output directory. Ensure 'trafilatura' is installed via pip.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial1

LANGUAGE: bash
CODE:
```
$ trafilatura -i list.txt -o txtfiles	# output as raw text
$ trafilatura --xml -i list.txt -o xmlfiles	# output in XML format
```

--------------------------------

TITLE: Web Crawling Process - Cho et al. (1998)
DESCRIPTION: Describes the fundamental process of a web crawler, starting with an initial URL, retrieving the page, extracting new URLs, and adding them to a queue for subsequent scanning. This forms the basis of automatic web navigation.

SOURCE: https://trafilatura.readthedocs.io/en/latest/compendium

LANGUAGE: General
CODE:
```
A crawler starts off with the URL for an initial page P0. It retrieves P0, extracts any URLs in it, and adds them to a queue of URLs to be scanned. Then the crawler gets URLs from the queue (in some order), and repeats the process.
```

--------------------------------

TITLE: Validate TEI XML from URL via Command Line
DESCRIPTION: Uses the Trafilatura command-line interface to fetch a URL, extract content as TEI XML, and validate it against the TEI schema. This command requires Trafilatura to be installed and accessible in the system's PATH.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial2

LANGUAGE: Bash
CODE:
```
trafilatura --xmltei --validate --URL "https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/"
```

--------------------------------

TITLE: Crawl Websites using Sitemaps with Command-Line
DESCRIPTION: This tutorial explains how to use sitemaps to crawl websites efficiently from the command-line. It details the process of leveraging sitemap files to discover and process web pages.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorials

LANGUAGE: Bash
CODE:
```
trafilatura --sitemap http://example.com/sitemap.xml --output output.txt
```

--------------------------------

TITLE: Install and Load Reticulate in R
DESCRIPTION: Installs the Reticulate package from CRAN and loads it into the R session, enabling Python-R interoperability.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-r

LANGUAGE: R
CODE:
```
> install.packages("reticulate")
> library(reticulate)

```

--------------------------------

TITLE: Install and Load Reticulate in R
DESCRIPTION: Installs the reticulate package from CRAN and loads it into the R session, enabling Python-R interoperability.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-r

LANGUAGE: R
CODE:
```
> install.packages("reticulate")
> library(reticulate)
```

--------------------------------

TITLE: URL Scrubbing for Query Parameters and Fragments (Python)
DESCRIPTION: This regex is used to remove query parameters (starting with '?') and URL fragments (starting with '#') from URLs, simplifying them for further processing.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/sitemaps

LANGUAGE: Python
CODE:
```
import re

SCRUB_REGEX = re.compile(r"\?.*$|#.*$")
```

--------------------------------

TITLE: Filter Links with Courlan
DESCRIPTION: This command-line example demonstrates how to filter a list of URLs using the 'courlan' tool, prioritizing German language and content richness. It reads from 'linkliste-roh.txt' and outputs to 'linkliste-gefiltert.txt'.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial-dwds

LANGUAGE: bash
CODE:
```
courlan --language de --strict --inputfile linkliste-roh.txt --outputfile linkliste-gefiltert.txt
```

--------------------------------

TITLE: Install Trafilatura in R using Reticulate
DESCRIPTION: Installs the Trafilatura Python package within the R environment using the `py_install()` function provided by Reticulate.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-r

LANGUAGE: R
CODE:
```
> library(reticulate)
> py_install("trafilatura")

```

--------------------------------

TITLE: Install Trafilatura using Reticulate
DESCRIPTION: Installs the Trafilatura Python package within the R environment using the py_install() function from the reticulate package.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-r

LANGUAGE: R
CODE:
```
> library(reticulate)
> py_install("trafilatura")
```

--------------------------------

TITLE: Filter by Target Language
DESCRIPTION: Filters the extracted output to include only content matching the specified target language (ISO 639-1 code). Requires additional components to be installed.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
# Example usage (assuming a URL is provided or piped):
# trafilatura --target-language en -u "URL"
```

--------------------------------

TITLE: Download and Extract Web Content with R
DESCRIPTION: Provides an example of how to use Trafilatura with the R programming language for downloading and extracting web page content. This allows R users to leverage Trafilatura's capabilities.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage

LANGUAGE: r
CODE:
```
# Assuming trafilatura is installed and accessible in R
url <- "http://example.com"

# Download and extract content
content <- trafilatura::extract_url(url)

# Print the extracted content
print(content)
```

--------------------------------

TITLE: CrawlParameters for Website Crawling
DESCRIPTION: Manages parameters for a focused web crawl, including start URL, base domain, language, robots.txt rules, and pruning rules. It helps in filtering and validating links during the crawling process.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/spider

LANGUAGE: Python
CODE:
```
class CrawlParameters:
    """Store necessary information to manage a focused crawl."""
    __slots__ = ["start", "base", "lang", "rules", "ref", "i", "known_num", "is_on", "prune_xpath"]

    def __init__(
        self,
        start: str,
        lang: Optional[str] = None,
        rules: Optional[RobotFileParser] = None,
        prune_xpath: Optional[str] = None,
    ) -> None:
        self.start: str = start
        self.base: str = self._get_base_url(start)
        self.ref: str = self._get_reference(start)
        self.lang: Optional[str] = lang
        self.rules: Optional[RobotFileParser] = rules or get_rules(self.base)
        self.i: int = 0
        self.known_num: int = 0
        self.is_on: bool = True
        self.prune_xpath: Optional[str] = prune_xpath

    def _get_base_url(self, start: str) -> str:
        """Set reference domain for the crawl."""
        base: str = get_base_url(start)
        if not base:
            raise ValueError(f"cannot start crawl: {start}")
        return base

    def _get_reference(self, start: str) -> str:
        """Determine the reference URL."""
        return start.rsplit("/", 1)[0] if start.count("/") >= 3 else start

    def update_metadata(self, url_store: UrlStore) -> None:
        """Adjust crawl data based on URL store info."""
        self.is_on = bool(url_store.find_unvisited_urls(self.base))
        self.known_num = len(url_store.find_known_urls(self.base))

    def filter_list(self, todo: Optional[List[str]]) -> List[str]:
        """Prepare the todo list, excluding invalid URLs."""
        if not todo:
            return []
        return [u for u in todo if u != self.start and self.ref in u]

    def is_valid_link(self, link: str) -> bool:
        """Run checks: robots.txt rules, URL type and crawl breadth."""
        return (
            (not self.rules or self.rules.can_fetch("*", link))
            and self.ref in link
            and not is_not_crawlable(link)
        )
```

--------------------------------

TITLE: Web Crawling and Data Processing - Python
DESCRIPTION: This snippet outlines the fundamental steps in building a web corpus, starting with web crawling to define the scope and content, followed by data pre-processing which influences subsequent stages. It highlights the process of downloading, cleaning, de-duplicating, annotating, and indexing data for linguistic research.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/compendium

LANGUAGE: Python
CODE:
```
def crawl_and_process_web_corpus():
    # Phase 1: Web crawling determines the range and the general contents of a web corpus
    print("Starting web crawling...")
    # ... crawling logic ...
    print("Web crawling complete.")

    # Phase 2: Data pre-processing impacts all the other steps downstream
    print("Starting data pre-processing...")
    # ... cleaning, de-duplication, annotation logic ...
    print("Data pre-processing complete.")

    # Phase 3: Storing the processed version as the linguistic corpus
    print("Storing the processed corpus...")
    # ... storage logic ...
    print("Corpus construction complete.")

# Example usage:
# crawl_and_process_web_corpus()
```

--------------------------------

TITLE: Extract Data via API using curl
DESCRIPTION: Demonstrates sending a POST request to the Trafilatura API using the curl command-line tool to extract data from a webpage in XML format. Requires curl to be installed.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-api

LANGUAGE: bash
CODE:
```
$ curl -X POST "https://trafilatura.mooo.com/extract-demo" \
           -H "content-type: application/json" \
           --data '{ \
                    "url": "https://example.org", \
                    "args": { \
                      "output_format": "xml" \
                     } \
                  }'
```

--------------------------------

TITLE: Sample URLs by Domain Name (Command-line)
DESCRIPTION: Shows how to sample URLs from a text file using the `courlan` command-line interface. The `--inputfile` specifies the source of URLs, `--outputfile` defines where the sampled URLs will be saved, and `--sample --samplesize 50` enables sampling with a target size of 50 URLs.

SOURCE: https://trafilatura.readthedocs.io/en/latest/url-management

LANGUAGE: Shell
CODE:
```
$ courlan --inputfile urls.txt --outputfile samples-urls.txt --sample --samplesize 50
```

--------------------------------

TITLE: Python: Perform another iteration of focused crawler
DESCRIPTION: This example shows how to perform subsequent iterations of the focused crawler using previously collected information. It continues the crawl with updated `to_visit` and `known_links` variables, and specifies limits for seen and known URLs.

SOURCE: https://trafilatura.readthedocs.io/en/latest/crawls

LANGUAGE: Python
CODE:
```
# perform another iteration using previously collected information
>>> to_visit, known_links = focused_crawler("https://example.org", max_seen_urls=10, max_known_urls=100000, todo=to_visit, known_links=known_links)
```

--------------------------------

TITLE: Handle Deprecated Parameters
DESCRIPTION: This code snippet addresses deprecated parameters like 'no_fallback' and 'as_dict', issuing warnings to guide users towards the current best practices. It also handles the deprecation of 'max_tree_size' by raising a ValueError.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/core

LANGUAGE: Python
CODE:
```
# deprecations
    if no_fallback:
        fast = no_fallback
        warnings.warn(
            '"no_fallback" will be deprecated in a future version, use "fast" instead',
            PendingDeprecationWarning
        )
    if as_dict:
        warnings.warn(
            '"as_dict" will be deprecated, use the .as_dict() method on bare_extraction results',
            PendingDeprecationWarning
        )
    if max_tree_size:
        raise ValueError("max_tree_size is deprecated, use settings.cfg file instead")
```

--------------------------------

TITLE: Customize MIN_OUTPUT_SIZE in Python
DESCRIPTION: Demonstrates how to modify Trafilatura's default configuration in Python by changing the 'MIN_OUTPUT_SIZE' setting. This example shows how a high value for this setting can cause extraction to fail for short content, while the default setting succeeds.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/settings

LANGUAGE: python
CODE:
```
# load necessary functions and data
>>> from copy import deepcopy
>>> from trafilatura import extract
>>> from trafilatura.settings import DEFAULT_CONFIG

# a very short HTML file
>>> my_html = "<html><body><p>Text.</p></body></html>"

# load the configuration and change the minimum output length
>>> my_config = deepcopy(DEFAULT_CONFIG)
>>> my_config['DEFAULT']['MIN_OUTPUT_SIZE'] = '1000'

# apply new settings, extraction will fail
>>> extract(my_html, config=my_config)
>>>
# default extraction works
>>> extract(my_html)
'Text.'
```

--------------------------------

TITLE: Run Trafilatura Command-line with Files
DESCRIPTION: Demonstrates how to use the Trafilatura command-line interface to read URLs from a file, process them, and save the output to a specified directory, with a backup directory for HTML files.

SOURCE: https://trafilatura.readthedocs.io/en/latest/downloads

LANGUAGE: bash
CODE:
```
$ trafilatura -i list.txt -o txtfiles/ --backup-dir htmlbackup/
```

--------------------------------

TITLE: Process Raw HTTP Response with Trafilatura
DESCRIPTION: Shows how to use `fetch_response` to get an HTTP response object and then pass its data and URL to `bare_extraction` for processing, useful for accessing redirection URLs.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
>>> from trafilatura import fetch_response, bare_extraction
>>> response = fetch_response("https://www.example.org")
>>> bare_extraction(response.data, url=response.url)
```

--------------------------------

TITLE: Web Crawling with Trafilatura
DESCRIPTION: Use the `--crawl` option to follow internal links on a website starting from a given URL, returning a list of discovered links. This is an experimental feature for content discovery.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-cli

LANGUAGE: bash
CODE:
```
# Select the --crawl option automatically looks for pages by following a fixed number of internal links on the website, starting from the given URL and returning a list of links.

```

--------------------------------

TITLE: Connect to Epsilla and Prepare Database
DESCRIPTION: This Python code demonstrates how to connect to a local Epsilla vector database instance, load a database, set it as the current database, drop an existing table if it exists, and create a new table with specified fields for storing document data and embeddings.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial-epsilla

LANGUAGE: python
CODE:
```
from pyepsilla import vectordb
client = vectordb.Client(
    # replace with a production server if not running a local docker container
    host='localhost',
    port='8888'
)

status_code, response = client.load_db(
    db_name="TrafilaturaDB",
    db_path="/tmp/trafilatura_store"
)
print(response)

client.use_db(db_name="TrafilaturaDB")

# creates a table called Trafilatura
client.drop_table('Trafilatura')
client.create_table(
  table_name="Trafilatura",
  table_fields=[
    {"name": "ID", "dataType": "INT"},
    {"name": "Doc", "dataType": "STRING"},
    {"name": "Embedding", "dataType": "VECTOR_FLOAT", "dimensions": 384}
  ]
)
```

--------------------------------

TITLE: Check Python Version
DESCRIPTION: Checks the installed Python version from the terminal. Reticulate requires Python 3.6 or higher.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-r

LANGUAGE: bash
CODE:
```
$ python3 --version
Python 3.10.12 # version 3.6 or higher is fine
```

--------------------------------

TITLE: Sample URLs via Command-Line with Courlan (Bash)
DESCRIPTION: The courlan command-line utility can sample URLs from an input file to an output file using the `--sample` and `--samplesize` options.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/url-management

LANGUAGE: bash
CODE:
```
$ courlan --inputfile urls.txt --outputfile samples-urls.txt --sample --samplesize 50
```

--------------------------------

TITLE: Extract Metadata with Trafilatura (Python)
DESCRIPTION: Shows how to import and use the `extract_metadata` function from Trafilatura's metadata module to get metadata like title, author, and URL from downloaded content.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-r

LANGUAGE: Python
CODE:
```
from trafilatura.metadata import extract_metadata
```

LANGUAGE: Python
CODE:
```
downloaded = trafilatura.fetch_url("https://github.com/rstudio/reticulate")
```

LANGUAGE: Python
CODE:
```
extract_metadata(downloaded)
```

--------------------------------

TITLE: Check Python Version
DESCRIPTION: Checks the installed Python version from the terminal. Reticulate requires Python 3.6 or higher.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-r

LANGUAGE: Shell
CODE:
```
$ python3 --version

```

--------------------------------

TITLE: Trafilatura Get Crawl Delay
DESCRIPTION: Demonstrates how to retrieve the crawl delay specified in a robots.txt file using Trafilatura's `get_crawl_delay` function, including providing a default value.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/downloads

LANGUAGE: python
CODE:
```
# get the desired information
seconds = get_crawl_delay(rules)
# provide a backup value in case no rule exists (happens quite often)
seconds = get_crawl_delay(rules, default=30)
```

--------------------------------

TITLE: Generate File-Safe Hash Filename
DESCRIPTION: Demonstrates the use of generate_hash_filename to create a filename-safe string by hashing the provided content, ensuring identical content gets identical filenames.

SOURCE: https://trafilatura.readthedocs.io/en/latest/deduplication

LANGUAGE: Python
CODE:
```
# create a filename-safe string by hashing the given content
from trafilatura.deduplication import generate_hash_filename
generate_hash_filename("This is a text.")
```

--------------------------------

TITLE: Extract Text with XML Output
DESCRIPTION: Demonstrates how to use the 'extract' function to get text content from a downloaded document, formatted as XML. This preserves some basic XML structure.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
>>> extract(downloaded, output_format="xml")
```

--------------------------------

TITLE: Extract text from a URL using Trafilatura on the command-line
DESCRIPTION: This command-line example shows how to use Trafilatura to directly extract main content and comments from a URL. It's a convenient way to process web content without writing Python scripts.

SOURCE: https://trafilatura.readthedocs.io/en/latest/index

LANGUAGE: bash
CODE:
```
$ trafilatura -u "https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/"
```

--------------------------------

TITLE: Python: Customize Output Format
DESCRIPTION: Shows how to customize the output format of extracted data in Trafilatura using Python. Examples include outputting as XML, JSON (discarding comments), and Markdown with metadata.

SOURCE: https://trafilatura.readthedocs.io/en/latest/quickstart

LANGUAGE: Python
CODE:
```
result = extract(downloaded, output_format="xml")
```

LANGUAGE: Python
CODE:
```
extract(downloaded, output_format="json", include_comments=False)
```

LANGUAGE: Python
CODE:
```
extract(downloaded, output_format="markdown", with_metadata=True)
```

--------------------------------

TITLE: Trafilatura: Process links as XML with HTML backup
DESCRIPTION: This command processes a list of links from `list.txt` using Trafilatura, saves the output in XML format in `xmlfiles/`, and creates a backup of the downloaded HTML files in `htmlfiles/`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial0

LANGUAGE: bash
CODE:
```
$ trafilatura --xml -i list.txt -o xmlfiles/ --backup-dir htmlfiles/
```

--------------------------------

TITLE: Discover Feeds with Trafilatura
DESCRIPTION: Automatically detect and process web feeds (Atom, RSS) starting from a homepage or using a known feed URL. The `--feed` option combined with `--list` extracts URLs from feeds. Lists of links can also be processed in parallel.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-cli

LANGUAGE: bash
CODE:
```
# automatically detecting feeds starting from the homepage
$ trafilatura --feed "https://www.dwds.de/" --list

# already known feed
$ trafilatura --feed "https://www.dwds.de/api/feed/themenglossar/Corona" --list

# processing a list in parallel
$ trafilatura -i mylist.txt --feed --list


```

--------------------------------

TITLE: Initialize Extractor with Options
DESCRIPTION: Shows how to use the `Extractor` class to define and manage multiple extraction parameters at once, such as output format and metadata inclusion.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
# import the Extractor class from the settings module
>>> from trafilatura.settings import Extractor

# set multiple options at once
>>> options = Extractor(output_format="json", with_metadata=True)
```

--------------------------------

TITLE: Get Retry Strategy
DESCRIPTION: Defines and returns a urllib3 retry strategy based on configuration parameters such as maximum redirects and download timeout. It uses a global variable to cache the strategy.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/downloads

LANGUAGE: Python
CODE:
```
def _get_retry_strategy(config: ConfigParser) -> urllib3.util.Retry:
    """Define a retry strategy according to the config file."""
    global RETRY_STRATEGY
    if not RETRY_STRATEGY:
        # or RETRY_STRATEGY.redirect != config.getint("DEFAULT", "MAX_REDIRECTS")
        RETRY_STRATEGY = urllib3.util.Retry(
            total=config.getint("DEFAULT", "MAX_REDIRECTS"),
            redirect=config.getint(
                "DEFAULT", "MAX_REDIRECTS"
            ),  # raise_on_redirect=False,
            connect=0,
            backoff_factor=config.getint("DEFAULT", "DOWNLOAD_TIMEOUT") / 2,
            status_forcelist=FORCE_STATUS,
            # unofficial: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#Unofficial_codes
        )
    return RETRY_STRATEGY
```

--------------------------------

TITLE: Initiate Buffered Downloads
DESCRIPTION: A public interface to initiate buffered downloads using a provided list of URLs, specifying the number of download threads and optional extraction options. This function likely orchestrates the download process using the `_buffered_downloads` helper.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/downloads

LANGUAGE: Python
CODE:
```
def buffered_downloads(
    bufferlist: List[str],
    download_threads: int,
    options: Optional[Extractor] = None,
)
```

--------------------------------

TITLE: Try Justext Extraction
DESCRIPTION: Initiates the Justext extraction process for a given HTML tree and URL, specifying the target language. This function is a starting point for using Justext for content extraction. Dependencies include the Justext library and HTML parsing capabilities.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/external

LANGUAGE: python
CODE:
```
[docs]
def try_justext(tree: HtmlElement, url: str, target_language: str) -> _Element:
```

--------------------------------

TITLE: Extract Metadata with Trafilatura in R
DESCRIPTION: This example demonstrates how to import the `extract_metadata` function from Trafilatura's metadata module and use it to extract title, author, URL, and hostname from a fetched web page. It utilizes `py_run_string` for importing and `trafilatura$fetch_url` for downloading content.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-r

LANGUAGE: R
CODE:
```
# import the metadata part of the package as a function
> metadatafunc <- py_run_string("from trafilatura.metadata import extract_metadata")
> downloaded <- trafilatura$fetch_url("https://github.com/rstudio/reticulate")
> metadatafunc$extract_metadata(downloaded)
$title
[1] "rstudio/reticulate"

$author
[1] "Rstudio"

$url
[1] "https://github.com/rstudio/reticulate"

$hostname
[1] "github.com"
# and so on...
```

--------------------------------

TITLE: Process List of Links with Trafilatura
DESCRIPTION: This section demonstrates how to process a list of URLs from a file using Trafilatura. It covers specifying input files, output directories, and different output formats like raw text or XML. It also shows how to back up HTML sources.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
$ trafilatura -i list.txt -o txtfiles/		# output as raw text
$ trafilatura --xml -i list.txt -o xmlfiles/	# output in XML format
$ trafilatura --input-file links.txt --output-dir converted/ --backup-dir html-sources/ --xml
```

--------------------------------

TITLE: Shuf and Head: Random sample of links
DESCRIPTION: This command first shuffles the URLs in a file using `shuf` and then takes the first 100 lines using `head`, creating a random sample of links in `myfile-random-sample.txt`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial0

LANGUAGE: bash
CODE:
```
$ shuf myfile.txt | head -100 > myfile-random-sample.txt
```

--------------------------------

TITLE: Extract and Refine Links
DESCRIPTION: Extracts and refines links from Atom, RSS, and JSON feeds. It calls find_links to get the initial list of links, then handles and filters them to produce a final list of valid links.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/feeds

LANGUAGE: Python
CODE:
```
def extract_links(feed_string: str, params: FeedParameters) -> List[str]:
    "Extract and refine links from Atom, RSS and JSON feeds."
    if not feed_string:
        LOGGER.debug("Empty feed: %s", params.domain)
        return []

    feed_links = find_links(feed_string.strip(), params)

    output_links = [
        link
        for link in handle_link_list(feed_links, params)
        if link != params.ref and link.count("/") > 2
    ]

    if feed_links:
        LOGGER.debug(
            "Links found: %s of which %s valid", len(feed_links), len(output_links)
        )
    else:
        LOGGER.debug("Invalid feed for %s", params.domain)

    return output_links
```

--------------------------------

TITLE: Extract Metadata from Raw HTTP Response
DESCRIPTION: Illustrates how to use `fetch_response` to get a raw HTTP response object and then pass its data and URL to `bare_extraction` for processing, useful for accessing redirection URLs.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
# necessary components
>>> from trafilatura import fetch_response, bare_extraction

# load an example
>>> response = fetch_response("https://www.example.org")

# perform extract() or bare_extraction() on Trafilatura's response object
>>> bare_extraction(response.data, url=response.url)  # here is the redirection URL
```

--------------------------------

TITLE: Python: Extract text with JSON output and metadata
DESCRIPTION: Shows how to use the `extract` function to get text content along with associated metadata, outputting the result in JSON format. This is useful for structured data retrieval.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
>>> extract(downloaded, output_format="json", with_metadata=True)
```

--------------------------------

TITLE: Decompress Compressed Files with Trafilatura
DESCRIPTION: Handles decompression of binary data using a cascade of installed packages, prioritizing magic numbers. It supports gzip, zstandard, brotli, and zlib formats, returning the decompressed content or the original data if decompression fails.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
import gzip
import zlib
import zstandard
import brotli

# Assuming HAS_GZIP, HAS_ZSTD, HAS_BROTLI, HAS_ZLIB are defined booleans
# Assuming LOGGER is a configured logger instance

def handle_compressed_file(filecontent: bytes) -> bytes:
    """
    Don't trust response headers and try to decompress a binary string
    with a cascade of installed packages. Use magic numbers when available.
    """
    if not isinstance(filecontent, bytes):
        return filecontent

    # source: https://stackoverflow.com/questions/3703276/how-to-tell-if-a-file-is-gzip-compressed
    if HAS_GZIP and filecontent[:3] == b"\x1f\x8b\x08":
        try:
            return gzip.decompress(filecontent)
        except Exception:  # EOFError, OSError, gzip.BadGzipFile
            LOGGER.warning("invalid GZ file")
    # try zstandard
    if HAS_ZSTD and filecontent[:4] == b"\x28\xb5\x2f\xfd":
        try:
            return zstandard.decompress(filecontent)  # max_output_size=???
        except zstandard.ZstdError:
            LOGGER.warning("invalid ZSTD file")
    # try brotli
    if HAS_BROTLI:
        try:
            return brotli.decompress(filecontent)  # type: ignore[no-any-return]
        except brotli.error:
            pass  # logging.debug('invalid Brotli file')
    # try zlib/deflate
    if HAS_ZLIB:
        try:
            return zlib.decompress(filecontent)
        except zlib.error:
            pass

    # return content unchanged if decompression failed
    return filecontent
```

--------------------------------

TITLE: Python: Check if navigation is still possible
DESCRIPTION: This example demonstrates how to check if there are still navigation pages to visit during a crawl using the `is_still_navigation()` function. It takes the `to_visit` variable as input and returns a boolean value.

SOURCE: https://trafilatura.readthedocs.io/en/latest/crawls

LANGUAGE: Python
CODE:
```
>>> from trafilatura.spider import is_still_navigation

>>> is_still_navigation(to_visit)
# returns True or False
```

--------------------------------

TITLE: Launch Trafilatura GUI
DESCRIPTION: Launches the Trafilatura graphical user interface by executing the 'trafilatura_gui' command in the terminal.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-gui

LANGUAGE: bash
CODE:
```
trafilatura_gui
```

--------------------------------

TITLE: Get Crawl Delay from Robots.txt Rules
DESCRIPTION: Demonstrates how to retrieve the crawl delay (in seconds) specified in a website's robots.txt file using Trafilatura's `get_crawl_delay` function, with an option to provide a default value.

SOURCE: https://trafilatura.readthedocs.io/en/latest/downloads

LANGUAGE: python
CODE:
```
# get the desired information
seconds = get_crawl_delay(rules)
# provide a backup value in case no rule exists (happens quite often)
seconds = get_crawl_delay(rules, default=30)
```

--------------------------------

TITLE: Send Urllib Request with Error Handling
DESCRIPTION: Sends an HTTP GET request using a urllib3 PoolManager, handling potential SSL errors and other exceptions. It streams the response content, enforces a maximum file size, and returns a standardized Response object.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/downloads

LANGUAGE: Python
CODE:
```
def _send_urllib_request(
    url: str, no_ssl: bool, with_headers: bool, config: ConfigParser
) -> Optional[Response]:
    """Internal function to robustly send a request (SSL or not) and return its result."""
    try:
        pool_manager = _initiate_pool(config, no_ssl=no_ssl)

        # execute request, stop downloading as soon as MAX_FILE_SIZE is reached
        response = pool_manager.request(
            "GET",
            url,
            headers=_determine_headers(config),
            retries=_get_retry_strategy(config),
            preload_content=False,
        )
        data = bytearray()
        for chunk in response.stream(2**17):
            data.extend(chunk)
            if len(data) > config.getint("DEFAULT", "MAX_FILE_SIZE"):
                raise ValueError("MAX_FILE_SIZE exceeded")
        response.release_conn()

        # necessary for standardization
        resp = Response(bytes(data), response.status, response.geturl())
        if with_headers:
            resp.store_headers(response.headers)
        return resp

    except urllib3.exceptions.SSLError:
        LOGGER.warning("retrying after SSLError: %s", url)
        return _send_urllib_request(url, True, with_headers, config)
    except Exception as err:
        LOGGER.error("download error: %s %s", url, err)  # sys.exc_info()[0]

    return None
```

--------------------------------

TITLE: Fetch URL with Trafilatura (Python)
DESCRIPTION: Demonstrates how to download a single web page using the `fetch_url` function from the Trafilatura library. It also shows how to perform sequential downloads by iterating through a list of URLs.

SOURCE: https://trafilatura.readthedocs.io/en/latest/downloads

LANGUAGE: Python
CODE:
```
from trafilatura.downloads import fetch_url

# single download
downloaded = fetch_url('https://www.example.org')

# sequential downloads using a list
mylist = ["https://www.example.org", "https://httpbin.org"]
for url in mylist:
    downloaded = fetch_url(url)
    # do something with it

```

--------------------------------

TITLE: Set target language for extraction - Python
DESCRIPTION: You can specify a target language using 2-letter ISO 639-1 codes for extraction. If the detected language doesn't match or the identification component is not installed, there will be no output or filtering.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
result = extract(downloaded, url, target_language="de")
```

--------------------------------

TITLE: Download and Process Web Documents with Wget and Trafilatura
DESCRIPTION: This snippet demonstrates how to download web documents using `wget` with specified options like directory prefix, wait time, and input file. It then shows how to process a directory of archived HTML files using `trafilatura` with options for output directory, XML TEI format, and comment exclusion.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial0

LANGUAGE: bash
CODE:
```
# download if necessary
$ wget --directory-prefix=download/ --wait 5 --input-file=mylist.txt
# process a directory with archived HTML files
$ trafilatura --input-dir download/ --output-dir corpus/ --xmltei --no-comments
```

--------------------------------

TITLE: Extract URLs from Tweets with Regex
DESCRIPTION: Shows how to extract URLs from tweet text using a regular expression in Python. It highlights the need to resolve shortened URLs to get the actual link targets.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/sources

LANGUAGE: python
CODE:
```
Links can be extracted from tweets with a regular expression such as ``re.findall(r'https?://[^ ]+')``. They probably need to be resolved first to get actual link targets and not just shortened URLs (like t.co/…).
```

--------------------------------

TITLE: Create a Random Sample of URLs with shuf and head
DESCRIPTION: This command first shuffles the URLs in `myfile.txt` using `shuf` and then selects the first 100 lines using `head -100`. The resulting random sample is saved to `myfile-random-sample.txt`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial0

LANGUAGE: bash
CODE:
```
$ shuf myfile.txt | head -100 > myfile-random-sample.txt
```

--------------------------------

TITLE: Display Trafilatura Help Message
DESCRIPTION: Displays the help message for the trafilatura command, showing all available options and arguments.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
$ trafilatura -h
```

--------------------------------

TITLE: Trafilatura CLI Usage
DESCRIPTION: This snippet shows the general usage of the Trafilatura command-line interface, outlining the main arguments and options for processing web content. It covers input sources, parallel processing, blacklisting, output, navigation methods, and extraction customization.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
trafilatura [-h] [-i INPUTFILE | --input-dir INPUTDIR | -u URL]
                   [--parallel PARALLEL] [-b BLACKLIST] [--list]
                   [-o OUTPUTDIR] [--backup-dir BACKUP_DIR] [--keep-dirs]
                   [--feed [FEED] | --sitemap [SITEMAP] | --crawl [CRAWL] |
                   --explore [EXPLORE] | --probe [PROBE]] [--archived]
                   [--url-filter URL_FILTER [URL_FILTER ...]] [-f]
                   [--formatting] [--links] [--images] [--no-comments]
                   [--no-tables] [--only-with-metadata] [--with-metadata]
                   [--target-language TARGET_LANGUAGE] [--deduplicate]
                   [--config-file CONFIG_FILE] [--precision] [--recall]
                   [--output-format {csv,json,html,markdown,txt,xml,xmltei} |
                   --csv | --html | --json | --markdown | --xml | --xmltei]
                   [--validate-tei] [-v] [--version]
```

--------------------------------

TITLE: Produce TEI File with Validation (Command Line)
DESCRIPTION: This command-line instruction demonstrates how to use Trafilatura to download a web page, extract its content as a TEI-compliant XML file, and validate it. It utilizes the `--xmltei`, `--validate`, and `--URL` flags.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial2

LANGUAGE: Shell
CODE:
```
trafilatura --xmltei --validate --URL "https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/"

```

--------------------------------

TITLE: Process Image Elements
DESCRIPTION: Processes HTML image elements (`<img>`) by extracting the source URL from attributes like `data-src` or `src`. It also captures the `alt` and `title` attributes for accessibility and display. The function ensures that the source URL is valid and handles relative URLs by prepending 'http://' if they start with '//'. Empty or invalid image elements are returned as None.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def handle_image(element: Optional[_Element]) -> Optional[_Element]:
    """Process image elements and their relevant attributes."""
    if element is None:
        return None

    processed_element = Element(element.tag)

    for attr in ("data-src", "src"):
        src = element.get(attr, "")
        if is_image_file(src):
            processed_element.set("src", src)
            break
    else:
        # take the first corresponding attribute
        for attr, value in element.attrib.items():
            if attr.startswith("data-src") and is_image_file(value):
                processed_element.set("src", value)
                break

    # additional data
    if alt_attr := element.get("alt"):
        processed_element.set("alt", alt_attr)
    if title_attr := element.get("title"):
        processed_element.set("title", title_attr)

    # don't return empty elements or elements without source, just None
    if not processed_element.attrib or not processed_element.get("src"):
        return None

    # post-processing: URLs
    src_attr = processed_element.get("src", "")
    if not src_attr.startswith("http"):
        processed_element.set("src", re.sub(r"^//", "http://", src_attr))

    return processed_element
```

--------------------------------

TITLE: Trafilatura: Process links as raw text
DESCRIPTION: This command processes a list of links from `list.txt` using Trafilatura and saves the output as raw text files in the `txtfiles/` directory.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial0

LANGUAGE: bash
CODE:
```
$ trafilatura -i list.txt -o txtfiles/
```

--------------------------------

TITLE: Trafilatura Utils Module - Initialization and Dependencies
DESCRIPTION: This Python code snippet initializes the `trafilatura.utils` module, defining flags for optional dependencies like gzip, zlib, brotli, and zstandard for compression. It also includes checks for language detection libraries (py3langid, cchardet) and character set normalization (charset_normalizer), along with lxml for HTML parsing. The code sets up logging and defines regular expressions for various text processing tasks, including doctype tags, faulty HTML, HTML tag stripping, line trimming, URL blacklisting, and image file extensions.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: python
CODE:
```
# pylint:disable-msg=E0611,I1101
"""
Module bundling functions related to HTML and text processing,
content filtering and language detection.
"""

try:
    import gzip
    HAS_GZIP = True
except ImportError:
    HAS_GZIP = False

import logging
import re

try:
    import zlib
    HAS_ZLIB = True
except ImportError:
    HAS_ZLIB = False

from functools import lru_cache
from itertools import islice
from typing import Any, List, Literal, Optional, Tuple, Union
from unicodedata import normalize

# response compression
try:
    import brotli  # type: ignore
    HAS_BROTLI = True
except ImportError:
    HAS_BROTLI = False

try:
    import zstandard
    HAS_ZSTD = True
except ImportError:
    HAS_ZSTD = False

# language detection
try:
    import py3langid  # type: ignore
    LANGID_FLAG = True
except ImportError:
    LANGID_FLAG = False

# CChardet is faster and can be more accurate
try:
    from cchardet import detect as cchardet_detect  # type: ignore
except ImportError:
    cchardet_detect = None

from charset_normalizer import from_bytes
from lxml.etree import _Element
from lxml.html import HtmlElement, HTMLParser, fromstring
# response types
from urllib3.response import HTTPResponse


LOGGER = logging.getLogger(__name__)

UNICODE_ALIASES = {'utf-8', 'utf_8'}

DOCTYPE_TAG = re.compile("^< ?! ?DOCTYPE.+?/ ?>", re.I)
FAULTY_HTML = re.compile(r"(<html.*?)\s*/>", re.I)
HTML_STRIP_TAGS = re.compile(r'(<!--.*?-->|<[^>]*>)')

# note: htmldate could use HTML comments
# huge_tree=True, remove_blank_text=True
HTML_PARSER = HTMLParser(collect_ids=False, default_doctype=False, encoding='utf-8', remove_comments=True, remove_pis=True)

LINES_TRIMMING = re.compile(r'(?<![p{P}>])\n', flags=re.UNICODE|re.MULTILINE)

URL_BLACKLIST_REGEX = re.compile(r'^https?://|/+$')

# Regex to check image file extensions
IMAGE_EXTENSION = re.compile(r'[^\s]+\.(avif|bmp|gif|hei[cf]|jpe?g|png|webp)(\b|$)'

FORMATTING_PROTECTED = {'cell', 'head', 'hi', 'item', 'p', 'quote', 'ref', 'td'}
SPACING_PROTECTED = {'code', 'pre'}

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Language
TARGET_LANG_ATTRS = ('http-equiv="content-language"', 'property="og:locale"')
RE_HTML_LANG = re.compile(r'([a-z]{2})')

# Mostly filters for social media
RE_FILTER = re.compile(r'\W*(Drucken|E-?Mail|Facebook|Flipboard|Google|Instagram|'
                        'Linkedin|Mail|PDF|Pinterest|Pocket|Print|QQ|Reddit|Twitter|'
                        'WeChat|WeiBo|Whatsapp|Xing|Mehr zum Thema:?|More on this.{,8}$)$',
                       flags=re.IGNORECASE)

```

--------------------------------

TITLE: Discover Feeds with Trafilatura
DESCRIPTION: This demonstrates how to use Trafilatura to discover and process content from web feeds (Atom and RSS). It shows how to automatically detect feeds from a homepage, use a known feed URL, and process a list of feeds in parallel.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
# automatically detecting feeds starting from the homepage
$ trafilatura --feed "https://www.dwds.de/" --list

# already known feed
$ trafilatura --feed "https://www.dwds.de/api/feed/themenglossar/Corona" --list

# processing a list in parallel
$ trafilatura -i mylist.txt --feed --list
```

--------------------------------

TITLE: Make JSON API Request via Command-line
DESCRIPTION: Demonstrates sending a POST request to the Trafilatura API using `curl` on the command-line. It specifies the target URL and requests the output in XML format.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-api

LANGUAGE: bash
CODE:
```
$ curl -X POST "https://trafilatura.mooo.com/extract-demo" \
       -H "content-type: application/json" \
       --data '{ "url": "https://example.org", "args": { "output_format": "xml" } }'

```

--------------------------------

TITLE: Collecting Web Pages with Python using RSS/Atom Feeds
DESCRIPTION: This tutorial details how to collect web pages using RSS and Atom feeds with Python. It's essential for syndication and content aggregation workflows.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorials

LANGUAGE: Python
CODE:
```
# Conceptual example using a feed parsing library like 'feedparser'
import feedparser

def get_links_from_feed(feed_url):
    feed = feedparser.parse(feed_url)
    links = []
    for entry in feed.entries:
        if 'link' in entry:
            links.append(entry.link)
    return links

# Example usage:
# rss_feed_url = 'http://example.com/feed.xml'
# page_links = get_links_from_feed(rss_feed_url)
# print(page_links)
```

--------------------------------

TITLE: Comparing Versions of Archived Web Pages
DESCRIPTION: This resource from GLAM-Workbench provides a method to compare two versions of an archived web page. It's useful for tracking changes and understanding content evolution.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorials

LANGUAGE: Python
CODE:
```
# Conceptual code snippet for comparing web page versions
# This might involve fetching two versions and using a diffing library
# import difflib

# def compare_page_versions(url1, url2):
#     try:
#         response1 = requests.get(url1)
#         response2 = requests.get(url2)
#         
#         # Extract text content from both versions (e.g., using Trafilatura)
#         text1 = trafilatura.extract(response1.text) or ""
#         text2 = trafilatura.extract(response2.text) or ""
#         
#         # Use difflib for comparison
#         diff = difflib.unified_diff(
#             text1.splitlines(keepends=True),
#             text2.splitlines(keepends=True),
#             fromfile='Version 1',
#             tofile='Version 2'
#         )
#         
#         return "".join(diff)
#         
#     except Exception as e:
#         return f"Error comparing pages: {e}"

# url_v1 = 'http://example.com/archive/v1'
# url_v2 = 'http://example.com/archive/v2'
# comparison_result = compare_page_versions(url_v1, url_v2)
# print(comparison_result)
```

--------------------------------

TITLE: Initialize Extractor with Options
DESCRIPTION: This snippet shows how to initialize the Extractor class with various configuration options. It handles deprecations and regroups parameters for extraction, including output format, speed, precision, content inclusion, language, and metadata settings.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/core

LANGUAGE: Python
CODE:
```
if not options or not isinstance(options, Extractor):
        options = Extractor(
            config=config,
            output_format=output_format,
            fast=fast,
            precision=favor_precision,
            recall=favor_recall,
            comments=include_comments,
            formatting=include_formatting,
            links=include_links,
            images=include_images,
            tables=include_tables,
            dedup=deduplicate,
            lang=target_language,
            url=url,
            with_metadata=with_metadata,
            only_with_metadata=only_with_metadata,
            author_blacklist=author_blacklist,
            url_blacklist=url_blacklist,
            date_params=date_extraction_params,
        )
```

--------------------------------

TITLE: Trafilatura CLI Basic Output
DESCRIPTION: Demonstrates basic command-line usage of Trafilatura to extract text from a list of URLs and save the output to a directory, with a backup directory for HTML files.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/downloads

LANGUAGE: bash
CODE:
```
$ trafilatura -i list.txt -o txtfiles/ --backup-dir htmlbackup/
```

--------------------------------

TITLE: Troubleshoot Trafilatura GUI on macOS (Python)
DESCRIPTION: Provides steps to troubleshoot Trafilatura GUI issues on macOS by running the interface script directly from the cloned repository and configuring the virtual environment.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-gui

LANGUAGE: bash
CODE:
```
python trafilatura_gui/interface.py
```

--------------------------------

TITLE: Collect Web Pages using RSS/Atom Feeds with Python
DESCRIPTION: This tutorial demonstrates how to use RSS and Atom feeds to collect web pages with Python. It covers the process of parsing feed data to retrieve URLs and download content.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorials

LANGUAGE: Python
CODE:
```
import feedparser
from trafilatura import fetch_url, extract

feed_url = 'http://example.com/feed.xml' # Replace with the actual feed URL

# Parse the feed
feed = feedparser.parse(feed_url)

# Iterate through feed entries and extract content
for entry in feed.entries:
    if 'link' in entry:
        url = entry.link
        print(f'Fetching content from: {url}')
        html = fetch_url(url)
        main_text = extract(html)
        if main_text:
            print(f'Extracted text: {main_text[:100]}...') # Print first 100 chars
        else:
            print('No text extracted.')
```

--------------------------------

TITLE: Discover Sitemap Links with Trafilatura CLI
DESCRIPTION: This command uses Trafilatura's `--sitemap` option to discover links from a given URL, typically a homepage or an XML sitemap. The `--list` option ensures that only the discovered URLs are outputted.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial0

LANGUAGE: bash
CODE:
```
$ trafilatura --sitemap "https://www.sitemaps.org/" --list
```

--------------------------------

TITLE: Tokenize text with SoMaJo
DESCRIPTION: Concatenates all text files from a directory and tokenizes the combined text using the SoMaJo tokenizer. The output is saved to a tokens.txt file.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial1

LANGUAGE: bash
CODE:
```
$ cat txtfiles/*.txt > txtfiles/all.txt
$ somajo-tokenizer txtfiles/all.txt > tokens.txt
```

--------------------------------

TITLE: Trafilatura: Process links as XML
DESCRIPTION: This command processes a list of links from `list.txt` using Trafilatura and saves the output in XML format in the `xmlfiles/` directory.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial0

LANGUAGE: bash
CODE:
```
$ trafilatura --xml -i list.txt -o xmlfiles/
```

--------------------------------

TITLE: Trafilatura CLI: Display Help Message
DESCRIPTION: Illustrates how to display the help message for the Trafilatura command-line tool to see available options.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-cli

LANGUAGE: bash
CODE:
```
$ trafilatura -h
```

--------------------------------

TITLE: Initiate Urllib3 Pool Manager
DESCRIPTION: Creates and returns a urllib3 PoolManager for making HTTP requests. It handles SSL certificate verification based on the `no_ssl` flag and caches the pool manager.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/downloads

LANGUAGE: Python
CODE:
```
def _initiate_pool(
    config: ConfigParser, no_ssl: bool = False
) -> Union[urllib3.PoolManager, Any]:
    """Create a urllib3 pool manager according to options in the config file and HTTPS setting."""
    global HTTP_POOL, NO_CERT_POOL
    pool = NO_CERT_POOL if no_ssl else HTTP_POOL

    if not pool:
        # define settings
        pool = create_pool(
            timeout=config.getint("DEFAULT", "DOWNLOAD_TIMEOUT"),
            ca_certs=None if no_ssl else certifi.where(),
            cert_reqs="CERT_NONE" if no_ssl else "CERT_REQUIRED",
        )
        # update variables
        if no_ssl:
            NO_CERT_POOL = pool
        else:
            HTTP_POOL = pool

    return pool
```

--------------------------------

TITLE: Evaluating Scraping and Text Extraction Tools with Python
DESCRIPTION: This tutorial focuses on evaluating different scraping and text extraction tools using Python. It provides insights into performance comparison and selection criteria for web scraping projects.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorials

LANGUAGE: Python
CODE:
```
# Conceptual example for evaluating scraping tools
import time
import requests

def evaluate_tool(url, extraction_function):
    start_time = time.time()
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Raise an exception for bad status codes
        extracted_text = extraction_function(response.text)
        end_time = time.time()
        return {
            'success': True,
            'time': end_time - start_time,
            'text_length': len(extracted_text) if extracted_text else 0
        }
    except Exception as e:
        end_time = time.time()
        return {'success': False, 'error': str(e), 'time': end_time - start_time}

# Example usage with a placeholder extraction function
# def my_trafilatura_extract(html):
#     # ... use trafilatura.extract(html) ...
#     return extracted_text

# results = evaluate_tool('http://example.com', my_trafilatura_extract)
# print(results)
```

--------------------------------

TITLE: Configure Trafilatura Extraction Options
DESCRIPTION: Demonstrates how to set formatting and source options for Trafilatura's extraction process. These options can be passed to extraction functions to customize the output.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
>>> options.formatting = True
>>> options.source = "My Source"
>>> extract(my_doc, options=options)
```

--------------------------------

TITLE: Process links with Trafilatura
DESCRIPTION: Processes a list of URLs from an input file and saves the extracted content. Supports outputting as raw text or XML files.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial1

LANGUAGE: bash
CODE:
```
$ trafilatura -i list.txt -o txtfiles       # output as raw text
$ trafilatura --xml -i list.txt -o xmlfiles # output in XML format
```

--------------------------------

TITLE: Fetch URL with Archive Snapshot (Python)
DESCRIPTION: This Python code snippet demonstrates how to fetch a URL, specifically targeting an archived version if the initial download fails. It constructs a new URL pointing to the Wayback Machine's archive.

SOURCE: https://trafilatura.readthedocs.io/en/latest/troubleshooting

LANGUAGE: Python
CODE:
```
if downloaded is None:
    new_url = "https://web.archive.org/web/20/" + url
    downloaded = fetch_url(new_url)
```

--------------------------------

TITLE: Process a List of Links with Trafilatura Command-Line
DESCRIPTION: Shows how to use the Trafilatura command-line tool to process a list of URLs provided in a text file. This enables batch downloading and extraction from multiple web sources.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage

LANGUAGE: bash
CODE:
```
trafilatura --input-file links.txt --output-dir downloaded_pages/
```

--------------------------------

TITLE: Creating URL Lists from DWDS for Trafilatura
DESCRIPTION: This part of the tutorial explains how to export URLs in a bundled format (TSV) from DWDS web corpora. These URL lists can then be downloaded and used as input for Trafilatura. The process involves opening the exported file in spreadsheet software and copying the URL column into a TXT file.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial-dwds

LANGUAGE: text
CODE:
```
Nachdem Sie die CSV- oder TSV-Datei mit der Tabellenkalkulationssoftware Ihrer Wahl geöffnet haben, können Sie die URL-Spalte auswählen und in einer TXT-Datei kopieren, die Sie als Eingabe für _Trafilatura_ verwenden werden (siehe unten).
```

--------------------------------

TITLE: Fetch and Extract Web Content with Trafilatura (Python)
DESCRIPTION: Demonstrates how to use the Trafilatura Python package to fetch content from a URL and extract the main text and comments. This involves importing the library, calling the fetch_url function, and then using the extract function on the downloaded content.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/index

LANGUAGE: python
CODE:
```
import trafilatura
downloaded = trafilatura.fetch_url('https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/')
trafilatura.extract(downloaded)
# outputs main content and comments as plain text ...
```

--------------------------------

TITLE: Fetch URL and Extract Metadata
DESCRIPTION: Shows how to download a webpage using `fetch_url` and then extract metadata using `bare_extraction`. It illustrates handling cases where metadata is missing and how providing the URL can improve extraction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
# define a URL and download the example
>>> url = "https://web.archive.org/web/20210613232513/https://www.thecanary.co/feature/2021/05/19/another-by-election-headache-is-incoming-for-keir-starmer/"
>>> downloaded = fetch_url(url)

# content discarded since necessary metadata couldn't be extracted
>>> bare_extraction(downloaded, only_with_metadata=True)
>>>

# date found in URL, extraction successful
>>> bare_extraction(downloaded, only_with_metadata=True, url=url)
```

--------------------------------

TITLE: Download and Extract Text from URL (Plain Text)
DESCRIPTION: Downloads a web page from the specified URL and extracts the main content and comments as plain text.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
$ trafilatura -u "https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/"
```

--------------------------------

TITLE: Extracting Data with Custom Configuration
DESCRIPTION: Demonstrates how to use Trafilatura's `extract` function with a custom configuration file. This allows for fine-tuning extraction parameters by loading settings from a specified file.

SOURCE: https://trafilatura.readthedocs.io/en/latest/settings

LANGUAGE: Python
CODE:
```
from trafilatura import extract
from trafilatura.settings import use_config

# Load new settings by providing a file name
newconfig = use_config("myfile.cfg")

# Use with a previously downloaded document
extract(downloaded, config=newconfig)

# Provide a file name directly (can be slower)
extract(downloaded, settingsfile="myfile.cfg")
```

--------------------------------

TITLE: Web Scraping and Metadata Extraction with R
DESCRIPTION: This resource covers web scraping and text/metadata extraction specifically using the R programming language. It's aimed at R users interested in web data.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorials

LANGUAGE: R
CODE:
```
# Conceptual example using R packages like 'rvest' and 'xml2'
# install.packages(c('rvest', 'xml2'))
library(rvest)
library(xml2)

# url <- 'http://example.com'
# page <- read_html(url)

# # Extracting text content (example using CSS selectors)
# main_text <- html_text(html_nodes(page, 'p'))
# print(head(main_text))

# # Extracting metadata (example for title)
# page_title <- html_text(html_node(page, 'title'))
# print(page_title)
```

--------------------------------

TITLE: Set Output Format via Option
DESCRIPTION: Sets the output format using the --output-format option, allowing selection from csv, json, html, markdown, txt, xml, xmltei.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
# Example usage (assuming a URL is provided or piped):
# trafilatura --output-format json -u "URL"
```

--------------------------------

TITLE: Load URLs for Download with Back-off
DESCRIPTION: Determines the threading strategy and retrieves URLs for download from a UrlStore, respecting domain-based back-off rules. It allows specifying a sleep time to manage the download rate and continues until all URLs are processed or the store is marked as done.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/downloads

LANGUAGE: Python
CODE:
```
def load_download_buffer(
    url_store: UrlStore,
    sleep_time: float = 5.0,
) -> Tuple[List[str], UrlStore]:
    """Determine threading strategy and draw URLs respecting domain-based back-off rules."""
    while True:
        bufferlist = url_store.get_download_urls(time_limit=sleep_time, max_urls=10**5)
        if bufferlist or url_store.done:
            break
        sleep(sleep_time)
    return bufferlist, url_store
```

--------------------------------

TITLE: Discover Sitemaps with Trafilatura
DESCRIPTION: Perform link discovery using sitemaps. Use `--sitemap` with a sitemap URL to find all potential pages. The `--list` option outputs the discovered links, which can be redirected to a file. Supports filtering by target language.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-cli

LANGUAGE: bash
CODE:
```
# run link discovery through a sitemap for sitemaps.org and store the resulting links in a file
$ trafilatura --sitemap "https://www.sitemaps.org/" --list > mylinks.txt

# using an already known sitemap URL
$ trafilatura --sitemap "https://www.sitemaps.org/sitemap.xml" --list

# targeting webpages in German
$ trafilatura --sitemap "https://www.sitemaps.org/" --list --target-language "de"


```

--------------------------------

TITLE: Perform Simple Downloads with fetch_url()
DESCRIPTION: Demonstrates how to download a single web page or multiple pages sequentially using the fetch_url() function from the trafilatura.downloads module. This method is suitable for single-threaded downloads.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/downloads

LANGUAGE: python
CODE:
```
from trafilatura.downloads import fetch_url

# single download
downloaded = fetch_url('https://www.example.org')

# sequential downloads using a list
mylist = ["https://www.example.org", "https://httpbin.org"]
for url in mylist:
    downloaded = fetch_url(url)
    # do something with it
```

--------------------------------

TITLE: Tokenize and Aggregate Text with SoMaJo and Bash
DESCRIPTION: This sequence of commands first concatenates all text files from a directory into a single file ('all.txt'). It then uses the 'somajo-tokenizer' to split the text into words and sentences, saving the output to 'tokens.txt'. SoMaJo is a Python-based tokenizer suitable for German and English texts.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial1

LANGUAGE: bash
CODE:
```
$ cat txtfiles/*.txt > txtfiles/all.txt
$ somajo-tokenizer txtfiles/all.txt > tokens.txt
```

--------------------------------

TITLE: Trafilatura CLI Usage
DESCRIPTION: This snippet displays the main help message for the Trafilatura command-line tool, outlining all available optional arguments for processing web content.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-cli

LANGUAGE: bash
CODE:
```
trafilatura [-h] [-i INPUTFILE | --input-dir INPUTDIR | -u URL] [--parallel PARALLEL] [-b BLACKLIST] [--list] [-o OUTPUTDIR] [--backup-dir BACKUP_DIR] [--keep-DIRS] [--feed [FEED] | --sitemap [SITEMAP] | --crawl [CRAWL] | --explore [EXPLORE] | --probe [PROBE]] [--archived] [--url-filter URL_FILTER [URL_FILTER ...]] [-f] [--formatting] [--links] [--images] [--no-comments] [--no-tables] [--only-with-metadata] [--with-metadata] [--target-language TARGET_LANGUAGE] [--deduplicate] [--config-file CONFIG_FILE] [--precision] [--recall] [--output-format {csv,json,html,markdown,txt,xml,xmltei} | --csv | --html | --json | --markdown | --xml | --xmltei] [--validate-tei] [-v] [--version]
```

--------------------------------

TITLE: Process List of Links with Trafilatura
DESCRIPTION: Bulk download and process a list of URLs from a file. Use `-i` or `--input-file` for the list of links and `-o` or `--output-dir` for storing results. Trafilatura includes default delays between requests to respect scraping etiquette.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-cli

LANGUAGE: bash
CODE:
```
$ trafilatura -i list.txt -o txtfiles/              # output as raw text
$ trafilatura --xml -i list.txt -o xmlfiles/        # output in XML format


```

LANGUAGE: bash
CODE:
```
$ trafilatura --input-file links.txt --output-dir converted/ --backup-dir html-sources/ --xml
```

--------------------------------

TITLE: Extract Web Content using Trafilatura (Command-Line)
DESCRIPTION: Shows how to use the Trafilatura command-line interface to download and extract content from a given URL. The output is the main content and comments in plain text format.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/index

LANGUAGE: bash
CODE:
```
$ trafilatura -u "https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/"
# outputs main content and comments as plain text ...
```

--------------------------------

TITLE: Set SOCKS Proxy for Downloads (Shell)
DESCRIPTION: Demonstrates how to configure Trafilatura to use a SOCKS proxy for all downloads by setting the `http_proxy` environment variable before running the script.

SOURCE: https://trafilatura.readthedocs.io/en/latest/downloads

LANGUAGE: Shell
CODE:
```
# set socks proxy
export http_proxy=socks5://PROXYHOST:PROXYPORT

```

--------------------------------

TITLE: Parallel Downloads with Trafilatura Threads (Python)
DESCRIPTION: Shows how to perform multi-threaded downloads using Trafilatura's `buffered_downloads` and `load_download_buffer` functions. This method is efficient for fetching pages from different websites concurrently and includes throttling.

SOURCE: https://trafilatura.readthedocs.io/en/latest/downloads

LANGUAGE: Python
CODE:
```
from trafilatura.downloads import add_to_compressed_dict, buffered_downloads, load_download_buffer

# list of URLs
mylist = ['https://www.example.org', 'https://www.httpbin.org/html']
# number of threads to use
threads = 4

# converted the input list to an internal format
url_store = add_to_compressed_dict(mylist)
# processing loop
while url_store.done is False:
    bufferlist, url_store = load_download_buffer(url_store, sleep_time=5)
    # process downloads
    for url, result in buffered_downloads(bufferlist, threads):
        # do something here
        print(url)
        print(result)

```

--------------------------------

TITLE: Exporting URLs in TSV Format from DWDS
DESCRIPTION: This method allows exporting URLs in a bundled TSV format directly from DWDS. By using a specific query format, users can obtain a list of sources that can be downloaded and used as input for tools like Trafilatura. This is particularly useful for web corpora.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial-dwds

LANGUAGE: url
CODE:
```
https://www.dwds.de/r?q=count%28Patienten+%7C%7C+Patientinnen%29+%23by%5Burl%5D&corpus=corona&date-start=2019&date-end=2020&format=full&sort=date_desc&limit=10
```

--------------------------------

TITLE: Fetch URL with Trafilatura
DESCRIPTION: Downloads a web page from a given URL, handling SSL connections, configuration, and optional extraction options. It returns the decoded HTML content of the page.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/downloads

LANGUAGE: Python
CODE:
```
def fetch_url(
    url: str,
    no_ssl: bool = False,
    config: ConfigParser = DEFAULT_CONFIG,
    options: Optional[Extractor] = None,
) -> Optional[str]:
    """Downloads a web page and seamlessly decodes the response.

    Args:
        url: URL of the page to fetch.
        no_ssl: Do not try to establish a secure connection (to prevent SSLError).

```

--------------------------------

TITLE: Download and Extract Text from URL (XML)
DESCRIPTION: Downloads a web page from the specified URL and extracts the main text with basic XML structure.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
$ trafilatura --xml --URL "https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/"
```

--------------------------------

TITLE: Trafilatura: Discover links using sitemap
DESCRIPTION: This command uses Trafilatura to discover links from a sitemap. The `--sitemap` option specifies the sitemap URL, and `--list` outputs the discovered links.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial0

LANGUAGE: bash
CODE:
```
$ trafilatura --sitemap "https://www.sitemaps.org/" --list
```

--------------------------------

TITLE: Pipe HTML Content via Alternative Syntax
DESCRIPTION: An alternative method to pipe HTML content from 'myfile.html' to trafilatura for processing.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
$ < myfile.html trafilatura
```

--------------------------------

TITLE: Fetch Response Object with Trafilatura (Python)
DESCRIPTION: Illustrates how to use `fetch_response` to retrieve a `Response` object, which contains more details than a simple string. This includes status codes, URLs, raw HTML data, and headers.

SOURCE: https://trafilatura.readthedocs.io/en/latest/downloads

LANGUAGE: Python
CODE:
```
# Response object instead of Unicode string
>>> response = fetch_response('https://www.example.org')
>>> response.status
200
>>> response.url
'https://www.example.org'
>>> response.data
# raw HTML in binary format
>>> response = fetch_response('https://www.example.org', decode=True, with_headers=True)
# headers and html attributes used

```

--------------------------------

TITLE: Trafilatura CLI: Output Formats
DESCRIPTION: Lists the command-line arguments for specifying different output formats for Trafilatura, such as CSV, JSON, XML, etc.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-cli

LANGUAGE: bash
CODE:
```
--csv
--html
--json
--markdown
--xml
--xmltei
--output-format {csv,json,html,markdown,txt,xml,xmltei}
```

--------------------------------

TITLE: Fetch Web Page Response with Trafilatura
DESCRIPTION: Fetches a web page and returns a full response object. It supports decoding data using HTML attributes, handling SSL verification, and optionally keeping track of response headers. Configuration values can be passed for output control.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/downloads

LANGUAGE: Python
CODE:
```
def fetch_response(
    url: str,
    *,
    decode: bool = False,
    no_ssl: bool = False,
    with_headers: bool = False,
    config: ConfigParser = DEFAULT_CONFIG,
) -> Optional[Response]:
    """Downloads a web page and returns a full response object.

    Args:
        url: URL of the page to fetch.
        decode: Use html attribute to decode the data (boolean).
        no_ssl: Don't try to establish a secure connection (to prevent SSLError).
        with_headers: Keep track of the response headers.
        config: Pass configuration values for output control.

    Returns:
        Response object or None in case of failed downloads and invalid results.

    """
    dl_function = _send_urllib_request if not HAS_PYCURL else _send_pycurl_request
    LOGGER.debug("sending request: %s", url)
    response = dl_function(url, no_ssl, with_headers, config)  # Response
    if not response:  # None or ""
        LOGGER.debug("request failed: %s", url)
        return None
    response.decode_data(decode)
    return response
```

--------------------------------

TITLE: Tokenize XML File with somajo-tokenizer
DESCRIPTION: This command uses the somajo-tokenizer to process an XML file. It's the initial step for extracting text content from XML documents before further analysis.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial1

LANGUAGE: shell
CODE:
```
# tokenize a file
$ somajo-tokenizer --xml xmlfiles/filename.xml
```

--------------------------------

TITLE: Download from Internet Archive (Python)
DESCRIPTION: This Python code snippet demonstrates how to use the Internet Archive to retrieve web pages that failed to download directly. It shows a basic structure for handling such cases.

SOURCE: https://trafilatura.readthedocs.io/en/latest/troubleshooting

LANGUAGE: Python
CODE:
```
# url is the target
# downloaded is the result of the download

```

--------------------------------

TITLE: Execute Parallel Downloads with Threads
DESCRIPTION: Illustrates how to perform multi-threaded downloads using Trafilatura's buffered_downloads, add_to_compressed_dict, and load_download_buffer functions. This method enhances efficiency by downloading pages concurrently and includes domain-aware throttling.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/downloads

LANGUAGE: python
CODE:
```
from trafilatura.downloads import add_to_compressed_dict, buffered_downloads, load_download_buffer

# list of URLs
mylist = ['https://www.example.org', 'https://www.httpbin.org/html']
# number of threads to use
threads = 4

# converted the input list to an internal format
url_store = add_to_compressed_dict(mylist)
# processing loop
while url_store.done is False:
    bufferlist, url_store = load_download_buffer(url_store, sleep_time=5)
    # process downloads
    for url, result in buffered_downloads(bufferlist, threads):
        # do something here
        print(url)
        print(result)
```

--------------------------------

TITLE: Set HTTP Proxy for Trafilatura
DESCRIPTION: Configures the HTTP proxy for Trafilatura using environment variables, specifying the proxy host, port, and authentication credentials.

SOURCE: https://trafilatura.readthedocs.io/en/latest/downloads

LANGUAGE: bash
CODE:
```
export http_proxy=socks5://USER:PASSWORD@PROXYHOST:PROXYPORT
```

--------------------------------

TITLE: Trafilatura CLI: Pipe Custom Download Utility
DESCRIPTION: Shows how to use a custom download utility (like wget) to fetch HTML content and pipe it to Trafilatura for extraction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-cli

LANGUAGE: bash
CODE:
```
$ wget -qO- "https://de.creativecommons.org/index.php/was-ist-cc/" | trafilatura
```

--------------------------------

TITLE: Trafilatura CLI Navigation Options
DESCRIPTION: This snippet outlines the command-line arguments for controlling how Trafilatura discovers and processes web content, including feed parsing, sitemap crawling, and URL filtering.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-cli

LANGUAGE: bash
CODE:
```
--feed [FEED]
look for feeds and/or pass a feed URL as input
--sitemap [SITEMAP]
look for sitemaps for the given website and/or enter a sitemap URL
--crawl [CRAWL]
crawl a fixed number of pages within a website starting from the given URL
--explore [EXPLORE]
explore the given websites (combination of sitemap and crawl)
--probe [PROBE]
probe for extractable content (works best with target language)
--archived
try to fetch URLs from the Internet Archive if downloads fail
--url-filter URL_FILTER [URL_FILTER ...]
only process/output URLs containing these patterns (space-separated strings)
```

--------------------------------

TITLE: Process Files Locally with Trafilatura
DESCRIPTION: Process downloaded HTML files or entire directories using Trafilatura. Specify input directories with `--input-dir` and output directories with `-o` or `--output-dir`. Results are printed to standard output if no output directory is specified.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-cli

LANGUAGE: bash
CODE:
```
$ trafilatura -i list.txt -o txtfiles/              # output as raw text
$ trafilatura --xml -i list.txt -o xmlfiles/        # output in XML format


```

LANGUAGE: bash
CODE:
```
$ trafilatura --input-file links.txt --output-dir converted/ --backup-dir html-sources/ --xml
```

--------------------------------

TITLE: Perform Focused Crawl with Trafilatura
DESCRIPTION: Demonstrates how to set up and initiate a focused crawler using Trafilatura's `focused_crawler()` function. This function integrates necessary components for crawling and can be customized with various arguments like `max_seen_urls` and `lang`. It returns the pages to visit and known links, allowing for step-by-step processing.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/crawls

LANGUAGE: python
CODE:
```
from trafilatura.spider import focused_crawler

# perform the first iteration (will not work with this website, there are no internal links)
>>> to_visit, known_links = focused_crawler("https://example.org", max_seen_urls=1)
```

--------------------------------

TITLE: Fallback Extraction with Justext
DESCRIPTION: The `try_justext` function acts as a second safety net, attempting extraction using the generic justext algorithm. It requires an HTML element, URL, and target language as input.

SOURCE: https://trafilatura.readthedocs.io/en/latest/corefunctions

LANGUAGE: python
CODE:
```
trafilatura.external.try_justext(_tree : HtmlElement_, _url : str_, _target_language : str_) → _Element
```

--------------------------------

TITLE: Replicating BootCaT Method for Web Corpora
DESCRIPTION: This snippet refers to a blog post detailing how to replicate the BootCaT method for building web corpora from search engines. The BootCaT method is a technique used in corpus construction for focused crawling.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/compendium

LANGUAGE: url
CODE:
```
https://adrien.barbaresi.eu/blog/replicate-bootcat-corpus-method.html
```

--------------------------------

TITLE: Pipe Downloaded HTML Content to Trafilatura
DESCRIPTION: Downloads the content of a URL using wget and pipes the output directly to trafilatura for extraction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
$ wget -qO- "https://de.creativecommons.org/index.php/was-ist-cc/" | trafilatura
```

--------------------------------

TITLE: Sample URLs by Domain Name (Python)
DESCRIPTION: Demonstrates how to sample URLs from a list, controlling the number of URLs per domain. The `sample_urls` function from the `courlan` library is used for this purpose. Optional parameters like `exclude_min`, `exclude_max`, `strict`, and `verbose` can be used to fine-tune the sampling process.

SOURCE: https://trafilatura.readthedocs.io/en/latest/url-management

LANGUAGE: Python
CODE:
```
>>> from courlan import sample_urls
>>> my_urls = ['…', '…', '…', ]  # etc.
>>> my_sample = sample_urls(my_urls, 50)
# optional: exclude_min=None, exclude_max=None, strict=False, verbose=False
```

--------------------------------

TITLE: Replicating BootCaT Method for Web Corpora
DESCRIPTION: This snippet refers to a blog post that explains how to replicate the BootCaT method for building web corpora using search engines. The BootCaT method is a technique for focused crawling.

SOURCE: https://trafilatura.readthedocs.io/en/latest/compendium

LANGUAGE: Python
CODE:
```
See blog post Replicating the BootCaT method to build web corpora from search engines
```

--------------------------------

TITLE: Define Publisher String for TEI Header
DESCRIPTION: Constructs a publisher string to be included in the TEI header. It prioritizes using both sitename and hostname if available, otherwise falls back to hostname or sitename. If neither is available, it defaults to 'N/A' and logs a warning. Dependencies include `Document` type and `logging` module.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
import logging
from typing import Optional

# Assuming Document and LOGGER are defined elsewhere

def _define_publisher_string(docmeta: Document) -> str:
    """Construct a publisher string to include in TEI header"""
    if docmeta.hostname and docmeta.sitename:
        publisher = f'{docmeta.sitename.strip()} ({docmeta.hostname})'
    else:
        publisher = docmeta.hostname or docmeta.sitename or 'N/A'
        if LOGGER.isEnabledFor(logging.WARNING) and publisher == 'N/A':
            LOGGER.warning('no publisher for URL %s', docmeta.url)
    return publisher


class Document:
    # Placeholder for Document class definition
    def __init__(self):
        self.hostname = None
        self.sitename = None
        self.url = None

LOGGER = logging.getLogger(__name__)

```

--------------------------------

TITLE: Web Scraping and Text Extraction with Trafilatura
DESCRIPTION: This tutorial focuses on web scraping and text extraction using the Trafilatura library in Python. It highlights the efficiency and speed improvements in recent versions of Trafilatura for these tasks.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorials

LANGUAGE: Python
CODE:
```
from trafilatura import fetch_url, extract

url = 'http://example.com'
html = fetch_url(url)
text = extract(html)

# Trafilatura is optimized for speed and efficiency in scraping and extraction.
```

--------------------------------

TITLE: Improving Web Scraping Speed with Trafilatura
DESCRIPTION: This tutorial discusses methods to make web scraping with Trafilatura faster. It offers practical tips for optimizing performance in large-scale scraping tasks.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorials

LANGUAGE: Python
CODE:
```
# Conceptual example for optimizing Trafilatura usage
# Consider using batch processing or parallel execution for speed improvements
# import trafilatura
# from concurrent.futures import ThreadPoolExecutor

# def process_url(url):
#     try:
#         downloaded = trafilatura.fetch_url(url)
#         return trafilatura.extract(downloaded)
#     except Exception as e:
#         return f'Error processing {url}: {e}'

# urls = ['http://example.com/page1', 'http://example.com/page2']
# with ThreadPoolExecutor(max_workers=5) as executor:
#     results = list(executor.map(process_url, urls))
# print(results)
```

--------------------------------

TITLE: Trafilatura CLI: Extract Main Content
DESCRIPTION: Demonstrates how to extract the main content and comments as plain text from a given URL using the Trafilatura command-line interface.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-cli

LANGUAGE: bash
CODE:
```
$ trafilatura -u "https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/"
```

--------------------------------

TITLE: Trafilatura Core Module Imports
DESCRIPTION: This snippet shows the essential imports for the trafilatura.core module. It includes standard libraries like logging and warnings, typing for advanced type hints, and specific elements from lxml for HTML parsing and XPath operations.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/core

LANGUAGE: python
CODE:
```
# pylint:disable-msg=E0611,I1101
"""
Extraction configuration and processing functions.
"""

import logging
import warnings

from copy import copy, deepcopy
from typing import Any, Dict, Optional, Set, Tuple, Union

from lxml.etree import _Element, Element, XPath, strip_tags
from lxml.html import HtmlElement

```

--------------------------------

TITLE: Add URLs to UrlStore with Filtering
DESCRIPTION: Filters and converts input URLs, then adds them to a domain-aware processing dictionary (UrlStore). It supports blacklisting URLs, filtering by a URL substring, and configuring compression and verbosity for the store.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/downloads

LANGUAGE: Python
CODE:
```
def add_to_compressed_dict(
    inputlist: List[str],
    blacklist: Optional[Set[str]] = None,
    url_filter: Optional[str] = None,
    url_store: Optional[UrlStore] = None,
    compression: bool = False,
    verbose: bool = False,
) -> UrlStore:
    """Filter, convert input URLs and add them to domain-aware processing dictionary"""
    if url_store is None:
        url_store = UrlStore(compressed=compression, strict=False, verbose=verbose)

    inputlist = list(dict.fromkeys(inputlist))

    if blacklist:
        inputlist = [
            u for u in inputlist if URL_BLACKLIST_REGEX.sub("", u) not in blacklist
        ]

    if url_filter:
        inputlist = [u for u in inputlist if any(f in u for f in url_filter)]

    url_store.add_urls(inputlist)
    return url_store
```

--------------------------------

TITLE: Process Files Locally with Trafilatura Command-Line
DESCRIPTION: Explains how to use the Trafilatura command-line interface to process local HTML files. This is useful for batch processing of downloaded content.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage

LANGUAGE: bash
CODE:
```
trafilatura --output-format=txt --output-path=output.txt input.html
```

--------------------------------

TITLE: Process Links from a File to XML Output
DESCRIPTION: This command processes a list of URLs from `list.txt` using Trafilatura, specifying the output format as XML using the `--xml` flag. The extracted content is saved to the directory `xmlfiles/`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial0

LANGUAGE: bash
CODE:
```
$ trafilatura --xml -i list.txt -o xmlfiles/
```

--------------------------------

TITLE: Fetch Web Page Response with trafilatura
DESCRIPTION: Downloads a web page and returns a full response object. Supports decoding, SSL configuration, and header tracking. Accepts a URL and optional configuration.

SOURCE: https://trafilatura.readthedocs.io/en/latest/corefunctions

LANGUAGE: Python
CODE:
```
trafilatura.fetch_response(_url: str_, _*_ , _decode: bool = False_, _no_ssl: bool = False_, _with_headers: bool = False_, _config: ~configparser.ConfigParser = <configparser.ConfigParser object>_) → Response | None
```

--------------------------------

TITLE: Import Core Libraries for Trafilatura Extractor
DESCRIPTION: Imports necessary libraries for the Trafilatura extractor, including logging, regular expressions, deep copy, typing, and lxml elements for HTML parsing and manipulation.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: python
CODE:
```
import logging
import re

from copy import deepcopy
from typing import Any, Optional, Tuple, Set, Union

from lxml.etree import _Element, Element, SubElement, strip_elements, strip_tags, tostring
from lxml.html import HtmlElement
```

--------------------------------

TITLE: Extract Metadata with URL
DESCRIPTION: Illustrates how to use the `bare_extraction` function, passing both the downloaded content and the URL to successfully extract metadata, especially when it might be present in the URL itself.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
>>> url = "https://web.archive.org/web/20210613232513/https://www.thecanary.co/feature/2021/05/19/another-by-election-headache-is-incoming-for-keir-starmer/"
>>> downloaded = fetch_url(url)
>>> bare_extraction(downloaded, only_with_metadata=True, url=url)
```

--------------------------------

TITLE: Output as XML
DESCRIPTION: Specifies that the extracted text should be formatted as XML.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
# Example usage (assuming a URL is provided or piped):
# trafilatura --xml -u "URL"
```

--------------------------------

TITLE: Load and Validate HTML Tree
DESCRIPTION: This snippet demonstrates loading an HTML tree from content and performing initial validation. It includes error handling for empty trees and checks the HTML language against the target language if specified and fast mode is enabled or language detection is available.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/core

LANGUAGE: Python
CODE:
```
# load the HTML tree
        tree = load_html(filecontent)
        if tree is None:
            LOGGER.error("empty HTML tree: %s", url)
            raise ValueError

        # quick and dirty HTML lang check
        if options.lang and (options.fast or not LANGID_FLAG):
            if check_html_lang(tree, options.lang) is False:
                LOGGER.error("wrong HTML meta language: %s", options.source)
                raise ValueError
```

--------------------------------

TITLE: Trafilatura Spacing Downloads with sleep_time
DESCRIPTION: Illustrates how to use the `load_download_buffer` function in Trafilatura to manage download intervals between requests for the same domain, preventing server overload and potential bans.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/downloads

LANGUAGE: python
CODE:
```
from trafilatura.downloads import load_download_buffer

# 30 seconds is a safe choice
mybuffer, threads, domain_dict, backoff_dict = load_download_buffer(url_store, sleep_time=30)
# then proceed as instructed above...
```

--------------------------------

TITLE: Adapt Trafilatura Settings in Python
DESCRIPTION: Demonstrates how to modify Trafilatura's default configuration in Python by changing the MIN_OUTPUT_SIZE setting. It shows how a very short HTML input is discarded with the modified setting, while default extraction still works.

SOURCE: https://trafilatura.readthedocs.io/en/latest/settings

LANGUAGE: python
CODE:
```
from copy import deepcopy
from trafilatura import extract
from trafilatura.settings import DEFAULT_CONFIG

# a very short HTML file
my_html = "<html><body><p>Text.</p></body></html>"

# load the configuration and change the minimum output length
my_config = deepcopy(DEFAULT_CONFIG)
my_config['DEFAULT']['MIN_OUTPUT_SIZE'] = '1000'

# apply new settings, extraction will fail
extract(my_html, config=my_config)

# default extraction works
extract(my_html)
```

--------------------------------

TITLE: Trafilatura XML Output and HTML Backup
DESCRIPTION: This command uses Trafilatura to process a list of URLs, outputting the extracted data in XML format and backing up the original HTML files to a specified directory. It's useful for creating structured XML datasets and preserving source HTML.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial0

LANGUAGE: bash
CODE:
```
trafilatura --xml -i list.txt -o xmlfiles/ --backup-dir htmlfiles/
```

--------------------------------

TITLE: Save token frequencies to CSV
DESCRIPTION: Sorts and counts token frequencies, then formats the output with a tab separator and saves it to a CSV file named frequencies.csv in the txtfiles directory.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial1

LANGUAGE: bash
CODE:
```
$ < tokens.txt sort | uniq -c | sort -nrk1 | sed -e "s|^ *||g" -e  "s| |\t|" > txtfiles/frequencies.csv
```

--------------------------------

TITLE: Parse Configuration for HTTP Headers
DESCRIPTION: Reads user-agent strings and cookie information from a configuration file. It supports loading multiple user-agents and a single cookie string.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/downloads

LANGUAGE: Python
CODE:
```
# @lru_cache(maxsize=2)
def _parse_config(config: ConfigParser) -> Tuple[Optional[List[str]], Optional[str]]:
    """Read and extract HTTP header strings from the configuration file."""
    # load a series of user-agents
    myagents = config.get("DEFAULT", "USER_AGENTS", fallback="").strip()
    agent_list = myagents.splitlines() if myagents else None
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
    # todo: support for several cookies?
    mycookie = config.get("DEFAULT", "COOKIE") or None
    return agent_list, mycookie
```

--------------------------------

TITLE: Python Robots.txt Parsing with urllib
DESCRIPTION: Shows how to use Python's `urllib.robotparser` to fetch and parse a website's robots.txt file to check crawling permissions for specific URLs and user agents.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/downloads

LANGUAGE: python
CODE:
```
import urllib.robotparser
from trafilatura import get_crawl_delay

# define a website to look for rules
base_url = 'https://www.example.org'

# load the necessary components, fetch and parse the file
rules = urllib.robotparser.RobotFileParser()
rules.set_url(base_url + '/robots.txt')
rules.read()

# determine if a page can be fetched by all crawlers
rules.can_fetch("*", "https://www.example.org/page1234.html")
# returns True or False
```

--------------------------------

TITLE: Trafilatura Metadata Options
DESCRIPTION: Options to control metadata extraction and inclusion in the output. `--with-metadata` extracts metadata, while `--only-with-metadata` filters for documents that already possess title, URL, and date.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
--only-with-metadata  only output those documents with title, URL and date
  --with-metadata       extract and add metadata to the output
```

--------------------------------

TITLE: Handle Web Response
DESCRIPTION: Processes a web response by first checking its suitability and then returning either the decoded HTML content or the raw response object. Returns None if the response is not suitable.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/downloads

LANGUAGE: Python
CODE:
```
def _handle_response(
    url: str, response: Response, decode: bool, options: Extractor
) -> Optional[Union[Response, str]]:  # todo: only return str
    """Internal function to run safety checks on response result."""
    if _is_suitable_response(url, response, options):
        return response.html if decode else response
    # catchall
    return None
```

--------------------------------

TITLE: Troubleshoot Mac OS X GUI Issues
DESCRIPTION: Provides solutions for common Mac OS X issues when running the Trafilatura GUI, such as 'This program needs access to the screen'. It suggests cloning the repository and running the interface script or configuring a virtual environment.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-gui

LANGUAGE: bash
CODE:
```
python trafilatura_gui/interface.py
```

--------------------------------

TITLE: Filter Links for Web Crawling with Python
DESCRIPTION: This tutorial covers techniques for filtering links to gather specific texts from the web using Python. It explains how to refine web crawling processes by selecting relevant URLs based on various criteria.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorials

LANGUAGE: Python
CODE:
```
from trafilatura import fetch_url, extract, set_logging, logging_level
from trafilatura.filters import filter_links

url = 'http://...' # Replace with the actual URL

# Download the page
html = fetch_url(url)

# Extract all links from the page
links = filter_links(html)

# You can further filter these links based on your criteria
# For example, keeping only links that contain a specific keyword:
filtered_links = [link for link in links if 'keyword' in link]

# Process the filtered links
for link in filtered_links:
    print(f'Processing link: {link}')
    # Further extraction or processing can be done here
```

--------------------------------

TITLE: Randomly Shuffle URLs with shuf
DESCRIPTION: This command shuffles the order of URLs in `myfile.txt` using the `shuf` utility and saves the randomly ordered list to `myfile-random.txt`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial0

LANGUAGE: bash
CODE:
```
shuf myfile.txt > myfile-random.txt
```

--------------------------------

TITLE: Output as Markdown
DESCRIPTION: Specifies that the extracted text should be formatted as Markdown. This format automatically includes text formatting.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
# Example usage (assuming a URL is provided or piped):
# trafilatura --markdown -u "URL"
```

--------------------------------

TITLE: Filtering Links for Text Gathering with Python
DESCRIPTION: This tutorial covers techniques for filtering links to gather texts from the web using Python. It's useful for building focused web corpora and managing crawling processes.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorials

LANGUAGE: Python
CODE:
```
# Conceptual example for link filtering
from urllib.parse import urlparse

def is_valid_link(link, base_domain):
    parsed_link = urlparse(link)
    # Check if the link belongs to the same domain or a subdomain
    return parsed_link.netloc.endswith(base_domain)

# Example usage:
# all_links = ['http://example.com/page1', 'http://example.com/about', 'http://other.com']
# base = 'example.com'
# filtered_links = [link for link in all_links if is_valid_link(link, base)]
# print(filtered_links)
```

--------------------------------

TITLE: Command-line: Basic Extraction
DESCRIPTION: Illustrates how to perform basic text extraction from a URL directly on the command-line using Trafilatura. It outputs main content and comments as plain text.

SOURCE: https://trafilatura.readthedocs.io/en/latest/quickstart

LANGUAGE: Shell
CODE:
```
$ trafilatura -u "https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/"
```

--------------------------------

TITLE: Produce TEI File with Validation (Python)
DESCRIPTION: This Python code snippet shows how to fetch a URL, extract information, and convert it into a TEI-compliant XML file with validation enabled. It uses `trafilatura.fetch_url` and `trafilatura.extract` with `output_format='xmltei'` and `tei_validation=True`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial2

LANGUAGE: Python
CODE:
```
# load the necessary components
from trafilatura import fetch_url, extract

# download a file
downloaded = fetch_url('https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/')

# extract information as XML TEI and validate the result
result = extract(downloaded, output_format='xmltei', tei_validation=True)

```

--------------------------------

TITLE: Access Response Object with fetch_response()
DESCRIPTION: Shows how to use fetch_response() to retrieve more detailed information about a web page download, including status, URL, raw data, and headers. The decode and with_headers parameters can be used to control the output.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/downloads

LANGUAGE: python
CODE:
```
# Response object instead of Unicode string
>>> response = fetch_response('https://www.example.org')
>>> response.status
200
>>> response.url
'https://www.example.org'
>>> response.data
# raw HTML in binary format
>>> response = fetch_response('https://www.example.org', decode=True, with_headers=True)
# headers and html attributes used
```

--------------------------------

TITLE: Process Links from a File to Raw Text Output
DESCRIPTION: This command processes a list of URLs from `list.txt` using Trafilatura. It outputs the extracted content in raw text format and saves it to the directory `txtfiles/`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial0

LANGUAGE: bash
CODE:
```
$ trafilatura -i list.txt -o txtfiles/
```

--------------------------------

TITLE: Sample URLs with Courlan (Python)
DESCRIPTION: The `sample_urls` function from courlan allows for sampling a specified number of URLs from a list, helping to control the distribution of URLs from different domains.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/url-management

LANGUAGE: python
CODE:
```
from courlan import sample_urls
my_urls = ['…', '…', '…', ]  # etc.
my_sample = sample_urls(my_urls, 50)
# optional: exclude_min=None, exclude_max=None, strict=False, verbose=False
```

--------------------------------

TITLE: Crawl a website and save links to a file
DESCRIPTION: This bash command demonstrates how to crawl a website using Trafilatura from the command line and redirect the output (the list of crawled links) to a file named 'links.txt'.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/crawls

LANGUAGE: bash
CODE:
```
trafilatura --crawl "https://www.example.org" > links.txt
```

--------------------------------

TITLE: Output as JSON
DESCRIPTION: Specifies that the extracted text should be formatted as JSON.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
# Example usage (assuming a URL is provided or piped):
# trafilatura --json -u "URL"
```

--------------------------------

TITLE: Trafilatura CLI: Pipe HTML File Content
DESCRIPTION: Demonstrates piping the content of an existing HTML file to Trafilatura for processing.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-cli

LANGUAGE: bash
CODE:
```
$ cat myfile.html | trafilatura
```

--------------------------------

TITLE: Shuf: Randomly ordered links
DESCRIPTION: This command uses shuf to randomly shuffle the order of URLs in a file. The output is redirected to `myfile-random.txt`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial0

LANGUAGE: bash
CODE:
```
shuf myfile.txt > myfile-random.txt
```

--------------------------------

TITLE: Trafilatura: Discover links using feed
DESCRIPTION: This command uses Trafilatura to discover links from an RSS or Atom feed. The `--feed` option specifies the feed URL, and `--list` outputs the discovered links.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial0

LANGUAGE: bash
CODE:
```
$ trafilatura --feed "https://www.dwds.de/" --list
```

--------------------------------

TITLE: Python: Basic HTML Extraction
DESCRIPTION: Demonstrates the basic process of fetching a URL and extracting main content and comments as plain text using Trafilatura in Python. It requires the `trafilatura` library.

SOURCE: https://trafilatura.readthedocs.io/en/latest/quickstart

LANGUAGE: Python
CODE:
```
from trafilatura import fetch_url, extract

downloaded = fetch_url('https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/')
result = extract(downloaded)
print(result)
```

--------------------------------

TITLE: Store and Retrieve Crawling Rules with Trafilatura
DESCRIPTION: Demonstrates how to store crawling rules in a dictionary using the `courlan` library to extract domains. This allows for convenient retrieval and application of rules for web crawling.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/downloads

LANGUAGE: python
CODE:
```
# this module comes with trafilatura
from courlan import extract_domain

rules_dict = dict()
# storing information
domain = extract_domain(base_url)
rules_dict[domain] = rules
# retrieving rules info
seconds = get_crawl_delay(rules_dict[domain])
```

--------------------------------

TITLE: Command-line: Pipe HTML Input
DESCRIPTION: Demonstrates how to pipe HTML content to Trafilatura for extraction, either from an existing file or directly from standard input. This allows processing of local HTML files.

SOURCE: https://trafilatura.readthedocs.io/en/latest/quickstart

LANGUAGE: Shell
CODE:
```
$ cat myfile.html | trafilatura
```

LANGUAGE: Shell
CODE:
```
$ < myfile.html trafilatura
```

--------------------------------

TITLE: Trafilatura Configuration File Option
DESCRIPTION: Allows overriding standard extraction parameters by providing a custom configuration file.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
--config-file CONFIG_FILE
                        override standard extraction parameters with a custom
                        config file
```

--------------------------------

TITLE: Download Web Documents with Trafilatura
DESCRIPTION: This Python code defines the `trafilatura.downloads` module, responsible for downloading web documents. It includes functions for creating download pools using `urllib3` or `SOCKSProxyManager`, setting default headers with a custom user agent, and handling various HTTP status codes and SSL errors. The `Response` class is used to store information from HTTP responses.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/downloads

LANGUAGE: Python
CODE:
```
# pylint:disable-msg=E0611,I1101
"""
All functions needed to steer and execute downloads of web documents.
"""

import logging
import os
import random

from concurrent.futures import ThreadPoolExecutor, as_completed
from configparser import ConfigParser
from functools import partial
from importlib.metadata import version
from io import BytesIO
from time import sleep
from typing import (
    Any,
    Callable,
    Dict,
    Generator,
    List,
    Optional,
    Set,
    Tuple,
    Union,
)

import certifi
import urllib3

from courlan import UrlStore
from courlan.network import redirection_test

from .settings import DEFAULT_CONFIG, Extractor
from .utils import URL_BLACKLIST_REGEX, decode_file, is_acceptable_length, make_chunks

try:
    from urllib3.contrib.socks import SOCKSProxyManager

    PROXY_URL = os.environ.get("http_proxy")
except ImportError:
    PROXY_URL = None

try:
    import pycurl  # type: ignore

    CURL_SHARE = pycurl.CurlShare()
    # available options:
    # https://curl.se/libcurl/c/curl_share_setopt.html
    CURL_SHARE.setopt(pycurl.SH_SHARE, pycurl.LOCK_DATA_DNS)
    CURL_SHARE.setopt(pycurl.SH_SHARE, pycurl.LOCK_DATA_SSL_SESSION)
    # not thread-safe
    # CURL_SHARE.setopt(pycurl.SH_SHARE, pycurl.LOCK_DATA_CONNECT)
    HAS_PYCURL = True
except ImportError:
    HAS_PYCURL = False


LOGGER = logging.getLogger(__name__)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
HTTP_POOL = None
NO_CERT_POOL = None
RETRY_STRATEGY = None


def create_pool(**args: Any) -> Union[urllib3.PoolManager, Any]:
    """Configure urllib3 download pool according to user-defined settings."""
    manager_class = SOCKSProxyManager if PROXY_URL else urllib3.PoolManager
    manager_args = {"proxy_url": PROXY_URL} if PROXY_URL else {}
    manager_args["num_pools"] = 50  # type: ignore[assignment]
    return manager_class(**manager_args, **args)  # type: ignore[arg-type]


DEFAULT_HEADERS = urllib3.util.make_headers(accept_encoding=True)  # type: ignore[no-untyped-call]
USER_AGENT = (
    "trafilatura/" + version("trafilatura") + " (+https://github.com/adbar/trafilatura)"
)
DEFAULT_HEADERS["User-Agent"] = USER_AGENT

FORCE_STATUS = [
    429,
    499,
    500,
    502,
    503,
    504,
    509,
    520,
    521,
    522,
    523,
    524,
    525,
    526,
    527,
    530,
    598,
]

CURL_SSL_ERRORS = {35, 54, 58, 59, 60, 64, 66, 77, 82, 83, 91}


class Response:
    """Store information gathered in a HTTP response object."""
    __slots__ = ["data", "headers", "html", "status", "url"]

    def __init__(self, data: bytes, status: int, url: str) -> None:
        self.data = data
        self.headers: Optional[Dict[str, str]] = None
        self.html: Optional[str] = None
        self.status = status
        self.url = url

    def __bool__(self) -> bool:
        return self.data is not None

    def __repr__(self) -> str:
        return self.html or decode_file(self.data)

    def store_headers(self, headerdict: Dict[str, str]) -> None:
        """Store response headers if required."""
        # further control steps here
        self.headers = {k.lower(): v for k, v in headerdict.items()}

    def decode_data(self, decode: bool) -> None:
        """Decode the bytestring in data and store a string in html."""
        if decode and self.data:
            self.html = decode_file(self.data)

    def as_dict(self) -> Dict[str, str]:
        """Convert the response object to a dictionary."""
        return {attr: getattr(self, attr) for attr in self.__slots__}


# caching throws an error

```

--------------------------------

TITLE: List URLs from Sitemap with URL Filter
DESCRIPTION: This command uses Trafilatura to list URLs from a sitemap, filtering them based on a provided URL pattern. It demonstrates how to specify a sitemap and apply a filter to the extracted URLs.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
trafilatura --sitemap "https://www.sitemaps.org/" --list --url-filter "https://www.sitemaps.org/de"
```

LANGUAGE: bash
CODE:
```
trafilatura --sitemap "https://www.sitemaps.org/" --list --url-filter "protocol"
```

--------------------------------

TITLE: Check Robots.txt Rules with Python
DESCRIPTION: Shows how to use Python's `urllib.robotparser` to fetch and parse a website's robots.txt file to determine if a specific page can be fetched by crawlers.

SOURCE: https://trafilatura.readthedocs.io/en/latest/downloads

LANGUAGE: python
CODE:
```
import urllib.robotparser
from trafilatura import get_crawl_delay

# define a website to look for rules
base_url = 'https://www.example.org'

# load the necessary components, fetch and parse the file
rules = urllib.robotparser.RobotFileParser()
rules.set_url(base_url + '/robots.txt')
rules.read()

# determine if a page can be fetched by all crawlers
rules.can_fetch("*", "https://www.example.org/page1234.html")
# returns True or False
```

--------------------------------

TITLE: Load Custom Configuration File in Python
DESCRIPTION: Shows how to load and apply a custom configuration file in Trafilatura using Python. This involves using the `use_config` function to load settings from a specified file and then passing this configuration to the `extract` function.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/settings

LANGUAGE: python
CODE:
```
# load the required functions
>>> from trafilatura import extract
>>> from trafilatura.settings import use_config

# load the new settings by providing a file name
>>> newconfig = use_config("myfile.cfg")

# use with a previously downloaded document
>>> extract(downloaded, config=newconfig)

# provide a file name directly (can be slower)
>>> extract(downloaded, settingsfile="myfile.cfg")
```

--------------------------------

TITLE: Extract Content with Justext Fallback
DESCRIPTION: This code snippet demonstrates the use of the Justext algorithm as a safety net for content extraction. It initializes the process, determines the appropriate stoplist based on the target language, and extracts paragraphs. Boilerplate content is skipped, and valid paragraphs are appended to the result body. Error handling is included for the extraction process.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/external

LANGUAGE: Python
CODE:
```
def extract_with_justext_fallback(tree: HtmlElement, target_language: str, url: str, duplicate_test: callable, get_stoplist: callable, custom_justext: callable, LOGGER: object, JT_STOPLIST: list, jt_stoplist_init: callable) -> Element:
    '''Second safety net: try with the generic algorithm justext'''
    # init
    result_body = Element('body')
    # determine language
    if target_language in JUSTEXT_LANGUAGES:
        justext_stoplist = get_stoplist(JUSTEXT_LANGUAGES[target_language])
    else:
        justext_stoplist = JT_STOPLIST or jt_stoplist_init()
    # extract
    try:
        paragraphs = custom_justext(tree, justext_stoplist)
    except Exception as err:
        LOGGER.error('justext %s %s', err, url)
    else:
        for paragraph in paragraphs:
            if paragraph.is_boilerplate:
                continue
            #if duplicate_test(paragraph) is not True:
            elem, elem.text = Element('p'), paragraph.text
            result_body.append(elem)
    return result_body
```

--------------------------------

TITLE: Build XML Output
DESCRIPTION: Constructs an XML output tree from document metadata, including cleaning attributes and setting the main body tag.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
def build_xml_output(docmeta: Document) -> _Element:
    '''Build XML output tree based on extracted information'''
    output = Element('doc')
    add_xml_meta(output, docmeta)
    docmeta.body.tag = 'main'

    # clean XML tree
    output.append(clean_attributes(docmeta.body))
    docmeta.commentsbody.tag = 'comments'
    output.append(clean_attributes(docmeta.commentsbody))

    return output
```

--------------------------------

TITLE: Trafilatura CLI: Extract with XML Output
DESCRIPTION: Shows how to extract content from a URL with basic XML structure as output using the Trafilatura command-line interface.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-cli

LANGUAGE: bash
CODE:
```
$ trafilatura --xml --URL "https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/"
```

--------------------------------

TITLE: Fetch Archived URL with Trafilatura
DESCRIPTION: This Python code snippet demonstrates how to fetch a URL from the Internet Archive if the initial download fails. It constructs a new URL pointing to the archive and attempts to download the content using a `fetch_url` function.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/troubleshooting

LANGUAGE: python
CODE:
```
# url is the target
# downloaded is the result of the download
# also needs a function fetch_url() or equivalent
if downloaded is None:
    new_url = "https://web.archive.org/web/20/" + url
    downloaded = fetch_url(new_url)
```

--------------------------------

TITLE: Sort and count tokens
DESCRIPTION: Sorts the tokens from the tokens.txt file, counts their occurrences, and displays the top 10 most frequent tokens.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial1

LANGUAGE: bash
CODE:
```
$ sort tokens.txt | uniq -c | sort -nrk1 | head -10
```

--------------------------------

TITLE: Output as XML-TEI
DESCRIPTION: Specifies that the extracted text should be formatted as XML-TEI (Text Encoding Initiative).

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
# Example usage (assuming a URL is provided or piped):
# trafilatura --xmltei -u "URL"
```

--------------------------------

TITLE: Extract URLs from Internet Archive/Common Crawl with cdx_toolkit
DESCRIPTION: This snippet demonstrates how to use the cdx_toolkit to fetch known URLs from the Wayback Machine and Common Crawl. It's a command-line tool for interacting with CDX indices.

SOURCE: https://trafilatura.readthedocs.io/en/latest/sources

LANGUAGE: bash
CODE:
```
gau <domain>
# or
cdx_toolkit <domain>
```

--------------------------------

TITLE: Probe Alternative Homepage for Redirects
DESCRIPTION: Fetches a given homepage URL, checks for HTTP redirects, and then analyzes the content for meta-refresh tags. It returns the potentially redirected homepage URL and its HTML content, handling potential errors during fetching or decoding.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/spider

LANGUAGE: Python
CODE:
```
def probe_alternative_homepage(
    homepage: str,
) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """Check if the homepage is redirected and return appropriate values."""
    response = fetch_response(homepage, decode=False)
    if not response or not response.data:
        return None, None, None

    # get redirected URL here?
    if response.url not in (homepage, "/"):
        logging.info("followed homepage redirect: %s", response.url)
        homepage = response.url

    # decode response
    htmlstring = decode_file(response.data)

    # is there a meta-refresh on the page?
    new_htmlstring, new_homepage = refresh_detection(htmlstring, homepage)
    if new_homepage is None:  # malformed or malicious content
        return None, None, None

    logging.debug("fetching homepage OK: %s", new_homepage)
    return new_htmlstring, new_homepage, None
```

--------------------------------

TITLE: Fetch and Decode Web Content with Trafilatura
DESCRIPTION: Handles fetching web content from URLs and decoding file content. Includes functions for retrieving responses and decoding files using various encodings.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/corefunctions

LANGUAGE: Python
CODE:
```
from trafilatura import fetch_url

# Example usage:
# url = "..."
# response = fetch_url(url)

```

LANGUAGE: Python
CODE:
```
from trafilatura import fetch_response

# Example usage:
# url = "..."
# response = fetch_response(url)

```

LANGUAGE: Python
CODE:
```
from trafilatura.utils import decode_file

# Example usage:
# filepath = "..."
# text = decode_file(filepath)

```

--------------------------------

TITLE: Discover Feed Links with Trafilatura CLI
DESCRIPTION: This command utilizes Trafilatura's `--feed` option to extract links from web feeds, such as RSS or Atom. It takes a homepage or a direct feed URL as input and outputs the discovered links using the `--list` flag.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial0

LANGUAGE: bash
CODE:
```
$ trafilatura --feed "https://www.dwds.de/" --list
```

--------------------------------

TITLE: Trafilatura Performance Benchmarks (Older Results)
DESCRIPTION: This snippet presents older benchmark results for trafilatura and other libraries, dated 2020-11-06. It includes similar performance metrics (Precision, Recall, Accuracy, F-Score) and highlights the 'Diff.' compared to a baseline.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/evaluation

LANGUAGE: text
CODE:
```
Python Package                  Precision  Recall     Accuracy  F-Score   Diff.
=============================== =========  ========== ========= ========= ======
trafilatura 0.6.0               0.924      0.849      0.890     0.885     3.9x
trafilatura 0.6.0 (+ fallbacks) 0.933      0.877      0.907     0.904     8.4x
```

--------------------------------

TITLE: Validating TEI-XML Documents with Python
DESCRIPTION: This resource explains how to validate TEI-XML documents using Python. It is relevant for users working with structured text data and ensuring data integrity.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorials

LANGUAGE: Python
CODE:
```
# Example of using a Python library for XML validation (e.g., lxml)
from lxml import etree

xml_file = 'your_document.xml'
xsd_file = 'your_schema.xsd'

try:
    xmlschema_doc = etree.parse(xsd_file)
    xmlschema = etree.XMLSchema(xmlschema_doc)
    xml_doc = etree.parse(xml_file)
    xmlschema.assertValid(xml_doc)
    print(f'{xml_file} is valid')
except etree.XMLSyntaxError as e:
    print(f'XML Syntax Error: {e}')
except etree.DocumentError as e:
    print(f'Document Error: {e}')
except etree.XMLSchemaParseError as e:
    print(f'XSD Parse Error: {e}')
except etree.DocumentInvalid as e:
    print(f'Document Invalid: {e}')
```

--------------------------------

TITLE: Extract Text using baseline
DESCRIPTION: Illustrates the use of the `baseline` function for a balanced approach to text extraction, returning the body, text, and text length.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
>>> from trafilatura import baseline
>>> postbody, text, len_text = baseline(downloaded)
```

--------------------------------

TITLE: Store and Retrieve Crawling Rules with Trafilatura
DESCRIPTION: Demonstrates storing custom crawling rules in a dictionary, keyed by extracted domain names. It shows how to retrieve specific rule information, such as the crawl delay, from the stored rules.

SOURCE: https://trafilatura.readthedocs.io/en/latest/downloads

LANGUAGE: Python
CODE:
```
# this module comes with trafilatura
from courlan import extract_domain

rules_dict = dict()
# storing information
domain = extract_domain(base_url)
rules_dict[domain] = rules
# retrieving rules info
seconds = get_crawl_delay(rules_dict[domain])

```

--------------------------------

TITLE: Sort: Randomly ordered links
DESCRIPTION: This command uses sort with the `-R` option to randomly shuffle the order of URLs in a file. The output is redirected to `myfile-random.txt`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial0

LANGUAGE: bash
CODE:
```
sort -R myfile.txt > myfile-random.txt
```

--------------------------------

TITLE: Embedding YouTube Video Player
DESCRIPTION: This snippet shows how to embed a YouTube video player into a web page using an iframe. It's a standard HTML method for displaying video content.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorials

LANGUAGE: HTML
CODE:
```
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/rEOoItpzlVw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

--------------------------------

TITLE: Extracting Main Text Content with Python
DESCRIPTION: This tutorial demonstrates how to extract the main text content from web pages using the Trafilatura library in Python. It covers the core functionality for web scraping and text processing.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorials

LANGUAGE: Python
CODE:
```
import trafilatura

# Download the content of a web page
url = 'http://example.com'
main_content = trafilatura.fetch_url(url)

# Extract the main text contentdownloaded = trafilatura.extract(main_content)

# Save the extracted text to a file
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(downloaded)
```

--------------------------------

TITLE: Compare Extraction Algorithms
DESCRIPTION: Compares the results of the library's custom extraction with an alternative algorithm (like readability) based on heuristics. It decides which extraction to use, considering factors like text length, focus (precision/recall), and document structure. It also incorporates a fallback to Justext for potentially cleaner results. Dependencies include 'try_readability', 'justext_rescue', and 'sanitize_tree'.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/external

LANGUAGE: python
CODE:
```
def compare_extraction(tree: HtmlElement, backup_tree: HtmlElement, body: _Element, text: str, len_text: int, options: Any) -> Tuple[_Element, str, int]:
    '''Decide whether to choose own or external extraction
       based on a series of heuristics'''
    # bypass for recall
    if options.focus == "recall" and len_text > options.min_extracted_size * 10:
        return body, text, len_text

    use_readability, jt_result = False, False
    # prior cleaning
    if options.focus == "precision":
        backup_tree = prune_unwanted_nodes(backup_tree, OVERALL_DISCARD_XPATH)

    # try with readability
    temppost_algo = try_readability(backup_tree)
    # unicode fix necessary on certain systems (#331)
    algo_text = trim(tostring(temppost_algo, method='text', encoding='utf-8').decode('utf-8'))
    len_algo = len(algo_text)

    # compare
    LOGGER.debug('extracted length: %s (algorithm) %s (extraction)', len_algo, len_text)
    # conditions to use alternative algorithms
    if len_algo in (0, len_text):
        use_readability = False
    elif len_text == 0 and len_algo > 0:
        use_readability = True
    elif len_text > 2 * len_algo:
        use_readability = False
    # quick fix for https://github.com/adbar/trafilatura/issues/632
    elif len_algo > 2 * len_text and not algo_text.startswith("{"):
        use_readability = True
    # borderline cases
    elif not body.xpath('.//p//text()') and len_algo > options.min_extracted_size * 2:
        use_readability = True
    elif len(body.findall('.//table')) > len(body.findall('.//p')) and len_algo > options.min_extracted_size * 2:
        use_readability = True
    # https://github.com/adbar/trafilatura/issues/354
    elif options.focus == "recall" and not body.xpath('.//head') and temppost_algo.xpath('.//h2|.//h3|.//h4') and len_algo > len_text:
        use_readability = True
    else:
        LOGGER.debug('extraction values: %s %s for %s', len_text, len_algo, options.source)
        use_readability = False

    # apply decision
    if use_readability:
        body, text, len_text = temppost_algo, algo_text, len_algo
        LOGGER.debug('using generic algorithm: %s', options.source)
    else:
        LOGGER.debug('using custom extraction: %s', options.source)

    # override faulty extraction: try with justext
    if body.xpath(SANITIZED_XPATH) or len_text < options.min_extracted_size:  # body.find(...)
        LOGGER.debug('unclean document triggering justext examination: %s', options.source)
        body2, text2, len_text2 = justext_rescue(tree, options)
        jt_result = bool(text2)
        # prevent too short documents from replacing the main text
        if text2 and not len_text > 4*len_text2:  # threshold could be adjusted
            LOGGER.debug('using justext, length: %s', len_text2)
            body, text, len_text = body2, text2, len_text2

    # post-processing: remove unwanted sections
    if use_readability and not jt_result:
        body, text, len_text = sanitize_tree(body, options)  # type: ignore[arg-type]

    return body, text, len_text
```

--------------------------------

TITLE: Article Extraction Routines - readabilipy
DESCRIPTION: readabilipy provides a Python wrapper for Mozilla's Node.js readability package, along with article extraction routines written purely in Python.

SOURCE: https://trafilatura.readthedocs.io/en/latest/evaluation

LANGUAGE: python
CODE:
```
from readabilipy import readabilipy

readable = readabilipy.Document(html_content)

print(readable.summary())
```

--------------------------------

TITLE: Text Extraction Comparison - Polish Texts
DESCRIPTION: A comparison on a small sample of Polish news texts and forums was conducted. Trafilatura has improved since this evaluation and is now integrated into the internal benchmark.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/evaluation

LANGUAGE: text
CODE:
```
Comparison on a small `sample of Polish news texts and forums <https://github.com/tsolewski/Text_extraction_comparison_PL>`_ (now integrated in the internal benchmark, Trafilatura has improved since)
```

--------------------------------

TITLE: Extract Content with Trafilatura Options
DESCRIPTION: The `_extract` function initializes extraction parameters based on `Extractor` options, such as preserving tables, images, and links. It then iterates through XPath expressions to select and prune subtrees, applying logic to adjust `potential_tags` based on content analysis and extraction focus.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def _extract(tree: HtmlElement, options: Extractor) -> Tuple[_Element, str, Set[str]]:
    # init
    potential_tags = set(TAG_CATALOG)
    if options.tables is True:
        potential_tags.update(['table', 'td', 'th', 'tr'])
    if options.images is True:
        potential_tags.add('graphic')
    if options.links is True:
        potential_tags.add('ref')
    result_body = Element('body')
    # iterate
    for expr in BODY_XPATH:
        # select tree if the expression has been found
        subtree = next((s for s in expr(tree) if s is not None), None)
        if subtree is None:
            continue
        # prune the subtree
        subtree = prune_unwanted_sections(subtree, potential_tags, options)
        # skip if empty tree
        if len(subtree) == 0:
            continue
        # no paragraphs containing text, or not enough
        ptest = subtree.xpath('//p//text()')
        if options.focus == "precision":
            factor = 1
        else:
            factor = 3
        if not ptest or len(''.join(ptest)) < options.min_extracted_size * factor:  # type: ignore[attr-defined]
            potential_tags.add('div')
        # polish list of potential tags

```

--------------------------------

TITLE: Download and Extract Web Content with Python
DESCRIPTION: Demonstrates how to download and extract main text content from a given URL using Trafilatura in Python. It shows basic usage for text extraction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage

LANGUAGE: python
CODE:
```
import trafilatura

url = "http://example.com"

# Download the webpage
response = trafilatura.fetch_url(url)

# Extract the main text
downloaded = trafilatura.extract(response)

# Print the extracted text
print(downloaded)
```

--------------------------------

TITLE: Produce TEI XML from URL with Trafilatura
DESCRIPTION: Extracts information from a given URL and converts it into a TEI-compliant XML file, with an option to validate the output against the TEI schema. This function requires the 'trafilatura' library.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial2

LANGUAGE: Python
CODE:
```
# load the necessary components
from trafilatura import fetch_url, extract

# download a file
downloaded = fetch_url('https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/')

# extract information as XML TEI and validate the result
result = extract(downloaded, output_format='xmltei', tei_validation=True)
```

--------------------------------

TITLE: Trafilatura Performance Benchmarks (Early Results)
DESCRIPTION: This snippet presents the earliest benchmark results from 2020-03-19, focusing on trafilatura and other libraries. It includes Precision, Recall, Accuracy, and F-Score, along with a 'Time' column indicating processing speed.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/evaluation

LANGUAGE: text
CODE:
```
Python Package                  Precision  Recall     Accuracy  F-Score   Time
=============================== =========  ========== ========= ========= =====
trafilatura 0.5.1               0.927      0.854      0.894     0.889     3.1x
```

--------------------------------

TITLE: Discover Feed URLs with Trafilatura
DESCRIPTION: Shows the import statement for the `feeds` module, which contains the `find_feed_urls` utility for discovering and downloading feeds from webpages.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
>>> from trafilatura import feeds
```

--------------------------------

TITLE: Build TEI-XML Output
DESCRIPTION: Constructs the TEI-XML output tree from document metadata. It involves building the initial TEI tree and then filtering and repairing it to ensure compliance with TEI standards.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
def build_tei_output(docmeta: Document) -> _Element:
    '''Build TEI-XML output tree based on extracted information'''
    # build TEI tree
    output = write_teitree(docmeta)
    # filter output (strip unwanted elements), just in case
    # check and repair
    output = check_tei(output, docmeta.url)
    return output
```

--------------------------------

TITLE: Trafilatura CLI: Alternative Pipe Syntax
DESCRIPTION: Provides an alternative syntax for piping HTML content to Trafilatura using input redirection.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-cli

LANGUAGE: bash
CODE:
```
$ < myfile.html trafilatura
```

--------------------------------

TITLE: readability-lxml Page Cleaning - Python
DESCRIPTION: The readability-lxml Python package cleans web pages and preserves some markup, offering an alternative for content extraction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/evaluation

LANGUAGE: python
CODE:
```
readability-lxml <https://github.com/buriy/python-readability>`_ cleans the page and preserves some markup
```

--------------------------------

TITLE: Bypass Output Conversion with bare_extraction
DESCRIPTION: Demonstrates the use of `bare_extraction` to bypass standard output conversion, returning Python variables for metadata and LXML objects for main text and comments.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
>>> from trafilatura import bare_extraction
>>> bare_extraction(downloaded)
```

--------------------------------

TITLE: Output as CSV
DESCRIPTION: Specifies that the extracted text should be formatted as CSV.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
# Example usage (assuming a URL is provided or piped):
# trafilatura --csv -u "URL"
```

--------------------------------

TITLE: Trafilatura CLI: Language Filtering
DESCRIPTION: Explains how to use the `--target-language` argument with a 2-letter ISO 639-1 code to filter output by language, requiring additional components.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-cli

LANGUAGE: bash
CODE:
```
--target-language <2-letter-code>
```

--------------------------------

TITLE: Extract License Information
DESCRIPTION: Searches HTML code for license information by looking for links labeled as 'license' or probing footer elements for Creative Commons links.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/metadata

LANGUAGE: Python
CODE:
```
def extract_license(tree: HtmlElement) -> Optional[str]:
    """Search the HTML code for license information and parse it."""
    # look for links labeled as license
    for element in tree.findall('.//a[@rel="license"][@href]'):
        result = parse_license_element(element, strict=False)
        if result is not None:
            return result
    # probe footer elements for CC links
    for element in tree.xpath(
        './/footer//a[@href]|.//div[contains(@class, "footer") or contains(@id, "footer")]//a[@href]'
    ):
        result = parse_license_element(element, strict=True)
        if result is not None:
            return result
    return None
```

--------------------------------

TITLE: Prioritize Precision
DESCRIPTION: Adjusts the extraction process to prioritize precision, focusing on the most central and relevant elements to reduce noise.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
# Example usage (assuming a URL is provided or piped):
# trafilatura --precision -u "URL"
```

--------------------------------

TITLE: Fallback Extraction with Readability
DESCRIPTION: The `try_readability` function serves as a safety net, attempting extraction using the generic readability algorithm on an HTML element.

SOURCE: https://trafilatura.readthedocs.io/en/latest/corefunctions

LANGUAGE: python
CODE:
```
trafilatura.external.try_readability(_htmlinput : HtmlElement_) → HtmlElement
```

--------------------------------

TITLE: Trafilatura: Buffered Downloads (String)
DESCRIPTION: Consumes a list of URLs, downloading them in a buffered manner using a specified number of threads. It returns a generator yielding tuples of URL and downloaded content as strings.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/downloads

LANGUAGE: Python
CODE:
```
def buffered_downloads(
    bufferlist: List[str],
    download_threads: int,
    options: Optional[Extractor] = None,
) -> Generator[Tuple[str, str], None, None]:
    """Download queue consumer, single- or multi-threaded."""
    worker = partial(fetch_url, options=options)

    return _buffered_downloads(bufferlist, download_threads, worker)
```

--------------------------------

TITLE: Linguistic Resource Creation - jusText
DESCRIPTION: jusText is a Python library specifically developed for creating linguistic resources. It focuses on preserving text that contains full sentences and some markup.

SOURCE: https://trafilatura.readthedocs.io/en/latest/evaluation

LANGUAGE: python
CODE:
```
from justext import justext

paragraphs = justext.justext(html_bytes, 'English')

for paragraph in paragraphs:
    if not paragraph.is_boilerplate:
        print(paragraph.text)
```

--------------------------------

TITLE: Crawl Websites, Generate Embeddings, and Store in Epsilla
DESCRIPTION: This Python script uses Trafilatura to fetch and extract text content from specified URLs, Langchain's HuggingFaceBgeEmbeddings to generate vector embeddings for the extracted text, and then inserts these records (ID, document text, and embedding vector) into the 'Trafilatura' table in the Epsilla database.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial-epsilla

LANGUAGE: python
CODE:
```
# import Trafilatura and embedding model
from trafilatura import fetch_url, extract
from langchain.embeddings import HuggingFaceBgeEmbeddings

model_name = "BAAI/bge-small-en"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}

hf = HuggingFaceBgeEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

# download the homepages from a few open source projects
urls = [
    'https://www.tensorflow.org/',
    'https://pytorch.org/',
    'https://react.dev/',
]
results = [extract(fetch_url(url)) for url in urls]

# get the embedding vector and store it in Epsilla
embeddings = [hf.embed_query(result) for result in results]
records = [
    {"ID": idx, "Doc": results[idx], "Embedding": embeddings[idx]} 
    for idx in range(len(results))
]
client.insert(
   table_name="Trafilatura",
   records=records
)
```

--------------------------------

TITLE: Search Sitemaps with Trafilatura (Python)
DESCRIPTION: Demonstrates how to import and use the `sitemap_search` function from Trafilatura's sitemaps module to find URLs within a given sitemap.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-r

LANGUAGE: Python
CODE:
```
from trafilatura.sitemaps import sitemap_search
```

LANGUAGE: Python
CODE:
```
sitemap_search("https://www.sitemaps.org/")
```

--------------------------------

TITLE: Trafilatura Performance Benchmarks (Even Older Results)
DESCRIPTION: This snippet shows even older benchmark results for trafilatura and other libraries, dated 2020-07-16. It continues to track performance metrics like Precision, Recall, Accuracy, and F-Score, along with the 'Diff.' column.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/evaluation

LANGUAGE: text
CODE:
```
Python Package                  Precision  Recall     Accuracy  F-Score   Diff.
=============================== =========  ========== ========= ========= ======
trafilatura 0.5.1               0.927      0.854      0.894     0.889     3.1x
trafilatura 0.5.1 (+ fallbacks) 0.933      0.885      0.911     0.908     6.8x
```

--------------------------------

TITLE: ReadabiliPy Wrapper and Extraction - Python
DESCRIPTION: ReadabiliPy provides a Python wrapper for Mozilla's Node.js package and includes article extraction routines written in pure Python.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/evaluation

LANGUAGE: python
CODE:
```
readabilipy <https://github.com/alan-turing-institute/ReadabiliPy>`_ contains a Python wrapper for Mozilla's Node.js package, as well as article extraction routines written in pure Python
```

--------------------------------

TITLE: Extract All Text (R)
DESCRIPTION: Shows how to use the `html2txt` function in R to extract all possible text content from a downloaded webpage.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-r

LANGUAGE: R
CODE:
```
trafilatura$html2txt(downloaded)
```

--------------------------------

TITLE: Corpus Construction Strategy
DESCRIPTION: Explains that the strategy for building a corpus is typically determined by the chosen corpus type. This allows for decisions on whether to retrieve an entire website or specific targeted URLs.

SOURCE: https://trafilatura.readthedocs.io/en/latest/compendium

LANGUAGE: General
CODE:
```
The corpus construction strategy usually follows from the chosen corpus type, one can decide to retrieve a whole website or just targeted URLs.
```

--------------------------------

TITLE: Command-line: Combined Options
DESCRIPTION: Shows how to combine different extraction options on the command-line when piping HTML content to Trafilatura, such as outputting as JSON and disabling table extraction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/quickstart

LANGUAGE: Shell
CODE:
```
$ < myfile.html trafilatura --json --no-tables
```

--------------------------------

TITLE: Extract with No Fallback
DESCRIPTION: Demonstrates optimizing extraction speed by bypassing fallback algorithms using the `no_fallback=True` parameter.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
# skip algorithms used as fallback
>>> result = extract(downloaded, no_fallback=True)
```

--------------------------------

TITLE: Perform Buffered Downloads with Thread Pool
DESCRIPTION: Utilizes a ThreadPoolExecutor to perform a series of downloads in parallel. It processes URLs in chunks and yields the URL along with its corresponding result from the worker function.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/downloads

LANGUAGE: Python
CODE:
```
def _buffered_downloads(
    bufferlist: List[str],
    download_threads: int,
    worker: Callable[[str], Any],
    chunksize: int = 10000,
) -> Generator[Tuple[str, Any], None, None]:
    """Use a thread pool to perform a series of downloads."""
    with ThreadPoolExecutor(max_workers=download_threads) as executor:
        for chunk in make_chunks(bufferlist, chunksize):
            future_to_url = {executor.submit(worker, url): url for url in chunk}
            for future in as_completed(future_to_url):
                yield future_to_url[future], future.result()
```

--------------------------------

TITLE: Trafilatura Extraction Sequence
DESCRIPTION: Executes the standard cascade of extractors used by Trafilatura. This includes the main content extraction, comparison with external extractors (if not in fast mode), and a fallback baseline extraction on the original tree if the extracted text is too short.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/core

LANGUAGE: python
CODE:
```
def trafilatura_sequence(
    cleaned_tree: HtmlElement,
    cleaned_tree_backup: HtmlElement,
    tree_backup: HtmlElement,
    options: Extractor,
) -> Tuple[_Element, str, int]:
    """Execute the standard cascade of extractors used by Trafilatura."""
    # Trafilatura's main extractor
    postbody, temp_text, len_text = extract_content(cleaned_tree, options)

    # comparison with external extractors
    if not options.fast:
        postbody, temp_text, len_text = compare_extraction(
            cleaned_tree_backup,
            deepcopy(tree_backup),
            postbody,
            temp_text,
            len_text,
            options,
        )

    # rescue: baseline extraction on original/dirty tree
    if len_text < options.min_extracted_size and not options.focus == "precision":  # type: ignore[attr-defined]
        postbody, temp_text, len_text = baseline(deepcopy(tree_backup))
        LOGGER.debug("non-clean extracted length: %s (extraction)", len_text)

    return postbody, temp_text, len_text
```

--------------------------------

TITLE: Determine HTTP Headers
DESCRIPTION: Determines the appropriate HTTP headers, including the User-Agent and Cookie, based on the provided configuration. If the configuration is not the default, it parses the config for headers.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/downloads

LANGUAGE: Python
CODE:
```
def _determine_headers(
    config: ConfigParser, headers: Optional[Dict[str, str]] = None
) -> Dict[str, str]:
    """Internal function to decide on user-agent string."""
    if config != DEFAULT_CONFIG:
        myagents, mycookie = _parse_config(config)
        headers = {}
        if myagents:
            headers["User-Agent"] = random.choice(myagents)
        if mycookie:
            headers["Cookie"] = mycookie
    return headers or DEFAULT_HEADERS
```

--------------------------------

TITLE: Vector Search Query
DESCRIPTION: This Python code snippet demonstrates how to perform a vector search. It embeds a query string using a Hugging Face model and then queries a database table to find the most relevant entry based on the embedding.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial-epsilla

LANGUAGE: Python
CODE:
```
query = "A modern frontend library"
query_embedding = hf.embed_query(query)
status_code, response = client.query(
    table_name="Trafilatura",
    query_field="Embedding",
    query_vector=query_embedding,
    limit=1
)
print(response)
```

--------------------------------

TITLE: Efficient Web Crawling - Edwards et al. (2001)
DESCRIPTION: Emphasizes the necessity of efficient and scalable web crawling due to finite and costly bandwidth. The goal is to maintain a reasonable measure of quality or freshness in the collected data.

SOURCE: https://trafilatura.readthedocs.io/en/latest/compendium

LANGUAGE: General
CODE:
```
Given that the bandwidth for conducting crawls is neither infinite nor free, it is becoming essential to crawl the Web in not only a scalable, but efficient way, if some reasonable measure of quality or freshness is to be maintained.
```

--------------------------------

TITLE: Run Python Trafilatura from R
DESCRIPTION: Illustrates how to execute Python code, specifically Trafilatura extraction, from within an R environment using `py_run_string` and `py_to_r`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-r

LANGUAGE: Python
CODE:
```
import trafilatura
```

LANGUAGE: R
CODE:
```
url <- "https://www.example.com"
```

LANGUAGE: Python
CODE:
```
trafilatura.extract(url)
```

LANGUAGE: R
CODE:
```
py_df <- py_run_string("trafilatura.extract(url)")
```

LANGUAGE: R
CODE:
```
df <- py_to_r(py_df)
```

--------------------------------

TITLE: Trafilatura: Buffered Downloads (Response)
DESCRIPTION: Consumes a list of URLs, downloading them in a buffered manner using a specified number of threads. It returns a generator yielding tuples of URL and full Response objects.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/downloads

LANGUAGE: Python
CODE:
```
def buffered_response_downloads(
    bufferlist: List[str],
    download_threads: int,
    options: Optional[Extractor] = None,
) -> Generator[Tuple[str, Response], None, None]:
    """Download queue consumer, returns full Response objects."""
    config = options.config if options else DEFAULT_CONFIG
    worker = partial(fetch_response, config=config)

    return _buffered_downloads(bufferlist, download_threads, worker)
```

--------------------------------

TITLE: Trafilatura Output Formats
DESCRIPTION: This command-line snippet illustrates how to specify different output formats for Trafilatura, including CSV, JSON, and XML (with or without TEI). By default, it outputs TXT files without metadata.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial-dwds

LANGUAGE: bash
CODE:
```
trafilatura --input-file linkliste.txt --output-dir ausgabe/ --backup-dir html-quellen/ --csv
```

LANGUAGE: bash
CODE:
```
trafilatura --input-file linkliste.txt --output-dir ausgabe/ --backup-dir html-quellen/ --json
```

LANGUAGE: bash
CODE:
```
trafilatura --input-file linkliste.txt --output-dir ausgabe/ --backup-dir html-quellen/ --xml
```

LANGUAGE: bash
CODE:
```
trafilatura --input-file linkliste.txt --output-dir ausgabe/ --backup-dir html-quellen/ --xmltei
```

--------------------------------

TITLE: Bundle Post and Comments into TEI Tree
DESCRIPTION: Bundles the extracted post and comments into a TEI (Text Encoding Initiative) XML tree structure. It creates a root 'TEI' element with a 'text' and 'body' element, then appends the post and comments as 'div' elements with specific types ('entry' and 'comments'). Dependencies include `Element` and `SubElement` from `xml.etree.ElementTree`, `Document` type, and `clean_attributes` function.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
from xml.etree.ElementTree import Element, SubElement, Element as _Element

# Assuming Document and clean_attributes are defined elsewhere

def write_teitree(docmeta: Document) -> _Element:
    """Bundle the extracted post and comments into a TEI tree"""
    teidoc = Element('TEI', xmlns='http://www.tei-c.org/ns/1.0')
    write_fullheader(teidoc, docmeta) # Assuming write_fullheader is defined elsewhere
    textelem = SubElement(teidoc, 'text')
    textbody = SubElement(textelem, 'body')
    # post
    postbody = clean_attributes(docmeta.body)
    postbody.tag = 'div'
    postbody.set('type', 'entry')
    textbody.append(postbody)
    # comments
    commentsbody = clean_attributes(docmeta.commentsbody)
    commentsbody.tag = 'div'
    commentsbody.set('type', 'comments')
    textbody.append(commentsbody)
    return teidoc


def clean_attributes(element):
    # Placeholder for clean_attributes function
    return element

class Document:
    # Placeholder for Document class definition
    def __init__(self):
        self.body = None
        self.commentsbody = None

```

--------------------------------

TITLE: Filter and Count Token Frequencies
DESCRIPTION: This command filters out punctuation, removes empty lines, converts all tokens to lowercase, and then sorts and counts the frequency of the remaining tokens, displaying the top 20. It uses 'sed' for text manipulation and standard Unix sorting utilities.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial1

LANGUAGE: bash
CODE:
```
$ < tokens.txt sed -e "s/[[:punct:]]//g" -e "/^$/d" -e "s/.*/\L\0/" > tokens-filtered.txt
# display most frequent tokens
$ < tokens-filtered.txt sort | uniq -c | sort -nrk1 | head -20
```

--------------------------------

TITLE: Trafilatura Performance Benchmarks
DESCRIPTION: This snippet summarizes the performance of the trafilatura package against other libraries like newspaper3k, boilerpy3, goose3, dragnet, and readability-lxml. It includes metrics such as Precision, Recall, Accuracy, and F-Score, along with a 'Diff.' column indicating performance differences.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/evaluation

LANGUAGE: text
CODE:
```
Python Package                  Precision  Recall     Accuracy  F-Score   Diff.
=============================== =========  ========== ========= ========= ======
trafilatura 0.8.2 (fast)        0.925      0.868      0.899     0.896     3.9x
trafilatura 0.8.2               0.934      0.890      0.914     0.912     8.4x
```

--------------------------------

TITLE: Trafilatura: Send PycURL Request
DESCRIPTION: An experimental function that uses libcurl and pycurl to speed up downloads. It handles SSL verification, redirects, timeouts, and optionally includes response headers.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/downloads

LANGUAGE: Python
CODE:
```
def _send_pycurl_request(
    url: str, no_ssl: bool, with_headers: bool, config: ConfigParser
) -> Optional[Response]:
    """Experimental function using libcurl and pycurl to speed up downloads"""
    # https://github.com/pycurl/pycurl/blob/master/examples/retriever-multi.py

    # init
    headerlist = [
        f"{header}: {content}" for header, content in _determine_headers(config).items()
    ]

    # prepare curl request
    # https://curl.haxx.se/libcurl/c/curl_easy_setopt.html
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, url.encode("utf-8"))
    # share data
    curl.setopt(pycurl.SHARE, CURL_SHARE)
    curl.setopt(pycurl.HTTPHEADER, headerlist)
    # curl.setopt(pycurl.USERAGENT, '')
    curl.setopt(pycurl.FOLLOWLOCATION, 1)
    curl.setopt(pycurl.MAXREDIRS, config.getint("DEFAULT", "MAX_REDIRECTS"))
    curl.setopt(pycurl.CONNECTTIMEOUT, config.getint("DEFAULT", "DOWNLOAD_TIMEOUT"))
    curl.setopt(pycurl.TIMEOUT, config.getint("DEFAULT", "DOWNLOAD_TIMEOUT"))
    curl.setopt(pycurl.MAXFILESIZE, config.getint("DEFAULT", "MAX_FILE_SIZE"))
    curl.setopt(pycurl.NOSIGNAL, 1)

    if no_ssl is True:
        curl.setopt(pycurl.SSL_VERIFYPEER, 0)
        curl.setopt(pycurl.SSL_VERIFYHOST, 0)
    else:
        curl.setopt(pycurl.CAINFO, certifi.where())

    if with_headers:
        headerbytes = BytesIO()
        curl.setopt(pycurl.HEADERFUNCTION, headerbytes.write)

    if PROXY_URL:
        curl.setopt(pycurl.PRE_PROXY, PROXY_URL)

    # TCP_FASTOPEN
    # curl.setopt(pycurl.FAILONERROR, 1)
    # curl.setopt(pycurl.ACCEPT_ENCODING, '')

    # send request
    try:
        bufferbytes = curl.perform_rb()
    except pycurl.error as err:
        LOGGER.error("pycurl error: %s %s", url, err)
        # retry in case of SSL-related error
        # see https://curl.se/libcurl/c/libcurl-errors.html
        # errmsg = curl.errstr_raw()
        # additional error codes: 80, 90, 96, 98
        if no_ssl is False and err.args[0] in CURL_SSL_ERRORS:
            LOGGER.debug("retrying after SSL error: %s %s", url, err)
            return _send_pycurl_request(url, True, with_headers, config)
        # traceback.print_exc(file=sys.stderr)
        # sys.stderr.flush()
        return None

    # additional info
    # ip_info = curl.getinfo(curl.PRIMARY_IP)

    resp = Response(
        bufferbytes, curl.getinfo(curl.RESPONSE_CODE), curl.getinfo(curl.EFFECTIVE_URL)
    )
    curl.close()

    if with_headers:
        respheaders = {}
        # https://github.com/pycurl/pycurl/blob/master/examples/quickstart/response_headers.py
        for line in (
            headerbytes.getvalue().decode("iso-8859-1", errors="replace").splitlines()
        ):
            # re.split(r'\r?\n') ?
            # This will botch headers that are split on multiple lines...
            if ":" not in line:
                continue
            # Break the header line into header name and value.
            name, value = line.split(":", 1)
            # Now we can actually record the header name and value.
            respheaders[name.strip()] = value.strip()  # name.strip().lower() ?
        resp.store_headers(respheaders)

    return resp
```

--------------------------------

TITLE: Prioritize Recall
DESCRIPTION: Adjusts the extraction process to prioritize recall, aiming to include more elements to capture potentially missing content.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
# Example usage (assuming a URL is provided or piped):
# trafilatura --recall -u "URL"
```

--------------------------------

TITLE: Page Cleaning and Markup Preservation - readability-lxml
DESCRIPTION: readability-lxml is a Python library that cleans web pages by removing extraneous elements while preserving some of the original markup.

SOURCE: https://trafilatura.readthedocs.io/en/latest/evaluation

LANGUAGE: python
CODE:
```
from readability import Document

doc = Document(html_content)

cleaned_html = doc.summary()
```

--------------------------------

TITLE: Convert XML to Plain Text with trafilatura.xml
DESCRIPTION: Converts XML output to plain text format. Optionally preserves formatting as markdown.

SOURCE: https://trafilatura.readthedocs.io/en/latest/corefunctions

LANGUAGE: Python
CODE:
```
trafilatura.xml.xmltotxt(_xmloutput : _Element | None_, _include_formatting : bool_) → str
```

--------------------------------

TITLE: Draw Random Word Tuples with Python
DESCRIPTION: Demonstrates how to draw a specified number of random word tuples from a given list using Python's `random.sample` function. This is useful for generating search queries for web corpus construction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/sources

LANGUAGE: python
CODE:
```
>>> import random
# use the list gathered in (1)
>>> wordlist = ['word1', 'word2', 'word3', 'word4']  # and so on
# draw 3 random words from the list
>>> selection = random.sample(wordlist, k=3)
```

--------------------------------

TITLE: Save Token Frequencies to CSV
DESCRIPTION: This command sorts tokens, counts their unique occurrences, sorts them by frequency in descending order, and then formats the output into a tab-separated CSV file named 'frequencies.csv'. It uses 'sed' to adjust the output format.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial1

LANGUAGE: bash
CODE:
```
$ < tokens.txt sort | uniq -c | sort -nrk1 | sed -e "s|^ *||g" -e  "s| |\t|" > txtfiles/frequencies.csv
```

--------------------------------

TITLE: Whitelisted Platforms for Domain Checks (Python)
DESCRIPTION: This regex defines a set of common blogging and website platforms that are whitelisted. Links from these platforms are treated as exceptions during domain-based filtering to avoid discarding potentially relevant URLs.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/sitemaps

LANGUAGE: Python
CODE:
```
import re

WHITELISTED_PLATFORMS = re.compile(
    r"(?:blogger|blogpost|ghost|hubspot|livejournal|medium|typepad|squarespace|tumblr|weebly|wix|wordpress)\."
)
```

--------------------------------

TITLE: Initialize Justext Stoplist
DESCRIPTION: Retrieves and consolidates stoplists from all available languages for Justext processing. It initializes a global variable 'JT_STOPLIST' with a tuple of all stopword characters. Dependencies include 'get_stoplists' and 'get_stoplist' functions.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/external

LANGUAGE: python
CODE:
```
def jt_stoplist_init() -> Tuple[str]:
    'Retrieve and return the content of all JusText stoplists'
    global JT_STOPLIST
    stoplist = set()
    for language in get_stoplists():
        stoplist.update(get_stoplist(language))
    JT_STOPLIST = tuple(stoplist)
    return JT_STOPLIST
```

--------------------------------

TITLE: Filter URLs on Command-Line with Courlan
DESCRIPTION: The `courlan` command-line utility allows for batch processing of URLs, including filtering and normalization. It supports reading from input files, writing to output files, and applying strict filtering with language options, leveraging multiprocessing for efficiency.

SOURCE: https://trafilatura.readthedocs.io/en/latest/url-management

LANGUAGE: Shell
CODE:
```
# simple filtering and normalization
courlan --inputfile url-list.txt --outputfile cleaned-urls.txt

# strict filtering
courlan --language de --strict --inputfile mylist.txt --outputfile mylist-filtered.txt

# strict filtering including language filter
courlan --language de --strict --inputfile mylist.txt --outputfile mylist-filtered.txt
```

--------------------------------

TITLE: Trafilatura CLI Output Format Options
DESCRIPTION: This section details the various options for specifying the output format when using the Trafilatura CLI, including specific file types and validation options.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-cli

LANGUAGE: bash
CODE:
```
--output-format {csv,json,html,markdown,txt,xml,xmltei}
                      determine output format
--csv                 shorthand for CSV output
--html                shorthand for HTML output
--json                shorthand for JSON output
--markdown            shorthand for MD output
--xml                 shorthand for XML output
--xmltei              shorthand for XML TEI output
--validate-tei        validate XML TEI output
```

--------------------------------

TITLE: Sort: Unique and sorted links
DESCRIPTION: This command uses sort with the `-u` option to sort a list of URLs and remove duplicates. The output is redirected to `myfile-sorted.txt`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial0

LANGUAGE: bash
CODE:
```
sort -u myfile.txt > myfile-sorted.txt
```

--------------------------------

TITLE: Process Metadata Sitename
DESCRIPTION: Handles the processing of the 'sitename' attribute within metadata. It addresses cases where 'sitename' is a list, dictionary, or string, including cleaning, capitalization, and extraction from URLs. Dependencies include the META_URL regex pattern.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/metadata

LANGUAGE: Python
CODE:
```
if isinstance(metadata.sitename, list):
            metadata.sitename = metadata.sitename[0]
        # hotfix: probably an error coming from json_metadata (#195)
        elif isinstance(metadata.sitename, dict):
            metadata.sitename = str(metadata.sitename)
        # scrap Twitter ID
        metadata.sitename = metadata.sitename.lstrip("@")
        # capitalize
        if (
            metadata.sitename
            and "." not in metadata.sitename
            and not metadata.sitename[0].isupper()
        ):
            metadata.sitename = metadata.sitename.title()
    # use URL
    elif metadata.url:
        mymatch = META_URL.match(metadata.url)
        if mymatch:
            metadata.sitename = mymatch[1]
```

--------------------------------

TITLE: Remove Tags from Tokenized XML
DESCRIPTION: This command pipes the output of the somajo-tokenizer to sed to remove all XML tags and empty lines. This prepares the text for subsequent processing steps.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial1

LANGUAGE: shell
CODE:
```
# remove tags
$ somajo-tokenizer --xml xmlfiles/filename.xml | sed -e "s|<\/*.*>||g" -e "/^$/d"
```

--------------------------------

TITLE: Python: Generate Random Word Tuples for Search Queries
DESCRIPTION: This snippet demonstrates how to generate random word tuples from a predefined list using Python's 'random' module. This is a key step in the BootCat method for creating search engine queries to gather seed URLs for web corpus construction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/sources

LANGUAGE: Python
CODE:
```
>>> import random
# use the list gathered in (1)
>>> wordlist = ['word1', 'word2', 'word3', 'word4']  # and so on
# draw 3 random words from the list
>>> selection = random.sample(wordlist, k=3)
```

--------------------------------

TITLE: Extract with Favor Precision
DESCRIPTION: Demonstrates how to use the `extract` function with the `favor_precision` parameter set to True to prioritize accuracy in text extraction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
>>> result = extract(downloaded, url, favor_precision=True)
```

--------------------------------

TITLE: Trafilatura Precision vs. Recall Options
DESCRIPTION: Options to tune the extraction process by favoring either precision (less noise, potentially less text) or recall (more text, potentially more noise).

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
--precision           favor extraction precision (less noise, possibly less
                        text)
  --recall              favor extraction recall (more text, possibly more
                        noise)
```

--------------------------------

TITLE: Fetch Web Page Content
DESCRIPTION: The `fetch_url` function downloads the content of a web page and handles response decoding. It supports disabling SSL verification and allows passing configuration or extraction options.

SOURCE: https://trafilatura.readthedocs.io/en/latest/corefunctions

LANGUAGE: python
CODE:
```
from trafilatura import fetch_url

# Example usage:
# page_content = fetch_url('http://example.com', no_ssl=False)
```

--------------------------------

TITLE: Parse License Element
DESCRIPTION: Probes an HTML link element for identifiable free license cues by parsing its href attribute and link text. It specifically looks for Creative Commons elements.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/metadata

LANGUAGE: Python
CODE:
```
def parse_license_element(element: HtmlElement, strict: bool = False) -> Optional[str]:
    """Probe a link for identifiable free license cues.
    Parse the href attribute first and then the link text."""
    # look for Creative Commons elements
    match = LICENSE_REGEX.search(element.get("href", ""))
    if match:
        return f"CC {match[1].upper()} {match[2]}"
    if element.text:
        # check if it could be a CC license
        if strict:
            match = TEXT_LICENSE_REGEX.search(element.text)
            return match[0] if match else None
        return trim(element.text)
    return None
```

--------------------------------

TITLE: Harvesting Text from Archived Web Pages
DESCRIPTION: This resource from GLAM-Workbench explains how to harvest collections of text from archived web pages. It likely involves using tools or scripts to extract content from web archives.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorials

LANGUAGE: Python
CODE:
```
# Conceptual code snippet for processing archived web pages (e.g., WARC files)
# This would typically involve libraries like 'warcio' or specific archive tools
# from warcio.archiveiterator import ArchiveIterator

# def extract_text_from_warc(warc_file_path):
#     texts = []
#     with open(warc_file_path, 'rb') as stream:
#         for record in ArchiveIterator(stream):
#             if record.rec_type == 'response' and record.http_headers.get_content_type() == 'text/html':
#                 try:
#                     # Use Trafilatura or similar to extract text from HTML content
#                     html_content = record.content_stream().read()
#                     extracted_text = trafilatura.extract(html_content.decode('utf-8', errors='ignore'))
#                     if extracted_text:
#                         texts.append(extracted_text)
#                 except Exception as e:
#                     print(f"Error processing record: {e}")
#     return texts

# warc_file = 'path/to/your/archive.warc.gz'
# extracted_texts = extract_text_from_warc(warc_file)
# print(f"Extracted {len(extracted_texts)} text documents.")
```

--------------------------------

TITLE: Python: Extract text with XML output
DESCRIPTION: Demonstrates how to use the `extract` function in Trafilatura to process downloaded content and output the extracted text in XML format, preserving basic XML structure.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
>>> extract(downloaded, output_format="xml")
```

--------------------------------

TITLE: Pipe HTML File Content to Trafilatura
DESCRIPTION: Reads HTML content from a file named 'myfile.html' and pipes it to trafilatura for text extraction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
$ cat myfile.html | trafilatura
```

--------------------------------

TITLE: Courlan: Filter link list
DESCRIPTION: This command uses the courlan package to filter a list of URLs. It reads from `raw-linklist.txt` and writes the filtered links to `filtered-linklist.txt`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial0

LANGUAGE: bash
CODE:
```
$ courlan --inputfile raw-linklist.txt --outputfile filtered-linklist.txt
```

--------------------------------

TITLE: Filter URLs with courlan
DESCRIPTION: This command demonstrates how to use the `courlan` utility to filter a list of URLs. It reads from an input file (`--inputfile`) and writes the filtered URLs to an output file (`--outputfile`), focusing on non-spam, text-rich HTML pages.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial0

LANGUAGE: bash
CODE:
```
$ courlan --inputfile raw-linklist.txt --outputfile filtered-linklist.txt
```

--------------------------------

TITLE: Make JSON API Request via Python
DESCRIPTION: Shows how to use the Python `requests` library to send a POST request to the Trafilatura API. The code extracts data from a webpage and prints the JSON response.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-api

LANGUAGE: python
CODE:
```
import requests

url = "https://trafilatura.mooo.com/extract-demo"

payload = {
        "url": "https://example.org",
        "args": { "output_format": "xml" }
}
headers = {
        "content-type": "application/json",
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())

```

--------------------------------

TITLE: Try Justext Extraction with Trafilatura
DESCRIPTION: Attempts to extract text content using the Justext algorithm via an external integration. This offers another method for text extraction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/corefunctions

LANGUAGE: Python
CODE:
```
from trafilatura.external import try_justext

# Example usage:
# html = "..."
# text = try_justext(html)

```

--------------------------------

TITLE: Crawl a web page
DESCRIPTION: Manages the crawling of a single web page. It retrieves the URL from the URL store, increments the crawl count, and either probes an alternative homepage for initial crawls or fetches and processes the response for subsequent pages.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/spider

LANGUAGE: Python
CODE:
```
def crawl_page(
    params: CrawlParameters,
    initial: bool = False,
) -> CrawlParameters:
    """Examine a webpage, extract navigation links and links."""
    # config=DEFAULT_CONFIG
    url = URL_STORE.get_url(params.base)
    if not url:
        params.is_on = False
        params.known_num = len(URL_STORE.find_known_urls(params.base))
        return params

    params.i += 1

    if initial:
        # probe and process homepage
        htmlstring, homepage, new_base_url = probe_alternative_homepage(url)
        if htmlstring and homepage and new_base_url:
            # register potentially new homepage
            URL_STORE.add_urls([homepage])
            # extract links on homepage
            process_links(htmlstring, params, url=url)
    else:
        response = fetch_response(url, decode=False)
        process_response(response, params)

    # optional backup of gathered pages without nav-pages ? ...

```

--------------------------------

TITLE: Extract from LXML Tree with Trafilatura
DESCRIPTION: Illustrates how Trafilatura can seamlessly handle input that is already parsed into an LXML object, directly extracting content from the provided HTML tree.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
>>> from lxml import html
>>> my_doc = "<html><body><article><p>
                Here is the main text.
                </p></article></body></html>"
>>> mytree = html.fromstring(my_doc)
>>> extract(mytree)
```

--------------------------------

TITLE: Extract Data with Arguments (R)
DESCRIPTION: Demonstrates how to extract data using Trafilatura in R, specifying output format and URL. The output is shown in XML format.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-r

LANGUAGE: R
CODE:
```
trafilatura$extract(downloaded, output_format="xml", url=url)
```

--------------------------------

TITLE: Try Readability Algorithm
DESCRIPTION: Safely attempts to use the generic readability algorithm for extracting content from HTML. It handles potential exceptions and returns a cleaned HTML element or an empty one if an error occurs. Dependencies include the 'readability_lxml' library and utility functions like 'fromstring_bytes' and 'trim'.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/external

LANGUAGE: python
CODE:
```
from .baseline import basic_cleaning
from .htmlprocessing import convert_tags, prune_unwanted_nodes, tree_cleaning
from .readability_lxml import Document as ReadabilityDocument  # fork
from .settings import JUSTEXT_LANGUAGES
from .utils import fromstring_bytes, trim
from .xml import TEI_VALID_TAGS
from .xpaths import OVERALL_DISCARD_XPATH

LOGGER = logging.getLogger(__name__)

JT_STOPLIST = None

SANITIZED_XPATH = './/aside|.//audio|.//button|.//fieldset|.//figure|.//footer|.//iframe|.//input|.//label|.//link|.//nav|.//noindex|.//noscript|.//object|.//option|.//select|.//source|.//svg|.//time'



[docs]
def try_readability(htmlinput: HtmlElement) -> HtmlElement:
    '''Safety net: try with the generic algorithm readability'''
    # defaults: min_text_length=25, retry_length=250
    try:
        doc = ReadabilityDocument(htmlinput, min_text_length=25, retry_length=250)
        # force conversion to utf-8 (see #319)
        summary = fromstring_bytes(doc.summary())
        return summary if summary is not None else HtmlElement()
    except Exception as err:
        LOGGER.warning('readability_lxml failed: %s', err)
        return HtmlElement()
```

--------------------------------

TITLE: Trafilatura Output Format Options
DESCRIPTION: Determines the output format for the extracted data, supporting various formats like CSV, JSON, HTML, Markdown, XML, and XML TEI.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
--output-format {csv,json,html,markdown,txt,xml,xmltei}
                        determine output format
  --csv                 shorthand for CSV output
  --html                shorthand for HTML output
  --json                shorthand for JSON output
  --markdown            shorthand for MD output
  --xml                 shorthand for XML output
  --xmltei              shorthand for XML TEI output
  --validate-tei        validate XML TEI output
```

--------------------------------

TITLE: Validate TEI-XML Documents with Python
DESCRIPTION: This tutorial explains how to validate TEI-XML documents using Python. It focuses on ensuring the structural integrity and correctness of TEI files, which are commonly used for representing text in digital humanities.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorials

LANGUAGE: Python
CODE:
```
from trafilatura.xml import validate_tei

# Path to your TEI-XML file
tei_file_path = 'path/to/your/tei_file.xml'

# Validate the TEI file
is_valid, errors = validate_tei(tei_file_path)

if is_valid:
    print(f'The TEI file {tei_file_path} is valid.')
else:
    print(f'The TEI file {tei_file_path} is invalid. Errors:')
    for error in errors:
        print(error)
```

--------------------------------

TITLE: Extract text from a URL using Trafilatura in Python
DESCRIPTION: This Python snippet demonstrates how to use Trafilatura to download content from a given URL and then extract the main text and comments. It first fetches the URL content and then processes it for extraction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/index

LANGUAGE: python
CODE:
```
import trafilatura
downloaded = trafilatura.fetch_url('https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/')
trafilatura.extract(downloaded)
```

--------------------------------

TITLE: Sort and Count Token Frequencies
DESCRIPTION: This command sorts the tokens, counts their unique occurrences, and then sorts them again by frequency in descending order, displaying the top 10 most frequent tokens. It utilizes standard Unix utilities like 'sort', 'uniq', and 'head'.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial1

LANGUAGE: bash
CODE:
```
$ sort tokens.txt | uniq -c | sort -nrk1 | head -10
```

--------------------------------

TITLE: Trafilatura Performance Comparison (Python)
DESCRIPTION: This snippet presents a comparative analysis of Trafilatura's performance against other Python libraries for web content extraction. It includes metrics like Precision, Recall, Accuracy, F-Score, and execution time differences.

SOURCE: https://trafilatura.readthedocs.io/en/latest/evaluation

LANGUAGE: Python
CODE:
```
## Results (2022-05-18)#
750 documents, 2236 text & 2250 boilerplate segments, Python 3.8  
---

Python Package | Precision | Recall | Accuracy | F-Score | Diff.  
_raw HTML_ | 0.527 | 0.874 | 0.546 | 0.658 | 0  
html2text 2020.1.16 | 0.486 | 0.709 | 0.481 | 0.577 | 7.6x  
html_text 0.5.2 | 0.529 | **0.958** | 0.554 | 0.682 | 2.2x  
inscriptis 2.2.0 (html to txt) | 0.534 | **0.959** | 0.563 | 0.686 | 3.5x  
newspaper3k 0.2.8 | 0.895 | 0.593 | 0.762 | 0.713 | 12x  
justext 3.0.0 (custom) | 0.865 | 0.650 | 0.775 | 0.742 | 5.2x  
boilerpy3 1.0.6 (article mode) | 0.814 | 0.744 | 0.787 | 0.777 | 4.1x  
_baseline (text markup)_ | 0.757 | 0.827 | 0.781 | 0.790 | **1x**  
goose3 3.1.9 | **0.934** | 0.690 | 0.821 | 0.793 | 22x  
readability-lxml 0.8.1 | 0.891 | 0.729 | 0.820 | 0.801 | 5.8x  
news-please 1.5.22 | 0.898 | 0.734 | 0.826 | 0.808 | 61x  
readabilipy 0.2.0 | 0.877 | 0.870 | 0.874 | 0.874 | 248x  
trafilatura 1.2.2 (fast) | 0.914 | 0.886 | 0.902 | 0.900 | 4.8x  
trafilatura 1.2.2 (precision) | **0.932** | 0.874 | 0.905 | 0.902 | 9.4x  
trafilatura 1.2.2 (standard) | 0.914 | 0.904 | **0.910** | **0.909** | 7.1x  
```

--------------------------------

TITLE: Extract Main Text Content using Python
DESCRIPTION: This tutorial demonstrates how to extract the main text content from web pages using the Trafilatura library in Python. It covers the process of identifying and isolating the primary textual information from HTML documents.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorials

LANGUAGE: Python
CODE:
```
from trafilatura import fetch_url, extract

url = 'http://...' # Replace with the actual URL

# Download the page
html = fetch_url(url)

# Extract the main text content
main_text = extract(html)

# Print the extracted text
if main_text:
    print(main_text)
else:
    print('No text extracted.')
```

--------------------------------

TITLE: Discover Links with Trafilatura
DESCRIPTION: Facilitates the discovery of various types of links, including sitemap URLs and RSS/Atom feed URLs, from web pages or provided data.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/corefunctions

LANGUAGE: Python
CODE:
```
from trafilatura.sitemaps import sitemap_search

# Example usage:
# url = "..."
# sitemaps = sitemap_search(url)

```

LANGUAGE: Python
CODE:
```
from trafilatura.feeds import find_feed_urls

# Example usage:
# html = "..."
# feeds = find_feed_urls(html)

```

--------------------------------

TITLE: Exporting Search Results from DWDS
DESCRIPTION: This section describes how to export search results from the DWDS portal. The exported data, typically in CSV or TSV format, can be opened with spreadsheet software like LibreOffice Calc, Microsoft Excel, or Apple Numbers. The URLs from the results can then be saved as a separate list for further processing.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial-dwds

LANGUAGE: text
CODE:
```
CSV- oder TSV-Dateien können von der frei verfügbaren Software LibreOffice Calc sowie von Microsoft Excel oder Apple Numbers geöffnet werden. Die Quellen (URLs) werden in einer Spalte aufgelistet und können dann als getrennte Liste anderswo gespeichert werden.
```

--------------------------------

TITLE: Making JSON Requests with Trafilatura API
DESCRIPTION: Illustrates how to interact with the Trafilatura API by making JSON requests. This is for programmatic access to Trafilatura's extraction functionalities, often used in web services.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage

LANGUAGE: bash
CODE:
```
curl -X POST -H "Content-Type: application/json" -d '{"url": "http://example.com"}' http://localhost:8080/extract
```

--------------------------------

TITLE: Filter and count tokens
DESCRIPTION: Filters out punctuation and empty lines from the tokenized text, converts all tokens to lowercase, and then sorts and counts the most frequent tokens, displaying the top 20.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial1

LANGUAGE: bash
CODE:
```
$ < tokens.txt sed -e "s/[[:punct:]]//g" -e "/^$/d" -e "s/.*/\L\0/" > tokens-filtered.txt
# display most frequent tokens
$ < tokens-filtered.txt sort | uniq -c | sort -nrk1 | head -20
```

--------------------------------

TITLE: Web Crawling Infrastructure - Courlan Library
DESCRIPTION: Mentions the 'courlan' library as the core component for web crawling tasks, providing the necessary 'brain' for managing and executing crawls and downloads.

SOURCE: https://trafilatura.readthedocs.io/en/latest/compendium

LANGUAGE: Python
CODE:
```
# See documentation on crawls and downloads as well as the “brain” for web crawling tasks: the library courlan.
```

--------------------------------

TITLE: Build JSON Output
DESCRIPTION: Constructs a JSON string representation of document metadata. Includes options to include or exclude metadata and formats specific fields like categories and tags.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
def build_json_output(docmeta: Document, with_metadata: bool = True) -> str:
    '''Build JSON output based on extracted information'''
    if with_metadata:
        outputdict = {slot: getattr(docmeta, slot, None) for slot in docmeta.__slots__}
        outputdict.update({
            'source': outputdict.pop('url'),
            'source-hostname': outputdict.pop('sitename'),
            'excerpt': outputdict.pop('description'),
            'categories': ';'.join(outputdict.pop('categories') or []),
            'tags': ';'.join(outputdict.pop('tags') or []),
            'text': xmltotxt(outputdict.pop('body'), include_formatting=False),
        })
        commentsbody = outputdict.pop('commentsbody')
    else:
        outputdict = {'text': xmltotxt(docmeta.body, include_formatting=False)}
        commentsbody = docmeta.commentsbody

    outputdict['comments'] = xmltotxt(commentsbody, include_formatting=False)

    return json_dumps(outputdict, ensure_ascii=False)
```

--------------------------------

TITLE: Crawl URLs, Generate Embeddings, and Store in Epsilla
DESCRIPTION: This Python snippet shows how to use Trafilatura to fetch and extract text content from URLs, then utilizes the HuggingFaceBgeEmbeddings model from Langchain to generate vector embeddings for the extracted text. Finally, it inserts the records containing document text and their embeddings into the Epsilla database.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial-epsilla

LANGUAGE: python
CODE:
```
# import Trafilatura and embedding model
from trafilatura import fetch_url, extract
from langchain.embeddings import HuggingFaceBgeEmbeddings

model_name = "BAAI/bge-small-en"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}

hf = HuggingFaceBgeEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

# download the homepages from a few open source projects
urls = [
    'https://www.tensorflow.org/',
    'https://pytorch.org/',
    'https://react.dev/',
]
results = [extract(fetch_url(url)) for url in urls]

# get the embedding vector and store it in Epsilla
embeddings = [hf.embed_query(result) for result in results]
records = [
    {"ID": idx, "Doc": results[idx], "Embedding": embeddings[idx]}
    for idx in range(len(results))
]
client.insert(
   table_name="Trafilatura",
   records=records
)
```

--------------------------------

TITLE: Python Trafilatura Document Extraction
DESCRIPTION: Demonstrates how to use the trafilatura library for document extraction. It covers parameter configuration, handling deprecated arguments, and post-processing steps like adding metadata and calculating fingerprints. The function returns the extracted document in a specified format or None.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/core

LANGUAGE: python
CODE:
```
import warnings
from trafilatura.settings import Extractor
from trafilatura.utils import use_config
from trafilatura.exceptions import PendingDeprecationWarning
from trafilatura.document import Document
from trafilatura.extractors import bare_extraction
from trafilatura.output import determine_returnstring
from trafilatura.fingerprint import content_fingerprint

TXT_FORMATS = {"txt", "json", "xml", "html", "csv", "yaml", "python"}

def extract_document(
    filecontent,
    output_format="txt",
    include_comments=False,
    include_tables=False,
    include_images=False,
    include_formatting=False,
    include_links=False,
    deduplicate=False,
    date_extraction_params=None,
    with_metadata=True,
    only_with_metadata=False,
    url_blacklist=None,
    author_blacklist=None,
    settingsfile=None,
    prune_xpath=None,
    config=None,
    options=None,
    fast=None,
    favor_precision=False,
    favor_recall=False,
    tei_validation=False,
    record_id=None,
    no_fallback=None,
    max_tree_size=None,
):
    """
    Extracts a document from a given HTML file content.

    Parameters:
        filecontent (str): The HTML content of the file.
        output_format (str): The desired output format (e.g., "txt", "json", "xml").
        include_comments (bool): Whether to include comments in the output.
        include_tables (bool): Whether to include information within HTML <table> elements.
        include_images (bool): Whether to include images (experimental).
        include_formatting (bool): Whether to keep structural elements related to formatting.
        include_links (bool): Whether to keep links along with their targets (experimental).
        deduplicate (bool): Whether to remove duplicate segments and documents.
        date_extraction_params (dict): Parameters for date extraction.
        with_metadata (bool): Whether to extract and add metadata to the output.
        only_with_metadata (bool): Whether to only keep documents with essential metadata.
        url_blacklist (set): A set of URLs to filter out.
        author_blacklist (set): A set of author names to filter out.
        settingsfile (str): Path to a configuration file.
        prune_xpath (str or list): XPath expression to prune the tree before extraction.
        config (configparser.ConfigParser): Directly provide a configparser configuration.
        options (Extractor): Directly provide a whole extractor configuration.
        fast (bool): Use faster extraction mode.
        favor_precision (bool): Favor precision over recall.
        favor_recall (bool): Favor recall over precision.
        tei_validation (bool): Whether to perform TEI validation.
        record_id (str): Identifier for the record.
        no_fallback (bool): Deprecated, use "fast" instead.
        max_tree_size (int): Deprecated, use settings.cfg file instead.

    Returns:
        A string in the desired format or None.

    """
    if no_fallback:
        fast = no_fallback
        warnings.warn(
            '"no_fallback" will be deprecated in a future version, use "fast" instead',
            PendingDeprecationWarning
        )

    if max_tree_size:
        raise ValueError("max_tree_size is deprecated, use settings.cfg file instead")

    # regroup extraction options
    if not options or not isinstance(options, Extractor):
        options = Extractor(
            config=use_config(settingsfile, config),
            output_format=output_format,
            fast=fast,
            precision=favor_precision,
            recall=favor_recall,
            comments=include_comments,
            formatting=include_formatting,
            links=include_links,
            images=include_images,
            tables=include_tables,
            dedup=deduplicate,
            lang=target_language,
            url=url,
            with_metadata=with_metadata,
            only_with_metadata=only_with_metadata,
            tei_validation=tei_validation,
            author_blacklist=author_blacklist,
            url_blacklist=url_blacklist,
            date_params=date_extraction_params,
        )

    # extraction
    document = bare_extraction(
        filecontent,
        options=options,
        as_dict=False,
        prune_xpath=prune_xpath,
    )

    # post-processing
    if not document or not isinstance(document, Document):
        return None

    if options.format not in TXT_FORMATS:
        # control output
        if options.format == "python":
            raise ValueError(
                "'python' format only usable in bare_extraction() function"
            )
        # add record ID to metadata
        document.id = record_id
        # calculate fingerprint
        if document.raw_text is not None:
            document.fingerprint = content_fingerprint(
                str(document.title) + " " + str(document.raw_text)
            )

    # return
    return determine_returnstring(document, options)
```

--------------------------------

TITLE: Generate Word Bigrams and Count Frequencies
DESCRIPTION: This command generates word bigrams (pairs of consecutive words) from the filtered tokens, counts their frequencies, and displays the top 20 most frequent bigrams. It uses 'tr' to replace newlines with spaces, 'awk' to create bigrams, and standard Unix sorting utilities.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial1

LANGUAGE: bash
CODE:
```
$ < tokens-filtered.txt tr "\n" " " | awk '{for (i=1; i<NF; i++) print $i, $(i+1)}' | sort | uniq -c | sort -nrk1 | head -20
```

--------------------------------

TITLE: Fetch and Extract Text from URL in R
DESCRIPTION: Demonstrates fetching a web page using Trafilatura's fetch_url and extracting text content using the extract function within an R session.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-r

LANGUAGE: R
CODE:
```
# getting started
> install.packages("reticulate")
> library(reticulate)

# loading the Trafilatura module
> trafilatura <- import("trafilatura")

# fetching a web page
> url <- "https://example.org/"
> downloaded <- trafilatura$fetch_url(url)

# extracting the text content
> text <- trafilatura$extract(downloaded)
> cat(text)
[1] "This domain is for use in illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission.\nMore information..."
```

--------------------------------

TITLE: Trafilatura Baseline Module
DESCRIPTION: This snippet provides the source code for the trafilatura.baseline module, which regroups baseline and basic extraction functions for web content.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/baseline

LANGUAGE: python
CODE:
```
"""
Module regrouping baseline and basic extraction functions.
"""
```

--------------------------------

TITLE: Extract Metadata with Bare Extraction
DESCRIPTION: Demonstrates using the `bare_extraction` function to bypass output conversion, returning Python variables for metadata (dictionary) and main text/comments (LXML objects).

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
from trafilatura import bare_extraction
>>> bare_extraction(downloaded)
```

--------------------------------

TITLE: Main Metadata Extraction Process
DESCRIPTION: The primary function for metadata extraction from HTML content. It orchestrates the calls to various extraction functions for title, author, URL, date, and sitename, with options for configuration and blacklisting.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/metadata

LANGUAGE: Python
CODE:
```
def extract_metadata(
    filecontent: Union[HtmlElement, str],
    default_url: Optional[str] = None,
    date_config: Optional[Any] = None,
    extensive: bool = True,
    author_blacklist: Optional[Set[str]] = None,
) -> Document:
    """Main process for metadata extraction.

    Args:
        filecontent: HTML code as string or parsed tree.
        default_url: Previously known URL of the downloaded document.
        date_config: Provide extraction parameters to htmldate as dict().
        author_blacklist: Provide a blacklist of Author Names as set() to filter out authors.

    Returns:
        A trafilatura.settings.Document containing the extracted metadata information or None.
        The Document class has .as_dict() method that will return a copy as a dict.
    """
    # init
    author_blacklist = author_blacklist or set()
    date_config = date_config or set_date_params(extensive)

    # load contents
    tree = load_html(filecontent)
    if tree is None:
        return Document()

    # initialize dict and try to strip meta tags
    metadata = examine_meta(tree)

    # to check: remove it and replace with author_blacklist in test case
    if metadata.author and " " not in metadata.author:
        metadata.author = None

    # fix: try json-ld metadata and override
    try:
        metadata = extract_meta_json(tree, metadata)
    except Exception as err:  # bugs in json_metadata.py
        LOGGER.warning("error in JSON metadata extraction: %s", err)

    # title
    if not metadata.title:
        metadata.title = extract_title(tree)

    # check author in blacklist
    if metadata.author and author_blacklist:
        metadata.author = check_authors(metadata.author, author_blacklist)
    # author
    if not metadata.author:
        metadata.author = extract_author(tree)
    # recheck author in blacklist
    if metadata.author and author_blacklist:
        metadata.author = check_authors(metadata.author, author_blacklist)

    # url
    if not metadata.url:
        metadata.url = extract_url(tree, default_url)

    # hostname
    if metadata.url:
        metadata.hostname = extract_domain(metadata.url, fast=True)

    # extract date with external module htmldate
    date_config["url"] = metadata.url
    metadata.date = find_date(tree, **date_config)

    # sitename
    if not metadata.sitename:
        metadata.sitename = extract_sitename(tree)
    if metadata.sitename:
        
```

--------------------------------

TITLE: Import External Libraries for Text Processing
DESCRIPTION: This snippet demonstrates the import of essential classes and functions from the 'justext' and 'lxml' libraries. These libraries are crucial for paragraph classification, stoplist management, and HTML element manipulation within the Trafilatura project.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/external

LANGUAGE: Python
CODE:
```
# pylint:disable-msg=E0611,I1101
"""
Functions grounding on third-party software.
"""

import logging

from typing import Any, Tuple

# third-party
from justext.core import ParagraphMaker, classify_paragraphs, revise_paragraph_classification  # type: ignore
from justext.utils import get_stoplist, get_stoplists  # type: ignore
from lxml.etree import _Element, Element, strip_tags, tostring
from lxml.html import HtmlElement
```

--------------------------------

TITLE: Search Sitemaps from Homepage (Python)
DESCRIPTION: Automatically discovers and retrieves sitemap URLs by providing a website's homepage URL. This is useful for indexing or crawling websites.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
from trafilatura import sitemaps

# automatically find sitemaps by providing the homepage
mylinks = sitemaps.sitemap_search('https://www.theguardian.com/')
```

--------------------------------

TITLE: Extract Metadata with Custom Date Parameters
DESCRIPTION: Shows how to pass custom parameters to the date extraction module, including enabling extensive search heuristics and setting a maximum acceptable date for extraction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
>>> extract(downloaded, output_format="xml", date_extraction_params={
        "extensive_search": True, "max_date": "2018-07-01"
    })
```

--------------------------------

TITLE: Trafilatura: Load HTML
DESCRIPTION: Loads HTML content, potentially from a file or a string. This function prepares the HTML for further processing by the library.

SOURCE: https://trafilatura.readthedocs.io/en/latest/genindex

LANGUAGE: python
CODE:
```
from trafilatura import load_html

# Example usage:
# html_file_path = "path/to/your/file.html"
# html_content = load_html(html_file_path)
```

--------------------------------

TITLE: Check Response Suitability
DESCRIPTION: Validates if a given response meets predefined criteria, such as having a status code of 200 and an acceptable content length. It logs errors for non-conforming responses.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/downloads

LANGUAGE: Python
CODE:
```
def _is_suitable_response(url: str, response: Response, options: Extractor) -> bool:
    """Check if the response conforms to formal criteria."""
    lentest = len(response.html or response.data or "")
    if response.status != 200:
        LOGGER.error("not a 200 response: %s for URL %s", response.status, url)
        return False
    # raise error instead?
    if not is_acceptable_length(lentest, options):
        return False
    return True
```

--------------------------------

TITLE: Exporting DWDS Search Results to CSV/TSV
DESCRIPTION: This section details how to export search results from the DWDS platform. Users can click the 'Export Results' button and choose formats like CSV or TSV. These files can be opened with spreadsheet software like LibreOffice Calc, Microsoft Excel, or Apple Numbers, allowing for the extraction of source URLs.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial-dwds

LANGUAGE: text
CODE:
```
Click the 'Export Results' button.
Choose between CSV or TSV formats.
Open the exported file with spreadsheet software (e.g., LibreOffice Calc).
Select the column containing URLs and copy them.
```

--------------------------------

TITLE: Optimize extraction speed with specific settings - Python
DESCRIPTION: For shorter processing times, combine settings like `include_comments=False`, `include_tables=False`, and `no_fallback=True`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
result = extract(downloaded, include_comments=False, include_tables=False, no_fallback=True)
```

--------------------------------

TITLE: Perform another iteration using previously collected information
DESCRIPTION: This Python code snippet demonstrates how to perform another iteration of the focused crawler using previously collected information. It takes the current `to_visit` and `known_links` as input and returns updated versions after crawling.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/crawls

LANGUAGE: python
CODE:
```
to_visit, known_links = focused_crawler("https://example.org", max_seen_urls=10, max_known_urls=100000, todo=to_visit, known_links=known_links)
```

--------------------------------

TITLE: Load Data with Pandas
DESCRIPTION: Demonstrates how to load data into the Pandas data analysis library, commonly used for data science tasks. It highlights the `read_csv` and `read_json` functions.

SOURCE: https://trafilatura.readthedocs.io/en/latest/corpus-data

LANGUAGE: python
CODE:
```
import pandas as pd

# Example for reading a CSV file
df_csv = pd.read_csv('your_data.csv')

# Example for reading a JSON file
df_json = pd.read_json('your_data.json')
```

--------------------------------

TITLE: Python: Skip tables and include links
DESCRIPTION: Demonstrates customizing the extraction process to exclude HTML table content while including hyperlinks found within the document. This allows for selective data capture.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
>>> result = extract(downloaded, include_tables=False, include_links=True)
```

--------------------------------

TITLE: Check if a Page is Live using urllib3
DESCRIPTION: Uses courlan's redirection test, which is based on urllib3, to send a HEAD request and check if a web page is live. It catches general exceptions that might occur during the process.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/downloads

LANGUAGE: Python
CODE:
```
def _urllib3_is_live_page(url: str) -> bool:
    """Use courlan redirection test (based on urllib3) to send a HEAD request."""
    try:
        _ = redirection_test(url)
    except Exception as err:
        LOGGER.debug("urllib3 HEAD error: %s %s", url, err)
        return False
    return True
```

--------------------------------

TITLE: Python: Fast Mode Extraction
DESCRIPTION: Illustrates how to use Trafilatura in a faster mode by bypassing fallback algorithms, which can improve performance at the potential cost of accuracy. This is done using the `no_fallback` option.

SOURCE: https://trafilatura.readthedocs.io/en/latest/quickstart

LANGUAGE: Python
CODE:
```
result = extract(downloaded, no_fallback=True)
```

--------------------------------

TITLE: Import Libraries for Feed Processing in Python
DESCRIPTION: This snippet imports essential Python libraries and custom modules required for feed examination and link extraction. It includes standard libraries for data handling, logging, regular expressions, iteration, time management, and type hinting, along with the 'courlan' library for URL manipulation and internal trafilatura modules for deduplication, downloads, settings, and utility functions.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/feeds

LANGUAGE: Python
CODE:
```
import json
import logging
import re

from itertools import islice
from time import sleep
from typing import List, Optional

from courlan import (
    check_url,
    clean_url,
    filter_urls,
    fix_relative_urls,
    get_hostinfo,
    is_valid_url,
)

from .deduplication import is_similar_domain
from .downloads import fetch_url
from .settings import MAX_LINKS
from .utils import load_html

LOGGER = logging.getLogger(__name__)
```

--------------------------------

TITLE: Boilerplate Removal and Fulltext Extraction - boilerpy3
DESCRIPTION: boilerpy3 is a Python implementation of the boilerpipe algorithm, designed for boilerplate removal and extracting the full text content from web pages.

SOURCE: https://trafilatura.readthedocs.io/en/latest/evaluation

LANGUAGE: python
CODE:
```
from boilerpy import extractors

extractor = extractors.ArticleExtractor()
text = extractor.get_full_text(html_content)
```

--------------------------------

TITLE: Generate Word Trigrams and Count Frequencies
DESCRIPTION: This command generates word trigrams (sequences of three consecutive words) from the filtered tokens, counts their frequencies, and displays the top 20 most frequent trigrams. It uses 'tr' to replace newlines with spaces, 'awk' to create trigrams, and standard Unix sorting utilities.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial1

LANGUAGE: bash
CODE:
```
$ < tokens-filtered.txt tr "\n" " " | awk '{for (i=1; i<NF; i++) print $i, $(i+1), $(i+2)}' | sort | uniq -c | sort -nrk1 | head -20
```

--------------------------------

TITLE: Handle HTML Elements in Trafilatura
DESCRIPTION: This snippet shows how trafilatura's `handle_paragraphs` and other element-specific handlers process different HTML tags like 'lb', 'table', and 'graphic' to extract content. It includes logic for formatting tags and other elements, returning a new element representing the processed content.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
new_element = handle_paragraphs(element, potential_tags, options)
    elif element.tag == 'lb':
        if text_chars_test(element.tail) is True:
            this_element = process_node(element, options)
            if this_element is not None:
                new_element = Element('p')
                new_element.text = this_element.tail
    elif element.tag in FORMATTING:
        new_element = handle_formatting(element, options)  # process_node(element, options)
    elif element.tag == 'table' and 'table' in potential_tags:
        new_element = handle_table(element, potential_tags, options)
    elif element.tag == 'graphic' and 'graphic' in potential_tags:
        new_element = handle_image(element)
    else:
        # other elements (div, ??, ??) 
        new_element = handle_other_elements(element, potential_tags, options)
    return new_element
```

--------------------------------

TITLE: Try Readability Extraction with Trafilatura
DESCRIPTION: Attempts to extract text content using the Readability.js algorithm via an external integration. This provides an alternative extraction method.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/corefunctions

LANGUAGE: Python
CODE:
```
from trafilatura.external import try_readability

# Example usage:
# html = "..."
# text = try_readability(html)

```

--------------------------------

TITLE: HTML to Plain Text Conversion - html_text
DESCRIPTION: The html_text Python package converts HTML code into plain text, simplifying the content for easier processing.

SOURCE: https://trafilatura.readthedocs.io/en/latest/evaluation

LANGUAGE: python
CODE:
```
from html_text import extract_text

plain_text = extract_text(html_content)
```

--------------------------------

TITLE: Set Download Sleep Time with Trafilatura
DESCRIPTION: Illustrates how to set a custom sleep time between download requests for the same domain when using Trafilatura's `load_download_buffer` function to manage politeness and avoid server overload.

SOURCE: https://trafilatura.readthedocs.io/en/latest/downloads

LANGUAGE: python
CODE:
```
from trafilatura.downloads import load_download_buffer

# 30 seconds is a safe choice
mybuffer, threads, domain_dict, backoff_dict = load_download_buffer(url_store, sleep_time=30)
# then proceed as instructed above...
```

--------------------------------

TITLE: Justext Rescue Function
DESCRIPTION: The `justext_rescue` function serves as a secondary fallback mechanism using the Justext algorithm. It first applies basic cleaning to the HTML tree, then attempts to extract text using Justext. The extracted text is further processed by trimming whitespace. The function returns the Justext result, the cleaned text, and its length.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/external

LANGUAGE: Python
CODE:
```
def justext_rescue(tree: HtmlElement, options: Any) -> Tuple[_Element, str, int]:
    '''Try to use justext algorithm as a second fallback'''
    # additional cleaning
    tree = basic_cleaning(tree)
    # proceed
    temppost_algo = try_justext(tree, options.url, options.lang)
    temp_text = trim(' '.join(temppost_algo.itertext()))
    return temppost_algo, temp_text, len(temp_text)
```

--------------------------------

TITLE: News Crawler and Structured Information Extraction - news-please
DESCRIPTION: news-please is a Python-based news crawler that extracts structured information from news articles, facilitating data analysis and aggregation.

SOURCE: https://trafilatura.readthedocs.io/en/latest/evaluation

LANGUAGE: python
CODE:
```
from news_please import NewsPlease

news_item = NewsPlease.get_from_url(url)

print(news_item.title)
print(news_item.text)
```

--------------------------------

TITLE: Discover Sitemap Links
DESCRIPTION: The `sitemap_search` function locates and gathers links from sitemaps associated with a given URL. It allows filtering by target language and whether to include external links, with configurable sleep times and a maximum number of sitemaps to process.

SOURCE: https://trafilatura.readthedocs.io/en/latest/corefunctions

LANGUAGE: python
CODE:
```
from trafilatura.sitemaps import sitemap_search

# Example usage:
# links = sitemap_search('http://example.com', target_lang='en', external=False, sleep_time=2.0)
```

--------------------------------

TITLE: Determine Return String Format
DESCRIPTION: Converts an XML tree to a chosen format (XML, CSV, JSON, HTML, Markdown, TXT), cleans the result, and outputs it as a string. It handles metadata inclusion and Unicode normalization.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/core

LANGUAGE: python
CODE:
```
def determine_returnstring(document: Document, options: Extractor) -> str:
    """Convert XML tree to chosen format, clean the result and output it as a string"""
    # XML (TEI) steps
    if "xml" in options.format:
        # last cleaning
        for element in document.body.iter("*"):
            if (
                element.tag != "graphic"
                and len(element) == 0
                and not element.text
                and not element.tail
            ):
                parent = element.getparent()
                # do not remove elements inside <code> to preserve formatting
                if parent is not None and parent.tag != "code":
                    parent.remove(element)
        # build output tree
        returnstring = control_xml_output(document, options)
    # CSV
    elif options.format == "csv":
        returnstring = xmltocsv(document, options.formatting)
    # JSON
    elif options.format == "json":
        returnstring = build_json_output(document, options.with_metadata)
    # HTML
    elif options.format == "html":
        returnstring = build_html_output(document, options.with_metadata)
    # Markdown and TXT
    else:
        if options.with_metadata:
            header = "---
"
            for attr in (
                "title",
                "author",
                "url",
                "hostname",
                "description",
                "sitename",
                "date",
                "categories",
                "tags",
                "fingerprint",
                "id",
                "license",
            ):
                if getattr(document, attr):
                    header += f"{attr}: {str(getattr(document, attr))}\n"
            header += "---
"
        else:
            header = ""
        returnstring = f"{header}{xmltotxt(document.body, options.formatting)}"
        if document.commentsbody is not None:
            returnstring = f"{returnstring}\n{xmltotxt(document.commentsbody, options.formatting)}".strip()
    # normalize Unicode format (defaults to NFC)
    return normalize_unicode(returnstring)
```

--------------------------------

TITLE: Check if a Page is Live using pycurl
DESCRIPTION: Sends a basic HTTP HEAD request using the pycurl library to determine if a web page is live. It includes options for connection timeout, SSL verification, and proxy settings. Error handling for pycurl exceptions is also included.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/downloads

LANGUAGE: Python
CODE:
```
def _pycurl_is_live_page(url: str) -> bool:
    """Send a basic HTTP HEAD request with pycurl."""
    page_exists = False
    # Initialize pycurl object
    curl = pycurl.Curl()
    # Set the URL and HTTP method (HEAD)
    curl.setopt(pycurl.URL, url.encode("utf-8"))
    curl.setopt(pycurl.CONNECTTIMEOUT, 10)
    # no SSL verification
    curl.setopt(pycurl.SSL_VERIFYPEER, 0)
    curl.setopt(pycurl.SSL_VERIFYHOST, 0)
    # Set option to avoid getting the response body
    curl.setopt(curl.NOBODY, True)
    if PROXY_URL:
        curl.setopt(pycurl.PRE_PROXY, PROXY_URL)
    # Perform the request
    try:
        curl.perform()
        # Get the response code
        page_exists = curl.getinfo(curl.RESPONSE_CODE) < 400
    except pycurl.error as err:
        LOGGER.debug("pycurl HEAD error: %s %s", url, err)
        page_exists = False
    # Clean up
    curl.close()
    return page_exists
```

--------------------------------

TITLE: Find Feed URLs with Trafilatura
DESCRIPTION: Demonstrates how to use the `feeds.find_feed_urls` function to automatically discover RSS or Atom feed URLs from a given homepage. It also shows how to filter these feeds by a target language using the `target_lang` argument.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
from trafilatura import feeds

# Use the homepage to automatically retrieve feeds
mylist = feeds.find_feed_urls('https://www.theguardian.com/')
print(mylist)

# Use a predetermined feed URL directly
mylist = feeds.find_feed_urls('https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
print(mylist is not [])

# Search for feeds in English
mylist = feeds.find_feed_urls('https://www.un.org/en/rss.xml', target_lang='en')
print(mylist is not [])

# Target language set to Japanese, English links are discarded
mylist = feeds.find_feed_urls('https://www.un.org/en/rss.xml', target_lang='ja')
print(mylist)
```

--------------------------------

TITLE: Discover and Download Feed URLs
DESCRIPTION: Explains the `find_feed_urls` utility function, which discovers and downloads feeds from a webpage, returning a sorted list of unique links.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
# The function `find_feed_urls` is a all-in-one utility that attempts to discover the feeds from a webpage if required and/or downloads and parses feeds. It returns the extracted links as list, more precisely as a sorted list of unique links.
```

--------------------------------

TITLE: Sort and Deduplicate URLs with sort
DESCRIPTION: This command sorts the URLs in `myfile.txt` and removes duplicate entries using the `-u` flag. The unique, sorted list is saved to `myfile-sorted.txt`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial0

LANGUAGE: bash
CODE:
```
sort -u myfile.txt > myfile-sorted.txt
```

--------------------------------

TITLE: Generate Word Bigrams
DESCRIPTION: This command generates a list of the 20 most frequent word bigrams from a text file. It processes the input by replacing newlines with spaces, extracts adjacent word pairs, sorts them, counts unique occurrences, and then sorts by count in descending order.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial1

LANGUAGE: bash
CODE:
```
# word bigrams
$ < tokens-filtered.txt tr "\n" " " | awk '{for (i=1; i<NF; i++) print $i, $(i+1)}' | sort | uniq -c | sort -nrk1 | head -20
```

--------------------------------

TITLE: Trafilatura Deduplication Option
DESCRIPTION: Filters out duplicate documents and sections to ensure unique content in the output.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
--deduplicate         filter out duplicate documents and sections
```

--------------------------------

TITLE: Convert BeautifulSoup to LXML for Trafilatura
DESCRIPTION: Demonstrates the process of converting a BeautifulSoup object to an LXML format using `convert_tree` before passing it to Trafilatura's `extract` function.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
>>> from bs4 import BeautifulSoup
>>> from lxml.html.soupparser import convert_tree
>>> from trafilatura import extract
>>> soup = BeautifulSoup("<html><body><time>The date is Feb 2, 2024</time></body></html>", "lxml")
>>> lxml_tree = convert_tree(soup)[0]
>>> extract(lxml_tree)
```

--------------------------------

TITLE: Randomly Sort URLs with sort
DESCRIPTION: This command randomly sorts the URLs in `myfile.txt` using the `-R` flag and saves the result to `myfile-random.txt`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial0

LANGUAGE: bash
CODE:
```
sort -R myfile.txt > myfile-random.txt
```

--------------------------------

TITLE: Trafilatura Target Language Option
DESCRIPTION: Specifies the target language for extraction using ISO 639-1 codes. This helps in processing documents in a specific language.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
--target-language TARGET_LANGUAGE
                        select a target language (ISO 639-1 codes)
```

--------------------------------

TITLE: Reuse Simhash Object with Existing Hash (Python)
DESCRIPTION: Demonstrates how to reuse an existing Simhash object by initializing a new Simhash instance with the hash value of a previously computed Simhash object. This allows for efficient comparison without recomputing the hash.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/deduplication

LANGUAGE: python
CODE:
```
from trafilatura.deduplication import Simhash

first = Simhash("This is a text.")
first_copy = Simhash(existing_hash=first.hash)
print(first_copy.similarity(first))
```

--------------------------------

TITLE: Filter URLs via Command-Line with Courlan (Bash)
DESCRIPTION: The courlan command-line utility allows filtering and normalization of URLs from input files to output files. Options like `--strict` and `--language` can be used for refined filtering.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/url-management

LANGUAGE: bash
CODE:
```
# simple filtering and normalization
$ courlan --inputfile url-list.txt --outputfile cleaned-urls.txt

# strict filtering
$ courlan --language de --strict --inputfile mylist.txt --outputfile mylist-filtered.txt

# strict filtering including language filter
$ courlan --language de --strict --inputfile mylist.txt --outputfile mylist-filtered.txt
```

--------------------------------

TITLE: Write TEI Header Metadata
DESCRIPTION: Writes the TEI header based on gathered metadata from a `Document` object. It includes file description, title statement (main title and author), and publication statement. Future enhancements may include adding language information. Dependencies include `Element`, `SubElement` from `xml.etree.ElementTree`, and `Document` type.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
from xml.etree.ElementTree import Element, SubElement, Element as _Element

# Assuming Document is defined elsewhere

def write_fullheader(teidoc: _Element, docmeta: Document) -> _Element:
    """Write TEI header based on gathered metadata"""
    # todo: add language info
    header = SubElement(teidoc, 'teiHeader')
    filedesc = SubElement(header, 'fileDesc')
    bib_titlestmt = SubElement(filedesc, 'titleStmt')
    SubElement(bib_titlestmt, 'title', type='main').text = docmeta.title
    if docmeta.author:
        SubElement(bib_titlestmt, 'author').text = docmeta.author

    publicationstmt_a = SubElement(filedesc, 'publicationStmt')
    # Further publication statement details would go here
    return header

class Document:
    # Placeholder for Document class definition
    def __init__(self):
        self.title = None
        self.author = None

```

--------------------------------

TITLE: Reuse Simhash Object with Existing Hash
DESCRIPTION: Shows how to create a new Simhash object using the hash value of an existing Simhash object, ensuring perfect similarity.

SOURCE: https://trafilatura.readthedocs.io/en/latest/deduplication

LANGUAGE: Python
CODE:
```
from trafilatura.deduplication import Simhash

first = Simhash("This is a text.")
first_copy = Simhash(existing_hash=first.hash)
first_copy.similarity(first)
```

--------------------------------

TITLE: Handle List of Links
DESCRIPTION: Examines a list of links, fixes relative URLs, checks their validity, and filters them based on domain similarity and other criteria. Returns a list of valid and refined links.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/feeds

LANGUAGE: Python
CODE:
```
def handle_link_list(linklist: List[str], params: FeedParameters) -> List[str]:
    """Examine links to determine if they are valid and
    lead to a web page"""
    output_links = []

    for item in sorted(set(linklist)):
        link = fix_relative_urls(params.base, item)
        checked = check_url(link, language=params.lang)

        if checked is not None:
            if (
                not params.ext
                and "feed" not in link
                and not is_similar_domain(params.domain, checked[1])
            ):
                LOGGER.warning(
                    "Rejected, diverging domain names: %s %s", params.domain, checked[1]
                )
            else:
                output_links.append(checked[0])
        # Feedburner/Google feeds
        elif "feedburner" in item or "feedproxy" in item:
            output_links.append(item)

    return output_links
```

--------------------------------

TITLE: Trafilatura CLI Extraction Customization
DESCRIPTION: This section details the command-line options for customizing the text extraction process in Trafilatura, including formatting, metadata, language targeting, and deduplication.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-cli

LANGUAGE: bash
CODE:
```
-f, --fast
fast (without fallback detection)
--formatting
include text formatting (bold, italic, etc.)
--links
include links along with their targets (experimental)
--images
include image sources in output (experimental)
--no-comments
don’t output any comments
--no-tables
don’t output any table elements
--only-with-metadata
only output those documents with title, URL and date
--with-metadata
extract and add metadata to the output
--target-language TARGET_LANGUAGE
select a target language (ISO 639-1 codes)
--deduplicate
filter out duplicate documents and sections
--config-file CONFIG_FILE
override standard extraction parameters with a custom config file
--precision
favor extraction precision (less noise, possibly less text)
--recall
favor extraction recall (more text, possibly more noise)
```

--------------------------------

TITLE: Extract Data via API using Python
DESCRIPTION: Provides a Python code snippet to send a POST request to the Trafilatura API for data extraction. The response is expected in JSON format. Requires Python and the 'requests' library.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-api

LANGUAGE: python
CODE:
```
import requests

url = "https://trafilatura.mooo.com/extract-demo"

payload = {
	"url": "https://example.org",
	"args": { "output_format": "xml" }
}
headers = {
	"content-type": "application/json",
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

--------------------------------

TITLE: Perform Vector Search in Epsilla
DESCRIPTION: This Python code performs a vector search in the 'Trafilatura' table of the Epsilla database. It takes a query string, generates its embedding using the same model, and then queries the database to find the most similar document based on the 'Embedding' field, limiting the result to one.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial-epsilla

LANGUAGE: python
CODE:
```
query = "A modern frontend library"
query_embedding = hf.embed_query(query)
status_code, response = client.query(
    table_name="Trafilatura",
    query_field="Embedding",
    query_vector=query_embedding,
    limit=1
)
print(response)
```

--------------------------------

TITLE: Find Feed URLs from Homepage (Python)
DESCRIPTION: Retrieves a list of feed URLs by providing a homepage URL. The function automatically discovers and filters relevant feeds.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
from trafilatura import feeds

mylist = feeds.find_feed_urls('https://www.theguardian.com/')
```

--------------------------------

TITLE: Extract Meta Information using XPath
DESCRIPTION: Iterates through a list of XPath expressions to extract meta information from an HTML tree. It selects the first valid content found that meets a specified length criteria.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/metadata

LANGUAGE: Python
CODE:
```
def extract_metainfo(tree: HtmlElement, expressions: List[XPath], len_limit: int = 200) -> Optional[str]:
    """Extract meta information"""
    for expression in expressions:
        results = expression(tree)
        for elem in results:
            content = trim(" ".join(elem.itertext()))
            if content and 2 < len(content) < len_limit:
                return content
        if len(results) > 1:
            LOGGER.debug("more than one invalid result: %s %s", expression, len(results))
    return None
```

--------------------------------

TITLE: Extract Text using html2txt
DESCRIPTION: Shows the usage of the `html2txt` function for basic text extraction from HTML content, often used as a last resort.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
>>> from trafilatura import html2txt
>>> html2txt(downloaded)
```

--------------------------------

TITLE: HTML to Markup Conversion - html2text
DESCRIPTION: The html2text Python package converts HTML pages into a markup language format, preserving the structure but not focusing on main text extraction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/evaluation

LANGUAGE: python
CODE:
```
import html2text

h = html2text.HTML2Text()
h.ignore_links = True
print(h.handle(html_content))
```

--------------------------------

TITLE: Extract Text with JSON and Metadata
DESCRIPTION: Shows how to use the 'extract' function to retrieve text content and associated metadata from a downloaded document, outputting the result in JSON format.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
>>> extract(downloaded, output_format="json", with_metadata=True)
```

--------------------------------

TITLE: Fetch and Extract Text from URL in R
DESCRIPTION: Demonstrates fetching a web page content and extracting text using Trafilatura functions imported into R via Reticulate. It first imports the Trafilatura module, then fetches the URL, and finally extracts the text content.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-r

LANGUAGE: R
CODE:
```
# getting started
> install.packages("reticulate")
> library(reticulate)

# loading the Trafilatura module
> trafilatura <- import("trafilatura")

# fetching a web page
> url <- "https://example.org/"
> downloaded <- trafilatura$fetch_url(url)

# extracting the text content
> text <- trafilatura$extract(downloaded)
> cat(text)

```

--------------------------------

TITLE: Convert XML to Plain Text with Formatting
DESCRIPTION: Converts an XML element to plain text, optionally preserving formatting as markdown. It handles various HTML tags, including images, newlines, and cells, to produce a readable text output. Dependencies include the `Element` type from `xml.etree.ElementTree` and helper functions like `unescape` and `sanitize`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
from typing import Optional
from xml.etree.ElementTree import Element as _Element

# Assuming process_element, unescape, sanitize, NEWLINE_ELEMS, MAX_TABLE_WIDTH, SPECIAL_FORMATTING are defined elsewhere

def xmltotxt(xmloutput: Optional[_Element], include_formatting: bool) -> str:
    """Convert to plain text format and optionally preserve formatting as markdown."""
    if xmloutput is None:
        return ""

    returnlist: List[str] = []

    process_element(xmloutput, returnlist, include_formatting)

    return unescape(sanitize("".join(returnlist)) or "")


def process_element(element, returnlist, include_formatting):
    # Placeholder for the actual process_element logic
    pass

```

--------------------------------

TITLE: View Htmldate Citations
DESCRIPTION: This link directs to the citation page of Htmldate's documentation, where users can find a comprehensive list of publications that have referenced the library.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/used-by

LANGUAGE: Markdown
CODE:
```
See `citation page of htmldate's documentation <https://htmldate.readthedocs.io/en/latest/used-by.html>`_.
```

--------------------------------

TITLE: Trafilatura Main Text Extraction - Python
DESCRIPTION: Trafilatura, the library documented here, focuses solely on main text extraction, without including metadata or comments, offering several options for this task.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/evaluation

LANGUAGE: python
CODE:
```
trafilatura <https://github.com/adbar/trafilatura>`_ is the library documented here, several options are tested regarding main text extraction only, without metadata or comments
```

--------------------------------

TITLE: Trafilatura Performance Benchmarks
DESCRIPTION: This snippet summarizes the performance metrics (Precision, Recall, Accuracy, F-Score) of Trafilatura and other Python libraries for web scraping across different dates. It highlights Trafilatura's improvements.

SOURCE: https://trafilatura.readthedocs.io/en/latest/evaluation

LANGUAGE: Python
CODE:
```
print("Trafilatura Performance Benchmarks")

# Example data structure (conceptual, not actual executable code)
results_2021_06_07 = {
    "trafilatura_0_8_2_fast": {"precision": 0.925, "recall": 0.868, "accuracy": 0.899, "f_score": 0.896},
    "trafilatura_0_8_2": {"precision": 0.934, "recall": 0.890, "accuracy": 0.914, "f_score": 0.912}
}

results_2020_11_06 = {
    "trafilatura_0_6_0": {"precision": 0.924, "recall": 0.849, "accuracy": 0.890, "f_score": 0.885},
    "trafilatura_0_6_0_fallbacks": {"precision": 0.933, "recall": 0.877, "accuracy": 0.907, "f_score": 0.904}
}

results_2020_07_16 = {
    "trafilatura_0_5_1": {"precision": 0.927, "recall": 0.854, "accuracy": 0.894, "f_score": 0.889},
    "trafilatura_0_5_1_fallbacks": {"precision": 0.933, "recall": 0.885, "accuracy": 0.911, "f_score": 0.908}
}

results_2020_03_19 = {
    "trafilatura_0_3_1_rule_based": {"precision": 0.901, "recall": 0.831, "accuracy": 0.871, "f_score": 0.865},
    "trafilatura_0_3_1_justext": {"precision": 0.897, "recall": 0.868, "accuracy": 0.884, "f_score": 0.882},
    "trafilatura_0_4": {"precision": 0.914, "recall": 0.869, "accuracy": 0.894, "f_score": 0.891},
    "trafilatura_0_4_fallback": {"precision": 0.925, "recall": 0.904, "accuracy": 0.916, "f_score": 0.914}
}

# To analyze or compare these results, you would typically use pandas or other data analysis tools.
# For example, to find the best F-Score for Trafilatura in 2021-06-07:
# print(f"Best F-Score in 2021-06-07: {results_2021_06_07['trafilatura_0_8_2']['f_score']}")

```

--------------------------------

TITLE: Grep: Exclude specific links
DESCRIPTION: This command uses grep with the `-v` option to filter a list of URLs, excluding lines that contain '/video/'. The output is redirected to `filtered-list.txt`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial0

LANGUAGE: bash
CODE:
```
grep -v "/video/" mylist.txt > filtered-list.txt
```

--------------------------------

TITLE: HTML to Text Conversion with Emphasis - inscriptis
DESCRIPTION: Inscriptis is a Python library that converts HTML to text, with a specific focus on handling nested tables and maintaining a particular emphasis on the text's structure.

SOURCE: https://trafilatura.readthedocs.io/en/latest/evaluation

LANGUAGE: python
CODE:
```
from inscriptis import get_text

text = get_text(html_content)
```

--------------------------------

TITLE: Keep Image Information
DESCRIPTION: Extracts text and retains information about images, including their alt text, source (src), and title attributes.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
# Example usage (assuming a URL is provided or piped):
# trafilatura --images -u "URL"
```

--------------------------------

TITLE: Web Crawling with Trafilatura
DESCRIPTION: Enables focused web crawling to discover and process specific content. The `focused_crawler` function allows for targeted navigation and data collection.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/corefunctions

LANGUAGE: Python
CODE:
```
from trafilatura.spider import focused_crawler

# Example usage:
# url = "..."
# # ... crawler configuration ...
# focused_crawler(url, ...)

```

--------------------------------

TITLE: Search and Gather Sitemap Links
DESCRIPTION: Searches for sitemaps associated with a given URL and gathers all extracted links. It supports filtering by target language and external hosts, with options to control request intervals and the maximum number of sitemaps to process.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/sitemaps

LANGUAGE: python
CODE:
```
def sitemap_search(
    url: str,
    target_lang: Optional[str] = None,
    external: bool = False,
    sleep_time: float = 2.0,
    max_sitemaps: int = MAX_SITEMAPS_SEEN,
) -> List[str]:
    """Look for sitemaps for the given URL and gather links.

    Args:
        url: Webpage or sitemap URL as string.
             Triggers URL-based filter if the webpage isn't a homepage.
        target_lang: Define a language to filter URLs based on heuristics
                     (two-letter string, ISO 639-1 format).
        external: Similar hosts only or external URLs
                  (boolean, defaults to False).
        sleep_time: Wait between requests on the same website.
        max_sitemaps: Maximum number of sitemaps to process.

    Returns:
        The extracted links as a list (sorted list of unique links).

    """
    domainname, baseurl = get_hostinfo(url)
    if domainname is None:
        LOGGER.warning("invalid URL: %s", url)
        return []

    if not is_live_page(baseurl):
        LOGGER.warning("base URL unreachable, dropping sitemap: %s", url)
        return []

    urlfilter = None

    if url.endswith((".gz", "sitemap", ".xml")):
        sitemapurls = [url]
    else:
        sitemapurls = []
        # set url filter to target subpages
        if len(url) > len(baseurl) + 2:
            urlfilter = url

    sitemap = SitemapObject(baseurl, domainname, sitemapurls, target_lang, external)

    # try sitemaps in robots.txt file, additional URLs just in case
    if not sitemap.sitemap_urls:
        sitemap.sitemap_urls = find_robots_sitemaps(baseurl) or [
            f"{baseurl}/{g}" for g in GUESSES
        ]

    # iterate through nested sitemaps and results
    while sitemap.sitemap_urls and len(sitemap.seen) < max_sitemaps:
        sitemap.current_url = sitemap.sitemap_urls.pop()
        sitemap.fetch()
        sitemap.process()
        # sanity check: keep track of visited sitemaps and exclude them
        sitemap.sitemap_urls = [
            s for s in sitemap.sitemap_urls if s not in sitemap.seen
        ]

        if len(sitemap.seen) < max_sitemaps:
            sleep(sleep_time)

    if urlfilter:
        sitemap.urls = filter_urls(sitemap.urls, urlfilter)

    LOGGER.debug("%s sitemap links found for %s", len(sitemap.urls), domainname)
    return sitemap.urls
```

--------------------------------

TITLE: Load HTML with Trafilatura
DESCRIPTION: Loads HTML content from a file path. This function is a utility for reading HTML files into memory for further processing.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/corefunctions

LANGUAGE: Python
CODE:
```
from trafilatura import load_html

# Example usage:
# filepath = "..."
# html = load_html(filepath)

```

--------------------------------

TITLE: BoilerPy3 Boilerplate Removal - Python
DESCRIPTION: BoilerPy3 is a Python implementation of the boilerpipe algorithm, designed for boilerplate removal and full-text extraction from web pages.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/evaluation

LANGUAGE: python
CODE:
```
boilerpy3 <https://github.com/jmriebold/BoilerPy3>`_ is a Python version of the boilerpipe algorithm for boilerplate removal and fulltext extraction
```

--------------------------------

TITLE: Validate Existing TEI XML File with Trafilatura
DESCRIPTION: Validates an existing TEI XML file using the `validate_tei` function from Trafilatura's XML module. This function requires the 'lxml' library for XML parsing and returns True if the file is valid, or an error message if validation fails.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial2

LANGUAGE: Python
CODE:
```
# load the necessary components
from lxml import etree
from trafilatura.xml import validate_tei

# open a file and parse it
mytree = etree.parse('document-name.xml')

# validate it
validate_tei(mytree)
# returns True or an error message
```

--------------------------------

TITLE: Control XML Output
DESCRIPTION: Manages the final XML output by stripping double tags, removing empty elements, building the XML/TEI tree, sanitizing, and validating if necessary.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
def control_xml_output(document: Document, options: Extractor) -> str:
    '''Make sure the XML output is conform and valid if required'''
    strip_double_tags(document.body)
    remove_empty_elements(document.body)

    func = build_xml_output if options.format == "xml" else build_tei_output
    output_tree = func(document)

    output_tree = sanitize_tree(output_tree)
    # necessary for cleaning
    output_tree = fromstring(tostring(output_tree, encoding='unicode'), CONTROL_PARSER)

    # validate
    if options.format == 'xmltei' and options.tei_validation:
        LOGGER.debug('TEI validation result: %s %s', validate_tei(output_tree), options.source)

    return tostring(output_tree, pretty_print=True, encoding='unicode').strip()
```

--------------------------------

TITLE: Process Sitemap Content
DESCRIPTION: Processes the content of a sitemap, determining if it's plausible and extracting links. It handles both plain text and XML sitemap formats, including language-specific link extraction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/sitemaps

LANGUAGE: python
CODE:
```
def process(self) -> None:
    """Download a sitemap and extract the links it contains."""
    plausible = is_plausible_sitemap(self.current_url, self.content)
    # safeguard
    if not plausible:
        return
    # try to extract links from TXT file
    if not SITEMAP_FORMAT.match(self.content):
        self.extract_links(DETECT_LINKS, 0, self.handle_link)
        return
    # process XML sitemap
    if self.target_lang is not None:
        self.extract_sitemap_langlinks()
        if self.sitemap_urls or self.urls:
            return
    self.extract_sitemap_links()
```

--------------------------------

TITLE: Keep Formatting Elements
DESCRIPTION: Extracts text and preserves formatting elements like bold (<b>, <strong>) and italic (<i>, <emph>) tags.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
# Example usage (assuming a URL is provided or piped):
# trafilatura --formatting -u "URL"
```

--------------------------------

TITLE: Discover Sitemap Links with Trafilatura in R
DESCRIPTION: This snippet shows how to use the `sitemap_search` function from Trafilatura's sitemaps module to find URLs within a given sitemap. It requires importing the function using `py_run_string`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-r

LANGUAGE: R
CODE:
```
# using the code for link discovery in sitemaps
> sitemapsfunc <- py_run_string("from trafilatura.sitemaps import sitemap_search")
> sitemapsfunc$sitemap_search("https://www.sitemaps.org/")
[1] "https://www.sitemaps.org"
[2] "https://www.sitemaps.org/protocol.html"
[3] "https://www.sitemaps.org/faq.html"
[4] "https://www.sitemaps.org/terms.html"
# and so on...
```

--------------------------------

TITLE: Python Focused Crawler Function
DESCRIPTION: Implements a basic crawler to target pages of interest within a website. It takes a homepage URL and several optional parameters to control the crawl, including maximum URLs to visit, language targeting, politeness rules, and XPath for pruning unwanted elements.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/spider

LANGUAGE: Python
CODE:
```
def focused_crawler(
    homepage: str,
    max_seen_urls: int = MAX_SEEN_URLS,
    max_known_urls: int = MAX_KNOWN_URLS,
    todo: Optional[List[str]] = None,
    known_links: Optional[List[str]] = None,
    lang: Optional[str] = None,
    config: ConfigParser = DEFAULT_CONFIG,
    rules: Optional[RobotFileParser] = None,
    prune_xpath: Optional[str] = None,
) -> Tuple[List[str], List[str]]:
    """Basic crawler targeting pages of interest within a website.

    Args:
        homepage: URL of the page to first page to fetch, preferably the homepage of a website.
        max_seen_urls: maximum number of pages to visit, stop iterations at this number or at the exhaustion of pages on the website, whichever comes first.
        max_known_urls: stop if the total number of pages "known" exceeds this number.
        todo: provide a previously generated list of pages to visit / crawl frontier.
        known_links: provide a list of previously known pages.
        lang: try to target links according to language heuristics.
        config: use a different configuration (configparser format).
        rules: provide politeness rules (urllib.robotparser.RobotFileParser() format).
        prune_xpath: remove unwanted elements from the HTML pages using XPath.

    Returns:
        List of pages to visit, deque format, possibly empty if there are no further pages to visit.
        Set of known links.

    """
    params = init_crawl(homepage, lang, rules, todo, known_links, prune_xpath)

    sleep_time = URL_STORE.get_crawl_delay(
        params.base, default=config.getfloat("DEFAULT", "SLEEP_TIME")
    )

    # visit pages until a limit is reached
    while (
        params.is_on and params.i < max_seen_urls and params.known_num < max_known_urls
    ):
        params = crawl_page(params)
        sleep(sleep_time)

    # refocus todo-list on URLs without navigation?
    todo = list(dict.fromkeys(URL_STORE.find_unvisited_urls(params.base)))
    # [u for u in todo if not is_navigation_page(u)]
    known_links = list(dict.fromkeys(URL_STORE.find_known_urls(params.base)))
    return todo, known_links

```

--------------------------------

TITLE: Extracting Links from Sitemaps (Python)
DESCRIPTION: This snippet demonstrates how to extract both sitemap URLs and direct web page links from a sitemap file using regular expressions. It handles different XML structures and cleans the extracted URLs.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/sitemaps

LANGUAGE: Python
CODE:
```
import re

LINK_REGEX = re.compile(r"<loc>(?:<!\[CDATA\[)?(http.+?)(?:]\]>)?</loc>")

def extract_sitemap_links(content: str) -> List[str]:
    """Extract sitemap links and web page links from a sitemap file."""
    links = []
    for match in LINK_REGEX.finditer(content):
        links.append(match.group(1))
    return links
```

--------------------------------

TITLE: Find Feed URLs from Direct Feed URL (Python)
DESCRIPTION: Fetches feed URLs directly from a provided RSS or Atom feed URL. It checks if the returned list is not empty.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
from trafilatura import feeds

mylist = feeds.find_feed_urls('https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
print(mylist is not [])
```

--------------------------------

TITLE: Validate Existing TEI File (Python)
DESCRIPTION: This Python code snippet illustrates how to validate an existing TEI XML file using Trafilatura's `validate_tei` function. It involves parsing the XML file with `lxml.etree` and then passing the parsed tree to `validate_tei`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial2

LANGUAGE: Python
CODE:
```
# load the necessary components
from lxml import etree
from trafilatura.xml import validate_tei

# open a file and parse it
mytree = etree.parse('document-name.xml')

# validate it
validate_tei(mytree)
# returns True or an error message

```

--------------------------------

TITLE: inscriptis HTML to Text Conversion - Python
DESCRIPTION: The inscriptis Python package converts HTML to text with a specific emphasis on nested tables, while preserving the structure.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/evaluation

LANGUAGE: python
CODE:
```
inscriptis <https://github.com/weblyzard/inscriptis>`_ converts HTML to text with a particular emphasis on nested tables
```

--------------------------------

TITLE: Extract with Target Language
DESCRIPTION: Shows how to specify a target language for text extraction using the `target_language` parameter with a 2-letter ISO 639-1 code.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
>>> result = extract(downloaded, url, target_language="de")
```

--------------------------------

TITLE: news-please News Crawler - Python
DESCRIPTION: The news-please Python library functions as a news crawler, extracting structured information from news articles.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/evaluation

LANGUAGE: python
CODE:
```
news-please <https://github.com/fhamborg/news-please>`_ is a news crawler that extracts structured information
```

--------------------------------

TITLE: Python: Handle Code Blocks
DESCRIPTION: Converts an element into a properly tagged code block by setting its tag to 'code' and marking all its descendants as 'done'. This function is used to isolate and format code snippets.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def handle_code_blocks(element: _Element) -> _Element:
    """Turn element into a properly tagged code block."""
    processed_element = deepcopy(element)
    for child in element.iter('*'):
        child.tag = "done"
    processed_element.tag = "code"
    return processed_element
```

--------------------------------

TITLE: Probe Google News for Feeds
DESCRIPTION: Gathers feed links using Google News as an alternative source. It constructs a Google News search query based on the domain and language, fetches the results, and extracts relevant links. The links are then filtered based on an optional URL filter.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/feeds

LANGUAGE: Python
CODE:
```
def probe_gnews(params: FeedParameters, urlfilter: Optional[str]) -> List[str]:
    """Alternative way to gather feed links: Google News."""
    if params.lang:
        downloaded = fetch_url(
            f"https://news.google.com/rss/search?q=site:{params.domain}&hl={params.lang}&scoring=n&num=100"
        )
        if downloaded:
            feed_links = extract_links(downloaded, params)
            feed_links = filter_urls(feed_links, urlfilter)
            LOGGER.debug(
                "%s Google news links found for %s", len(feed_links), params.domain
            )
            return feed_links
    return []
```

--------------------------------

TITLE: Extract Metadata License
DESCRIPTION: Extracts the license information from the HTML tree. This function is responsible for identifying and retrieving license details.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/metadata

LANGUAGE: Python
CODE:
```
# license
    metadata.license = extract_license(tree)
```

--------------------------------

TITLE: Grep: Filter relevant links
DESCRIPTION: This command uses grep to filter a list of URLs, keeping only lines that contain '/article/'. The output is redirected to `filtered-list.txt`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/tutorial0

LANGUAGE: bash
CODE:
```
grep "/article/" mylist.txt > filtered-list.txt
```

--------------------------------

TITLE: Article Information Extraction - goose3
DESCRIPTION: The goose3 Python library can extract information from embedded content within web pages but does not preserve the original markup structure.

SOURCE: https://trafilatura.readthedocs.io/en/latest/evaluation

LANGUAGE: python
CODE:
```
from goose3 import Goose

g = Goose()
article = g.extract(url=url)

title = article.title
text = article.text
```

--------------------------------

TITLE: Load Data with Pandas
DESCRIPTION: Demonstrates how to load extracted text data into the Pandas library for data analysis. Supports CSV and JSON formats.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/corpus-data

LANGUAGE: Python
CODE:
```
import pandas as pd

# Load data from CSV
df_csv = pd.read_csv('your_data.csv')

# Load data from JSON
df_json = pd.read_json('your_data.json')
```

--------------------------------

TITLE: Extract Metadata and Apply Filters
DESCRIPTION: This code block handles the extraction of metadata from the HTML tree. It includes logic to filter documents based on blacklisted URLs and checks for the presence of essential metadata (date, title, URL) when 'only_with_metadata' is enabled.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/core

LANGUAGE: Python
CODE:
```
# extract metadata if necessary
        if options.with_metadata:

            document = extract_metadata(
                tree,
                options.url,
                options.date_params,
                options.fast,
                options.author_blacklist,
            )

            # cut short if extracted URL in blacklist
            if document.url in options.url_blacklist:
                LOGGER.warning("blacklisted URL: %s", document.url)
                raise ValueError

            # cut short if core elements are missing
            if options.only_with_metadata and not (
                document.date and document.title and document.url
            ):
                LOGGER.error("no metadata: %s", options.source)
                raise ValueError

        else:
            document = Document()
```

--------------------------------

TITLE: Generate Word Trigrams
DESCRIPTION: This command generates a list of the 20 most frequent word trigrams from a text file. It processes the input by replacing newlines with spaces, extracts groups of three adjacent words, sorts them, counts unique occurrences, and then sorts by count in descending order.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial1

LANGUAGE: bash
CODE:
```
# word trigrams
$ < tokens-filtered.txt tr "\n" " " | awk '{for (i=1; i<NF; i++) print $i, $(i+1), $(i+2)}' | sort | uniq -c | sort -nrk1 | head -20
```

--------------------------------

TITLE: Filter Links Matching a Pattern with grep
DESCRIPTION: This command uses `grep` to filter a list of URLs, keeping only those lines that contain the pattern "/article/". The output is redirected to a new file named `filtered-list.txt`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial0

LANGUAGE: bash
CODE:
```
grep "/article/" mylist.txt > filtered-list.txt
```

--------------------------------

TITLE: Determine Page Liveness
DESCRIPTION: Checks if a web page is live by first attempting to use pycurl if available, and falling back to a urllib3-based method if pycurl is not present or fails. This function provides a robust way to check page availability.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/downloads

LANGUAGE: Python
CODE:
```
def is_live_page(url: str) -> bool:
    """Send a HTTP HEAD request without taking anything else into account."""
    result = _pycurl_is_live_page(url) if HAS_PYCURL else False
    # use urllib3 as backup
    return result or _urllib3_is_live_page(url)
```

--------------------------------

TITLE: Extract text using baseline - Python
DESCRIPTION: The baseline function offers a balance between precision and recall for text extraction, along with improved performance. It returns an LXML element, the extracted text, and its length, using heuristics for more accurate results than html2txt.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
from trafilatura import baseline
postbody, text, len_text = baseline(downloaded)
```

--------------------------------

TITLE: Handle Meta-Refresh Redirects in HTML
DESCRIPTION: Detects and handles meta-refresh tags within HTML content to follow page redirects. If a redirect is found and successfully processed, it returns the new HTML content and URL; otherwise, it returns the original content or None.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/spider

LANGUAGE: Python
CODE:
```
def refresh_detection(
    htmlstring: str,
    homepage: str,
) -> Tuple[Optional[str], Optional[str]]:
    """Check if there could be a redirection by meta-refresh tag."""
    if '"refresh"' not in htmlstring and '"REFRESH"' not in htmlstring:
        return htmlstring, homepage

    html_tree = load_html(htmlstring)
    if html_tree is None:
        return htmlstring, homepage

    # test meta-refresh redirection
    # https://stackoverflow.com/questions/2318446/how-to-follow-meta-refreshes-in-python
    results = html_tree.xpath(
        './/meta[@http-equiv="refresh" or @http-equiv="REFRESH"]/@content'
    )

    result = results[0] if results else ""

    if not result or ";" not in result:
        logging.info("no redirect found: %s", homepage)
        return htmlstring, homepage

    url2 = result.split(";")[1].strip().lower().replace("url=", "")
    if not url2.startswith("http"):
        # Relative URL, adapt
        base_url = get_base_url(url2)
        url2 = fix_relative_urls(base_url, url2)
    # second fetch
    newhtmlstring = fetch_url(url2)
    if newhtmlstring is None:
        logging.warning("failed redirect: %s", url2)
        return None, None
    # else:
    logging.info("successful redirect: %s", url2)
    return newhtmlstring, url2
```

--------------------------------

TITLE: Extract Text Favoring Precision
DESCRIPTION: Demonstrates using the 'extract' function with the 'favor_precision' parameter set to True to prioritize accuracy in the text extraction process.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
>>> result = extract(downloaded, url, favor_precision=True)
```

--------------------------------

TITLE: Find Sitemaps in Robots.txt
DESCRIPTION: Guesses the location of the robots.txt file for a given base URL and attempts to extract sitemap URLs listed within it.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/sitemaps

LANGUAGE: python
CODE:
```
def find_robots_sitemaps(baseurl: str) -> List[str]:
    """Guess the location of the robots.txt file and try to extract
    sitemap URLs from it"""
    robotstxt = fetch_url(baseurl + "/robots.txt")
    return extract_robots_sitemaps(robotstxt, baseurl)
```

--------------------------------

TITLE: Keep Link Targets
DESCRIPTION: Extracts text and includes link targets (href attributes), converting relative URLs to absolute where possible.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
# Example usage (assuming a URL is provided or piped):
# trafilatura --links -u "URL"
```

--------------------------------

TITLE: Extract Text with XML Output in R
DESCRIPTION: Shows how to extract text content from a web page using Trafilatura in R, specifying the output format as XML and including the URL.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-r

LANGUAGE: R
CODE:
```
> trafilatura$extract(downloaded, output_format="xml", url=url)
[1] "<doc sitename=\"example.org\" title=\"Example Domain\" source=\"https://example.org/\" hostname=\"example.org\" categories=\"\" tags=\"\" fingerprint=\"lxZaiIwoxp80+AXA2PtCBnJJDok=\">
  <main>
    <div>
      <head>Example Domain</head>
      <p>This domain is for use in illustrative examples in documents. You may use this
domain in literature without prior coordination or asking for permission.</p>
      <p>More information...</p>
    </div>
  </main>
  <comments/>
</doc>"
```

--------------------------------

TITLE: Trafilatura: Fetch Response
DESCRIPTION: Fetches the response from a given URL. This function handles the HTTP request and retrieves the raw content of a web page.

SOURCE: https://trafilatura.readthedocs.io/en/latest/genindex

LANGUAGE: python
CODE:
```
from trafilatura import fetch_response

# Example usage:
# url = "https://example.com"
# response = fetch_response(url)
```

--------------------------------

TITLE: Skip Tables and Include Links
DESCRIPTION: Demonstrates using the 'extract' function to skip HTML table elements while including link targets in the output by setting 'include_tables' to False and 'include_links' to True.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
>>> result = extract(downloaded, include_tables=False, include_links=True)
```

--------------------------------

TITLE: jusText Text Extraction - Python
DESCRIPTION: jusText is a Python library developed to create linguistic resources by preserving mainly text containing full sentences along with some markup.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/evaluation

LANGUAGE: python
CODE:
```
jusText <https://github.com/miso-belica/jusText>`_ is designed to preserve mainly text containing full sentences along with some markup, it has been explicitly developed to create linguistic resources
```

--------------------------------

TITLE: Try Homepage for Feeds
DESCRIPTION: Attempts to find feed URLs by probing the homepage of a given base URL. This function is called when initial attempts to find feeds from a specific URL fail, suggesting a fallback to the main site.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/feeds

LANGUAGE: Python
CODE:
```
def try_homepage(baseurl: str, target_lang: Optional[str]) -> List[str]:
    """Shift into reverse and try the homepage instead of the particular feed
    page that was given as input."""
    LOGGER.debug("Probing homepage for feeds instead: %s", baseurl)
    return find_feed_urls(baseurl, target_lang)
```

--------------------------------

TITLE: BibTeX Entry for htmldate
DESCRIPTION: This snippet provides a BibTeX formatted entry for the 'htmldate' Python package, as published in the Journal of Open Source Software. It includes details such as title, author, journal, volume, number, pages, URL, publisher, and year.

SOURCE: https://trafilatura.readthedocs.io/en/latest/used-by

LANGUAGE: BibTeX
CODE:
```
@article{barbaresi-2020-htmldate,
  title = {{htmldate: A Python package to extract publication dates from web pages}},
  author = "Barbaresi, Adrien",
  journal = "Journal of Open Source Software",
  volume = 5,
  number = 51,
  pages = 2439,
  url = {https://doi.org/10.21105/joss.02439},
  publisher = {The Open Journal},
  year = 2020,
}

```

--------------------------------

TITLE: Extract Metadata with Custom Date Parameters
DESCRIPTION: Demonstrates how to extract metadata using the `extract` function, passing custom parameters for date extraction. This includes enabling extensive search and setting a maximum date.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
from trafilatura import extract

# import the extract() function, use a previously downloaded document
# pass the new parameters as dict
>>> extract(downloaded, output_format="xml", date_extraction_params={
        "extensive_search": True, "max_date": "2018-07-01"
    })
```

--------------------------------

TITLE: Extract Text Content with Trafilatura
DESCRIPTION: Provides functions for extracting main text content from HTML documents. Includes general extraction, bare extraction, baseline extraction, and HTML to text conversion.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/corefunctions

LANGUAGE: Python
CODE:
```
from trafilatura import extract

# Example usage:
# html = "..."
# text = extract(html)

```

LANGUAGE: Python
CODE:
```
from trafilatura import bare_extraction

# Example usage:
# html = "..."
# text = bare_extraction(html)

```

LANGUAGE: Python
CODE:
```
from trafilatura import baseline

# Example usage:
# html = "..."
# text = baseline(html)

```

LANGUAGE: Python
CODE:
```
from trafilatura import html2txt

# Example usage:
# html = "..."
# text = html2txt(html)

```

--------------------------------

TITLE: Extract Metadata from Webpages in Python
DESCRIPTION: This Python code defines a module for scraping metadata from webpages. It includes functions for extracting domain names, normalizing URLs, finding dates, and extracting JSON metadata. The module uses libraries such as courlan, htmldate, and lxml.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/metadata

LANGUAGE: Python
CODE:
```
"""
Module bundling all functions needed to scrape metadata from webpages.
"""

import json
import logging
import re

from copy import deepcopy
from html import unescape
from typing import Any, Dict, List, Optional, Set, Tuple, Union

from courlan import (
    extract_domain,
    get_base_url,
    is_valid_url,
    normalize_url,
    validate_url,
)
from htmldate import find_date
from lxml.etree import XPath
from lxml.html import HtmlElement, tostring

from .htmlprocessing import prune_unwanted_nodes
from .json_metadata import (
    extract_json,
    extract_json_parse_error,
    normalize_authors,
    normalize_json,
)
from .settings import Document, set_date_params
from .utils import HTML_STRIP_TAGS, line_processing, load_html, trim
from .xpaths import (
    AUTHOR_DISCARD_XPATHS,
    AUTHOR_XPATHS,
    CATEGORIES_XPATHS,
    TAGS_XPATHS,
    TITLE_XPATHS,
)

__all__ = ["Document"]

LOGGER = logging.getLogger(__name__)
logging.getLogger("htmldate").setLevel(logging.WARNING)

META_URL = re.compile(r"https?://(?:www\.|w[0-9]+\.)?([^/]+)")

JSON_MINIFY = re.compile(r'("(?:\\"|[^"])*")|\s')

HTMLTITLE_REGEX = re.compile(
    r"^(.+)?\s+[–•·—|⁄*⋆~‹«<›»>:-]\s+(.+)$"
)  # part without dots?

CLEAN_META_TAGS = re.compile(r'["\']')

LICENSE_REGEX = re.compile(
    r"/(by-nc-nd|by-nc-sa|by-nc|by-nd|by-sa|by|zero)/([1-9]\.[0-9])"
)
TEXT_LICENSE_REGEX = re.compile(
    r"(cc|creative commons) (by-nc-nd|by-nc-sa|by-nc|by-nd|by-sa|by|zero) ?([1-9]\.[0-9])?",
    re.I,
)

METANAME_AUTHOR = {
    "article:author",
    "atc-metaauthor",
    "author",
    "authors",
    "byl",
    "citation_author",
    "creator",
    "dc.creator",
    "dc.creator.aut",
    "dc:creator",
    "dcterms.creator",
    "dcterms.creator.aut",
    "dcsext.author",
    "parsely-author",
    "rbauthors",
    "sailthru.author",
    "shareaholic:article_author_name",
}  # questionable: twitter:creator
METANAME_DESCRIPTION = {
    "dc.description",
    "dc:description",
    "dcterms.abstract",
    "dcterms.description",
    "description",
    "sailthru.description",
    "twitter:description",
}
METANAME_PUBLISHER = {
    "article:publisher",
    "citation_journal_title",
    "copyright",
    "dc.publisher",
    "dc:publisher",
    "dcterms.publisher",
    "publisher",
    "sailthru.publisher",
    "rbpubname",
    "twitter:site",
}  # questionable: citation_publisher
METANAME_TAG = {
    "citation_keywords",
    "dcterms.subject",
    "keywords",
    "parsely-tags",
    "shareaholic:keywords",
    "tags",
}
METANAME_TITLE = {
    "citation_title",
    "dc.title",
    "dcterms.title",
    "fb_title",
    "headline",
    "parsely-title",
    "sailthru.title",
    "shareaholic:title",
    "rbtitle",
    "title",
    "twitter:title",
}
METANAME_URL = {"rbmainurl", "twitter:url"}
METANAME_IMAGE = {
    "image",
    "og:image",
    "og:image:url",
    "og:image:secure_url",
    "twitter:image",
    "twitter:image:src",
}
PROPERTY_AUTHOR = {"author", "article:author"}
TWITTER_ATTRS = {"twitter:site", "application-name"}

```

--------------------------------

TITLE: Exclude Links Matching a Pattern with grep
DESCRIPTION: This command uses `grep -v` to filter a list of URLs, excluding any lines that contain the pattern "/video/". The remaining lines are redirected to a new file named `filtered-list.txt`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/tutorial0

LANGUAGE: bash
CODE:
```
grep -v "/video/" mylist.txt > filtered-list.txt
```

--------------------------------

TITLE: Python: Convert relative links to absolute links
DESCRIPTION: Shows how to use the `extract` function with the `include_links=True` parameter and a base URL to convert relative hyperlinks to absolute URLs, ensuring link integrity.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
>>> extract(downloaded, output_format='xml', include_links=True, url=url)
```

--------------------------------

TITLE: XML to Dictionary Conversion with xmltodict
DESCRIPTION: Utilizes the 'xmltodict' Python package to convert XML files into a JSON-like dictionary format, simplifying data manipulation.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/corpus-data

LANGUAGE: Python
CODE:
```
import xmltodict
import json

with open('your_file.xml', 'r') as file:
    xml_content = file.read()

# Convert XML to a Python dictionary
data_dict = xmltodict.parse(xml_content)

# Optionally, convert to JSON string
json_data = json.dumps(data_dict, indent=4)
```

--------------------------------

TITLE: Convert Links to Absolute URLs in XML
DESCRIPTION: Shows how to use the 'extract' function to convert relative links to absolute URLs when outputting in XML format, requiring the original URL as an argument.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
>>> extract(downloaded, output_format='xml', include_links=True, url=url)
```

--------------------------------

TITLE: Extract Sitemaps from Robots.txt
DESCRIPTION: Reads the content of a robots.txt file and extracts all URLs specified in 'Sitemap:' directives. It handles potential comments and ensures URLs are properly formatted relative to the base URL.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/sitemaps

LANGUAGE: python
CODE:
```
def extract_robots_sitemaps(robotstxt: Optional[str], baseurl: str) -> List[str]:
    """Read a robots.txt file and find sitemap links."""
    # sanity check on length (cause: redirections)
    if robotstxt is None or len(robotstxt) > 10000:
        return []

    candidates = []
    # source: https://github.com/python/cpython/blob/3.12/Lib/urllib/robotparser.py
    for line in robotstxt.splitlines():
        # remove optional comment and strip line
        i = line.find("#")
        if i >= 0:
            line = line[:i]
        line = line.strip()
        if not line:
            continue
        line_parts = line.split(":", 1)
        if len(line_parts) == 2:
            line_parts[0] = line_parts[0].strip().lower()
            if line_parts[0] == "sitemap":
                # urllib.parse.unquote(line[1].strip())
                candidates.append(line_parts[1].strip())

    candidates = list(dict.fromkeys(candidates))
    sitemapurls = [fix_relative_urls(baseurl, u) for u in candidates if u]

    LOGGER.debug("%s sitemaps found in robots.txt", len(sitemapurls))
    return sitemapurls
```

--------------------------------

TITLE: Blacklist URLs via CLI
DESCRIPTION: Prevent Trafilatura from processing URLs listed in a file using the `--blacklist` argument on the command line. The file should contain one URL per line.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/url-management

LANGUAGE: bash
CODE:
```
trafilatura --blacklist blacklist.txt <url>
```

--------------------------------

TITLE: Calculate Similarity with Simhash
DESCRIPTION: Demonstrates how to create Simhash objects for two texts and calculate their similarity score, which ranges from 0 to 1.

SOURCE: https://trafilatura.readthedocs.io/en/latest/deduplication

LANGUAGE: Python
CODE:
```
from trafilatura.deduplication import Simhash

first = Simhash("This is a text.")
second = Simhash("This is a test.")
second.similarity(first)
```

--------------------------------

TITLE: Main Text Extraction - trafilatura
DESCRIPTION: Trafilatura, the library documented here, focuses on main text extraction from web pages. It offers various options for this task without extracting metadata or comments.

SOURCE: https://trafilatura.readthedocs.io/en/latest/evaluation

LANGUAGE: python
CODE:
```
import trafilatura

# Download the content from a URL
# downloaded_content = trafilatura.fetch_url(url)

# Or use a string containing HTML
# html_content = "..."

# Extract the main text
main_text = trafilatura.extract(html_content)

print(main_text)
```

--------------------------------

TITLE: html-text Conversion - Python
DESCRIPTION: The html_text Python package converts HTML code to plain text. It keeps the structure intact but does not focus on main text extraction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/evaluation

LANGUAGE: python
CODE:
```
html_text <https://github.com/TeamHG-Memex/html-text>`_ converts HTML code to plain text
```

--------------------------------

TITLE: Trafilatura Citation (BibTeX)
DESCRIPTION: BibTeX entry for citing the Trafilatura software in academic publications. It includes title, author, booktitle, publisher, URL, and year.

SOURCE: https://trafilatura.readthedocs.io/en/latest/index

LANGUAGE: BibTeX
CODE:
```
@inproceedings{barbaresi-2021-trafilatura,
  title = {{Trafilatura: A Web Scraping Library and Command-Line Tool for Text Discovery and Extraction}},
  author = "Barbaresi, Adrien",
  booktitle = "Proceedings of the Joint Conference of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing: System Demonstrations",
  pages = "122--131",
  publisher = "Association for Computational Linguistics",
  url = "https://aclanthology.org/2021.acl-demo.15",
  year = 2021,
}

```

--------------------------------

TITLE: HTML to Text Conversion with trafilatura
DESCRIPTION: The `html2txt` function performs a basic conversion of HTML content to plain text. It offers an option to clean the content by removing potentially undesirable elements.

SOURCE: https://trafilatura.readthedocs.io/en/latest/corefunctions

LANGUAGE: python
CODE:
```
trafilatura.html2txt(_content : Any_, _clean : bool = True_) → str
```

--------------------------------

TITLE: Trafilatura Extraction Function Signature
DESCRIPTION: This defines the main `extract` function for the trafilatura package, which serves as a wrapper for text extraction and conversion. It accepts various parameters to control the extraction process, including the HTML content, URL, output format, and specific options for handling comments, metadata, and precision/recall trade-offs. The function is designed to be flexible and accommodate different extraction needs.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/core

LANGUAGE: python
CODE:
```
def extract(
    filecontent: Any,
    url: Optional[str] = None,
    record_id: Optional[str] = None,
    fast: bool = False,
    no_fallback: bool = False,
    favor_precision: bool = False,
    favor_recall: bool = False,
    include_comments: bool = True,
    output_format: str = "txt",
    tei_validation: bool = False,
    target_language: Optional[str] = None,
    include_tables: bool = True,
    include_images: bool = False,
    include_formatting: bool = False,
    include_links: bool = False,
    deduplicate: bool = False,
    date_extraction_params: Optional[Dict[str, Any]] = None,
    with_metadata: bool = False,
    only_with_metadata: bool = False,
    max_tree_size: Optional[int] = None,
    url_blacklist: Optional[Set[str]] = None,
    author_blacklist: Optional[Set[str]] = None,
    settingsfile: Optional[str] = None,
    prune_xpath: Optional[Any] = None,
    config: Any = DEFAULT_CONFIG,
    options: Optional[Extractor] = None,
) -> Optional[str]:
    """Main function exposed by the package:
       Wrapper for text extraction and conversion to chosen output format.

    Args:
        filecontent: HTML code as string.
        url: URL of the webpage.
        record_id: Add an ID to the metadata.
        fast: Use faster heuristics and skip backup extraction.
        no_fallback: Will be deprecated, use "fast" instead.
        favor_precision: prefer less text but correct extraction.
        favor_recall: when unsure, prefer more text.
        include_comments: Extract comments along with the main text.
        output_format: Define an output format:
            "csv", "html", "json", "markdown", "txt", "xml", and "xmltei".
        tei_validation: Validate the XML-TEI output with respect to the TEI standard.

```

--------------------------------

TITLE: Handle Table Element in Trafilatura
DESCRIPTION: Processes a single table element by creating a new 'table' element and stripping structural tags like 'thead', 'tbody', and 'tfoot'. It also calculates the maximum number of columns per row, considering colspan.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def handle_table(table_elem: _Element, potential_tags: Set[str], options: Extractor) -> Optional[_Element]:
    """Process single table element."""
    newtable = Element("table")

    # strip these structural elements
    strip_tags(table_elem, "thead", "tbody", "tfoot")

    # calculate maximum number of columns per row, includin colspan
    max_cols = 0
    for tr in table_elem.iter('tr'):
```

--------------------------------

TITLE: Extract Main Content from HTML
DESCRIPTION: Extracts the main content of an HTML page using XPath expressions. It handles element stripping, unwanted subparts, and text recovery for short or empty content. Dependencies include `lxml` for HTML parsing and a custom `Extractor` class.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def _extract(subtree: HtmlElement, options: Extractor) -> Tuple[_Element, str, Set[str]]:
    if 'ref' not in potential_tags:
        strip_tags(subtree, 'ref')
    if 'span' not in potential_tags:
        strip_tags(subtree, 'span')
    LOGGER.debug(sorted(potential_tags))
    # proper extraction
    subelems = subtree.xpath('.//*')
    # e.g. only lb-elems in a div
    if {e.tag for e in subelems} == {'lb'}:
        subelems = [subtree]
    # extract content
    result_body.extend([el for el in (handle_textelem(e, potential_tags, options) for e in subelems) if el is not None])
    # remove trailing titles
    while len(result_body) > 0 and (result_body[-1].tag in NOT_AT_THE_END):
        delete_element(result_body[-1], keep_tail=False)
    # exit the loop if the result has children
    if len(result_body) > 1:
        LOGGER.debug(trim(str(expr)))
        break
    temp_text = ' '.join(result_body.itertext()).strip()
    return result_body, temp_text, potential_tags

def extract_content(cleaned_tree: HtmlElement, options: Extractor) -> Tuple[_Element, str, int]:
    '''Find the main content of a page using a set of XPath expressions,
       then extract relevant elements, strip them of unwanted subparts and
       convert them'''
    # backup
    backup_tree = deepcopy(cleaned_tree)

    result_body, temp_text, potential_tags = _extract(cleaned_tree, options)
    #if len(result_body) == 0:
    #    result_body, temp_text, potential_tags = _extract(tree_backup, options)

    # try parsing wild <p> elements if nothing found or text too short
    # todo: test precision and recall settings here
    if len(result_body) == 0 or len(temp_text) < options.min_extracted_size:  # type: ignore[attr-defined]
        result_body = recover_wild_text(backup_tree, result_body, options, potential_tags)
        temp_text = ' '.join(result_body.itertext()).strip()
    # filter output
    strip_elements(result_body, 'done')
    strip_tags(result_body, 'div')
    # return
    return result_body, temp_text, len(temp_text)
```

--------------------------------

TITLE: html2text Conversion - Python
DESCRIPTION: The html2text Python package converts HTML pages to Markup language, maintaining the structure but not focusing on main text extraction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/evaluation

LANGUAGE: python
CODE:
```
html2text <https://github.com/Alir3z4/html2text>`_ converts HTML pages to Markup language
```

--------------------------------

TITLE: Search Sitemaps with Target Language Filter (Python)
DESCRIPTION: Searches for sitemaps on a given website and filters the results based on the specified target language, similar to feed filtering.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
from trafilatura import sitemaps

# the target_lang argument works as explained above
mylinks = sitemaps.sitemap_search('https://www.un.org/', target_lang='en')
```

--------------------------------

TITLE: Validate Sitemap Format
DESCRIPTION: Checks if a given URL and its content correspond to an expected sitemap format (TXT or XML). It performs checks on the URL structure and the content's initial bytes to identify potential mismatches.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/sitemaps

LANGUAGE: python
CODE:
```
def is_plausible_sitemap(url: str, contents: Optional[str]) -> bool:
    """Check if the sitemap corresponds to an expected format,
    i.e. TXT or XML."""
    if contents is None:
        return False

    # strip query and fragments
    url = SCRUB_REGEX.sub("", url)

    # check content
    if (
        POTENTIAL_SITEMAP.search(url)
        and (not isinstance(contents, str) or not SITEMAP_FORMAT.match(contents))
        or "<html" in contents[:150].lower()
    ):
        LOGGER.warning("not a valid XML sitemap: %s", url)
        return False

    return True
```

--------------------------------

TITLE: Convert XML to Dictionary with xmltodict
DESCRIPTION: Shows how to use the `xmltodict` Python package to read XML files and convert them into a dictionary format, similar to JSON. This is useful for handling XML data in Python.

SOURCE: https://trafilatura.readthedocs.io/en/latest/corpus-data

LANGUAGE: python
CODE:
```
import xmltodict

with open('your_file.xml', 'r') as f:
    xml_content = f.read()

data_dict = xmltodict.parse(xml_content)

# Now you can work with data_dict as if it were a JSON object
```

--------------------------------

TITLE: Custom Justext Processing
DESCRIPTION: Provides a customized version of the Justext processing pipeline. It involves making paragraphs from the HTML tree, classifying them using specific parameters, and then revising the classification. Dependencies include 'ParagraphMaker', 'classify_paragraphs', and 'revise_paragraph_classification'.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/external

LANGUAGE: python
CODE:
```
def custom_justext(tree: HtmlElement, stoplist: Tuple[str]) -> Any:
    'Customized version of JusText processing'
    paragraphs = ParagraphMaker.make_paragraphs(tree)
    classify_paragraphs(paragraphs, stoplist, 50, 150, 0.1, 0.2, 0.25, True)
    revise_paragraph_classification(paragraphs, 150)
    return paragraphs
```

--------------------------------

TITLE: Parse HTML Bytes with LXML
DESCRIPTION: Attempts to parse HTML content provided as bytes using the LXML parser. It handles potential exceptions during the parsing process and logs any errors encountered.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
from typing import Optional
from lxml.etree import fromstring, HTMLParser, HtmlElement

# Assuming HTML_PARSER is a configured HTMLParser instance
# Assuming LOGGER is a configured logger instance

def fromstring_bytes(htmlobject: str) -> Optional[HtmlElement]:
    """Try to pass bytes to LXML parser."""
    tree = None
    try:
        tree = fromstring(htmlobject.encode("utf8", "surrogatepass"), parser=HTML_PARSER)
    except Exception as err:
        LOGGER.error("lxml parser bytestring %s", err)
    return tree
```

--------------------------------

TITLE: Search Sitemaps with Trafilatura
DESCRIPTION: Illustrates how to use the `sitemaps.sitemap_search` function to find all links within a website's sitemaps. The `target_lang` argument can be used to filter the discovered links by language.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
from trafilatura import sitemaps

# Automatically find sitemaps by providing the homepage
mylinks = sitemaps.sitemap_search('https://www.theguardian.com/')
print(mylinks)

# The target_lang argument works as explained above
mylinks = sitemaps.sitemap_search('https://www.un.org/', target_lang='en')
print(mylinks)
```

--------------------------------

TITLE: Convert Complex TEI Head Elements to <ab> (Python)
DESCRIPTION: This Python function converts complex TEI `<head>` elements into `<ab>` (analysis block) elements. It handles nested `<p>` tags by inserting `<lb>` (line break) elements and correctly assigns text content and tails.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
from lxml.etree import Element, SubElement, _Element

def _tei_handle_complex_head(element: _Element) -> _Element:
    """Convert certain child elements to <ab> and <lb>."""
    new_element = Element('ab', attrib=element.attrib)
    new_element.text = element.text.strip() if element.text else None
    for child in element.iterchildren():
        if child.tag == 'p':
            if len(new_element) > 0 or new_element.text:
                # add <lb> if <ab> has no children or last tail contains text
                if len(new_element) == 0 or new_element[-1].tail:
                    SubElement(new_element, 'lb')
                new_element[-1].tail = child.text
            else:
                new_element.text = child.text
        else:
            new_element.append(child)
    tail = element.tail.strip() if element.tail else None
    if tail:
        new_element.tail = tail
    return new_element

```

--------------------------------

TITLE: Extract RSS/Atom Feeds with Regex - Bash
DESCRIPTION: This bash script uses a regular expression to identify and extract links to web syndication feeds (RSS/Atom) from HTML content. It's useful for discovering feed sources on websites.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/sources

LANGUAGE: bash
CODE:
```
"<link[^>]*(?:\s(?:type=[\"']?(application\/rss\+xml|application\/atom\+xml|application\/rss|application\/atom|application\/rdf\+xml|application\/rdf|text\/rss\+xml|text\/atom\+xml|text\/rss|text\/atom|text\/rdf\+xml|text\/rdf|text\/xml|application\/xml)[\"']?|rel=[\"']?(?:alternate)[\"']?))[^>]*>)"
```

--------------------------------

TITLE: Bare Text Extraction with trafilatura
DESCRIPTION: The `bare_extraction` function performs internal text extraction, returning bare Python variables. It offers numerous parameters to control the extraction process, including output format, language targeting, inclusion of comments, tables, images, formatting, and links, as well as deduplication and metadata handling.

SOURCE: https://trafilatura.readthedocs.io/en/latest/corefunctions

LANGUAGE: python
CODE:
```
trafilatura.bare_extraction(_filecontent: ~typing.Any_, _url: str | None = None_, _fast: bool = False_, _no_fallback: bool = False_, _favor_precision: bool = False_, _favor_recall: bool = False_, _include_comments: bool = True_, _output_format: str = 'python'_, _target_language: str | None = None_, _include_tables: bool = True_, _include_images: bool = False_, _include_formatting: bool = False_, _include_links: bool = False_, _deduplicate: bool = False_, _date_extraction_params: ~typing.Dict[str_, _~typing.Any] | None = None_, _with_metadata: bool = False_, _only_with_metadata: bool = False_, _max_tree_size: int | None = None_, _url_blacklist: ~typing.Set[str] | None = None_, _author_blacklist: ~typing.Set[str] | None = None_, _as_dict: bool = False_, _prune_xpath: ~typing.Any | None = None_, _config: ~typing.Any = <configparser.ConfigParser object>_, _options: ~trafilatura.settings.Extractor | None = None_) → Document | Dict[str, Any] | None
```

--------------------------------

TITLE: Python script for Internet Archive URL extraction
DESCRIPTION: A Python script designed to extract all known URLs for a specific domain from the Internet Archive. This can be useful for historical data retrieval.

SOURCE: https://trafilatura.readthedocs.io/en/latest/sources

LANGUAGE: python
CODE:
```
import requests

def get_archive_urls(domain):
    url = f"https://web.archive.org/cdx/search/cdx?url={domain}&output=json"
    response = requests.get(url)
    data = response.json()
    urls = [f"https://web.archive.org/web/{item[1]}/{item[2]}" for item in data[1:]]
    return urls

# Example usage:
domain_to_check = "example.com"
archive_urls = get_archive_urls(domain_to_check)
for url in archive_urls:
    print(url)
```

--------------------------------

TITLE: Check if Page is Readable
DESCRIPTION: Demonstrates how to use `is_probably_readerable` to guess if a web page contains main text content, ported from Mozilla's Readability.js.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
>>> from trafilatura.readability_lxml import is_probably_readerable
>>> is_probably_readerable(html)  # HTML string or already parsed tree
```

--------------------------------

TITLE: Load and Validate HTML Object with trafilatura
DESCRIPTION: Loads an HTML object provided as input and validates its type. Accepted types include lxml.html trees, trafilatura/urllib3 responses, bytestrings, and strings.

SOURCE: https://trafilatura.readthedocs.io/en/latest/corefunctions

LANGUAGE: Python
CODE:
```
trafilatura.load_html(_htmlobject : Any_) → HtmlElement | None
```

--------------------------------

TITLE: Baseline Extraction with trafilatura
DESCRIPTION: The `baseline` function utilizes a baseline extraction method to target text paragraphs and/or JSON metadata from HTML content. It returns an LXML body element, the main text as a string, and its length.

SOURCE: https://trafilatura.readthedocs.io/en/latest/corefunctions

LANGUAGE: python
CODE:
```
trafilatura.baseline(_filecontent : Any_) → Tuple[_Element, str, int]
```

--------------------------------

TITLE: Load HTML with Trafilatura
DESCRIPTION: Loads HTML content from a given object and validates its type. This function serves as an entry point for processing HTML data within the trafilatura library.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
from typing import Any, Optional
from lxml.etree import HtmlElement

def load_html(htmlobject: Any) -> Optional[HtmlElement]:
    """Load object given as input and validate its type

```

--------------------------------

TITLE: Validate TEI Document Conformance
DESCRIPTION: Checks if an XML document conforms to the Text Encoding Initiative (TEI) guidelines using a DTD. It loads the TEI schema if not already loaded and logs a warning if validation fails.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
def validate_tei(xmldoc: _Element) -> bool:
    '''Check if an XML document is conform to the guidelines of the Text Encoding Initiative'''
    global TEI_DTD

    if TEI_DTD is None:
        # https://tei-c.org/release/xml/tei/custom/schema/dtd/tei_corpus.dtd
        TEI_DTD = DTD(TEI_SCHEMA)

    result = TEI_DTD.validate(xmldoc)
    if result is False:
        LOGGER.warning('not a valid TEI document: %s', TEI_DTD.error_log.last_error)

    return result
```

--------------------------------

TITLE: XML Processing with Trafilatura
DESCRIPTION: Includes functions for processing XML data, specifically converting XML to plain text and validating XML against TEI standards.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/corefunctions

LANGUAGE: Python
CODE:
```
from trafilatura.xml import xmltotxt

# Example usage:
# xml_content = "..."
# text = xmltotxt(xml_content)

```

LANGUAGE: Python
CODE:
```
from trafilatura.xml import validate_tei

# Example usage:
# xml_filepath = "..."
# is_valid = validate_tei(xml_filepath)

```

--------------------------------

TITLE: Sanitize and Trim Text with Trafilatura
DESCRIPTION: Provides utility functions for cleaning and preparing text data. `sanitize` removes unwanted characters, and `trim` removes leading/trailing whitespace.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/corefunctions

LANGUAGE: Python
CODE:
```
from trafilatura.utils import sanitize

# Example usage:
# text = "..."
# clean_text = sanitize(text)

```

LANGUAGE: Python
CODE:
```
from trafilatura.utils import trim

# Example usage:
# text = "..."
# trimmed_text = trim(text)

```

--------------------------------

TITLE: Python: Extract All Text Content
DESCRIPTION: Demonstrates how to extract all text content from an HTML document in a `html2txt` manner using the `html2txt` function in Trafilatura.

SOURCE: https://trafilatura.readthedocs.io/en/latest/quickstart

LANGUAGE: Python
CODE:
```
from trafilatura import html2txt
html2txt(downloaded)
```

--------------------------------

TITLE: Extract from LXML Tree
DESCRIPTION: Shows how to use the `extract` function with an already parsed LXML tree object as input, allowing for direct processing of HTML content.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
# define document and load it with LXML
>>> from lxml import html
>>> my_doc = """<html><body><article><p>
                    Here is the main text.
                    </p></article></body></html>"""
>>> mytree = html.fromstring(my_doc)

# extract from the already loaded LXML tree
>>> extract(mytree)
'Here is the main text.'
```

--------------------------------

TITLE: Optimize extraction speed by skipping fallback - Python
DESCRIPTION: To increase extraction speed, you can bypass fallback algorithms by setting `no_fallback=True`. This can make extraction approximately twice as fast.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
result = extract(downloaded, no_fallback=True)
```

--------------------------------

TITLE: Process HTML Content with Trafilatura
DESCRIPTION: This snippet demonstrates the core text extraction process using the trafilatura library. It involves cleaning the HTML tree, converting tags, extracting comments, pruning unwanted nodes, and performing various sanity checks on the extracted content, such as tree size, minimum text and comment length, duplicate detection, and language filtering. The function handles potential errors during processing and returns a processed document object or its dictionary representation.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/core

LANGUAGE: python
CODE:
```
cleaned_tree = tree_cleaning(copy(tree), options)
cleaned_tree_backup = copy(cleaned_tree)

# convert tags, the rest does not work without conversion
cleaned_tree = convert_tags(cleaned_tree, options, options.url or document.url)

# comments first, then remove
if options.comments:
    commentsbody, temp_comments, len_comments, cleaned_tree = extract_comments(
        cleaned_tree, options
    )
else:
    commentsbody, temp_comments, len_comments = Element("body"), "", 0
if options.focus == "precision":
    cleaned_tree = prune_unwanted_nodes(cleaned_tree, REMOVE_COMMENTS_XPATH)

postbody, temp_text, len_text = trafilatura_sequence(
    cleaned_tree, cleaned_tree_backup, tree, options
)

# tree size sanity check
if options.max_tree_size:
    # strip tags
    if len(postbody) > options.max_tree_size:
        LOGGER.debug("output tree too long: %s", len(postbody))
        strip_tags(postbody, "hi")
    # still too long, raise an error
    if len(postbody) > options.max_tree_size:
        LOGGER.debug(
            "output tree too long: %s, discarding %s",
            len(postbody),
            options.source,
        )
        raise ValueError
# size checks
if options.comments and len_comments < options.min_extracted_comm_size:  # type: ignore[attr-defined]
    LOGGER.debug("not enough comments: %s", options.source)
if (
    len_text < options.min_output_size  # type: ignore[attr-defined]
    and len_comments < options.min_output_comm_size  # type: ignore[attr-defined]
):
    LOGGER.debug(
        "text and comments not long enough: %s %s %s",
        len_text,
        len_comments,
        options.source,
    )
    raise ValueError

# check duplicates at body level
if options.dedup and duplicate_test(postbody, options) is True:
    LOGGER.debug("discarding duplicate document: %s", options.source)
    raise ValueError

# sanity check on language
if options.lang:
    is_not_target_lang, document = language_filter(
        temp_text, temp_comments, options.lang, document
    )
    if is_not_target_lang is True:
        LOGGER.debug("wrong language: %s", options.source)
        raise ValueError

except (TypeError, ValueError):
    LOGGER.warning("discarding data: %s", options.source)
    return None

# special case: python variables
if options.format == "python":
    document.text = xmltotxt(postbody, options.formatting)
    if options.comments:
        document.comments = xmltotxt(commentsbody, options.formatting)
        document.commentsbody = commentsbody
    document.raw_text = document.text
else:
    document.raw_text, document.commentsbody = temp_text, commentsbody
document.body = postbody

return document if not as_dict else document.as_dict()
```

--------------------------------

TITLE: Trafilatura External: Try Justext
DESCRIPTION: Attempts to use the 'Justext' library for text extraction. This function provides an alternative method for content extraction, leveraging an external library.

SOURCE: https://trafilatura.readthedocs.io/en/latest/genindex

LANGUAGE: python
CODE:
```
from trafilatura.external import try_justext

# Example usage:
# html_content = "<html><body><p>Content.</p></body></html>"
# # try_justext requires 'justext' to be installed
# # text = try_justext(html_content)
```

--------------------------------

TITLE: Examine Meta Tags for Information in Python
DESCRIPTION: This function comprehensively examines meta tags within an HTML document to extract relevant information. It prioritizes OpenGraph tags and then falls back to other meta tags like 'name' and 'property' for title, author, description, and site name.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/metadata

LANGUAGE: Python
CODE:
```
def examine_meta(tree: HtmlElement) -> Document:
    """Search meta tags for relevant information"""
    # bootstrap from potential OpenGraph tags
    metadata = Document().from_dict(extract_opengraph(tree))

    # test if all values not assigned in the following have already been assigned
    if all(
        (
            metadata.title,
            metadata.author,
            metadata.url,
            metadata.description,
            metadata.sitename,
            metadata.image,
        )
    ):  # tags
        return metadata

    tags, backup_sitename = [], None

    # iterate through meta tags
    for elem in tree.iterfind(".//head/meta[@content]"):
        # content
        content_attr = HTML_STRIP_TAGS.sub("", elem.get("content", "")).strip()
        if not content_attr:
            continue
        # todo: image info
        # ...
        # property
        if "property" in elem.attrib:
            property_attr = elem.get("property", "").lower()
            # no opengraph a second time
            if property_attr.startswith("og:"):
                continue
            if property_attr == "article:tag":
                tags.append(normalize_tags(content_attr))
            elif property_attr in PROPERTY_AUTHOR:
                metadata.author = normalize_authors(metadata.author, content_attr)
            elif property_attr == "article:publisher":
                metadata.sitename = metadata.sitename or content_attr
            elif property_attr in METANAME_IMAGE:
                metadata.image = metadata.image or content_attr
        # name attribute
        elif "name" in elem.attrib:
            name_attr = elem.get("name", "").lower()
            # author
            if name_attr in METANAME_AUTHOR:
                metadata.author = normalize_authors(metadata.author, content_attr)
            # title
            elif name_attr in METANAME_TITLE:
                metadata.title = metadata.title or content_attr
            # description
            elif name_attr in METANAME_DESCRIPTION:
                metadata.description = metadata.description or content_attr
            # site name
            elif name_attr in METANAME_PUBLISHER:

```

--------------------------------

TITLE: Python: Define New Element
DESCRIPTION: Creates a new sub-element attached to an original element, copying the tag, text, and tail from a processed element. This is used to structure the output during HTML parsing.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def define_newelem(processed_elem: _Element, orig_elem: _Element) -> None:
    """Create a new sub-element if necessary."""
    if processed_elem is not None:
        childelem = SubElement(orig_elem, processed_elem.tag)
        childelem.text, childelem.tail = processed_elem.text, processed_elem.tail
```

--------------------------------

TITLE: Python: Extract Metadata
DESCRIPTION: Shows how to extract specific metadata such as title, author, or publication date from a web page using the `extract_metadata` function in Trafilatura.

SOURCE: https://trafilatura.readthedocs.io/en/latest/quickstart

LANGUAGE: Python
CODE:
```
from trafilatura import fetch_url, extract_metadata
downloaded = fetch_url('https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/')
extract_metadata(downloaded)
```

--------------------------------

TITLE: Perform Safety Checks and Clean Metadata
DESCRIPTION: Applies safety checks to the metadata, including setting the file date to the maximum configured date. It also calls a 'clean_and_trim' method on the metadata object to finalize processing.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/metadata

LANGUAGE: Python
CODE:
```
# safety checks
    metadata.filedate = date_config["max_date"]
    metadata.clean_and_trim()

    return metadata
```

--------------------------------

TITLE: Baseline Text Extraction from HTML
DESCRIPTION: Extracts text content from HTML, prioritizing JSON metadata (articleBody), then article tags, then paragraphs, and finally the entire body content. It handles different input types (binary string or string) and returns a tuple containing a LXML body element, the extracted text, and its length. It utilizes load_html, trim, basic_cleaning, and json parsing.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/baseline

LANGUAGE: Python
CODE:
```
def baseline(filecontent: Any) -> Tuple[_Element, str, int]:
    """Use baseline extraction function targeting text paragraphs and/or JSON metadata.

    Args:
        filecontent: HTML code as binary string or string.

    Returns:
        A LXML <body> element containing the extracted paragraphs,
        the main text as string, and its length as integer.

    """
    tree = load_html(filecontent)
    postbody = Element('body')
    if tree is None:
        return postbody, '', 0

    # scrape from json text
    temp_text = ""
    for elem in tree.iterfind('.//script[@type="application/ld+json"]'):
        if elem.text and 'articleBody' in elem.text:
            try:
                json_body = json.loads(elem.text).get("articleBody", "")
            except Exception:  # JSONDecodeError or 'list' object has no attribute 'get'
                json_body = ""
            if json_body:
                if "<p>" in json_body:
                    parsed = load_html(json_body)
                    text = trim(parsed.text_content()) if parsed is not None else ""
                else:
                    text = trim(json_body)
                SubElement(postbody, 'p').text = text
                temp_text += " " + text if temp_text else text
                # return postbody, elem.text, len(elem.text)
    if len(temp_text) > 100:
        return postbody, temp_text, len(temp_text)

    tree = basic_cleaning(tree)

    # scrape from article tag
    temp_text = ""
    for article_elem in tree.iterfind('.//article'):
        text = trim(article_elem.text_content())
        if len(text) > 100:
            SubElement(postbody, 'p').text = text
            temp_text += " " + text if temp_text else text
    if len(postbody) > 0:
        # temp_text = trim('\n'.join(postbody.itertext()))
        return postbody, temp_text, len(temp_text)

    # scrape from text paragraphs
    results = set()
    temp_text = ""
    # postbody = Element('body')
    for element in tree.iter('blockquote', 'code', 'p', 'pre', 'q', 'quote'):
        entry = trim(element.text_content())
        if entry not in results:
            SubElement(postbody, 'p').text = entry
            temp_text += " " + entry if temp_text else entry
            results.add(entry)
    # temp_text = trim('\n'.join(postbody.itertext()))
    if len(temp_text) > 100:
        return postbody, temp_text, len(temp_text)

    # default strategy: clean the tree and take everything
    postbody = Element('body')
    body_elem = tree.find('.//body')
    if body_elem is not None:
        p_elem = SubElement(postbody, 'p')
        # todo: sanitize?
        text_elems = [trim(e) for e in body_elem.itertext()]
        p_elem.text = '\n'.join([e for e in text_elems if e])
        return postbody, p_elem.text, len(p_elem.text)

    # new fallback
    text = html2txt(tree, clean=False)
    SubElement(postbody, 'p').text = text
    return postbody, text, len(text)
```

--------------------------------

TITLE: Python: Handle Other Elements
DESCRIPTION: Handles diverse or unknown HTML elements, including specific cases like 'w3-code' divs which are treated as code blocks. It also filters elements based on a set of potential tags and logs discarded elements.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def handle_other_elements(element: _Element, potential_tags: Set[str], options: Extractor) -> Optional[_Element]:
    """Handle diverse or unknown elements in the scope of relevant tags."""
    # handle w3schools code
    if element.tag == "div" and "w3-code" in element.get("class", ""):
        return handle_code_blocks(element)

    # delete unwanted
    if element.tag not in potential_tags:
        if element.tag != "done":
            _log_event("discarding element", element.tag, element.text)
        return None

    if element.tag == "div":
```

--------------------------------

TITLE: URL Filtering with Trafilatura
DESCRIPTION: Filter discovered URLs using the `--url-filter` option. This can be used to include or exclude specific URL patterns, protocols, or subparts of a website during processing.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-cli

LANGUAGE: bash
CODE:
```
$ trafilatura --sitemap "https://www.sitemaps.org/" --list --url-filter "https://www.sitemaps.org/de"
$ trafilatura --sitemap "https://www.sitemaps.org/" --list --url-filter "protocol"


```

LANGUAGE: bash
CODE:
```
Using a subpart of the site also acts like a filter, for example `--sitemap "https://www.sitemaps.org/de/"`.
```

--------------------------------

TITLE: Bare Extraction Function
DESCRIPTION: Internal function for text extraction that returns bare Python variables. It accepts various parameters to control the extraction process, including input content, URL, extraction modes (fast, precision, recall), output format, language targeting, metadata inclusion, and more.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/core

LANGUAGE: python
CODE:
```
def bare_extraction(
    filecontent: Any,
    url: Optional[str] = None,
    fast: bool = False,
    no_fallback: bool = False,
    favor_precision: bool = False,
    favor_recall: bool = False,
    include_comments: bool = True,
    output_format: str = "python",
    target_language: Optional[str] = None,
    include_tables: bool = True,
    include_images: bool = False,
    include_formatting: bool = False,
    include_links: bool = False,
    deduplicate: bool = False,
    date_extraction_params: Optional[Dict[str, Any]] = None,
    with_metadata: bool = False,
    only_with_metadata: bool = False,
    max_tree_size: Optional[int] = None,
    url_blacklist: Optional[Set[str]] = None,
    author_blacklist: Optional[Set[str]] = None,
    as_dict: bool = False,
    prune_xpath: Optional[Any] = None,
    config: Any = DEFAULT_CONFIG,
    options: Optional[Extractor] = None,
) -> Optional[Union[Document, Dict[str, Any]]]:
    """Internal function for text extraction returning bare Python variables.

    Args:
        filecontent: HTML code as string.
        url: URL of the webpage.

```

--------------------------------

TITLE: Check and Scrub TEI XML
DESCRIPTION: Validates and cleans an XML document according to TEI guidelines. It handles tag conversions (e.g., 'head' to 'ab'), repairs structural issues, and removes invalid TEI elements and attributes, logging warnings for discrepancies.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
def check_tei(xmldoc: _Element, url: Optional[str]) -> _Element:
    '''Check if the resulting XML file is conform and scrub remaining tags'''
    # convert head tags
    for elem in xmldoc.iter('head'):
        elem.tag = 'ab'
        elem.set('type', 'header')
        parent = elem.getparent()
        if parent is None:
            continue
        if len(elem) > 0:
            new_elem = _tei_handle_complex_head(elem)
            parent.replace(elem, new_elem)
            elem = new_elem
        if parent.tag == "p":
            _move_element_one_level_up(elem)
    # convert <lb/> when child of <div> to <p>
    for elem in xmldoc.findall(".//text/body//div/lb"):
        if elem.tail and elem.tail.strip():
            elem.tag, elem.text, elem.tail = 'p', elem.tail, None
    # look for elements that are not valid
    for elem in xmldoc.findall('.//text/body//*'):
        # check elements
        if elem.tag not in TEI_VALID_TAGS:
            # disable warnings for chosen categories
            # if element.tag not in ('div', 'span'):
            LOGGER.warning('not a TEI element, removing: %s %s', elem.tag, url)
            merge_with_parent(elem)
            continue
        if elem.tag in TEI_REMOVE_TAIL:
            _handle_unwanted_tails(elem)
        elif elem.tag == "div":
            _handle_text_content_of_div_nodes(elem)
            _wrap_unwanted_siblings_of_div(elem)
            #if len(elem) == 0:
            #    elem.getparent().remove(elem)
        # check attributes
        for attribute in [a for a in elem.attrib if a not in TEI_VALID_ATTRS]:
            LOGGER.warning('not a valid TEI attribute, removing: %s in %s %s', attribute, elem.tag, url)
            elem.attrib.pop(attribute)
    return xmldoc
```

--------------------------------

TITLE: Manage Element Tails for TEI Conformity (Python)
DESCRIPTION: This Python function cleans and manages the `tail` attribute of TEI elements, specifically `<p>` and `<ab>`. It either appends the tail text to the element's text content or creates a new `<p>` sibling element to contain the tail.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
from lxml.etree import Element, _Element

def _handle_unwanted_tails(element: _Element) -> None:
    """Handle tail on p and ab elements"""
    element.tail = element.tail.strip() if element.tail else None
    if not element.tail:
        return

    if element.tag == "p":
        element.text = " ".join(filter(None, [element.text, element.tail]))
    else:
        new_sibling = Element('p')
        new_sibling.text = element.tail
        parent = element.getparent()
        if parent is not None:
            parent.insert(parent.index(element) + 1 , new_sibling)
    element.tail = None

```

--------------------------------

TITLE: Repair Faulty HTML with Trafilatura
DESCRIPTION: Repairs common faulty HTML string structures to make them palatable for libxml2 parsing. It addresses issues like missing doctype declarations and malformed closing tags, particularly for documents with less than three lines.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
from typing import Optional
import re

# Assuming DOCTYPE_TAG and FAULTY_HTML are pre-compiled regex patterns

def repair_faulty_html(htmlstring: str, beginning: str) -> str:
    """Repair faulty HTML strings to make then palatable for libxml2."""
    # libxml2/LXML issue: https://bugs.launchpad.net/lxml/+bug/1955915
    if "doctype" in beginning:
        firstline, _, rest = htmlstring.partition("\n")
        htmlstring = DOCTYPE_TAG.sub("", firstline, count=1) + "\n" + rest
    # other issue with malformed documents: check first three lines
    for i, line in enumerate(iter(htmlstring.splitlines())):
        if "<html" in line and line.endswith("/>"):
            htmlstring = FAULTY_HTML.sub(r"\1>", htmlstring, count=1)
            break
        if i > 2:
            break
    return htmlstring
```

--------------------------------

TITLE: Trafilatura Sitemaps: Search Sitemap URLs
DESCRIPTION: Searches for and extracts URLs from sitemap files. This function is crucial for discovering all pages indexed by a website.

SOURCE: https://trafilatura.readthedocs.io/en/latest/genindex

LANGUAGE: python
CODE:
```
from trafilatura.sitemaps import sitemap_search

# Example usage:
# sitemap_url = "https://example.com/sitemap.xml"
# urls = sitemap_search(sitemap_url)
```

--------------------------------

TITLE: Process HTTP response
DESCRIPTION: Processes a urllib3 response object, extracts links, and adds the final document URL to the known links. It decodes the response data and calls `process_links` to handle the extracted content.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/spider

LANGUAGE: Python
CODE:
```
def process_response(
    response: Optional[Response],
    params: CrawlParameters,
) -> None:
    """Convert urllib3 response object and extract links."""
    if response is None or not response.data:
        return
    # add final document URL to known_links
    URL_STORE.add_urls([response.url], visited=True)

    # convert urllib3 response to string and proceed to link extraction
    process_links(decode_file(response.data), params, params.base)
```

--------------------------------

TITLE: Use Extractor class for custom settings - Python
DESCRIPTION: The Extractor class allows defining and managing extraction parameters, providing a convenient way to customize options. You can set multiple options at once or adjust them individually.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
from trafilatura.settings import Extractor

options = Extractor(output_format="json", with_metadata=True)
options.formatting = True
options.source = "My Source"

extract(my_doc, options=options)
```

--------------------------------

TITLE: Convert HTML to Text in R
DESCRIPTION: Utilizes the html2txt function from Trafilatura in R to extract all possible text content from a downloaded HTML document.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-r

LANGUAGE: R
CODE:
```
> trafilatura$html2txt(downloaded)
```

--------------------------------

TITLE: Convert BeautifulSoup to LXML for Trafilatura
DESCRIPTION: Demonstrates the process of converting a BeautifulSoup object to an LXML tree format, which can then be used with Trafilatura's `extract` function.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
>>> from bs4 import BeautifulSoup
>>> from lxml.html.soupparser import convert_tree
>>> from trafilatura import extract

>>> soup = BeautifulSoup("<html><body><time>The date is Feb 2, 2024</time></body></html>", "lxml")
>>> lxml_tree = convert_tree(soup)[0]
>>> extract(lxml_tree)
```

--------------------------------

TITLE: Article Extraction Benchmark - ScrapingHub
DESCRIPTION: Trafilatura was identified as the most efficient open-source library in ScrapingHub's article extraction benchmark. This highlights its effectiveness in extracting articles from web pages.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/evaluation

LANGUAGE: text
CODE:
```
Most efficient open-source library in *ScrapingHub*'s `article extraction benchmark <https://github.com/scrapinghub/article-extraction-benchmark>`_
```

--------------------------------

TITLE: Focused Web Crawler
DESCRIPTION: The `focused_crawler` function implements a basic web crawler that targets specific pages within a website. It allows setting limits on visited and known URLs, providing initial lists of pages to visit or known links, language filtering, and custom rules for politeness and content pruning.

SOURCE: https://trafilatura.readthedocs.io/en/latest/corefunctions

LANGUAGE: python
CODE:
```
from trafilatura.spider import focused_crawler

# Example usage:
# pages_to_visit, known_links = focused_crawler('http://example.com', max_seen_urls=10, lang='en')
```

--------------------------------

TITLE: Process Formatting Elements in HTML
DESCRIPTION: Processes formatting elements like 'b' or 'i' (converted to 'hi') found outside of paragraphs. It cleans and repairs orphan elements, ensuring they are correctly placed within the document structure.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def handle_formatting(element: _Element, options: Extractor) -> Optional[_Element]:
    """Process formatting elements (b, i, etc. converted to hi) found
       outside of paragraphs"""
    formatting = process_node(element, options)
    if formatting is None:  #  and len(element) == 0
        return None

    # repair orphan elements
    # if formatting is None:
    #    formatting = Element(element.tag)
    #     return None
    # if len(element) > 0:
    #    for child in element.iter('*'):
    #        if child.tag not in potential_tags:
    #            LOGGER.debug('unexpected in title: %s %s %s', child.tag, child.text, child.tail)
    #            continue
    #        processed_child = handle_textnode(child, options, comments_fix=False)
    #        if processed_child is not None:
    #            formatting.append(processed_child)
    #        child.tag = 'done'
    # if text_chars_test(element.text) is True:
    #    processed_child.text = trim(element.text)
    # if text_chars_test(element.tail) is True:
    #    processed_child.tail = trim(element.tail)
    # if len(element) == 0:
    #    processed_element = process_node(element, options)
    # children
    # else:
    #    processed_element = Element(element.tag)
    #    processed_element.text, processed_element.tail = element.text, element.tail
    #    for child in element.iter('*'):
    #        processed_child = handle_textnode(child, options, comments_fix=False)
    #        if processed_child is not None:
    #            processed_element.append(processed_child)
    #        child.tag = 'done'
    # repair orphan elements
    # shorter code but triggers warning:
    # parent = element.getparent() or element.getprevious()

    parent = element.getparent()
    if parent is None:
        parent = element.getprevious()
    if parent is None or parent.tag not in FORMATTING_PROTECTED:
        processed_element = Element('p')
        processed_element.insert(0, formatting)
    else:
        processed_element = formatting
    return processed_element

```

--------------------------------

TITLE: Test Duplicate Text Content with Trafilatura
DESCRIPTION: Demonstrates how to use the `duplicate_test` function from Trafilatura to check for duplicate text content within LXML elements. It configures the `Extractor` to consider short segments and disallow repetitions, showing how the function returns False for new elements and True for duplicates.

SOURCE: https://trafilatura.readthedocs.io/en/latest/deduplication

LANGUAGE: python
CODE:
```
from lxml.etree import fromstring
from trafilatura.deduplication import duplicate_test
from trafilatura.settings import Extractor

options = Extractor()
options.min_duplcheck_size = 0  # even short segments are considered
options.max_repetitions = 0  # no repetition allowed

elem = fromstring("<p>Here is text.</p>")
print(duplicate_test(elem, options))
print(duplicate_test(elem, options))
```

--------------------------------

TITLE: Parse robots.txt
DESCRIPTION: Parses a robots.txt file using Python's standard library `urllib.robotparser`. It handles potential exceptions during parsing and returns a `RobotFileParser` object or None if an error occurs.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/spider

LANGUAGE: Python
CODE:
```
def parse_robots(robots_url: str, data: str) -> Optional[RobotFileParser]:
    """Parse a robots.txt file with the standard library urllib.robotparser."""
    # https://github.com/python/cpython/blob/main/Lib/urllib/robotparser.py
    rules = RobotFileParser()
    rules.set_url(robots_url)
    # exceptions happening here
    try:
        rules.parse(data.splitlines())
    except Exception as exc:
        LOGGER.error("cannot read robots.txt: %s", exc)
        return None
    return rules
```

--------------------------------

TITLE: Handle Loose Text in TEI Elements (Python)
DESCRIPTION: This Python function ensures that loose text content within an element is wrapped in a `<p>` tag for TEI conformity. It handles cases where the element contains other tags, specifically checking for a preceding `<p>` tag.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
from lxml.etree import Element, SubElement, _Element

def _handle_text_content_of_div_nodes(element: _Element) -> None:
    """Wrap loose text in <div> within <p> elements for TEI conformity."""
    if element.text and element.text.strip():
        if len(element) > 0 and element[0].tag == "p":
            element[0].text = f'{element.text} {element[0].text or ""}'.strip()
        else:
            new_child = Element("p")
            new_child.text = element.text
            element.insert(0, new_child)
        element.text = None

    if element.tail and element.tail.strip():
        if len(element) > 0 and element[-1].tag == "p":
            element[-1].text = f'{element[-1].text or ""} {element.tail}'.strip()
        else:
            new_child = Element("p")
            new_child.text = element.tail
            element.append(new_child)
        element.tail = None

```

--------------------------------

TITLE: Trafilatura: Fetch URL
DESCRIPTION: Fetches the content of a URL, likely performing the necessary HTTP request and returning the content. This is a common operation for web scraping.

SOURCE: https://trafilatura.readthedocs.io/en/latest/genindex

LANGUAGE: python
CODE:
```
from trafilatura import fetch_url

# Example usage:
# url = "https://example.com"
# content = fetch_url(url)
```

--------------------------------

TITLE: Trafilatura External: Try Readability
DESCRIPTION: Attempts to use the 'Readability' library for text extraction. This function offers another method for extracting main content, relying on the Readability algorithm.

SOURCE: https://trafilatura.readthedocs.io/en/latest/genindex

LANGUAGE: python
CODE:
```
from trafilatura.external import try_readability

# Example usage:
# html_content = "<html><body><p>Content.</p></body></html>"
# # try_readability requires 'readability-lxml' to be installed
# # text = try_readability(html_content)
```

--------------------------------

TITLE: Check if there are still navigation pages to visit
DESCRIPTION: This Python code snippet shows how to check if there are still navigation pages to visit using the `is_still_navigation` function from Trafilatura's spider module. It takes the `to_visit` list as input and returns a boolean indicating whether further navigation is possible.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/crawls

LANGUAGE: python
CODE:
```
from trafilatura.spider import is_still_navigation

is_still_navigation(to_visit)
```

--------------------------------

TITLE: Handle Text Elements with Potential Tags
DESCRIPTION: Processes generic text elements (`<p>`, `<div>`, etc.) within an HTML structure. It identifies and delegates specific element types like lists (`<list>`), quotes (`<code>`, `<pre>`), and headings (`<head>`) to their respective handler functions. For other elements, it attempts to process them as text, potentially preserving spaces and handling comments.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def handle_textelem(element: _Element, potential_tags: Set[str], options: Extractor) -> Optional[_Element]:
    '''Process text element and determine how to deal with its content'''
    new_element = None
    # bypass: nested elements
    if element.tag == 'list':
        new_element = handle_lists(element, options)
    elif element.tag in CODES_QUOTES:
        new_element = handle_quotes(element, options)
    elif element.tag == 'head':
        new_element = handle_titles(element, options)
    elif element.tag == 'p':
        # Placeholder for paragraph processing
        pass
    # Add other specific element handling here if needed
    return new_element
```

--------------------------------

TITLE: goose3 Content Extraction - Python
DESCRIPTION: The goose3 Python library can extract information for embedded content but does not preserve markup. It is an alternative for content extraction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/evaluation

LANGUAGE: python
CODE:
```
goose3 <https://github.com/goose3/goose3>`_ can extract information for embedded content but doesn't preserve markup
```

--------------------------------

TITLE: Sitemap URL Detection (Python)
DESCRIPTION: This snippet defines a regular expression to detect potential sitemap URLs, typically ending with '.xml' or variations thereof, which might indicate the presence of a sitemap file.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/sitemaps

LANGUAGE: Python
CODE:
```
import re

DETECT_SITEMAP_LINK = re.compile(r"\.xml(..{2,4})?$|\.xml[?#]")
```

--------------------------------

TITLE: Best Single Tool - Bevendorff et al. 2023
DESCRIPTION: In the paper 'An Empirical Comparison of Web Content Extraction Algorithms' by Bevendorff et al. (2023), Trafilatura was rated the best single tool based on ROUGE-LSum Mean F1 Page Scores.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/evaluation

LANGUAGE: text
CODE:
```
Best single tool by ROUGE-LSum Mean F1 Page Scores in `An Empirical Comparison of Web Content Extraction Algorithms <https://webis.de/downloads/publications/papers/bevendorff_2023b.pdf>`_ (Bevendorff et al. 2023)
```

--------------------------------

TITLE: Language-Focused Crawling - Jauhiainen et al. (2020)
DESCRIPTION: Highlights the use of indicators, such as language identification, during web scouting to influence the crawling process and maintain a language focus within the collected data.

SOURCE: https://trafilatura.readthedocs.io/en/latest/compendium

LANGUAGE: General
CODE:
```
Certain indicators can be applied while scouting the Web and potentially affect the course of events, such as language identification in order to keep the crawl language-focused
```

--------------------------------

TITLE: Generate Hash Filename (Python)
DESCRIPTION: Creates a filename-safe string by hashing the provided content. This ensures consistent naming for identical or similar content, aiding in file management.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/deduplication

LANGUAGE: python
CODE:
```
# create a filename-safe string by hashing the given content
from trafilatura.deduplication import generate_hash_filename
generate_hash_filename("This is a text.")
```

--------------------------------

TITLE: Handle Paragraphs in Trafilatura
DESCRIPTION: Processes paragraph elements and their children, trimming and cleaning the content. It handles nested elements, formatting tags like 'hi' and 'ref', and line breaks.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def handle_paragraphs(element: _Element, potential_tags: Set[str], options: Extractor) -> Optional[_Element]:
    """Process paragraphs along with their children, trim and clean the content."""
    element.attrib.clear()  # todo: test if necessary
    # strip_tags(element, 'p') # change in precision due to spaces?

    # no children
    if len(element) == 0:
        return process_node(element, options)

    # children
    processed_element = Element(element.tag)
    for child in element.iter("*"):
        if child.tag not in potential_tags and child.tag != "done":
            _log_event("unexpected in p", child.tag, child.text)
            continue
        # spacing = child.tag in SPACING_PROTECTED  # todo: outputformat.startswith('xml')?
        # todo: act on spacing here?
        processed_child = handle_textnode(child, options, comments_fix=False, preserve_spaces=True)
        if processed_child is not None:
            # todo: needing attention!
            if processed_child.tag == "p":
                _log_event("extra in p", "p", processed_child.text)
                if processed_element.text:
                    processed_element.text += " " + (processed_child.text or "")
                else:
                    processed_element.text = processed_child.text
                child.tag = "done"
                continue
            # handle formatting
            newsub = Element(child.tag)
            if processed_child.tag in P_FORMATTING:
                # check depth and clean
                if len(processed_child) > 0:
                    for item in processed_child:  # children are lists
                        if text_chars_test(item.text) is True:
                            item.text = " " + item.text  # type: ignore[operator]
                        strip_tags(processed_child, item.tag)
                # correct attributes
                if child.tag == "hi":
                    newsub.set("rend", child.get("rend", ""))
                elif child.tag == "ref":
                    if child.get("target") is not None:
                        newsub.set("target", child.get("target", ""))
            # handle line breaks
            # elif processed_child.tag == 'lb':
            #    try:
            #        processed_child.tail = process_node(child, options).tail
            #    except AttributeError:  # no text
            #        pass
            # prepare text
            # todo: to be moved to handle_textnode()
            # if text_chars_test(processed_child.text) is False:
            #    processed_child.text = ''
            # if text_chars_test(processed_child.tail) is False:
            #    processed_child.tail = ''
            # if there are already children
            # if len(processed_element) > 0:
            #    if text_chars_test(processed_child.tail) is True:
            #        newsub.tail = processed_child.text + processed_child.tail
            #    else:
            #        newsub.tail = processed_child.text
            newsub.text, newsub.tail = processed_child.text, processed_child.tail

            if processed_child.tag == 'graphic':
                image_elem = handle_image(processed_child)
                if image_elem is not None:
                    newsub = image_elem
            processed_element.append(newsub)
        child.tag = "done"
    # finish
    if len(processed_element) > 0:
        last_elem = processed_element[-1]
        # clean trailing lb-elements
        if last_elem.tag == "lb" and last_elem.tail is None:
            delete_element(last_elem)
        return processed_element
    if processed_element.text:
        return processed_element
    _log_event("discarding element:", "p", tostring(processed_element))
    return None
```

--------------------------------

TITLE: Determine Element Text with Formatting
DESCRIPTION: Determines the text content of an LXML element, optionally including formatting conversion to Markdown. It handles specific tags like 'head', 'del', 'hi', 'code', 'ref', 'cell', and 'item' to represent their content appropriately.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
def replace_element_text(element: _Element, include_formatting: bool) -> str:
    """Determine element text based on just the text of the element. One must deal with the tail separately."""
    elem_text = element.text or ""
    # handle formatting: convert to markdown
    if include_formatting and element.text:
        if element.tag == "head":
            try:
                number = int(element.get("rend")[1])  # type: ignore[index]
            except (TypeError, ValueError):
                number = 2
            elem_text = f'{"#" * number} {elem_text}'
        elif element.tag == "del":
            elem_text = f"~~{elem_text}~~"
        elif element.tag == "hi":
            rend = element.get("rend")
            if rend in HI_FORMATTING:
                elem_text = f"{HI_FORMATTING[rend]}{elem_text}{HI_FORMATTING[rend]}"
        elif element.tag == "code":
            if "\n" in element.text:
                elem_text = f"```\n{elem_text}\n```"
            else:
                elem_text = f"`{elem_text}`"
    # handle links
    if element.tag == "ref":
        if elem_text:
            link_text = f"[{elem_text}]"
            target = element.get("target")
            if target:
                elem_text = f"{link_text}({target})"
            else:
                LOGGER.warning("missing link attribute: %s %s'", elem_text, element.attrib)
                elem_text = link_text
        else:
            LOGGER.warning("empty link: %s %s", elem_text, element.attrib)
    # cells
    if element.tag == "cell" and elem_text and len(element) > 0:
        if element[0].tag == 'p':
            elem_text = f"{elem_text} " if element.getprevious() is not None else f"| {elem_text} "
    elif element.tag == 'cell' and elem_text:
        # add | before first cell
        elem_text = f"{elem_text}" if element.getprevious() is not None else f"| {elem_text}"
    # lists
    elif element.tag == "item" and elem_text:
        elem_text = f"- {elem_text}\n"
    return elem_text
```

--------------------------------

TITLE: Clean URL Format with Courlan (Python)
DESCRIPTION: The `clean_url` function normalizes URLs to a standard format by removing unnecessary characters and handling case sensitivity, ensuring consistency.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/url-management

LANGUAGE: python
CODE:
```
from courlan import clean_url

clean_url('HTTPS://WWW.DWDS.DE:80/')
# 'https://www.dwds.de'
```

--------------------------------

TITLE: Compile Regular Expressions for Feed Parsing
DESCRIPTION: Compiles regular expressions used to identify feed opening tags, extract link attributes and elements, blacklist comment feeds, and validate link formats. These regexes are used throughout the feed parsing process.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/feeds

LANGUAGE: Python
CODE:
```
FEED_OPENING = re.compile(r"<(feed|rss|\?xml)")

LINK_ATTRS = re.compile(r'<link .*?href=".+?"')
LINK_HREF = re.compile(r'href="(.+?)"')
LINK_ELEMENTS = re.compile(
    r"<link>(?:\s*)(?:<!\[CDATA\[)?(.+?)(?:\]\]>)?(?:\s*)</link>"
)

BLACKLIST = re.compile(r"\bcomments\b")  # no comment feed

LINK_VALIDATION_RE = re.compile(
    r"\.(?:atom|rdf|rss|xml)$|"
    r"\b(?:atom|rss)\b|"
    r"\?type=100$|"  # Typo3
    r"feeds/posts/default/?$|"  # Blogger
    r"\?feed=(?:atom|rdf|rss|rss2)|"
    r"feed$"  # Generic
)
```

--------------------------------

TITLE: Check URL with Courlan (Python)
DESCRIPTION: The `check_url` function from the `courlan` package validates and cleans a given URL, returning the cleaned URL and its domain name. It can also filter URLs based on specified languages and remove noisy query parameters.

SOURCE: https://trafilatura.readthedocs.io/en/latest/url-management

LANGUAGE: Python
CODE:
```
from courlan import check_url

# checking a URL returns None or a tuple (cleaned url, hostname)
check_url('https://github.com/adbar/courlan')

# noisy query parameters can be removed
check_url('https://httpbin.org/redirect-to?url=http%3A%2F%2Fexample.org', strict=True)

# optional argument targeting webpages in English or German
my_url = 'https://www.un.org/en/about-us'
url, domain_name = check_url(my_url, language='en')
url, domain_name = check_url(my_url, language='de')
```

--------------------------------

TITLE: Extract Metadata from HTML
DESCRIPTION: The `extract_metadata` function is the primary method for extracting metadata from HTML content. It accepts HTML as a string or a parsed tree and can optionally take a default URL, date configuration, and an author blacklist for filtering.

SOURCE: https://trafilatura.readthedocs.io/en/latest/corefunctions

LANGUAGE: python
CODE:
```
from trafilatura import extract_metadata

# Example usage:
# metadata = extract_metadata(html_content, default_url='http://example.com', extensive=True)
```

--------------------------------

TITLE: Extract Categories and Tags
DESCRIPTION: Finds category and tag information from HTML using custom XPath expressions and regular expressions. It supports fallback mechanisms for category extraction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/metadata

LANGUAGE: Python
CODE:
```
def extract_catstags(metatype: str, tree: HtmlElement) -> List[str]:
    """Find category and tag information"""
    results: List[str] = []
    regexpr = "/" + metatype + "[s|ies]?/"
    xpath_expression = CATEGORIES_XPATHS if metatype == "category" else TAGS_XPATHS
    # search using custom expressions
    for catexpr in xpath_expression:
        results.extend(
            elem.text_content()
            for elem in catexpr(tree)
            if re.search(regexpr, elem.attrib["href"])
        )
        if results:
            break
    # category fallback
    if metatype == "category" and not results:
        for element in tree.xpath(
            './/head//meta[@property="article:section" or contains(@name, "subject")][@content]'
        ):
            results.append(element.attrib["content"])
        # optional: search through links
        # if not results:
        #    for elem in tree.xpath('.//a[@href]'):
        #        search for 'category'
    return [r for r in dict.fromkeys(line_processing(x) for x in results if x) if r]
```

--------------------------------

TITLE: Find Feed URLs
DESCRIPTION: The `find_feed_urls` function attempts to discover feed URLs (like RSS or Atom) for a given web page URL. Similar to `sitemap_search`, it supports language filtering, external link inclusion, and configurable sleep times.

SOURCE: https://trafilatura.readthedocs.io/en/latest/corefunctions

LANGUAGE: python
CODE:
```
from trafilatura.feeds import find_feed_urls

# Example usage:
# feed_links = find_feed_urls('http://example.com', target_lang='en')
```

--------------------------------

TITLE: Check for navigation pages
DESCRIPTION: Determines if there are still navigation URLs remaining in a given list of URLs. It iterates through the list and checks each URL using `is_navigation_page`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/spider

LANGUAGE: Python
CODE:
```
def is_still_navigation(todo: List[str]) -> bool:
    """Probe if there are still navigation URLs in the queue."""
    return any(is_navigation_page(url) for url in todo)
```

--------------------------------

TITLE: Run Python Code and Extract Data in R
DESCRIPTION: Executes Python code directly within R using py_run_string to import Trafilatura, extract data, and then convert the Python object to an R data frame.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-r

LANGUAGE: R
CODE:
```
> py_run_string("import trafilatura")
> url <- "https://www.example.com"
> py_df <- py_run_string("trafilatura.extract(url)")
> df <- py_to_r(py_df)
```

--------------------------------

TITLE: Find Feed URLs from a Given URL
DESCRIPTION: The main function to find feed URLs from a given URL. It handles both web pages and direct feed URLs. If the input is a web page, it attempts to find feed links within the page and also tries to probe the homepage if direct extraction fails. It supports language filtering and controlling external URL inclusion.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/feeds

LANGUAGE: Python
CODE:
```
def find_feed_urls(
    url: str,
    target_lang: Optional[str] = None,
    external: bool = False,
    sleep_time: float = 2.0,
) -> List[str]:
    """Try to find feed URLs.

    Args:
        url: Webpage or feed URL as string.
             Triggers URL-based filter if the webpage isn't a homepage.
        target_lang: Define a language to filter URLs based on heuristics
                     (two-letter string, ISO 639-1 format).
        external: Similar hosts only or external URLs
                  (boolean, defaults to False).
        sleep_time: Wait between requests on the same website.

    Returns:
        The extracted links as a list (sorted list of unique links).

    """
    domain, baseurl = get_hostinfo(url)
    if domain is None:
        LOGGER.warning("Invalid URL: %s", url)
        return []

    params = FeedParameters(baseurl, domain, url, external, target_lang)
    urlfilter = None
    downloaded = fetch_url(url)

    if downloaded is not None:
        # assume it's a feed
        feed_links = extract_links(downloaded, params)
        if not feed_links:
            # assume it's a web page
            for feed in determine_feed(downloaded, params):
                feed_string = fetch_url(feed)
                if feed_string:
                    feed_links.extend(extract_links(feed_string, params))
            # filter triggered, prepare it
            if len(url) > len(baseurl) + 2:
                urlfilter = url
        # return links found
        if feed_links:
            feed_links = filter_urls(feed_links, urlfilter)
            LOGGER.debug("%s feed links found for %s", len(feed_links), domain)
            return feed_links
        LOGGER.debug("No usable feed links found: %s", url)
    else:
        LOGGER.error("Could not download web page: %s", url)
        if url.strip("/") != baseurl:
            sleep(sleep_time)
            return try_homepage(baseurl, target_lang)

    return probe_gnews(params, urlfilter)
```

--------------------------------

TITLE: Parse HTML to lxml Tree
DESCRIPTION: Parses various input types (lxml tree, HTTP response, bytestring, string) into an lxml HTML tree. It handles encoding, repairs faulty HTML, and includes fallback parsing mechanisms for robustness. Rejects non-HTML content.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
from lxml.etree import HTMLParser, fromstring as fromstring_bytes
from urllib.response import HTTPResponse
from typing import Optional, Literal
from functools import lru_cache
from logging import getLogger
from unicodedata import normalize
from re import sub as sub_re

from .utils import decode_file, is_dubious_html, repair_faulty_html

LOGGER = getLogger(__name__)

# HTML_PARSER is a global variable that is not defined in the provided snippet.
# Assuming it's an instance of lxml.etree.HTMLParser
# Example: HTML_PARSER = HTMLParser(encoding='utf-8')

# SPACING_PROTECTED and FORMATTING_PROTECTED are global variables not defined in the snippet.
# Assuming they are sets of tags.
# Example: SPACING_PROTECTED = {'pre', 'code'}
# Example: FORMATTING_PROTECTED = {'b', 'i', 'strong', 'em'}

# LINES_TRIMMING is a global variable not defined in the snippet.
# Assuming it's a compiled regex for trimming lines.
# Example: LINES_TRIMMING = re.compile(r'\s+')

# _Element is a type hint for lxml elements, not defined in the snippet.
# Assuming it's an alias for lxml.etree._Element


def parse_html(htmlobject) -> Optional[_Element]:
    """
    Parse HTML content from various input types into an lxml tree.

    Args:
        htmlobject: The input HTML content, which can be an lxml.html tree,
                    a trafilatura/urllib3 response, a bytestring, or a string.

    Returns:
        An lxml.etree._Element representing the parsed HTML tree, or None if parsing fails.
    """
    # use tree directly
    if isinstance(htmlobject, HtmlElement):
        return htmlobject
    # use trafilatura or urllib3 responses directly
    if isinstance(htmlobject, HTTPResponse) or hasattr(htmlobject, "data"):
        htmlobject = htmlobject.data
    # do not accept any other type after this point
    if not isinstance(htmlobject, (bytes, str)):
        raise TypeError("incompatible input type", type(htmlobject))
    # start processing
    tree = None
    # try to guess encoding and decode file: if None then keep original
    htmlobject = decode_file(htmlobject)
    # sanity checks
    beginning = htmlobject[:50].lower()
    check_flag = is_dubious_html(beginning)
    # repair first
    htmlobject = repair_faulty_html(htmlobject, beginning)
    # first pass: use Unicode string
    fallback_parse = False
    try:
        tree = fromstring(htmlobject, parser=HTML_PARSER)
    except ValueError:
        # "Unicode strings with encoding declaration are not supported."
        tree = fromstring_bytes(htmlobject)
        fallback_parse = True
    except Exception as err:  # pragma: no cover
        LOGGER.error("lxml parsing failed: %s", err)
    # second pass: try passing bytes to LXML
    if (tree is None or len(tree) < 1) and not fallback_parse:
        tree = fromstring_bytes(htmlobject)
    # rejection test: is it (well-formed) HTML at all?
    # log parsing errors
    if tree is not None and check_flag is True and len(tree) < 2:
        LOGGER.error(
            "parsed tree length: %s, wrong data type or not valid HTML", len(tree)
        )
        tree = None
    return tree

```

--------------------------------

TITLE: Process internal links
DESCRIPTION: Examines HTML code to extract and filter internal links. It performs an optional language check, prunes unwanted nodes using XPath, and stores the links in a to-do list, prioritizing navigation links.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/spider

LANGUAGE: Python
CODE:
```
def process_links(
    htmlstring: str,
    params: CrawlParameters,
    url: Optional[str] = "",
) -> None:
    """Examine the HTML code and process the retrieved internal links.
    Extract and filter new internal links after an optional language check.
    Store the links in todo-list while prioritizing the navigation ones."""
    if not is_target_language(htmlstring, params.lang):
        return

    if htmlstring and params.prune_xpath is not None:
        if isinstance(params.prune_xpath, str):
            params.prune_xpath = [params.prune_xpath]  # type: ignore[assignment]
        tree = load_html(htmlstring)
        if tree is not None:
            tree = prune_unwanted_nodes(tree, [XPath(x) for x in params.prune_xpath])
            htmlstring = tostring(tree).decode()

    links, links_priority = [], []
    for link in extract_links(
        pagecontent=htmlstring,
        url=url or params.base,
        external_bool=False,
        language=params.lang,
        with_nav=True,
        strict=False,
    ):
        if not params.is_valid_link(link):
            continue
        if is_navigation_page(link):
            links_priority.append(link)
        else:
            links.append(link)

    URL_STORE.add_urls(urls=links, appendleft=links_priority)
```

--------------------------------

TITLE: Best Overall Tool - Lejeune & Barbaresi 2020
DESCRIPTION: Trafilatura was recognized as the best overall tool in the study 'Bien choisir son outil d'extraction de contenu à partir du Web' by Lejeune & Barbaresi (2020).

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/evaluation

LANGUAGE: text
CODE:
```
Best overall tool according to `Bien choisir son outil d'extraction de contenu à partir du Web <https://hal.archives-ouvertes.fr/hal-02768510v3/document>`_ (Lejeune & Barbaresi 2020)
```

--------------------------------

TITLE: Trafilatura Feeds: Find Feed URLs
DESCRIPTION: Searches for and identifies feed URLs (like RSS or Atom) within a web page. This is useful for discovering syndication feeds associated with a site.

SOURCE: https://trafilatura.readthedocs.io/en/latest/genindex

LANGUAGE: python
CODE:
```
from trafilatura.feeds import find_feed_urls

# Example usage:
# html_content = "<html><body><link rel='alternate' type='application/rss+xml' href='/feed.xml'></body></html>"
# feed_urls = find_feed_urls(html_content)
```

--------------------------------

TITLE: Extract Metadata with Trafilatura
DESCRIPTION: Function to extract metadata (like title, author, date) from web content. It processes the HTML to identify and return structured metadata.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/corefunctions

LANGUAGE: Python
CODE:
```
from trafilatura import extract_metadata

# Example usage:
# html = "..."
# metadata = extract_metadata(html)

```

--------------------------------

TITLE: Find Feed URLs with Target Language Filter (Python)
DESCRIPTION: Finds feed URLs from a given URL and filters them based on the specified target language. This helps in retrieving feeds in a specific language.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
from trafilatura import feeds

# Search for feeds in English
mylist = feeds.find_feed_urls('https://www.un.org/en/rss.xml', target_lang='en')
print(mylist is not [])

# Target language set to Japanese, English links are discarded
mylist = feeds.find_feed_urls('https://www.un.org/en/rss.xml', target_lang='ja')
print(mylist)
```

--------------------------------

TITLE: Convert XML Document to CSV
DESCRIPTION: Converts an internal XML document representation to a CSV string. It extracts various metadata fields such as URL, ID, fingerprint, hostname, title, image, date, post text, comments text, license, and page type. The function utilizes the `xmltotxt` function for text conversion and the `csv` module for formatting. Dependencies include `Document` type, `StringIO`, `csv`, and `xmltotxt`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
import csv
from io import StringIO
from typing import Optional
from xml.etree.ElementTree import Element as _Element

# Assuming Document, xmltotxt, and other necessary types/functions are defined elsewhere

def xmltocsv(document: Document, include_formatting: bool, *, delim: str = "\t", null: str = "null") -> str:
    """Convert the internal XML document representation to a CSV string."""
    # preprocessing
    posttext = xmltotxt(document.body, include_formatting) or null
    commentstext = xmltotxt(document.commentsbody, include_formatting) or null

    # output config
    output = StringIO()
    outputwriter = csv.writer(output, delimiter=delim, quoting=csv.QUOTE_MINIMAL)

    # organize fields
    outputwriter.writerow([d if d else null for d in (
        document.url,
        document.id,
        document.fingerprint,
        document.hostname,
        document.title,
        document.image,
        document.date,
        posttext,
        commentstext,
        document.license,
        document.pagetype
    )])
    return output.getvalue()


class Document:
    # Placeholder for Document class definition
    def __init__(self):
        self.body = None
        self.commentsbody = None
        self.url = None
        self.id = None
        self.fingerprint = None
        self.hostname = None
        self.title = None
        self.image = None
        self.date = None
        self.license = None
        self.pagetype = None

```

--------------------------------

TITLE: Extract Metadata from HTML Elements
DESCRIPTION: Processes HTML elements to extract and normalize metadata such as sitename, author, URL, and tags. It handles various attribute types like 'name', 'property', and 'itemprop', with specific logic for Twitter attributes and URL validation.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/metadata

LANGUAGE: Python
CODE:
```
def extract_metadata(tree: HtmlElement, content_attr: str) -> Metadata:
    metadata = Metadata()
    tags = []
    backup_sitename = None
    for elem in tree.iterfind(".//head//meta[@content]"):
        name_attr = elem.get("name", "").lower()
        content_attr = elem.get("content", "")
        # ... (rest of the metadata extraction logic)
    metadata.sitename = metadata.sitename or backup_sitename
    metadata.tags = tags
    return metadata
```

--------------------------------

TITLE: Cite Trafilatura - BibTeX
DESCRIPTION: Provides the BibTeX entry for citing the Trafilatura library in academic publications. This citation includes the paper title, author, publication details, and DOI.

SOURCE: https://trafilatura.readthedocs.io/en/latest/used-by

LANGUAGE: bibtex
CODE:
```
@inproceedings{barbaresi-2021-trafilatura,
  title = {{Trafilatura: A Web Scraping Library and Command-Line Tool for Text Discovery and Extraction}},
  author = "Barbaresi, Adrien",
  booktitle = "Proceedings of the Joint Conference of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing: System Demonstrations",
  pages = "122--131",
  publisher = "Association for Computational Linguistics",
  url = "https://aclanthology.org/2021.acl-demo.15",
  year = 2021,
}

```

--------------------------------

TITLE: Extract URL from Canonical Link
DESCRIPTION: Extracts the URL from canonical link tags or other specified selectors in the HTML. It handles relative URLs by attempting to resolve them against base URLs found in meta tags and validates the final URL.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/metadata

LANGUAGE: Python
CODE:
```
def extract_url(tree: HtmlElement, default_url: Optional[str] = None) -> Optional[str]:
    """Extract the URL from the canonical link"""
    for selector in URL_SELECTORS:
        element = tree.find(selector)
        url = element.attrib.get("href") if element is not None else None
        if url:
            break
    if url and url.startswith("/"):
        for element in tree.iterfind(".//head//meta[@content]"):
            attrtype = element.get("name") or element.get("property") or ""
            if attrtype.startswith("og:") or attrtype.startswith("twitter:"):
                base_url = get_base_url(element.attrib["content"])
                if base_url:
                    url = base_url + url
                    break
    if url:
        validation_result, parsed_url = validate_url(url)
        url = normalize_url(parsed_url) if validation_result else None
    return url or default_url
```

--------------------------------

TITLE: Extract Metadata Categories and Tags
DESCRIPTION: Extracts categories and tags from the HTML tree using the 'category' and 'tag' selectors respectively. This function is called only if the metadata attributes are not already populated.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/metadata

LANGUAGE: Python
CODE:
```
# categories
    if not metadata.categories:
        metadata.categories = extract_catstags("category", tree)

    # tags
    if not metadata.tags:
        metadata.tags = extract_catstags("tag", tree)
```

--------------------------------

TITLE: Extract Sitename
DESCRIPTION: Extracts the sitename from the HTML tree. The specific implementation details for extracting the sitename are not provided in this snippet, but it's a function within the trafilatura library.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/metadata

LANGUAGE: Python
CODE:
```
def extract_sitename(tree: HtmlElement) -> Optional[str]:
    # Implementation details for extracting sitename would go here.
```

--------------------------------

TITLE: Reset Trafilatura Caches
DESCRIPTION: Provides a code snippet to reset Trafilatura's internal caches, which can help free up memory in large-scale applications by releasing RAM.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
# import the function
>>> from trafilatura.meta import reset_caches

# use it at any given point
>>> reset_caches()
```

--------------------------------

TITLE: Define Feed Parameters Class
DESCRIPTION: Defines a class to store parameters related to a feed, such as the base URL, domain, reference URL, language, and whether the feed is external. This class is used to pass context to feed processing functions.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/feeds

LANGUAGE: Python
CODE:
```
class FeedParameters:
    "Store necessary information to proceed a feed."
    __slots__ = ["base", "domain", "ext", "lang", "ref"]

    def __init__(
        self,
        baseurl: str,
        domain: str,
        reference: str,
        external: bool = False,
        target_lang: Optional[str] = None,
    ) -> None:
        self.base: str = baseurl
        self.domain: str = domain
        self.ext: bool = external
        self.lang: Optional[str] = target_lang
        self.ref: str = reference
```

--------------------------------

TITLE: Check Acceptable Length
DESCRIPTION: Verifies if a given length falls within predefined minimum and maximum file size boundaries. Logs an error if the length is outside the acceptable range.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
def is_acceptable_length(my_len: int, options: Any) -> bool:
    """Check if the document length is within acceptable boundaries."""
    if my_len < options.min_file_size:
        LOGGER.error("too small/incorrect for URL %s", options.url)
        return False
    if my_len > options.max_file_size:
        LOGGER.error("too large: length %s for URL %s", my_len, options.url)
        return False
    return True
```

--------------------------------

TITLE: Python: Handle Quotes
DESCRIPTION: Processes quote elements, first checking if they are code blocks. If not, it recursively processes child elements, defines new elements, and strips nested tags to clean the quote content.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def handle_quotes(element: _Element, options: Extractor) -> Optional[_Element]:
    """Process quotes elements."""
    if is_code_block_element(element):
        return handle_code_blocks(element)

    processed_element = Element(element.tag)
    for child in element.iter('*'):
        processed_child = process_node(child, options)  # handle_textnode(child, comments_fix=True)
        if processed_child is not None:
            define_newelem(processed_child, processed_element)
        child.tag = "done"
    if is_text_element(processed_element):
        # avoid double/nested tags
        strip_tags(processed_element, "quote")
        return processed_element
    return None
```

--------------------------------

TITLE: Calculate Text Similarity with Simhash (Python)
DESCRIPTION: Uses the Simhash class to determine the degree of similarity between two pieces of text. The similarity method returns a value between 0 and 1, indicating how alike the texts are, based on locality-sensitive hashing.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/deduplication

LANGUAGE: python
CODE:
```
from trafilatura.deduplication import Simhash

first = Simhash("This is a text.")
second = Simhash("This is a test.")
print(second.similarity(first))
```

--------------------------------

TITLE: Check URL and Domain with Courlan (Python)
DESCRIPTION: The `check_url` function from the courlan package validates a URL and returns a cleaned URL along with its domain name. It can also remove noisy query parameters and target specific languages.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/url-management

LANGUAGE: python
CODE:
```
from courlan import check_url

check_url('https://github.com/adbar/courlan')
# ('https://github.com/adbar/courlan', 'github.com')

check_url('https://httpbin.org/redirect-to?url=http%3A%2F%2Fexample.org', strict=True)
# ('https://httpbin.org/redirect-to', 'httpbin.org')

my_url = 'https://www.un.org/en/about-us'
url, domain_name = check_url(my_url, language='en')
url, domain_name = check_url(my_url, language='de')
```

--------------------------------

TITLE: Generate Content Fingerprint (Python)
DESCRIPTION: Generates a simhash value for a given string, returning it as a hexadecimal string. This function operates independently of the Trafilatura class.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/deduplication

LANGUAGE: python
CODE:
```
from trafilatura.deduplication import content_fingerprint
content_fingerprint("Here is text.")
```

--------------------------------

TITLE: Trafilatura Utils: Decode File
DESCRIPTION: Decodes a file, likely handling different character encodings to ensure proper text representation. This utility function is found in the trafilatura.utils module.

SOURCE: https://trafilatura.readthedocs.io/en/latest/genindex

LANGUAGE: python
CODE:
```
from trafilatura.utils import decode_file

# Example usage:
# file_path = "path/to/your/file.html"
# decoded_text = decode_file(file_path)
```

--------------------------------

TITLE: Recover Wild Text Elements with Trafilatura
DESCRIPTION: This function, `recover_wild_text`, searches the HTML tree for unconsidered elements, including those outside the main frame, to recover potentially missing text. It uses XPath expressions to find elements like blockquotes, code blocks, paragraphs, and tables, and applies text element handling.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def recover_wild_text(tree: HtmlElement, result_body: _Element, options: Extractor, potential_tags: Any = TAG_CATALOG) -> _Element:
    '''Look for all previously unconsidered wild elements, including outside of the determined
       frame and throughout the document to recover potentially missing text parts'''
    LOGGER.debug('Recovering wild text elements')
    search_expr = './/blockquote|.//code|.//p|.//pre|.//q|.//quote|.//table|.//div[contains(@class, 'w3-code')]'
    if options.focus == "recall":
        potential_tags.update(['div', 'lb'])
        search_expr += '|.//div|.//lb|.//list'
    # prune
    search_tree = prune_unwanted_sections(tree, potential_tags, options)
    # decide if links are preserved
    if 'ref' not in potential_tags:
        strip_tags(search_tree, 'a', 'ref', 'span')
    else:
        strip_tags(search_tree, 'span')
    subelems = search_tree.xpath(search_expr)
    result_body.extend(filter(lambda x: x is not None, (handle_textelem(e, potential_tags, options)
                       for e in subelems)))  # type: ignore[arg-type]
    return result_body
```

--------------------------------

TITLE: Blacklist URLs in Python
DESCRIPTION: Exclude specific URLs from being processed by Trafilatura using the `url_blacklist` parameter. This parameter expects a set of URLs.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/url-management

LANGUAGE: Python
CODE:
```
trafilatura.fetch_url(url, url_blacklist={'http://example.com/page1', 'http://example.com/page2'})
```

--------------------------------

TITLE: Clean URL with Courlan (Python)
DESCRIPTION: The `clean_url` function from the `courlan` package normalizes URLs by removing unnecessary characters and converting them to a standard format. This helps prevent errors and inconsistencies caused by malformed or duplicate URLs.

SOURCE: https://trafilatura.readthedocs.io/en/latest/url-management

LANGUAGE: Python
CODE:
```
from courlan import clean_url

clean_url('HTTPS://WWW.DWDS.DE:80/')
```

--------------------------------

TITLE: Trafilatura Extract Function
DESCRIPTION: The main function for extracting text content from HTML. It supports various output formats, metadata extraction, and advanced filtering options.

SOURCE: https://trafilatura.readthedocs.io/en/latest/corefunctions

LANGUAGE: python
CODE:
```
trafilatura.extract(_filecontent: ~typing.Any_, _url: str | None = None_, _record_id: str | None = None_, _fast: bool = False_, _no_fallback: bool = False_, _favor_precision: bool = False_, _favor_recall: bool = False_, _include_comments: bool = True_, _output_format: str = 'txt'_, _tei_validation: bool = False_, _target_language: str | None = None_, _include_tables: bool = True_, _include_images: bool = False_, _include_formatting: bool = False_, _include_links: bool = False_, _deduplicate: bool = False_, _date_extraction_params: ~typing.Dict[str_, _~typing.Any] | None = None_, _with_metadata: bool = False_, _only_with_metadata: bool = False_, _max_tree_size: int | None = None_, _url_blacklist: ~typing.Set[str] | None = None_, _author_blacklist: ~typing.Set[str] | None = None_, _settingsfile: str | None = None_, _prune_xpath: ~typing.Any | None = None_, _config: ~typing.Any = <configparser.ConfigParser object>_, _options: ~trafilatura.settings.Extractor | None = None_) → str | None
```

--------------------------------

TITLE: Decode and Decompress File Content with trafilatura.utils
DESCRIPTION: Checks if a bytestring is GZip compressed and decompresses it. It also guesses the bytestring encoding and decodes it to a Unicode string, resorting to destructive conversion if necessary.

SOURCE: https://trafilatura.readthedocs.io/en/latest/corefunctions

LANGUAGE: Python
CODE:
```
trafilatura.utils.decode_file(_filecontent : bytes | str_) → str
```

--------------------------------

TITLE: Handling Language-Specific Links in Sitemaps (Python)
DESCRIPTION: This code extracts links associated with a specific target language from sitemap content, utilizing hreflang attributes. It filters these links to ensure they match the desired language or are marked as 'x-default'.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/sitemaps

LANGUAGE: Python
CODE:
```
import re
from typing import List, Optional

XHTML_REGEX = re.compile(r"<xhtml:link.+?>", re.DOTALL)
HREFLANG_REGEX = re.compile(r'href=["\'](.+?)["\']')

def extract_sitemap_langlinks(content: str, target_lang: Optional[str]) -> List[str]:
    """Extract links corresponding to a given target language."""
    if "hreflang=" not in content or target_lang is None:
        return []

    lang_regex = re.compile(rf'hreflang=["\']({target_lang}.*?|x-default)["\']', re.DOTALL)
    lang_links = []

    for xhtml_match in XHTML_REGEX.finditer(content):
        attrs = xhtml_match.group(0)
        if lang_regex.search(attrs):
            href_match = HREFLANG_REGEX.search(attrs)
            if href_match:
                lang_links.append(href_match.group(1))
    return lang_links
```

--------------------------------

TITLE: Extract Feed URLs from HTML
DESCRIPTION: Parses HTML content to extract feed URLs. It first looks for links with rel="alternate" and a valid feed type or URL pattern. If no such links are found, it falls back to searching for any link that matches a validation pattern. The extracted URLs are then cleaned, validated, and filtered.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/feeds

LANGUAGE: Python
CODE:
```
def extract_feed_urls_from_html(htmlstring: str, params: FeedParameters) -> List[str]:
    """Parse the HTML and try to extract feed URLs from the home page.
    Adapted from http://www.aaronsw.com/2002/feedfinder/"""
    tree = load_html(htmlstring)
    if tree is None:
        LOGGER.debug("Invalid HTML/Feed page: %s", params.base)
        return []

    # most common case + websites like geo.de
    feed_urls = [
        link.get("href", "")
        for link in tree.xpath('//link[@rel="alternate"][@href]')
        if link.get("type") in FEED_TYPES
        or LINK_VALIDATION_RE.search(link.get("href", ""))
    ]

    # backup
    if not feed_urls:
        feed_urls = [
            link.get("href", "")
            for link in tree.xpath("//a[@href]")
            if LINK_VALIDATION_RE.search(link.get("href", ""))
        ]

    # refine
    output_urls = []
    for link in dict.fromkeys(feed_urls):
        link = fix_relative_urls(params.base, link)
        link = clean_url(link)
        if (
            link
            and link != params.ref
            and is_valid_url(link)
            and not BLACKLIST.search(link)
        ):
            output_urls.append(link)

    # log result
    LOGGER.debug(
        "Feed URLs found: %s of which %s valid", len(feed_urls), len(output_urls)
    )
    return output_urls
```

--------------------------------

TITLE: Examine and Extract Title Element
DESCRIPTION: Extracts the text content from the main HTML <title> element. It also attempts to parse the title using a regular expression to separate the main title from potential secondary parts.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/metadata

LANGUAGE: Python
CODE:
```
def examine_title_element(tree: HtmlElement) -> Tuple[str, Optional[str], Optional[str]]:
    """Extract text segments out of main <title> element."""
    title = ""
    title_element = tree.find(".//head//title")
    if title_element is not None:
        title = trim(title_element.text_content())
        if match := HTMLTITLE_REGEX.match(title):
            return title, match[1], match[2]
    LOGGER.debug("no main title found")
    return title, None, None
```

--------------------------------

TITLE: Decode File Content with Trafilatura
DESCRIPTION: Decodes file content, first attempting to decompress it if it appears to be compressed (e.g., GZip, Brotli). It then guesses the encoding using detected methods and decodes the content to a Unicode string, resorting to a destructive conversion if necessary.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
from typing import Union

# Assuming LOGGER is a configured logger instance

def decode_file(filecontent: Union[bytes, str]) -> str:
    """Check if the bytestring could be GZip and eventually decompress it,
       guess bytestring encoding and try to decode to Unicode string.
       Resort to destructive conversion otherwise."""
    if isinstance(filecontent, str):
        return filecontent

    htmltext = None

    # GZip and Brotli test
    filecontent = handle_compressed_file(filecontent)
    # encoding
    for guessed_encoding in detect_encoding(filecontent):
        try:
            htmltext = filecontent.decode(guessed_encoding)
        except (LookupError, UnicodeDecodeError): # VISCII: lookup
            LOGGER.warning('wrong encoding detected: %s', guessed_encoding)
            htmltext = None
        else:
            break

    # return original content if nothing else succeeded
    return htmltext or str(filecontent, encoding='utf-8', errors='replace')
```

--------------------------------

TITLE: Create Batches from Iterable
DESCRIPTION: Chunks an iterable into smaller pieces of a specified size. It utilizes `itertools.islice` and is compatible with Python 3.12+'s `itertools.batched`.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
def make_chunks(iterable: Any, n: int) -> Any:
    """Chunk data into smaller pieces."""
    # 3.12+: https://docs.python.org/3/library/itertools.html#itertools.batched
    iterator = iter(iterable)
    while batch := tuple(islice(iterator, n)):
        yield batch
```

--------------------------------

TITLE: Generate TEI Publication Statement with Trafilatura
DESCRIPTION: This Python code generates a TEI publication statement for a document, including publisher information, license details, and document identifiers. It utilizes the `lxml` library's `SubElement` function to build the XML structure.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
def _define_publisher_string(docmeta):
    # Placeholder for actual publisher string definition
    return docmeta.publisher or 'Unknown Publisher'

def generate_tei_header(docmeta, PKG_VERSION):
    # Assuming 'header' is an existing lxml Element object
    # For demonstration, let's create a dummy header if it doesn't exist
    from lxml.etree import Element, SubElement
    if 'header' not in locals():
        header = Element('teiHeader')

    filedesc = SubElement(header, 'fileDesc')
    publicationstmt_a = SubElement(filedesc, 'publicationStmt')

    publisher_string = _define_publisher_string(docmeta)
    # license, if applicable
    if docmeta.license:
        SubElement(publicationstmt_a, 'publisher').text = publisher_string
        availability = SubElement(publicationstmt_a, 'availability')
        SubElement(availability, 'p').text = docmeta.license
    # insert an empty paragraph for conformity
    else:
        SubElement(publicationstmt_a, 'p')

    notesstmt = SubElement(filedesc, 'notesStmt')
    if docmeta.id:
        SubElement(notesstmt, 'note', type='id').text = docmeta.id
    SubElement(notesstmt, 'note', type='fingerprint').text = docmeta.fingerprint

    sourcedesc = SubElement(filedesc, 'sourceDesc')
    source_bibl = SubElement(sourcedesc, 'bibl')

    sigle = ', '.join(filter(None, [docmeta.sitename, docmeta.date]))
    if not sigle:
        # Assuming LOGGER is defined elsewhere
        # LOGGER.warning('no sigle for URL %s', docmeta.url)
        pass
    source_bibl.text = ', '.join(filter(None, [docmeta.title, sigle]))
    SubElement(sourcedesc, 'bibl', type='sigle').text = sigle

    biblfull = SubElement(sourcedesc, 'biblFull')
    bib_titlestmt = SubElement(biblfull, 'titleStmt')
    SubElement(bib_titlestmt, 'title', type='main').text = docmeta.title
    if docmeta.author:
        SubElement(bib_titlestmt, 'author').text = docmeta.author

    publicationstmt = SubElement(biblfull, 'publicationStmt')
    SubElement(publicationstmt, 'publisher').text = publisher_string
    if docmeta.url:
        SubElement(publicationstmt, 'ptr', type='URL', target=docmeta.url)
    SubElement(publicationstmt, 'date').text = docmeta.date

    profiledesc = SubElement(header, 'profileDesc')
    abstract = SubElement(profiledesc, 'abstract')
    SubElement(abstract, 'p').text = docmeta.description

    if docmeta.categories or docmeta.tags:
        textclass = SubElement(profiledesc, 'textClass')
        keywords = SubElement(textclass, 'keywords')
        if docmeta.categories:
            SubElement(keywords, 'term', type='categories').text = ','.join(docmeta.categories)
        if docmeta.tags:
            SubElement(keywords, 'term', type='tags').text = ','.join(docmeta.tags)

    creation = SubElement(profiledesc, 'creation')
    SubElement(creation, 'date', type="download").text = docmeta.filedate

    encodingdesc = SubElement(header, 'encodingDesc')
    appinfo = SubElement(encodingdesc, 'appInfo')
    application = SubElement(appinfo, 'application', version=PKG_VERSION, ident='Trafilatura')
    SubElement(application, 'label').text = 'Trafilatura'
    SubElement(application, 'ptr', target='https://github.com/adbar/trafilatura')

    return header

```

--------------------------------

TITLE: Regular expression for discovering web feeds
DESCRIPTION: This regular expression is used to identify web feeds, such as RSS and Atom feeds, within HTML content. It targets `<link>` tags with specific `type` or `rel` attributes.

SOURCE: https://trafilatura.readthedocs.io/en/latest/sources

LANGUAGE: regex
CODE:
```
"(<link[^>]*(?:\s(?:type=[\"']?(application\/rss\+xml|application\/atom\+xml|application\/rss|application\/atom|application\/rdf\+xml|application\/rdf|text\/rss\+xml|text\/atom\+xml|text\/rss|text\/atom|text\/rdf\+xml|text\/rdf|text\/xml|application\/xml)[\"']?|rel=[\"']?(?:alternate)[\"']?))[^>]*>)"
```

--------------------------------

TITLE: Handle Text Nodes in Trafilatura
DESCRIPTION: Processes a single text node, cleaning it and potentially converting it to a paragraph tag if it's a 'div'. It also handles text character tests and attribute clearing.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def handle_textnode(element, options, comments_fix=False, preserve_spaces=True):
        """Process a text node, clean it and potentially convert it to a paragraph tag."""
        # make a copy and prune it in case it contains sub-elements handled on their own?
        # divcopy = deepcopy(element)
        processed_element = handle_textnode(element, options, comments_fix=False, preserve_spaces=True)
        if processed_element is not None and text_chars_test(processed_element.text) is True:
            processed_element.attrib.clear()
            # small div-correction # could be moved elsewhere
            if processed_element.tag == "div":
                processed_element.tag = "p"
            # insert
            return processed_element

    return None
```

--------------------------------

TITLE: HTML to Plain Text Conversion
DESCRIPTION: Converts an HTML document or element to plain text. It can optionally clean the HTML before conversion. The function handles potential errors during HTML loading and returns the extracted text or an empty string. Dependencies include load_html and basic_cleaning.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/baseline

LANGUAGE: Python
CODE:
```
def html2txt(content: Any, clean: bool = True) -> str:
    """Run basic html2txt on a document.

    Args:
        content: HTML document as string or LXML element.
        clean: remove potentially undesirable elements.

    Returns:
        The extracted text in the form of a string or an empty string.

    """
    tree = load_html(content)
    if tree is None:
        return ""
    body = tree.find(".//body")
    if body is None:
        return ""
    if clean:
        body = basic_cleaning(body)
    return " ".join(body.text_content().split()).strip()
```

--------------------------------

TITLE: Check for Dubious HTML with Trafilatura
DESCRIPTION: Assesses if a given string represents proper HTML by checking for the presence of 'html' within its beginning. This is a simple heuristic to identify potentially malformed or non-HTML content.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
def is_dubious_html(beginning: str) -> bool:
    """Assess if the object is proper HTML (awith a corresponding tag or declaration)."""
    return "html" not in beginning
```

--------------------------------

TITLE: Move Element Up One Level for TEI Compatibility
DESCRIPTION: This function restructures the XML tree to fix TEI compatibility issues by moving specific p-elements up one level. It handles cases where elements are nested too deeply, ensuring a n+2 nesting for p-elements within the TEI structure.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
def _move_element_one_level_up(element: _Element) -> None:
    """
    Fix TEI compatibility issues by moving certain p-elems up in the XML tree.
    There is always a n+2 nesting for p-elements with the minimal structure ./TEI/text/body/p
    """
    parent = element.getparent()
    grand_parent = parent.getparent() if parent is not None else None
    if parent is None or grand_parent is None:
        return

    new_elem = Element("p")
    new_elem.extend(list(element.itersiblings()))

    grand_parent.insert(grand_parent.index(parent) + 1, element)

    tail = element.tail.strip() if element.tail else None
    if tail:
        new_elem.text = tail
        element.tail = None

    tail = parent.tail.strip() if parent.tail else None
    if tail:
        new_elem.tail = tail
        parent.tail = None

    if len(new_elem) > 0 or new_elem.text or new_elem.tail:
        grand_parent.insert(grand_parent.index(element) + 1, new_elem)

    if len(parent) == 0 and not parent.text:
        grand_parent.remove(parent)
```

--------------------------------

TITLE: Extract text using html2txt - Python
DESCRIPTION: The html2txt function is a last resort for extracting all possible text from HTML content, prioritizing recall over precision. It emulates similar functions in other packages but may not always produce accurate results due to a lack of context consideration.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
from trafilatura import html2txt
html2txt(downloaded)
```

--------------------------------

TITLE: Extract OpenGraph Metadata in Python
DESCRIPTION: This function extracts metadata from meta tags that follow the OpenGraph protocol guidelines. It specifically looks for properties like 'og:title', 'og:description', and 'og:url' to populate a result dictionary.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/metadata

LANGUAGE: Python
CODE:
```
def extract_opengraph(tree: HtmlElement) -> Dict[str, Optional[str]]:
    """Search meta tags following the OpenGraph guidelines (https://ogp.me/)"""
    result = dict.fromkeys(
        ("title", "author", "url", "description", "sitename", "image", "pagetype")
    )

    # detect OpenGraph schema
    for elem in tree.xpath('.//head/meta[starts-with(@property, "og:")]'):
        property_name, content = elem.get("property"), elem.get("content")
        # safeguard
        if content and not content.isspace():
            if property_name in OG_PROPERTIES:
                result[OG_PROPERTIES[property_name]] = content
            elif property_name == "og:url" and is_valid_url(content):
                result["url"] = content
            elif property_name in OG_AUTHOR:
                result["author"] = normalize_authors(None, content)
        # og:locale
        # elif elem.get('property') == 'og:locale':
        #    pagelocale = elem.get('content')
    return result
```

--------------------------------

TITLE: Python: Handle List Elements
DESCRIPTION: Processes list elements (e.g., <ul>, <ol>) and their descendants, extracting 'item' elements. It handles nested lists and text content within list items, preserving 'rend' attributes.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def handle_lists(element: _Element, options: Extractor) -> Optional[_Element]:
    """Process lists elements including their descendants."""
    processed_element = Element(element.tag)

    if element.text is not None and element.text.strip():
        new_child_elem = SubElement(processed_element, "item")
        new_child_elem.text = element.text
    # if element.tail is not None:
    #    processed_element.tail = element.text

    for child in element.iterdescendants("item"):
        new_child_elem = Element("item")
        if len(child) == 0:
            processed_child = process_node(child, options)
            if processed_child is not None:
                new_child_elem.text = processed_child.text or ""
                if processed_child.tail and processed_child.tail.strip():
                    new_child_elem.text += " " + processed_child.tail
                processed_element.append(new_child_elem)
        else:
            process_nested_elements(child, new_child_elem, options)
            if child.tail is not None and child.tail.strip():
                new_child_elem_children = [el for el in new_child_elem if el.tag != "done"]
                if new_child_elem_children:
                    last_subchild = new_child_elem_children[-1]
                    if last_subchild.tail is None or not last_subchild.tail.strip():
                        last_subchild.tail = child.tail
                    else:
                        last_subchild.tail += " " + child.tail
        if new_child_elem.text or len(new_child_elem) > 0:
            update_elem_rendition(child, new_child_elem)
            processed_element.append(new_child_elem)
        child.tag = "done"
    element.tag = "done"
    # test if it has children and text. Avoid double tags??
    if is_text_element(processed_element):
        update_elem_rendition(element, processed_element)
        return processed_element
    return None
```

--------------------------------

TITLE: Trafilatura: Extract Metadata
DESCRIPTION: Extracts metadata (like title, description, keywords) from an HTML document. This function helps in gathering structured information about the web page.

SOURCE: https://trafilatura.readthedocs.io/en/latest/genindex

LANGUAGE: python
CODE:
```
from trafilatura import extract_metadata

# Example usage:
# html_content = "<html><head><title>Page Title</title></head><body></body></html>"
# metadata = extract_metadata(html_content)
```

--------------------------------

TITLE: Trafilatura Utils: Sanitize Text
DESCRIPTION: Sanitizes text content, likely removing unwanted characters, normalizing whitespace, or cleaning up the text for better readability or processing.

SOURCE: https://trafilatura.readthedocs.io/en/latest/genindex

LANGUAGE: python
CODE:
```
from trafilatura.utils import sanitize

# Example usage:
# raw_text = "  Some text with extra   spaces.  "
# clean_text = sanitize(raw_text)
```

--------------------------------

TITLE: Prune HTML Tree with XPath
DESCRIPTION: This snippet demonstrates how to prune unwanted nodes from an HTML tree using XPath expressions provided by the user. It supports single XPath strings or a list of strings and replaces the original tree with the pruned version.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/core

LANGUAGE: Python
CODE:
```
# prune all xpath expressions that user specified
        # no backup as this is unetre full control of the user
        if prune_xpath is not None:
            if isinstance(prune_xpath, str):
                prune_xpath = [prune_xpath]
            tree = prune_unwanted_nodes(tree, [XPath(x) for x in prune_xpath])
```

--------------------------------

TITLE: Validate TEI XML Document with trafilatura.xml
DESCRIPTION: Checks if an XML document conforms to the guidelines of the Text Encoding Initiative (TEI).

SOURCE: https://trafilatura.readthedocs.io/en/latest/corefunctions

LANGUAGE: Python
CODE:
```
trafilatura.xml.validate_tei(_xmldoc : _Element_) → bool
```

--------------------------------

TITLE: Extract Document Title
DESCRIPTION: Extracts the document title by prioritizing a single H1 element, then using XPath expressions, the main title tag, and finally falling back to the first H1 or H2 element.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/metadata

LANGUAGE: Python
CODE:
```
def extract_title(tree: HtmlElement) -> Optional[str]:
    """Extract the document title"""
    h1_results = tree.findall(".//h1")
    if len(h1_results) == 1:
        title = trim(h1_results[0].text_content())
        if title:
            return title
    title = extract_metainfo(tree, TITLE_XPATHS) or ""
    if title:
        return title
    title, first, second = examine_title_element(tree)
    for t in (first, second):
        if t and "." not in t:
            return t
    if h1_results:
        return h1_results[0].text_content()
    try:
        title = tree.xpath(".//h2")[0].text_content()
    except IndexError:
        LOGGER.debug("no h2 title found")
    return title
```

--------------------------------

TITLE: Blacklist Author Names in Python
DESCRIPTION: Filter out content based on author names in Python by passing a blacklist of author names to the relevant Trafilatura function. Refer to the core functions documentation for details.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/url-management

LANGUAGE: Python
CODE:
```
# See documentation <corefunctions.html> for details on blacklisting author names.
```

--------------------------------

TITLE: Sanitize Text with trafilatura.utils
DESCRIPTION: Converts text and discards incompatible and invalid characters. Allows for preserving or discarding trailing whitespace.

SOURCE: https://trafilatura.readthedocs.io/en/latest/corefunctions

LANGUAGE: Python
CODE:
```
trafilatura.utils.sanitize(_text : str_, _preserve_space : bool = False_, _trailing_space : bool = False_) → str | None
```

--------------------------------

TITLE: Reset Trafilatura Caches
DESCRIPTION: Provides the method to reset all cached information within Trafilatura to release memory, which can be crucial for large-scale applications to prevent memory leaks.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
>>> from trafilatura.meta import reset_caches
>>> reset_caches()
```

--------------------------------

TITLE: Trafilatura Utils: Trim Whitespace
DESCRIPTION: Trims leading and trailing whitespace from a string. This is a common text cleaning operation to ensure consistent formatting.

SOURCE: https://trafilatura.readthedocs.io/en/latest/genindex

LANGUAGE: python
CODE:
```
from trafilatura.utils import trim

# Example usage:
# text_with_spaces = "   Trimmed text   "
# trimmed_text = trim(text_with_spaces)
```

--------------------------------

TITLE: Trafilatura Spider: Focused Crawler
DESCRIPTION: Implements a focused crawler, likely designed to navigate and extract data from a specific set of websites or pages based on certain criteria.

SOURCE: https://trafilatura.readthedocs.io/en/latest/genindex

LANGUAGE: python
CODE:
```
from trafilatura.spider import focused_crawler

# Example usage:
# start_urls = ["https://example.com"]
# # ... crawler configuration ...
# # focused_crawler(start_urls, ...)
```

--------------------------------

TITLE: Check Authors Against Blacklist in Python
DESCRIPTION: This function validates author strings against a provided blacklist. It returns a cleaned list of authors, excluding those on the blacklist, or None if no valid authors remain.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/metadata

LANGUAGE: Python
CODE:
```
def check_authors(authors: str, author_blacklist: Set[str]) -> Optional[str]:
    """Check if the authors string correspond to expected values."""
    author_blacklist = {a.lower() for a in author_blacklist}
    new_authors = [
        author.strip()
        for author in authors.split(";")
        if author.strip().lower() not in author_blacklist
    ]
    if new_authors:
        return "; ".join(new_authors).strip("; ")
    return None
```

--------------------------------

TITLE: Generate Simhash Value as Hex String
DESCRIPTION: Utilizes the content_fingerprint function to generate a simhash value for a given string, returning it as a hexadecimal string.

SOURCE: https://trafilatura.readthedocs.io/en/latest/deduplication

LANGUAGE: Python
CODE:
```
from trafilatura.deduplication import content_fingerprint
content_fingerprint("Here is text.")
```

--------------------------------

TITLE: Extract Metadata from JSON-LD in Python
DESCRIPTION: This function parses and extracts metadata from JSON-LD script tags within an HTML document. It handles potential JSON parsing errors and integrates extracted data into a Document object.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/metadata

LANGUAGE: Python
CODE:
```
def extract_meta_json(tree: HtmlElement, metadata: Document) -> Document:
    """Parse and extract metadata from JSON-LD data"""
    for elem in tree.xpath(
        './/script[@type="application/ld+json" or @type="application/settings+json"]'
    ):
        if not elem.text:
            continue
        element_text = normalize_json(JSON_MINIFY.sub(r"\1", elem.text))
        try:
            schema = json.loads(element_text)
            metadata = extract_json(schema, metadata)
        except json.JSONDecodeError:
            metadata = extract_json_parse_error(element_text, metadata)
    return metadata
```

--------------------------------

TITLE: Process HTML Table Rows and Cells
DESCRIPTION: Processes HTML table elements, including rows (`<tr>`), header cells (`<th>`), and data cells (`<td>`). It handles nested elements, attributes like `colspan`, and extracts text content, supporting options for specific extraction modes like 'recall'. The code iterates through table descendants, defines cell types based on whether they are headers, and processes their content, including nested lists and text elements.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def process_table_row(table_elem: _Element, options: Extractor) -> Optional[_Element]:
    max_cols = max(max_cols, sum(int(td.get("colspan", 1)) for td in tr.iter(TABLE_ELEMS)))

    # explore sub-elements
    seen_header_row = False
    seen_header = False
    span_attr = str(max_cols) if max_cols > 1 else ""
    newrow = Element("row")
    if span_attr:
        newrow.set("span", span_attr)

    for subelement in table_elem.iterdescendants():
        if subelement.tag == "tr":
            # process existing row
            if len(newrow) > 0:
                newtable.append(newrow)
                newrow = Element("row")
                if span_attr:
                    newrow.set("span", span_attr)
                seen_header_row = seen_header_row or seen_header
        elif subelement.tag in TABLE_ELEMS:
            is_header = subelement.tag == "th" and not seen_header_row
            seen_header = seen_header or is_header
            new_child_elem = define_cell_type(is_header)
            # process
            if len(subelement) == 0:
                processed_cell = process_node(subelement, options)
                if processed_cell is not None:
                    new_child_elem.text, new_child_elem.tail = processed_cell.text, processed_cell.tail
            else:
                # proceed with iteration, fix for nested elements
                new_child_elem.text, new_child_elem.tail = subelement.text, subelement.tail
                subelement.tag = "done"
                for child in subelement.iterdescendants():
                    if child.tag in TABLE_ALL:
                        # todo: define attributes properly
                        if child.tag in TABLE_ELEMS:
                            # subcell_elem = define_cell_type(is_header)
                            child.tag = "cell"
                        processed_subchild = handle_textnode(child, options, preserve_spaces=True, comments_fix=True)
                    # todo: lists in table cells
                    elif child.tag == "list" and options.focus == "recall":
                        processed_subchild = handle_lists(child, options)
                        if processed_subchild is not None:
                            new_child_elem.append(processed_subchild)
                            processed_subchild = None  # don't handle it anymore
                    else:
                        # subcell_elem = Element(child.tag)
                        processed_subchild = handle_textelem(child, potential_tags.union(["div"]),
                                                              options)
                    # add child element to processed_element
                    if processed_subchild is not None:
                        define_newelem(processed_subchild, new_child_elem)
                    child.tag = "done"
            # add to tree
            if new_child_elem.text or len(new_child_elem) > 0:
                newrow.append(new_child_elem)
        # beware of nested tables
        elif subelement.tag == "table":
            break
        # cleanup
        subelement.tag = "done"

    # clean up row attributes
    newrow.attrib.pop("span", None)

    # end of processing
    if len(newrow) > 0:
        newtable.append(newrow)
    if len(newtable) > 0:
        return newtable
    return None
```

--------------------------------

TITLE: Cite Trafilatura Paper
DESCRIPTION: This snippet provides the BibTeX citation for the Trafilatura paper, which is useful for academic referencing. It includes the title, author, and publication details.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/used-by

LANGUAGE: bibtex
CODE:
```
@inproceedings{barbaresi-2021-trafilatura,
  title = {{Trafilatura: A Web Scraping Library and Command-Line Tool for Text Discovery and Extraction}},
  author = "Barbaresi, Adrien",

```

--------------------------------

TITLE: Disable Table Extraction
DESCRIPTION: Extracts text from a web page while excluding any tables found in the HTML.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
# Example usage (assuming a URL is provided or piped):
# trafilatura --no-tables -u "URL"
```

--------------------------------

TITLE: Process Nested HTML Elements
DESCRIPTION: Iterates through the descendants of an HTML element child and rewires them. Specifically handles 'list' elements by processing them with `handle_lists` and appending the result.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def process_nested_elements(child: _Element, new_child_elem: _Element, options: Extractor) -> None:
    """Iterate through an element child and rewire its descendants."""
    new_child_elem.text = child.text
    for subelem in child.iterdescendants("*"):
        if subelem.tag == "list":
            processed_subchild = handle_lists(subelem, options)
            if processed_subchild is not None:
                new_child_elem.append(processed_subchild)

```

--------------------------------

TITLE: Extract Publication Dates with htmldate
DESCRIPTION: The htmldate component is a Python package designed to extract publication dates from web pages. It is referenced in academic publications, highlighting its utility in web scraping and data extraction tasks.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/used-by

LANGUAGE: shell
CODE:
```
@article{barbaresi-2020-htmldate,
  title = {{htmldate: A Python package to extract publication dates from web pages}},
  author = "Barbaresi, Adrien",
  journal = "Journal of Open Source Software",
  volume = 5,
  number = 51,
  pages = 2439,
  url = {https://doi.org/10.21105/joss.02439},
  publisher = {The Open Journal},
  year = 2020,
}
```

--------------------------------

TITLE: Extract Site Name from Title
DESCRIPTION: Extracts the site name from the main title element of an HTML document. It looks for parts containing a period, typically indicating a domain name.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/metadata

LANGUAGE: Python
CODE:
```
def extract_sitename_from_title(tree: HtmlElement) -> Optional[str]:
    """Extract the name of a site from the main title (if it exists)"""
    _, *parts = examine_title_element(tree)
    return next((part for part in parts if part and "." in part), None)
```

--------------------------------

TITLE: Add XML Metadata
DESCRIPTION: Appends metadata attributes from a Document object to an XML output element if the values are present.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
def add_xml_meta(output: _Element, docmeta: Document) -> None:
    '''Add extracted metadata to the XML output tree'''
    for attribute in META_ATTRIBUTES:
        value = getattr(docmeta, attribute, None)
        if value:
```

--------------------------------

TITLE: Test Duplicate Text Content with LRU Cache (Python)
DESCRIPTION: Checks for duplicate text content within an LXML element using an LRU cache. It evaluates if the text content has been encountered before and how many times, helping to identify repetitive text based on specified criteria like minimum segment size and maximum repetitions.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/deduplication

LANGUAGE: python
CODE:
```
from lxml.etree import fromstring
from trafilatura.deduplication import duplicate_test
from trafilatura.settings import Extractor

options = Extractor()
options.min_duplcheck_size = 0  # even short segments are considered
options.max_repetitions = 0  # no repetition allowed

elem = fromstring("<p>Here is text.</p>")
print(duplicate_test(elem, options))
print(duplicate_test(elem, options))
```

--------------------------------

TITLE: Check target language
DESCRIPTION: Checks if the content of an HTML string matches a target language using a language detection library. It performs a baseline extraction and returns True if the detected language matches the target or if language checks are bypassed.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/spider

LANGUAGE: Python
CODE:
```
def is_target_language(htmlstring: str, language: Optional[str]) -> bool:
    """Run a baseline extraction and use a language detector to
    check if the content matches the target language.
    Return True if language checks are bypassed."""
    if htmlstring and language and LANGID_FLAG:
        _, text, _ = baseline(htmlstring)
        result, _ = py3langid.classify(text)
        return bool(result == language)
    return True
```

--------------------------------

TITLE: Process LXML Element Recursively
DESCRIPTION: Recursively processes an LXML element and its children to generate a flattened string representation. It appends the text content of the element, after potentially formatting it, to a provided list.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
def process_element(element: _Element, returnlist: List[str], include_formatting: bool) -> None:
    """Recursively convert a LXML element and its children to a flattened string representation."""
    if element.text:
        # this is the text that comes before the first child
        returnlist.append(replace_element_text(element, include_formatting))
```

--------------------------------

TITLE: newspaper3k Text Extraction - Python
DESCRIPTION: The newspaper3k Python library is primarily geared towards newspaper texts and offers additional functions, but it does not provide structured text or comment extraction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/evaluation

LANGUAGE: python
CODE:
```
newspaper3k <https://github.com/codelucas/newspaper>`_ is mostly geared towards newspaper texts, provides additional functions but no structured text or comment extraction
```

--------------------------------

TITLE: Trim Whitespace from String with trafilatura.utils
DESCRIPTION: Removes unnecessary spaces within a text string, ensuring cleaner output.

SOURCE: https://trafilatura.readthedocs.io/en/latest/corefunctions

LANGUAGE: Python
CODE:
```
trafilatura.utils.trim(_string : str_) → str
```

--------------------------------

TITLE: Detect Encoding with Trafilatura
DESCRIPTION: Detects the character encoding of a bytestring by first checking for UTF-8 compatibility. It then utilizes external libraries like cchardet and charset_normalizer to guess the encoding, returning a list of potential encodings.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
from typing import List, Optional

# Assuming cchardet_detect is an imported function or None
# Assuming from_bytes is an imported function
# Assuming UNICODE_ALIASES is a defined set of string aliases

def detect_encoding(bytesobject: bytes) -> List[str]:
    """Read all input or first chunk and return a list of encodings"""
    # alternatives: https://github.com/scrapy/w3lib/blob/master/w3lib/encoding.py
    # unicode-test
    if isutf8(bytesobject):
        return ['utf-8']
    guesses = []
    # additional module
    if cchardet_detect is not None:
        cchardet_guess = cchardet_detect(bytesobject)['encoding']
        if cchardet_guess is not None:
            guesses.append(cchardet_guess.lower())
    # try charset_normalizer on first part, fallback on full document
    if len(bytesobject) < 10000:
        detection_results = from_bytes(bytesobject)
    else:
        detection_results = from_bytes(bytesobject[:5000] + bytesobject[-5000:]) or \
                            from_bytes(bytesobject)
    # return alternatives
    if len(detection_results) > 0:
        guesses.extend([r.encoding for r in detection_results])
    # it cannot be utf-8 (tested above)
    return [g for g in guesses if g not in UNICODE_ALIASES]
```

--------------------------------

TITLE: Check HTML Language Attribute
DESCRIPTION: Examines HTML meta-elements and the 'lang' attribute of the 'html' tag to determine if the content matches a target language. Supports strict checking and handles multiple language declarations.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
def check_html_lang(tree: HtmlElement, target_language: str, strict: bool = False) -> bool:
    """Check HTML meta-elements for language information and split
       the result in case there are several languages."""
    for attr in TARGET_LANG_ATTRS:
        elems = tree.findall(f'.//meta[@{attr}][@content]')
        if elems:
            if any(target_language in RE_HTML_LANG.split(elem.get("content", "").lower()) for elem in elems):
                return True
            LOGGER.debug("%s lang attr failed", attr)
            return False

    # HTML lang attribute: sometimes a wrong indication
    if strict:
        elems = tree.xpath("//html[@lang]")
        if elems:
            if any(target_language in RE_HTML_LANG.split(elem.get("lang", "").lower()) for elem in elems):
                return True
            LOGGER.debug("HTML lang failed")
            return False

    LOGGER.debug("No relevant lang elements found")
    return True
```

--------------------------------

TITLE: Guess if text is readable - Python
DESCRIPTION: The is_probably_readerable function, ported from Mozilla's Readability.js, helps guess if a web page likely contains main text content. It is available from version 1.10 onwards.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
from trafilatura.readability_lxml import is_probably_readerable
is_probably_readerable(html)  # HTML string or already parsed tree
```

--------------------------------

TITLE: Trafilatura: Bare Extraction
DESCRIPTION: Performs a basic extraction of text content from HTML. This function is part of the main trafilatura module and is a fundamental operation for content retrieval.

SOURCE: https://trafilatura.readthedocs.io/en/latest/genindex

LANGUAGE: python
CODE:
```
from trafilatura import bare_extraction

# Example usage:
# html_content = "<html><body><p>This is content.</p></body></html>"
# text = bare_extraction(html_content)
```

--------------------------------

TITLE: Trafilatura: Baseline Extraction
DESCRIPTION: Calculates a baseline for text extraction, likely used for comparison or evaluation purposes. This function is also located in the main trafilatura module.

SOURCE: https://trafilatura.readthedocs.io/en/latest/genindex

LANGUAGE: python
CODE:
```
from trafilatura import baseline

# Example usage:
# html_content = "<html><body><p>This is content.</p></body></html>"
# baseline_result = baseline(html_content)
```

--------------------------------

TITLE: Python: Update Element Rendition
DESCRIPTION: Copies the 'rend' attribute from a source element to a target element if it exists. This is useful for preserving styling or rendering information during HTML processing.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def update_elem_rendition(elem: _Element, new_elem: _Element) -> None:
    """Copy the rend attribute from an existing element to a new one."""
    if rend_attr := elem.get("rend"):
        new_elem.set("rend", rend_attr)
```

--------------------------------

TITLE: Validate URL with Courlan (Python)
DESCRIPTION: The `validate_url` function from the `courlan` package checks if a URL conforms to the expected format. It returns a boolean indicating validity and a `ParseResult` object if the URL is valid, helping to prevent errors in subsequent processing.

SOURCE: https://trafilatura.readthedocs.io/en/latest/url-management

LANGUAGE: Python
CODE:
```
from courlan import validate_url

validate_url('http://1234')
validate_url('http://www.example.org/')
```

--------------------------------

TITLE: Validate URL Format with Courlan (Python)
DESCRIPTION: The `validate_url` function checks if a URL conforms to the expected format, returning a boolean indicating validity and a parsed result object if valid.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/url-management

LANGUAGE: python
CODE:
```
from courlan import validate_url

validate_url('http://1234')
# (False, None)
validate_url('http://www.example.org/')
# (True, ParseResult(scheme='http', netloc='www.example.org', path='/', params='', query='', fragment=''))
```

--------------------------------

TITLE: Handle Titles in HTML Elements
DESCRIPTION: Processes head elements (titles) in an HTML document. It extracts text from the title element, cleans it, and returns it as a processed element. Handles cases with no children and processes child nodes recursively.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
from .htmlprocessing import (
    delete_by_link_density,
    handle_textnode,
    link_density_test_tables,
    process_node,
    prune_unwanted_nodes
)
from .settings import TAG_CATALOG, Extractor
from .utils import FORMATTING_PROTECTED, is_image_file, text_chars_test, trim
from .xml import delete_element
from .xpaths import (
    BODY_XPATH,
    COMMENTS_DISCARD_XPATH,
    COMMENTS_XPATH,
    DISCARD_IMAGE_ELEMENTS,
    OVERALL_DISCARD_XPATH,
    PRECISION_DISCARD_XPATH,
    TEASER_DISCARD_XPATH
)


LOGGER = logging.getLogger(__name__)

P_FORMATTING = {'hi', 'ref'}
TABLE_ELEMS = {'td', 'th'}
TABLE_ALL = {'td', 'th', 'hi'}
FORMATTING = {'hi', 'ref', 'span'}
CODES_QUOTES = {'code', 'quote'}
NOT_AT_THE_END = {'head', 'ref'}


def _log_event(msg: str, tag: Any, text: Optional[Union[bytes, str]]) -> None:
    """Format extraction event for debugging purposes."""
    LOGGER.debug("%s: %s %s", msg, tag, trim(text or "") or "None")


def handle_titles(element: _Element, options: Extractor) -> Optional[_Element]:
    """Process head elements (titles)"""
    if len(element) == 0:
        # maybe needs attention?
        # if element.tail and re.search(r'\w', element.tail):
        #    LOGGER.debug('tail in title, stripping: %s', element.tail)
        #    element.tail = None
        title = process_node(element, options)
    # children
    else:
        title = deepcopy(element)
        # list instead of element.iter('*')
        # TODO: write tests for it and check
        for child in list(element):
            # if child.tag not in potential_tags:
            #    LOGGER.debug('unexpected in title: %s %s %s', child.tag, child.text, child.tail)
            #    continue
            processed_child = handle_textnode(child, options, comments_fix=False)
            if processed_child is not None:
                title.append(processed_child)
            child.tag = 'done'
    if title is not None and text_chars_test(''.join(title.itertext())) is True:
        return title
    return None

```

--------------------------------

TITLE: Newspaper Text Extraction - newspaper3k
DESCRIPTION: The newspaper3k Python library is primarily designed for newspaper texts. It offers additional functions but does not provide structured text or comment extraction.

SOURCE: https://trafilatura.readthedocs.io/en/latest/evaluation

LANGUAGE: python
CODE:
```
from newspaper import Article

article = Article(url)
article.download()
article.parse()

title = article.title
text = article.text
```

--------------------------------

TITLE: Normalize Tags in Python
DESCRIPTION: This function cleans and normalizes tag strings by removing special characters and extra whitespace. It's useful for preparing tag data for consistent processing.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/metadata

LANGUAGE: Python
CODE:
```
def normalize_tags(tags: str) -> str:
    """Remove special characters of tags"""
    trimmed = trim(unescape(tags))
    if not trimmed:
        return ""
    tags = CLEAN_META_TAGS.sub(r"", trimmed)
    return ", ".join(filter(None, tags.split(", ")))
```

--------------------------------

TITLE: Trafilatura: HTML to Text Conversion
DESCRIPTION: Converts HTML content into plain text. This function is useful for stripping HTML tags and extracting only the readable text.

SOURCE: https://trafilatura.readthedocs.io/en/latest/genindex

LANGUAGE: python
CODE:
```
from trafilatura import html2txt

# Example usage:
# html_content = "<html><body><p>Text with <b>bold</b>.</p></body></html>"
# plain_text = html2txt(html_content)
```

--------------------------------

TITLE: Find Links in Feed String
DESCRIPTION: Tries different feed types (JSON, Atom, RSS) and returns the corresponding links extracted from the feed string. It handles JSON decoding errors and extracts links based on the feed format.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/feeds

LANGUAGE: Python
CODE:
```
def find_links(feed_string: str, params: FeedParameters) -> List[str]:
    "Try different feed types and return the corresponding links."
    if not is_potential_feed(feed_string):
        # JSON
        if feed_string.startswith("{"):
            try:
                # fallback: https://www.jsonfeed.org/version/1.1/
                candidates = [
                    item.get("url") or item.get("id")
                    for item in json.loads(feed_string).get("items", [])
                ]
                return [c for c in candidates if c is not None]
            except json.decoder.JSONDecodeError:
                LOGGER.debug("JSON decoding error: %s", params.domain)
        else:
            LOGGER.debug("Possibly invalid feed: %s", params.domain)
        return []

    # Atom
    if "<link " in feed_string:
        return [
            LINK_HREF.search(link)[1]  # type: ignore[index]
            for link in (
                m[0] for m in islice(LINK_ATTRS.finditer(feed_string), MAX_LINKS)
            )
            if "atom+xml" not in link and 'rel="self"' not in link
        ]
        # if '"' in feedlink:
        #    feedlink = feedlink.split('"')[0]

    # RSS
    if "<link>" in feed_string:
        return [
            m[1].strip()
            for m in islice(LINK_ELEMENTS.finditer(feed_string, re.DOTALL), MAX_LINKS)
        ]

    return []
```

--------------------------------

TITLE: Python: Extract URLs from Tweets using Regular Expressions
DESCRIPTION: This Python code snippet shows how to extract URLs from tweet text using a regular expression. It uses `re.findall` to find all occurrences of the URL pattern. The extracted URLs may need to be resolved to their final destinations, especially if they are shortened.

SOURCE: https://trafilatura.readthedocs.io/en/latest/sources

LANGUAGE: Python
CODE:
```
re.findall(r'https?://[^ ]+')
```

--------------------------------

TITLE: Check if String is Potential Feed
DESCRIPTION: Checks if a given string could potentially be a web feed by looking for common feed opening tags (e.g., <feed, <rss, <?xml). Returns True if a potential feed is detected, False otherwise.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/feeds

LANGUAGE: Python
CODE:
```
def is_potential_feed(feed_string: str) -> bool:
    "Check if the string could be a feed."
    if FEED_OPENING.match(feed_string):
        return True
    beginning = feed_string[:100]
    return "<rss" in beginning or "<feed" in beginning
```

--------------------------------

TITLE: Process Line for Sanitization
DESCRIPTION: Processes a single line of text by removing HTML space entities, incompatible Unicode, and invalid XML characters. It can optionally preserve whitespace and trailing spaces.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
@lru_cache(maxsize=1024)
def line_processing(line: str, preserve_space: bool = False, trailing_space: bool = False) -> Optional[str]:
    '''Remove HTML space entities, then discard incompatible unicode
       and invalid XML characters on line level'''
    # spacing HTML entities: https://www.w3.org/MarkUp/html-spec/html-spec_13.html
    # unique code spaces
    new_line = remove_control_characters(line.replace('&#13;', '\r').replace('&#10;', '\n').replace('&nbsp;', '\u00A0'))
    if not preserve_space:
        # remove newlines that are not related to punctuation or markup
        # remove non-printable chars and normalize space characters (including Unicode spaces)
        new_line = trim(LINES_TRIMMING.sub(r" ", new_line))
        # prune empty lines
        if all(map(str.isspace, new_line)):
            new_line = None  # type: ignore[assignment]
        elif trailing_space:
            space_before = " " if line[0].isspace() else ""
            space_after = " " if line[-1].isspace() else ""
            new_line = "".join([space_before, new_line, space_after])
    return new_line
```

--------------------------------

TITLE: Extract Comments from HTML
DESCRIPTION: Extracts comments from potential comment sections in an HTML document. It iterates through predefined XPath expressions, prunes unwanted nodes, strips specific tags like 'a', 'ref', and 'span', and processes found comment elements. Dependencies include `lxml` and a custom `Extractor` class.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def extract_comments(tree: HtmlElement, options: Extractor) -> Tuple[_Element, str, int, HtmlElement]:
    """Try to extract comments out of potential sections in the HTML."""
    comments_body = Element("body")
    # define iteration strategy
    potential_tags = set(TAG_CATALOG)  # 'span'
    # potential_tags.add('div') trouble with <div class="comment-author meta">
    for expr in COMMENTS_XPATH:
        # select tree if the expression has been found
        subtree = next((s for s in expr(tree) if s is not None), None)
        if subtree is None:
            continue
        # prune
        subtree = prune_unwanted_nodes(subtree, COMMENTS_DISCARD_XPATH)
        # todo: unified stripping function, taking include_links into account
        strip_tags(subtree, "a", "ref", "span")
        # extract content
        # for elem in subtree.xpath('.//*'):
        #    processed_elem = process_comments_node(elem, potential_tags)
        #    if processed_elem is not None:
        #        comments_body.append(processed_elem)
        # processed_elems = (process_comments_node(elem, potential_tags, options) for elem in
        #                    subtree.xpath('.//*'))
        comments_body.extend(filter(lambda x: x is not None, (process_comments_node(e, potential_tags, options) for e in subtree.xpath(".//*"))))  # type: ignore[arg-type]
        # control
        if len(comments_body) > 0:  # if it has children
            LOGGER.debug(expr)
            # remove corresponding subtree
            delete_element(subtree, keep_tail=False)
            break
    # lengths
    temp_comments = " ".join(comments_body.itertext()).strip()
    return comments_body, temp_comments, len(temp_comments), tree
```

--------------------------------

TITLE: Strip Double Tags
DESCRIPTION: Prevents nested tags for a predefined list of tags (head, code, p) by merging duplicate nested tags if they are not in a whitelist.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
def strip_double_tags(tree: _Element) -> _Element:
    """Prevent nested tags among a fixed list of tags."""
    for elem in reversed(tree.xpath(".//head | .//code | .//p")):
        for subelem in elem.iterdescendants("code", "head", "p"):
            if subelem.tag == elem.tag and subelem.getparent().tag not in NESTING_WHITELIST:
                merge_with_parent(subelem)
    return tree
```

--------------------------------

TITLE: Remove Empty HTML Elements
DESCRIPTION: Iterates through an HTML tree and removes elements that are empty (no children, text, or tail text). Excludes elements within 'code' tags and 'graphic' tags.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
def remove_empty_elements(tree: _Element) -> _Element:
    '''Remove text elements without text.'''
    for element in tree.iter('*'):  # 'head', 'hi', 'item', 'p'
        if len(element) == 0 and text_chars_test(element.text) is False and text_chars_test(element.tail) is False:
            parent = element.getparent()
            # not root element or element which is naturally empty
            # do not remove elements inside <code> to preserve formatting
            if parent is not None and element.tag != "graphic" and parent.tag != 'code':
                parent.remove(element)
    return tree
```

--------------------------------

TITLE: Clean HTML Attributes
DESCRIPTION: Removes all attributes from HTML elements that are not explicitly allowed in the WITH_ATTRIBUTES list.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
def clean_attributes(tree: _Element) -> _Element:
    '''Remove unnecessary attributes.'''
    for elem in tree.iter('*'):
        if elem.tag not in WITH_ATTRIBUTES:
            elem.attrib.clear()
    return tree
```

--------------------------------

TITLE: Merge Element with Parent
DESCRIPTION: Merges an element's text content with its parent, optionally converting formatting to markdown. The element is then removed from the tree.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
def merge_with_parent(element: _Element, include_formatting: bool = False) -> None:
    '''Merge element with its parent and convert formatting to markdown.'''
    parent = element.getparent()
    if parent is None:
        return

    full_text = replace_element_text(element, include_formatting)
    if element.tail is not None:
        full_text += element.tail

    previous = element.getprevious()
    if previous is not None:
        # There is a previous node, append text to its tail
        previous.tail = f'{previous.tail} {full_text}' if previous.tail else full_text
    elif parent.text is not None:
        parent.text = f'{parent.text} {full_text}'
    else:
        parent.text = full_text
    parent.remove(element)
```

--------------------------------

TITLE: Python: Check if Element is Code Block
DESCRIPTION: Identifies if an element represents a code block based on common HTML attributes and structures, such as 'lang' attribute, 'code' tag, or parent class 'highlight'.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def is_code_block_element(element: _Element) -> bool:
    """Check if it is a code element according to common structural markers."""
    # pip
    if element.get("lang") or element.tag == "code":
        return True
    # GitHub
    parent = element.getparent()
    if parent is not None and "highlight" in parent.get("class", ""):
        return True
    # highlightjs
    code = element.find("code")
    if code is not None and len(element) == 1:
        return True
    return False
```

--------------------------------

TITLE: Check if Element is Image
DESCRIPTION: Determines if an HTML element is a valid image by checking for 'data-src' or 'src' attributes that point to image files. It iterates through attributes to find potential image sources.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
def is_image_element(element: _Element) -> bool:
    '''Check if an element is a valid img element'''
    for attr in ("data-src", "src"):
        src = element.get(attr, "")
        if is_image_file(src):
            return True
    else:
        # take the first corresponding attribute
        for attr, value in element.attrib.items():
            if attr.startswith("data-src") and is_image_file(value):
                return True
    return False
```

--------------------------------

TITLE: Filter Text by Language
DESCRIPTION: Filters text based on language detection results. It uses `language_classifier` to determine the language and compares it with the target language, logging a warning if they don't match.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
def language_filter(temp_text: str, temp_comments: str, target_language: str, docmeta: Any) -> Tuple[bool, Any]:
    '''Filter text based on language detection and store relevant information'''
    # todo: run and pass info along anyway?
    if target_language is not None:
        # more thorough: detection on actual text content
        docmeta.language = language_classifier(temp_text, temp_comments)
        # HTML lang check? sometimes contradicted by detection above
        #if docmeta.language is None:
        #    if check_html_lang(tree, target_language) is False:
        #        LOGGER.error('wrong HTML meta language for URL %s', url)
        #        raise ValueError
        if docmeta.language is not None and docmeta.language != target_language:
            LOGGER.warning('wrong language: %s %s', docmeta.language, docmeta.url)
            return True, docmeta
    return False, docmeta
```

--------------------------------

TITLE: Test String for Text Characters
DESCRIPTION: Determines if a string contains actual text characters, excluding strings composed solely of spaces or control characters. Returns true if the string is non-empty and not just whitespace.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
def text_chars_test(string: Optional[str]) -> bool:
    '''Determine if a string is only composed of spaces and/or control characters'''
    # or not re.search(r'\w', string)
    # return string is not None and len(string) != 0 and not string.isspace()
    return bool(string) and not string.isspace()  # type: ignore[union-attr]
```

--------------------------------

TITLE: Trafilatura XML: XML to Text Conversion
DESCRIPTION: Converts XML content into plain text. This function is useful for extracting textual data from structured XML documents.

SOURCE: https://trafilatura.readthedocs.io/en/latest/genindex

LANGUAGE: python
CODE:
```
from trafilatura.xml import xmltotxt

# Example usage:
# xml_content = "<root><item>Text</item></root>"
# plain_text = xmltotxt(xml_content)
```

--------------------------------

TITLE: Extract Comments with Trafilatura
DESCRIPTION: Extracts comments from web pages. This function specifically targets and retrieves comment sections within the HTML structure.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/corefunctions

LANGUAGE: Python
CODE:
```
from trafilatura.core import extract_comments

# Example usage:
# html = "..."
# comments = extract_comments(html)

```

--------------------------------

TITLE: Detect UTF-8 Encoding with Trafilatura
DESCRIPTION: Provides a simple heuristic to determine if a bytestring uses the standard UTF-8 encoding. It attempts to decode the bytestring and returns True if successful, False otherwise.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
def isutf8(data: bytes) -> bool:
    """Simple heuristic to determine if a bytestring uses standard unicode encoding"""
    try:
        data.decode('UTF-8')
    except UnicodeDecodeError:
        return False
    return True
```

--------------------------------

TITLE: Prune Unwanted Sections in Trafilatura
DESCRIPTION: The `prune_unwanted_sections` function implements rule-based deletion of targeted document sections within an HTML tree. It removes unwanted nodes based on XPath expressions, handles image discarding, balances precision and recall, and iteratively prunes elements based on link density.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def prune_unwanted_sections(tree: HtmlElement, potential_tags: Set[str], options: Extractor) -> HtmlElement:
    'Rule-based deletion of targeted document sections'
    favor_precision = options.focus == "precision"
    # prune the rest
    tree = prune_unwanted_nodes(tree, OVERALL_DISCARD_XPATH, with_backup=True)
    # decide if images are preserved
    if 'graphic' not in potential_tags:
        tree = prune_unwanted_nodes(tree, DISCARD_IMAGE_ELEMENTS)
    # balance precision/recall
    if options.focus != "recall":
        tree = prune_unwanted_nodes(tree, TEASER_DISCARD_XPATH)
        if favor_precision:
            tree = prune_unwanted_nodes(tree, PRECISION_DISCARD_XPATH)
    # remove elements by link density, several passes
    for _ in range(2):
        tree = delete_by_link_density(tree, 'div', backtracking=True, favor_precision=favor_precision)
        tree = delete_by_link_density(tree, 'list', backtracking=False, favor_precision=favor_precision)
        tree = delete_by_link_density(tree, 'p', backtracking=False, favor_precision=favor_precision)
    # tables
    if 'table' in potential_tags or favor_precision:
        # tree = delete_by_link_density(tree, 'table', backtracking=False, favor_precision=favor_precision)
        for elem in tree.iter('table'):
            if link_density_test_tables(elem) is True:
                delete_element(elem, keep_tail=False)
    # also filter fw/head, table and quote elements?
    if favor_precision:
        # delete trailing titles
        while len(tree) > 0 and (tree[-1].tag == 'head'):
            delete_element(tree[-1], keep_tail=False)
        tree = delete_by_link_density(tree, 'head', backtracking=False, favor_precision=True)
        tree = delete_by_link_density(tree, 'quote', backtracking=False, favor_precision=True)
    return tree
```

--------------------------------

TITLE: Sanitize Text
DESCRIPTION: Sanitizes a given text string by processing it line by line using `line_processing`. It handles the removal of control characters and normalization of Unicode, with options to preserve space and trailing spaces.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
def sanitize(text: str, preserve_space: bool = False, trailing_space: bool = False) -> Optional[str]:
    '''Convert text and discard incompatible and invalid characters'''
    # consider all text as a single line
    if trailing_space:
        return line_processing(text, preserve_space, True)
    # process line by line
    try:
        return '\n'.join(filter(None, (line_processing(l, preserve_space) for l in text.splitlines()))).replace('\u2424', '')
    except AttributeError:
        return None
```

--------------------------------

TITLE: Normalize Unicode
DESCRIPTION: Normalizes a given string to a specified Unicode format (NFC, NFD, NFKC, NFKD) to ensure consistent character representation.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
def normalize_unicode(string: str, unicodeform: Literal['NFC', 'NFD', 'NFKC', 'NFKD'] = 'NFC') -> str:
    'Normalize the given string to the specified unicode format.'
    return normalize(unicodeform, string)
```

--------------------------------

TITLE: Sanitize HTML Tree
DESCRIPTION: The `sanitize_tree` function performs post-processing on an HTML tree obtained from a generic extraction algorithm. It includes cleaning the tree, optionally stripping anchor tags, converting specific table-related tags (tr, td, th) to custom tags (row, cell), and sanitizing the tree by removing tags not present in a predefined list of valid tags (TEI_VALID_TAGS). Finally, it returns the cleaned tree, the extracted text, and its length.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/external

LANGUAGE: Python
CODE:
```
def sanitize_tree(tree: HtmlElement, options: Any) -> Tuple[HtmlElement, str, int]:
    '''Convert and sanitize the output from the generic algorithm (post-processing)'''
    # 1. clean
    cleaned_tree = tree_cleaning(tree, options)
    if options.links is False:
        strip_tags(cleaned_tree, 'a')
    strip_tags(cleaned_tree, 'span')
    # 2. convert
    cleaned_tree = convert_tags(cleaned_tree, options)
    for elem in cleaned_tree.iter('td', 'th', 'tr'):
        # elem.text, elem.tail = trim(elem.text), trim(elem.tail)
        # finish table conversion
        if elem.tag == 'tr':
            elem.tag = 'row'
        elif elem.tag in ('td', 'th'):
            if elem.tag == 'th':
                elem.set('role', 'head')
            elem.tag = 'cell'
    # 3. sanitize
    sanitization_list = [
        tagname
        for tagname in [element.tag for element in set(cleaned_tree.iter('*'))]
        if tagname not in TEI_VALID_TAGS
    ]
    strip_tags(cleaned_tree, *sanitization_list)
    # 4. return
    text = trim(' '.join(cleaned_tree.itertext()))
    return cleaned_tree, text, len(text)
```

--------------------------------

TITLE: Basic Cleaning of HTML Elements
DESCRIPTION: Removes specific section types from an HTML document using predefined XPath expressions. It takes an HtmlElement as input and returns the modified HtmlElement. Dependencies include lxml.etree and lxml.html.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/baseline

LANGUAGE: Python
CODE:
```
import json

from typing import Any, Tuple

from lxml.etree import _Element, Element, SubElement
from lxml.html import HtmlElement

from .settings import BASIC_CLEAN_XPATH
from .utils import load_html, trim
from .xml import delete_element


def basic_cleaning(tree: HtmlElement) -> HtmlElement:
    """Remove a few section types from the document."""
    for elem in BASIC_CLEAN_XPATH(tree):
        delete_element(elem)
    return tree
```

--------------------------------

TITLE: Extract Comments from HTML
DESCRIPTION: The `extract_comments` function is designed to extract comments from specific sections within an HTML document. It requires a parsed HTML tree and extractor options.

SOURCE: https://trafilatura.readthedocs.io/en/latest/corefunctions

LANGUAGE: python
CODE:
```
from trafilatura.core import extract_comments

# Example usage:
# comments = extract_comments(html_tree, extractor_options)
```

--------------------------------

TITLE: Add Sub-Element to HTML Element
DESCRIPTION: Appends a processed sub-child element to a new child element, copying its text, tail, and attributes. This is used for restructuring HTML content.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def add_sub_element(new_child_elem: _Element, subelem: _Element, processed_subchild: _Element) -> None:
    """Add a sub-element to an existing child element."""
    sub_child_elem = SubElement(new_child_elem, processed_subchild.tag)
    sub_child_elem.text, sub_child_elem.tail = processed_subchild.text, processed_subchild.tail
    for attr in subelem.attrib:
        sub_child_elem.set(attr, subelem.attrib[attr])

```

--------------------------------

TITLE: Sanitize HTML Tree Elements
DESCRIPTION: Iterates through an lxml HTML tree, sanitizing the text content of each element. It removes invalid attributes, control characters, and normalizes Unicode, while respecting specified whitespace preservation rules.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
def sanitize_tree(tree: _Element) -> _Element:
    '''Trims spaces, removes control characters and normalizes unicode'''
    for elem in tree.iter():
        parent = elem.getparent()
        parent_tag = parent.tag if parent is not None else ""

        # preserve space if the element or its parent is a specific tag, or if the element has text and children
        # the last part is relevant for item elements with ref inside for example
        preserve_space = elem.tag in SPACING_PROTECTED or parent_tag in SPACING_PROTECTED
        trailing_space = elem.tag in FORMATTING_PROTECTED or parent_tag in FORMATTING_PROTECTED or preserve_space

        # remove invalid attributes
        for attribute in elem.attrib:
            if ':' in attribute:  # colon is reserved for namespaces in XML
                if not elem.attrib[attribute] or attribute.split(':', 1)[0] not in tree.nsmap:
                    elem.attrib.pop(attribute)

        if elem.text:
            elem.text = sanitize(elem.text, preserve_space, trailing_space)
```

--------------------------------

TITLE: Trafilatura XML: Validate TEI
DESCRIPTION: Validates XML content against the Text Encoding Initiative (TEI) schema. This function is used for ensuring the correctness and structure of TEI-formatted data.

SOURCE: https://trafilatura.readthedocs.io/en/latest/genindex

LANGUAGE: python
CODE:
```
from trafilatura.xml import validate_tei

# Example usage:
# tei_xml_content = "<TEI>...</TEI>"
# # is_valid = validate_tei(tei_xml_content)
```

--------------------------------

TITLE: Trafilatura: Extract Main Content
DESCRIPTION: Extracts the main textual content from a given HTML document. This is a core function of the library, designed to isolate significant text from boilerplate.

SOURCE: https://trafilatura.readthedocs.io/en/latest/genindex

LANGUAGE: python
CODE:
```
from trafilatura import extract

# Example usage:
# html_content = "<html><body><h1>Title</h1><p>Main content.</p></body></html>"
# text = extract(html_content)
```

--------------------------------

TITLE: Extract Document Author(s)
DESCRIPTION: Extracts the author(s) of a document by first pruning unwanted nodes from the HTML tree and then using XPath expressions to find author information. It also normalizes the extracted author data.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/metadata

LANGUAGE: Python
CODE:
```
def extract_author(tree: HtmlElement) -> Optional[str]:
    """Extract the document author(s)"""
    subtree = prune_unwanted_nodes(deepcopy(tree), AUTHOR_DISCARD_XPATHS)
    author = extract_metainfo(subtree, AUTHOR_XPATHS, len_limit=120)
    if author:
        author = normalize_authors(None, author)
    return author
```

--------------------------------

TITLE: Process Comment Nodes
DESCRIPTION: Processes individual comment nodes within an HTML tree. It checks if the element's tag is in the set of potential comment tags and handles text nodes, potentially filtering them based on content or length. Returns a processed element or None.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def process_comments_node(elem: _Element, potential_tags: Set[str], options: Extractor) -> Optional[_Element]:
    '''Process comment node and determine how to deal with its content'''
    if elem.tag in potential_tags:
        # print(elem.tag, elem.text_content())
        processed_element = handle_textnode(elem, options, comments_fix=True)
        # test length and remove
        if processed_element is not None:  # and processed_element.text not in COMMENTS_BLACKLIST:
            processed_element.attrib.clear()
            # if textfilter(elem) is True:  # ^Pingback
            #    return None
            return processed_element
    return None
```

--------------------------------

TITLE: Insert New Sibling Element in XML
DESCRIPTION: This function iterates through siblings of a given div element to find and group specific TEI sibling elements. It inserts a new div element containing these siblings after the target element, maintaining the original order.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
new_sibling = Element("div")
new_sibling_index = None
parent = div_element.getparent()
if parent is None:
    return
# check siblings after target element
for sibling in div_element.itersiblings():
    if sibling.tag == "div":
        break
    if sibling.tag in TEI_DIV_SIBLINGS:
        new_sibling_index = new_sibling_index or parent.index(sibling)
        new_sibling.append(sibling)
    # some elements (e.g. <lb/>) can appear next to div, but
    # order of elements should be kept, thus add and reset new_sibling
    else:
        if new_sibling_index and len(new_sibling) > 0:
            parent.insert(new_sibling_index, new_sibling)
            new_sibling = Element("div")
            new_sibling_index = None
if new_sibling_index and len(new_sibling) != 0:
    parent.insert(new_sibling_index, new_sibling)
```

--------------------------------

TITLE: Wrap Siblings of TEI Div Elements (Python)
DESCRIPTION: This Python function is designed to wrap unwanted sibling elements of a TEI `<div>` element within a new `<div>` element, likely for structural or formatting purposes within TEI XML.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
from lxml.etree import Element, _Element

def _wrap_unwanted_siblings_of_div(div_element: _Element) -> None:
    """Wrap unwanted siblings of a div element in a new div element."""
    # Implementation details would follow here, operating on div_element and its siblings.
    pass

```

--------------------------------

TITLE: Python: Exclude comments during extraction
DESCRIPTION: Illustrates how to configure the `extract` function to ignore comment sections within the HTML content, focusing the extraction on the main article text.

SOURCE: https://trafilatura.readthedocs.io/en/latest/usage-python

LANGUAGE: Python
CODE:
```
>>> result = extract(downloaded, include_comments=False)
```

--------------------------------

TITLE: Exclude Comments from Extraction
DESCRIPTION: Illustrates how to use the 'extract' function while excluding comment sections from the extracted text by setting 'include_comments' to False.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-python

LANGUAGE: python
CODE:
```
>>> result = extract(downloaded, include_comments=False)
```

--------------------------------

TITLE: Define Feed Types
DESCRIPTION: Defines a set of common MIME types associated with web feeds (Atom, RSS, JSON). This set is used to identify potential feed documents based on their content type.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/feeds

LANGUAGE: Python
CODE:
```
FEED_TYPES = {
    "application/atom",  # not IANA-compatible
    "application/atom+xml",
    "application/feed+json",  # not IANA-compatible
    "application/json",
    "application/rdf",  # not IANA-compatible
    "application/rdf+xml",
    "application/rss",  # not IANA-compatible
    "application/rss+xml",
    "application/x.atom+xml",  # not IANA-compatible
    "application/x-atom+xml",  # not IANA-compatible
    "application/xml",
    "text/atom",  # not IANA-compatible
    "text/atom+xml",
    "text/plain",
    "text/rdf",  # not IANA-compatible
    "text/rdf+xml",
    "text/rss",  # not IANA-compatible
    "text/rss+xml",
    "text/xml",
}
```

--------------------------------

TITLE: Trim Whitespace from String
DESCRIPTION: Removes unnecessary spaces within a text string, including extra newlines and leading/trailing whitespace. Handles potential errors by returning an empty string if the input is not a string.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
@lru_cache(maxsize=1024)
def trim(string: str) -> str:
    """Remove unnecessary spaces within a text string."""
    try:
        # remove newlines that are not related to punctuation or markup + proper trimming
        return " ".join(string.split()).strip()
    except (AttributeError, TypeError):
        return ""
```

--------------------------------

TITLE: Delete HTML Element
DESCRIPTION: Removes an HTML element and its children from the tree. Optionally preserves tail text by appending it to the previous element or parent.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/xml

LANGUAGE: Python
CODE:
```
def delete_element(element: _Element, keep_tail: bool = True) -> None:
    """
    Removes this element from the tree, including its children and
    text. The tail text is joined to the previous element or parent.
    """
    parent = element.getparent()
    if parent is None:
        return

    if keep_tail and element.tail:
        previous = element.getprevious()
        if previous is None:
            parent.text = (parent.text or "") + element.tail
        else:
            previous.tail = (previous.tail or "") + element.tail

    parent.remove(element)
```

--------------------------------

TITLE: Disable Comment Extraction
DESCRIPTION: Extracts text from a web page while excluding any comments found in the HTML.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_sources/usage-cli

LANGUAGE: bash
CODE:
```
# Example usage (assuming a URL is provided or piped):
# trafilatura --no-comments -u "URL"
```

--------------------------------

TITLE: Trafilatura Core: Extract Comments
DESCRIPTION: Extracts comments from an HTML document. This function is part of the core functionality and is useful for analyzing or processing comments separately.

SOURCE: https://trafilatura.readthedocs.io/en/latest/genindex

LANGUAGE: python
CODE:
```
from trafilatura.core import extract_comments

# Example usage:
# html_content = "<html><body><!-- This is a comment --></body></html>"
# comments = extract_comments(html_content)
```

--------------------------------

TITLE: Classify Text Language
DESCRIPTION: Identifies the language of a given text using an external component (`py3langid`). It compares the lengths of the main text and comments to decide which to analyze for better accuracy.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
def language_classifier(temp_text: str, temp_comments: str) -> Optional[str]:
    '''Run external component (if installed) for language identification'''
    if LANGID_FLAG is True:
        result, _ = (
            py3langid.classify(temp_text)
            if len(temp_text) > len(temp_comments)
            else py3langid.classify(temp_comments)
        )
    else:  # pragma: no cover
        LOGGER.warning('Language detector not installed, skipping detection')
        result = None
    return result  # type: ignore[no-any-return]
```

--------------------------------

TITLE: Check if String is Image File
DESCRIPTION: Validates if a given string corresponds to a valid image file extension using a regular expression. It also includes a length check to filter out excessively long strings.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
def is_image_file(imagesrc: Optional[str]) -> bool:
    '''Check if the observed string corresponds to a valid image extension.
       Use a length threshold and apply a regex on the content.'''
    if imagesrc is None or len(imagesrc) > 8192:
        return False
    return bool(IMAGE_EXTENSION.search(imagesrc))
```

--------------------------------

TITLE: Python: Check if Element Contains Text
DESCRIPTION: Determines if an XML/HTML element contains any significant text content. It joins all text nodes within the element and checks if they pass a character test, ignoring whitespace.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def is_text_element(elem: _Element) -> bool:
    """Find if the element contains text."""
    return elem is not None and text_chars_test(''.join(elem.itertext())) is True
```

--------------------------------

TITLE: Remove Control Characters
DESCRIPTION: Removes non-printable and XML invalid characters from a string to prevent errors during processing. It maps characters to their printable or space equivalents.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
@lru_cache(maxsize=2**14)  # sys.maxunicode = 1114111
def return_printables_and_spaces(char: str) -> str:
    'Return a character if it belongs to certain classes'
    return char if char.isprintable() or char.isspace() else ''

def remove_control_characters(string: str) -> str:
    '''Prevent non-printable and XML invalid character errors'''
    return ''.join(map(return_printables_and_spaces, string))
```

--------------------------------

TITLE: Define Cell Type in Trafilatura
DESCRIPTION: Determines the type of a table cell element ('cell') and sets its 'role' attribute to 'head' if it's a header cell.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/main_extractor

LANGUAGE: Python
CODE:
```
def define_cell_type(is_header: bool) -> _Element:
    """Determine cell element type and mint new element."""
    # define tag
    cell_element = Element("cell")
    if is_header:
        cell_element.set("role", "head")
    return cell_element
```

--------------------------------

TITLE: Filter Unwanted Text
DESCRIPTION: Filters out text elements that are considered unwanted, such as empty strings, strings containing only whitespace, or lines that match a specific filter pattern.

SOURCE: https://trafilatura.readthedocs.io/en/latest/_modules/trafilatura/utils

LANGUAGE: Python
CODE:
```
def textfilter(element: _Element) -> bool:
    '''Filter out unwanted text'''
    testtext = element.tail if element.text is None else element.text
    # to check: line len → continue if len(line) <= 5
    return not testtext or testtext.isspace() or any(map(RE_FILTER.match, testtext.splitlines()))
```