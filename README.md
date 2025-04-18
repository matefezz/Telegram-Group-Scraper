# 🔍 Telegram Group Member Scraper  

*A Python script to extract member details from multiple Telegram groups, including user IDs, usernames, phone numbers, and more.*  

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![Telethon](https://img.shields.io/badge/Telethon-1.24%2B-green.svg)](https://docs.telethon.dev/)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/yourusername/telegram-group-scraper/pulls)  

---

## ✨ Features  
- 🚀 **Multi-Group Scraping**: Fetch members from multiple Telegram groups at once.  
- 📊 **Structured Data**: Export to **CSV/JSON** with fields like `user_id`, `username`, `phone`, `verified`, etc.  
- 🤖 **Flexible Auth**: Supports both **user accounts (MTProto)** and **bots (Bot API)**.  
- 🔒 **Privacy-Aware**: Respects Telegram’s rate limits and privacy policies.  

---

## 🛠️ Installation  

### Prerequisites  
- Python 3.7+  
- A [Telegram API ID & Hash](https://my.telegram.org/auth) (for user accounts) or a [Bot Token](https://core.telegram.org/bots#botfather) (for bots).  

### Steps  
1. **Clone the repo**:  
   ```bash
   git clone https://github.com/yourusername/telegram-group-scraper.git
   cd telegram-group-scraper
