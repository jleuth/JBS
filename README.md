# JBS - Jake's Build Server

*Barely any interface, barely any complexity!*

Jake's Build Server is a super simple online make build server. It allows developers to upload their project files, run a build script, and download the resulting build artifacts.

## Features

- Simple authentication to protect the build server
- Upload project files and run a build script
- Download the resulting build artifacts

## Prerequisites

- Python 3.x
- Flask
- python-dotenv

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/jleuth/jbs.git
    cd jbs
    ```

2. Create a virtual environment and activate it:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:

    ```sh
    pip install flask python-dotenv
    ```

4. Create a `.env` file in the project directory and add your environment variables:

    ```env
    PASSWORD=your_password_here
    ```

5. Update the `build_script.sh` with your build commands.

## Usage

1. Run the Flask application:

    ```sh
    python server.py
    ```

2. Open your web browser and navigate to `http://localhost:5000`.

3. Enter the password you set in .env to access the build server.

4. Upload your project files and run the build.

5. The items in your /outputs folder will be automatically downloaded.

## File Structure
