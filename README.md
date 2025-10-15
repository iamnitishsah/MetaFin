![IIT- ISM Certificate](https://github.com/iamnitishsah/MetaFin/IIT-ISM Certificate.jpg?raw=true)



## 📑 Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Tech Stack](#tech-stack)
- [API Reference](#api-reference)
- [Workflows](#workflows)
- [Deployment](#deployment)

# Description

### Welcome to **Metafin** – Your Intelligent, Jargon-Free Investment Companion

Metafin is an AI-powered platform built to simplify investing with a **completely no-jargon UI**, featuring clear **iconography and logos** for every section—so you always know exactly where to go.

- **Personalized Dashboard**  
  Your home base, tailored to your goals, with custom logos guiding you through your portfolio at a glance.

- **Mutual Funds & ETFs**  
  Discover top performers and the single best pick for you. Each fund page sports its own logo, and our "i" button decodes any remaining complexity in plain English.

- **Stock Performance Recommendations**  
  Powered by both cutting-edge LLMs and a custom-built model, get concise summaries, interactive graphs, and a clear **Invest/Pass** verdict—each with a dedicated logo for easy navigation.

- **Ongoing Trends**  
  Real-time candlestick charts for stocks, forex, and more, driven by our proprietary ML model that predicts optimal buy/sell windows. Look for the trend-tracker logo to dive in.

- **Sentiment Analysis Engine**  
  Aggregates insights from Yahoo Finance and Reddit APIs to gauge market mood. Spot the sentiment-meter icon wherever you need a pulse check.

- **Detailed Stock Analysis**  
  A complete stock analysis based on real-time values and a comprehensive summary translated for a non-jargon user.

- **Stock Recommendations**  
  A custom-built hybrid (content-based + performance-based) recommendation system that suggests top-performing stocks based on user history.

- **Stock Comparator**  
  Side-by-side stock comparison based on real-time data from the Yahoo Finance API, enhanced with LLM-generated non-jargon feedback.

- **Custom News Hub**  
  Curates headlines and deep dives on your past and current investments, all under one news-feed logo.

Metafin isn’t just another fintech tool—it’s your clear, icon-driven co-pilot for smarter investing. 🚀

# Installation

### Clone the repo

```bash
git clone https://github.com/iamnitishsah/MetaFin.git
cd MetaFin
```



For the frontend:
```bash
cd MetaFin-Frontend
```
### Install dependencies
```bash
npm i --force
```

### Run the development server
```bash
npm run dev
```



For the backend:
```bash
cd MetaFin-Backend
```
set up a virtual environment and install dependencies:
```bash
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```
### Migrate the database
```bash
python manage.py makemigrations
python manage.py migrate
```
### Run the development server
```bash
python manage.py runserver
```


# Tech Stack

### 🧠 Full Stack for ML-Driven Fintech Applications

**🖥️ Frontend:**  
- **Next.js**: Server-side rendering and routing.  
- **React**: Dynamic UI components.  
- **TailwindCSS**: Utility-first CSS for responsive design.

**🌐 Backend:**  
- **Django**: Scalable backend for business logic, auth, and integrations.  
- **PostgreSQL**: Robust relational database for storing user and market data.

**🔍 Machine Learning API Serving:**  
- ML models are integrated into Django views or served via custom APIs from Django apps.

# API Reference

### Data Sources Used:
- **FMP (Financial Modeling Prep)**
- **Alpha Vantage**
- **TradersView**
- **Reddit (r/stocks, r/investing, etc.)**
- **Yahoo Finance**

# Workflows

### Recommendation System Workflow
![Recommendation Workflow](https://res.cloudinary.com/dk6m1qejk/image/upload/v1743924275/Hackfest%20workflows/ywrbdhru1jioerxsefvb.jpg)

### Sentiment Analysis
![Sentiment Workflow](https://res.cloudinary.com/dk6m1qejk/image/upload/v1743924275/Hackfest%20workflows/gjdfhxvck8ekbycqequ6.jpg)

### Personalized News Recommendation
![News Workflow](https://res.cloudinary.com/dk6m1qejk/image/upload/v1743924275/Hackfest%20workflows/oehtvsat7zgswa8rcg2d.jpg)
