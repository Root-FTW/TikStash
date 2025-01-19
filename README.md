# TikStash 📦

> 💾 Backup • Archive • Preserve Your TikTok Content

TikStash is a user-friendly tool designed to help you create complete backups of TikTok channels. Whether you're a content creator wanting to preserve your work, or a user looking to save your favorite TikTok content locally, TikStash makes it simple and organized.

![logo](https://github.com/user-attachments/assets/56555249-65d3-4287-a624-c4ecdc6f25aa)

## 🎯 Quick Start Guide (For Non-Technical Users)

1. **Install Required Programs**
   - Install Python from [python.org](https://www.python.org/downloads/)
   - During Python installation, CHECK ✅ "Add Python to PATH"
   - Open Command Prompt (Windows) or Terminal (Mac/Linux)
   - Type: `pip install yt-dlp` and press Enter

2. **Get TikStash**
   - Download TikStash by clicking the green "Code" button above
   - Choose "Download ZIP"
   - Extract the ZIP file to your desktop

3. **Run TikStash**
   - Open the extracted folder
   - Double-click `tikstash.py`
   - Enter a TikTok username or URL when prompted
   - Wait for the backup to complete!

Need more detailed instructions? Check the [Detailed Installation Guide](#-installation-guide) below.

## 🌟 What is TikStash?

TikStash is a Python-based application that helps you:
- Download all videos from any public TikTok channel
- Save video metadata (views, dates, descriptions)
- Organize content in a structured way
- Create detailed spreadsheets of your content
- Preserve your digital content locally

### 🎁 Key Benefits
- **Content Safety**: Never lose your TikTok videos
- **Organized Backup**: Everything sorted and labeled
- **Easy to Use**: Simple command-line interface
- **Detailed Information**: Complete metadata preservation
- **Progress Tracking**: Real-time download status

## 🔧 Technical Overview

### Architecture and Components

```plaintext
TikStash
├── Core Functions
│   ├── get_video_info(): JSON metadata retrieval
│   └── download_tiktok_videos(): Main download handler
├── Data Management
│   ├── Videos Backup/: Video storage directory
│   └── MetaData Backup/: CSV data storage
└── Input Processing
    ├── URL validation
    └── Username extraction
```

### Technical Features

- **Asynchronous Operations**: Uses subprocess for non-blocking operations
- **Error Handling**: Comprehensive try-catch blocks for robust execution
- **Progress Visualization**: Dynamic loading animation during operations
- **File Management**: Automatic directory creation and organization
- **Data Validation**: Input validation and URL pattern matching
- **Resource Management**: Proper file handling with context managers

### Output Structure

#### Video Files
```plaintext
Videos Backup/
└── {view_count}_{upload_date}_{channel_name}_video_{id}.{ext}
```

#### Metadata Files
```plaintext
MetaData Backup/
└── {channel_name}_datainfo.csv
```

## 📋 Requirements

### Essential Software
1. **Python 3.x**
   - Windows: [Python's official website](https://www.python.org/downloads/)
   - Mac: `brew install python3`
   - Linux: `sudo apt-get install python3`

2. **yt-dlp**
   ```bash
   pip install yt-dlp
   ```

### System Requirements
- OS: Windows 7+ / macOS 10.13+ / Linux
- RAM: 2GB minimum
- Storage: Depends on videos to backup
- Internet: Stable connection required

## 🚀 Detailed Installation Guide

### Windows Step-by-Step

1. **Install Python**
   - Download Python 3.x from [python.org](https://www.python.org/downloads/)
   - Run the installer
   - ✅ Check "Add Python to PATH"
   - ✅ Check "Install launcher for all users"
   - Click "Install Now"
   - Wait for installation to complete
   - Click "Close"

2. **Verify Python Installation**
   - Press `Win + R`
   - Type `cmd` and press Enter
   - In Command Prompt, type:
     ```bash
     python --version
     ```
   - You should see something like `Python 3.x.x`

3. **Install yt-dlp**
   - In the same Command Prompt, type:
     ```bash
     pip install yt-dlp
     ```
   - Wait for installation to complete

4. **Download TikStash**
   - Download ZIP from GitHub
   - Right-click ZIP and select "Extract All"
   - Choose a location (e.g., Desktop)
   - Click "Extract"

### macOS Step-by-Step

1. **Install Homebrew (if not installed)**
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python**
   ```bash
   brew install python3
   ```

3. **Install yt-dlp**
   ```bash
   pip3 install yt-dlp
   ```

4. **Download and Extract TikStash**
   - Download ZIP from GitHub
   - Double-click to extract
   - Move to desired location

### Linux Step-by-Step

1. **Update Package Manager**
   ```bash
   sudo apt update
   ```

2. **Install Python and pip**
   ```bash
   sudo apt install python3 python3-pip
   ```

3. **Install yt-dlp**
   ```bash
   pip3 install yt-dlp
   ```

4. **Clone TikStash**
   ```bash
   git clone https://github.com/Root-FTW/tikstash.git
   ```

## 📱 Usage Guide

### Basic Usage

1. **Start TikStash**
   - Windows: Double-click `tikstash.py` or run:
     ```bash
     python tikstash.py
     ```
   - Mac/Linux: Open Terminal and run:
     ```bash
     python3 tikstash.py
     ```

2. **Enter Channel Information**
   - Use TikTok URL: `https://www.tiktok.com/@username`
   - Or just username: `username`

3. **Wait for Completion**
   - Progress indicator will show status
   - Don't close the window during download


## 📂 Output Details

### Video Files
- Located in: `Videos Backup/` directory
- Naming convention: `views_date_channelname_videoid.mp4`
- Example: `1000000_20230615_username_7123456789.mp4`

### Metadata CSV
- Located in: `MetaData Backup/` directory
- Filename: `channelname_datainfo.csv`
- Fields:
  - Channel Name
  - Views
  - Upload Date
  - Video ID
  - Description
  - Song/Sound Name

## 🔧 Advanced Troubleshooting

### Error Codes and Solutions

1. **Error Code 1: Python Path Issues**
   ```bash
   'python' is not recognized...
   ```
   Solution: Add Python to system PATH

2. **Error Code 2: yt-dlp Installation**
   ```bash
   No module named 'yt_dlp'
   ```
   Solution: Reinstall using pip with admin rights

3. **Error Code 3: Permission Denied**
   ```bash
   PermissionError: [Errno 13]
   ```
   Solution: Run with appropriate permissions


## 🛡️ Technical Considerations

### Performance Optimization
- Progress tracking
- Error recovery

### Security Considerations
- Data validation
- Safe file handling

## 🔄 Development Workflow

### Setting Up Development Environment
1. Clone repository
2. Install dependencies
3. Set up virtual environment
4. Run tests

### Contributing Code
1. Fork repository
2. Create feature branch
3. Implement changes
4. Submit pull request

## 📈 Roadmap

### Version 1.1 (Current)
- Dwnload functionality
- CSV metadata export
- Progress tracking
- Error handling

### Version 1.2 (Planned)
- GUI interface
- Batch processing
- Custom templates
- Advanced filters

## 💖 Support and Community

### Getting Help
- Create GitHub issue
- LinkedIn support
- Email support

### Supporting Development
- Star repository
- Report bugs
- Submit features
- Share project

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python
- Powered by yt-dlp
- Inspired by content preservation needs
- Community contributions

---

Made with 💝 by [Jonathan Paz](https://www.linkedin.com/in/jonathanftw/)
