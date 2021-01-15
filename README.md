## 🤔 What is FBDownloader?
  - A tool to download videos of Facebook in HD or SD qualities.

<br><br>

## ☁️ Download & Install
  - git clone https://github.com/z3ox1s/fbdownloader
  - cd fbdownloader
  
<br><br>

## ⚙️ Setup
  - To install all requirements, run 'pip install -r requirements.txt' in console.

<br><br>

## ❓ Usage
  - Run 'python main.py' and use valid parameters:
    - -h or --help -> To see available valid parameters;
    - -l or --link -> Video Link;
    - -hd -> To download HD Quality;
    - -sd -> To download SD Quality;
    - -n or --name -> To stipulate file name (Without spaces).
  - Example: 'python main.py -l https://facebook.com/' -> Speed setup, but, you can't choose quality and filename.
  - Example: 'python main.py -l https://facebook.com/ -hd -n video' -> Will download your vid, if HD quality exists, and set the filename 'video.mp4'.
