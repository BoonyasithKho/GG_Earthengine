# Google Earth Engine

## Python Installation - Conda Install
### 1. Install Anaconda
### 2. Install Earth Engine Python API
   - The Earth Engine Python API is distributed as a conda-forge package at: https://anaconda.org/conda-forge/earthengine-api.

        ```
        conda install -c conda-forge earthengine-api
        ```
### 3. Get credentials
   - Before using the Earth Engine API or earthengine command line tool, you must perform a one-time authentication that authorizes access to Earth Engine on behalf of your Google account. To authenticate, use the authenticate command from the earthengine command line tool.

        ```
        earthengine authenticate
        ```
   - Upon entering the authorization code, an authorization token gets saved to a credentials file which can be found below. Subsequent use of the API's ```ee.Initialize()``` command and the earthengine command line tool will look to this file to authenticate. If you want to revoke authorization, simply delete the credentials file.

        For Windows:
        ```
        dir %UserProfile%\.config\earthengine\credentials
        ```
        For Mac:
        ```
        ls $HOME/.config/earthengine/credentials
        ```
### 4. Testing the API
   - Run the following Python lines one-by-one to print the metadata for a DEM dataset

        ```python
        import ee

        # Initialize the Earth Engine module.
        ee.Initialize()

        # Print metadata for a DEM dataset.
        print(ee.Image('USGS/SRTMGL1_003').getInfo())
        ```
### 5. Updating the API (Optional)
   - Use the conda update command to update to the latest API version. Remember to first activate your earth engine environment, if it is not already active.

      ```
      conda update -c conda-forge earthengine-api
      ```
   - Get the currently installed version number in Python.

     ```python
     import ee
     print(ee.__version__)
     ```
