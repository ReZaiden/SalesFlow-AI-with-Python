# 🤖 AI Sales Agent with Lead Generation

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-API-brightgreen)
![Gradio](https://img.shields.io/badge/Gradio-Interactive%20UI-orange)
![ntfy.sh](https://img.shields.io/badge/ntfy.sh-RealTime%20Alerts-red)
![Pandas](https://img.shields.io/badge/Pandas-Excel%20Loader-lightgrey)
![PyPDF](https://img.shields.io/badge/PyPDF-PDF%20Parser-purple)

A **conversational AI sales agent** capable of interacting with users,
filtering products from Excel/PDF/TXT, capturing leads, and sending
**real-time notifications** using `ntfy.sh`.\
Powered by **OpenAI**, **Gradio**, and a fully **modular architecture**.

> ⚠️ **Note:** This project is built for development and testing.\
> For production, ensure secure API keys, HTTPS, and proper rate
> limiting.

## 🚀 Features

-   💬 **Natural AI chat** using OpenAI function-calling\
-   🔍 **Product filtering** by name, min/max price\
-   📥 **Lead capturing** (email & phone)\
-   🚨 **Instant notifications** via ntfy.sh\
-   📚 **Knowledge Base** from Excel, PDF, and TXT\
-   🎨 **Beautiful Gradio UI** with custom themes\
-   📝 **Centralized logging** (file + console)\
-   🧪 **Full test coverage** with pytest

## 🧠 Tech Stack

  Technology          Version   Description
  ------------------- --------- -----------------------
  **Python**          3.9+      Core language
  **OpenAI API**      Latest    LLM & tool calling
  **Gradio**          4.0+      Interactive UI
  **ntfy.sh**         API       Real-time alerts
  **Pandas**          2.0+      Excel loader
  **PyPDF**           Latest    PDF parser
  **PyYAML**          Latest    Config management
  **python-dotenv**   Latest    Environment variables

## ⚙️ Prerequisites

Before running the project, ensure you have:

-   🐍 **Python 3.9+**\
-   📦 **pip**\
-   🌐 **Git**\
-   🔔 **ntfy.sh topic** (free)\
-   🔑 **AI API key** like OpenAI

## 🛠️ Installation

``` bash
git clone https://github.com/yourusername/SalesFlow-AI.git
cd SalesFlow-AI
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🗝️ Edit .env file
1. Rename `.env.sample` file to `.env`
2. Put your environment variables to it(like AI_API_KEY)

## 📃 Run Tests
``` bash
python -m pytest
```

## ▶️ Run the Project

``` bash
python -m app
```
and then go to http://localhost:8000/

## 📡 How It Works

1.  User starts the chat → Agent greets as **AidenAI**\
2.  Smart questions detect customer needs\
3.  Product filtering using `filter_products` tool\
4.  Results explained naturally\
5.  Lead capture (email/phone)\
6.  Real‑time ntfy.sh alert\
7.  Logging saved in `logs/*.log`

## 🧩 Project Structure

``` plaintext
files/
├── info.pdf
├── products.xlsx
└── summary.txt
logs/
└── *.log
src/
├── agent.py
├── tools.py
├── data.py
├── config.py
├── logger.py
└── ui.py
app.py
config.yaml
```

## 🔒 Security Notes

-   Keep API keys inside `.env`\
-   Change values in config.yaml

## 💡 Future Improvements

-   [ ] Vector search with ChromaDB\
-   [ ] Database chat history\
-   [ ] Lead analytics dashboard

## 🧑‍💻 Author

**Developed by:** ReZaiden 
💼 **GitHub:** [@ReZaiden](https://github.com/ReZaiden)  
📧 **Contact:** rezaidensalmani@gmail.com  

