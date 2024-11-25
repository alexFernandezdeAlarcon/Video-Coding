## FFMPEG version
We run ffmpeg version 2024-09-26-git-f43916e217-full_build-www.gyan.dev built with gcc 13.2.0 (Rev5, Built by MSYS2 project) in our PCs. Make sure you have ffmpeg added to PATH at environment variables.

## Setting the API (With FastAPI)

1. In windows, donwload Git Bash (to insert docker commands) and Docker Desktop (to install the Docker engine).
2. Open Git Bash and execute "cd directory_where_the_L1_folder_is"
3. Execute "docker build -t lab1_image:latest ." to generate the image which will be based on the main.py code.
4. Execute "docker run -d -p 80:80 lab1_image:latest" to run a container with the image inside it.
5. Go to "http://127.0.0.1" to see the interface. It should load correctly, displaying the API main page.

With Docker Desktop, you can stop the container and resume it whenever you wish, without going through the previous process again.

## Report

As this is the fisrt time we deal with the build of an API, we basically implemented two things: Two interactive endpoints (resize an image, compress and transform an image to black & white, both using ffmpeg) and a direct dowload link to obtain the rest of the seminar 1 tasks.

With the use of ChatGPT we managed to customize a little bit the interface and face code issues.


## Setting the API (With FastAPI)

1. In windows, donwload Git Bash (to insert docker commands) and Docker Desktop (to install the Docker engine).
2. Open Git Bash and execute "cd directory_where_the_practice1_folder_is"
3. Execute "docker build -t lab1_image:latest ." to generate the image which will be based on the main.py code.
4. Execute "docker run -d -p 80:80 lab1_image:latest" to run a container with the image inside it.
5. Go to "http://127.0.0.1" to see the interface. It should load correctly, displaying the API main page.

With Docker Desktop, you can stop the container and resume it whenever you wish, without going through the previous process again.

## Report

As this is our first time building an API, we implemented two key features: two interactive endpoints (resize an image, compress, and transform an image to black and white, all using FFmpeg), and a direct download link for the remaining tasks of Seminar 1.

With the help of ChatGPT, we managed to customize the interface a bit and resolve some coding issues.
