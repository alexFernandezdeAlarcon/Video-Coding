# Report

## FFMPEG & FastAPI version
We run ffmpeg version 2024-09-26-git-f43916e217-full_build-www.gyan.dev built with gcc 13.2.0 (Rev5, Built by MSYS2 project) in our PCs. Make sure you have ffmpeg added to PATH at environment variables.
FastAPI (standard version) 0.115.4.

## Setting the API (With FastAPI)

1. In windows, donwload Git Bash (to insert docker commands) and Docker Desktop (to install the Docker engine).
2. Open Git Bash and execute "cd directory_where_the_practice1_folder_is"
3. Execute "docker build -t lab1_image:latest ." to generate the image which will be based on the main.py code.
4. Execute "docker run -d -p 80:80 lab1_image:latest" to run a container with the image inside it.
5. Go to "http://127.0.0.1" to see the interface. It should load correctly, displaying the API main page.

With Docker Desktop, you can stop the container and resume it whenever you wish, without going through the previous process again.

## Explanation

Since this is the first time we have dealt with building an API, we implemented two basic features: interactive endpoints (resize an image, compress and transform an image to black & white, both using FFmpeg) and a direct download link to obtain the remaining Seminar 1 tasks. With the help of ChatGPT, we customized the interface and resolved various coding issues. We followed the tutorial *FastAPI in Containers - Docker* as explained here¹.

Inside the practice1 folder, we set up the Dockerfile instructions along with the *requirements.txt* file containing the necessary libraries to run the API inside the container. Additionally, we structured the project as follows:

### /api: 
This folder contains the implemented endpoints. It includes three files:

*end_point_bw.py*: Handles the process of compressing and transforming an image to black & white.
*end_point_resize_image.py*: Handles the process of resizing an image to SD quality.
To use these methods, you only need to submit an image file of any type supported by FFmpeg (JPEG, JPG, PNG, BMP, etc.) and adjust a single parameter to set the dimensions or compression rate, respectively. After running the methods, the interface provides a button to download the resulting file in each case.
*end_point_scripts.py*: Provides a direct download link for the *first_seminar.ipynb* file via the main page.

### /scripts_S1:
It contains the *first_seminar.ipynb* file, which includes all the code tasks from Seminar 1.

### /services:
This folder contains the core Python files responsible for implementing the program's logic. These files contain the functions used by the endpoints mentioned above and rely on FFmpeg commands executed during runtime.

### /main.py:
This file initializes and configures the API. It imports the necessary routes to enable communication between */api* and */services*. It also deploys the HTML content to customize a bit the main page.

## References
1. https://fastapi.tiangolo.com/deployment/docker/#containers-and-processes
2. *FastAPI*: https://fastapi.tiangolo.com/

