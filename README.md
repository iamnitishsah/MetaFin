## 📑 Table of Contents

- [ Description](#description)
- [ Installation](#installation)
- [ TechStack](#techstack)
- [ API Reference](#api-reference)
- [ Workflows](#workflows)
- [ Deployment](#deployment)

# Description

### Welcome to **Metafin** – Your Intelligent, Jargon‑Free Investment Companion


Metafin is an AI‑powered platform built to simplify investing with a **completely no‑jargon UI**, featuring clear **iconography and logos** for every section—so you always know exactly where to go.

- **Personalized Dashboard**  
  Your home base, tailored to your goals, with custom logos guiding you through your portfolio at a glance.

- **Mutual Funds & ETFs**  
  Discover top performers and the single best pick for you. Each fund page sports its own logo, and our “i” button decodes any remaining complexity in plain English.

- **Stock Performance Recommendations**  
  Powered by both cutting‑edge LLMs and a custom from‑scratch model, get concise summaries, interactive graphs, and a clear **Invest/Pass** verdict—each with a dedicated logo for easy navigation.

- **Ongoing Trends**  
  Real‑time candlestick charts for stocks, forex, and more, driven by our proprietary ML model that predicts optimal buy/sell windows. Look for the trend‑tracker logo to dive in.

- **Sentiment Analysis Engine**  
  Aggregates insights from Yahoo Finance and Reddit APIs to gauge market mood. Spot the sentiment‑meter icon wherever you need a pulse check.

- **Detailed Stock Analysis**  
  A complete stock analysis based on Real‑time values and a 
  comprehensive summary with feedback to a non-jargon user.

- **Stock Recommendations**  
  A custom built hybrid(content based+Performance based) Recommendation system that gives the most performing stocks based 
  on user history.

- **Stock Comparator**  
  Side‑by‑side stock comparator based on Real‑time analysis from 
  YahooFinance Api and a feedback from a llm to a non-jargon user.

- **Custom News Hub**  
  Curates headlines and deep dives on your past and current investments, all under one news‑feed logo.

Metafin isn’t just another fintech tool—it’s your clear, icon‑driven co‑pilot for smarter investing. 🚀



# Installation
### Clone the repo
```
git clone https://github.com/VVUx21/team-meta_cognition
cd team-meta_cognition
```

### Install dependencies
```
npm i --force
```

### Run the development server
```
npm run dev
```
# TechStack
### 🌟 Enhanced Tech Stack for Complex ML Model Deployment 🌟

**🖥️ Client-Side:**  
- **React**: For dynamic and interactive user interfaces.  
- **Redux**: To manage application state efficiently.  
- **TailwindCSS**: For sleek, responsive, and modern styling.  
- **Next.js**: Optimized for server-side rendering (SSR) and seamless integration with APIs.

**🌐 Server-Side:**  
- **Node.js**: Acts as an intermediary server for preprocessing and routing between the frontend and backend APIs.  
- **Express.js**: Facilitates robust API creation and request handling.  
- **Flask**: Lightweight Python framework to serve ML models as RESTful APIs, ideal for quick deployments and prototyping.  
- **Django**: A robust Python framework for scalable and feature-rich backend applications, suitable for handling complex ML model deployments.

### 🚀 Deployment Workflow:
1. **Frontend Interaction (Next.js)**: Users interact with the interface to upload data or query predictions.
2. **Intermediate Processing (Node.js + Express)**: The frontend sends data to the Node.js server, which preprocesses it before forwarding the request.
3. **Model Inference (Flask/Django)**:
   - Flask handles lightweight deployments with RESTful APIs for quick responses.
   - Django is used for larger-scale applications requiring advanced features like caching or database integration.
4. **Result Display**: The prediction results are routed back through Node.js to Next.js and displayed to the user.

### 🔧 Why This Stack?
- **Next.js + Flask/Django Integration**: Combines fast rendering capabilities of Next.js with Flask/Django’s ability to serve complex ML models efficiently.  
- **Scalability**: Django ensures scalability for high-demand applications, while Flask is perfect for lightweight prototypes.  
- **Flexibility**: Flask allows custom routes and preprocessing, while Django supports advanced features like caching and authentication.  

This stack is ideal for deploying machine learning models in real-world applications, ensuring performance, scalability, and user-friendly interfaces!
## API Reference

### Data Sources

This API aggregates and serves financial data from the following sources:

- **FMP (Financial Modeling Prep)**
- **Alpha Vantage**
- **TradersView**
- **Reddit (r/stocks, r/investing, etc.)**
- **Yahoo Finance**

---



# Workflows
### Recommendation System Workflow
![Workflow Diagram](https://res.cloudinary.com/dk6m1qejk/image/upload/v1743924275/Hackfest%20workflows/ywrbdhru1jioerxsefvb.jpg)
### Sentiment Analysis
![Workflow Diagram](https://res.cloudinary.com/dk6m1qejk/image/upload/v1743924275/Hackfest%20workflows/gjdfhxvck8ekbycqequ6.jpg)
### Personalised News Recommendation
![workflow Diagram](https://res.cloudinary.com/dk6m1qejk/image/upload/v1743924275/Hackfest%20workflows/oehtvsat7zgswa8rcg2d.jpg)

## Deployment
This Project is deployed on Vercel and Render.

