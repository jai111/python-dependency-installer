# **Python Dependency installer**

<br />

## **Local installation**

> ```sh
> git clone https://github.com/jai111/python-dependency-installer.git
> cd python-dependency-installer
> sudo python setup.py install
> ```

_Above steps will install **jb** systemwide._

<hr/>

## **Usage**

- Dependency file should be a valid JSON file
  e.g:

  ```json
  {
    "dependencies": {
      "beautifulsoup4": "4.4.1"
    }
  }
  ```

- Validate dependency File<br />
  **Usage:**

  ```shell
  jb validate ./dependecy.json
  ```

  **OPTIONS:**<br />
  **--help** : for help

- Install dependencies from a json file
  **Usage:**

  ```shell
  jb install ./dependency.json
  ```

  **OPTIONS:**<br />

  - **--help** : for help
  - **--hide-output** : Hide stdout of pip
    - **Usage**
    ```shell
    jb install ./dependency.json --hide-output
    ```

_Use **jb --help** or **jb COMMAND --help** to get the usage_

<hr/>

## **Libraries Used**

- [Pip](https://github.com/pypa/pip) For installing pythong dependencies
- [Typer](https://github.com/tiangolo/typer) For taking commandline arguments
- [Rich](https://github.com/Textualize/rich) For coloring the output

<hr/>
