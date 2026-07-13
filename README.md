# 🏥 AI Health Guardian
### Agentic AI for Chronic Disease Monitoring

AI Health Guardian is an intelligent healthcare assistant that combines **Machine Learning**, **IBM watsonx.ai Foundation Models**, and **Agentic AI** to predict diabetes risk and provide personalized medical insights, lifestyle recommendations, health reminders, and AI-powered healthcare assistance.

## 📌 Project Overview
The application predicts a patient's diabetes risk using a trained Machine Learning model and enhances the prediction using multiple AI agents powered by **IBM watsonx.ai**.
The system provides:

- 🩺 Diabetes Risk Prediction
- 🧠 AI Medical Reasoning
- 🥗 Personalized Lifestyle Planning
- ⏰ Daily Health Reminders
- 📄 Professional PDF Health Reports
- 📚 Patient History Tracking
- 💬 AI Health Chat Assistant
- 
## 🚀 Features

- Machine Learning based Diabetes Prediction
- IBM watsonx.ai Foundation Models Integration
- Meta Llama 3.3 70B Instruct Model
- Multi-Agent AI Architecture
- Professional Dashboard
- Patient Information Form
- AI Medical Analysis
- Personalized Lifestyle Recommendations
- Rule-Based Reminder System
- Downloadable PDF Reports
- Patient History Management
- Interactive AI Health Chat
- Modern Streamlit User Interface

# 🧠 Agentic AI Architecture

The project follows a multi-agent architecture where each AI agent performs a specialized healthcare task.

### Health Prediction Agent
- Predicts diabetes risk using Machine Learning.

### Medical Reasoning Agent
- Explains prediction results.
- Identifies important health indicators.
- Provides AI-generated medical reasoning.

### Lifestyle Planning Agent
- Generates personalized diet plans.
- Suggests exercise routines.
- Recommends healthy lifestyle improvements.

### Reminder Agent
- Generates daily healthcare reminders.
- Suggests routine checkups.
- Provides preventive care recommendations.

### Chat Agent
- Answers healthcare-related questions.
- Provides AI-powered assistance.

### History Agent
- Stores patient records.
- Displays previous health analyses.

# 🏗️ System Architecture

```
Patient Information
        │
        ▼
Data Preprocessing
        │
        ▼
Machine Learning Prediction
        │
        ▼
Risk Probability
        │
 ┌──────┼─────────┐
 ▼      ▼         ▼
Medical Lifestyle Reminder
 Agent    Agent     Agent
   │        │         │
   └────────┴─────────┘
            │
            ▼
 AI Health Guardian
            │
    ┌───────┼────────┐
    ▼       ▼        ▼
 Reports History Chat
```

# 💻 Technology Stack

## Frontend
- Streamlit
- Streamlit Lottie

## Machine Learning
- Scikit-learn
- NumPy
- Pandas
- Joblib

## AI Platform
- IBM watsonx.ai
- Meta Llama 3.3 70B Instruct

## Visualization
- Plotly

## Report Generation
- FPDF

# 📂 Project Structure

```
AI-Health-Guardian/
│
├── agents/
│   ├── health_agent.py
│   ├── medical_agent.py
│   ├── lifestyle_agent.py
│   ├── reminder_agent.py
│   ├── history_agent.py
│   └── chat_agent.py
│
├── components/
│   ├── dashboard.py
│   ├── patient_form.py
│   ├── prediction.py
│   ├── analysis.py
│   ├── reports.py
│   ├── history.py
│   ├── sidebar.py
│   ├── chat.py
│   └── footer.py
│
├── models/
│
├── assets/
│
├── utils/
│   ├── pdf_generator.py
│   ├── lottie_loader.py
│   └── watsonx.py
│
├── data/
│
├── app.py
├── requirements.txt
├── README.md
└── .env
```

# ⚙️ Installation

Clone the repository
```bash
git clone https://github.com/yourusername/AI-Health-Guardian.git
```
Move into the project directory
```bash
cd AI-Health-Guardian
```
Create a virtual environment
```bash
python -m venv venv
```
Activate the virtual environment
### Windows
```bash
venv\Scripts\activate
```
### Linux / macOS
```bash
source venv/bin/activate
```
Install dependencies
```bash
pip install -r requirements.txt
```

# 🔑 Environment Variables

Create a `.env` file.

```text
IBM_API_KEY=your_api_key

IBM_PROJECT_ID=your_project_id

IBM_URL=https://us-south.ml.cloud.ibm.com
```
# ▶️ Run the Application

```bash
streamlit run app.py
```

# 📊 Workflow

1. Enter patient information.
2. Machine Learning predicts diabetes risk.
3. IBM watsonx.ai generates medical reasoning.
4. Lifestyle agent creates a personalized health plan.
5. Reminder agent provides preventive recommendations.
6. PDF report is generated.
7. Patient history is stored.
8. AI Health Chat answers healthcare questions.
   

# 🌟 Key Highlights

- Agentic AI Healthcare System
- Explainable AI Predictions
- IBM watsonx.ai Integration
- Personalized Health Guidance
- Professional Medical Reports
- Interactive Healthcare Assistant

# 🔮 Future Scope

- Integration with wearable IoT devices.
- Real-time patient monitoring.
- Multi-disease prediction models.
- Doctor–patient teleconsultation support.
- Cloud deployment with secure authentication.

# 👩‍💻 Developed By

**Raparthi Bhavya Deepika Rani**

B.Tech – Computer Science & Engineering

Anil Neerukonda Institute of Technology & Sciences

# 🙏 Acknowledgements

- IBM SkillsBuild
- IBM watsonx.ai
- Scikit-learn
- Streamlit
- Meta Llama 3.3 Foundation Model

# 📜 License

This project is developed for educational and research purposes.

© 2026 AI Health Guardian. All Rights Reserved.
