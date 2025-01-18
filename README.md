# TikStash 📦

> 💾 Backup • Archive • Preserve Your TikTok Content

TikStash is a user-friendly tool designed to help you create complete backups of TikTok channels. Whether you're a content creator wanting to preserve your work, or a user looking to save your favorite TikTok content locally, TikStash makes it simple and organized.

![logo](https://github.com/user-attachments/assets/56555249-65d3-4287-a624-c4ecdc6f25aa)


## 🌟 What is TikStash?

TikStash is a Python-based application that allows you to:
- Download all videos from any TikTok channel
- Save important information about each video (views, upload dates, descriptions, etc.)
- Organize videos in a clean, structured way
- Create detailed spreadsheets of your content

## 📋 Requirements

Before you start using TikStash, you'll need to have these installed on your computer:

### Essential Software
1. **Python 3.x**
   - Windows: Download from [Python's official website](https://www.python.org/downloads/)
   - Mac: Usually pre-installed, or use Homebrew: `brew install python3`
   - Linux: Usually pre-installed, or use: `sudo apt-get install python3`

2. **yt-dlp**
   - After installing Python, open your terminal/command prompt and run:
     ```bash
     pip install yt-dlp
     ```

## 🚀 Installation Guide

### For Windows Users:

1. **Download the Project**
   - Click the green "Code" button above
   - Select "Download ZIP"
   - Extract the ZIP file to a folder on your computer

2. **Install Python**
   - Download Python from [python.org](https://www.python.org/downloads/)
   - During installation, make sure to check ✅ "Add Python to PATH"
   - Click "Install Now"

3. **Install Required Tools**
   - Open Command Prompt (search for "cmd" in Start menu)
   - Type this command and press Enter:
     ```bash
     pip install yt-dlp
     ```

### For Mac Users:

1. **Download the Project**
   - Click the green "Code" button above
   - Select "Download ZIP"
   - Extract the ZIP file

2. **Install Python (if not installed)**
   ```bash
   brew install python3
   ```

3. **Install Required Tools**
   ```bash
   pip3 install yt-dlp
   ```

### For Linux Users:

1. **Download the Project**
   ```bash
   git clone https://github.com/yourusername/tikstash.git
   ```

2. **Install Required Tools**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   pip3 install yt-dlp
   ```

## 📱 How to Use

1. **Open Your Terminal/Command Prompt**
   - Windows: Press `Win + R`, type `cmd`, press Enter
   - Mac/Linux: Open Terminal app

2. **Navigate to TikStash Folder**
   ```bash
   cd path/to/tikstash
   ```

3. **Run the Program**
   ```bash
   python tikstash.py
   ```

4. **Follow the Prompts**
   - Enter a TikTok channel URL (e.g., https://www.tiktok.com/@username)
   - OR just enter the username (e.g., username)
   - The program will start downloading videos and creating your backup

## 📂 Understanding the Output

TikStash creates two types of files:

1. **Video Files**
   - Format: `views_date_channelname_videoid.mp4`
   - Example: `1000000_20230615_username_7123456789.mp4`

2. **CSV Spreadsheet**
   - Name: `channelname_videos.csv`
   - Contains:
     - Channel name
     - View count
     - Upload date
     - Video ID
     - Description
     - Location
     - Sound/music used

## 🔧 Troubleshooting

### Common Issues and Solutions

1. **"Python is not recognized..."**
   - Solution: Reinstall Python and make sure to check "Add Python to PATH"

2. **"yt-dlp is not recognized..."**
   - Solution: Run `pip install yt-dlp` again

3. **Download Errors**
   - Check your internet connection
   - Verify the TikTok URL is correct
   - Make sure the account is public

### Still Having Problems?
- Create an issue on GitHub
- Include the error message
- Describe what you were trying to do

## 🛡️ Important Notes

- Only use TikStash for content you have permission to download
- Some TikTok accounts may be private and inaccessible
- Download speeds depend on your internet connection
- Very large accounts may take significant time to backup

## 📈 Features

### Current Features
- Complete channel downloads
- Metadata preservation
- Organized file naming
- CSV data export
- Progress tracking
- Error handling

### Planned Features
- GUI interface
- Selective video download
- Multiple account backup
- Custom naming templates
- Advanced filtering options

## 🤝 Contributing

Want to improve TikStash? Here's how you can help:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 💖 Support the Project

If you find TikStash useful, please:
- Star the repository
- Share it with others
- Report any issues you find
- Contribute improvements

## 🙏 Acknowledgments

- Built with Python
- Uses yt-dlp for downloading
- Inspired by the need for reliable TikTok content backup

---

Made with 💝 by [Jonathan Paz](https://www.linkedin.com/in/jonathanftw/)
