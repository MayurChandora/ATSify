# Technical Specifications: ATSify - AI Resume Analyser

This document provides the technical blueprints required for the **Antigravity AI Agent** to implement the project accurately.

---

## 1. Database Schema (ERD)
The system uses **MySQL** as specified in the Tech Stack. Below are the core models.

### 1.1 User Model
*Extends Django's AbstractUser.*
| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | UUID | Primary Key |
| `email` | String | Unique, used for login |
| `full_name` | String | User's display name |
| `date_joined` | DateTime | Auto-generated |

### 1.2 Resume Model
| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | UUID | Primary Key |
| `user` | ForeignKey | Link to User model |
| `file` | FileField | Path to uploaded PDF |
| `parsed_text` | TextField | Extracted text from PDF |
| `uploaded_at` | DateTime | Auto-generated |

### 1.3 Analysis Model
| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | UUID | Primary Key |
| `user` | ForeignKey | Link to User model |
| `resume` | ForeignKey | Link to Resume model |
| `job_description` | TextField | The JD text pasted by user |
| `match_score` | Integer | 0-100 score from AI |
| `missing_keywords` | JSONField | List of detected missing keywords |
| `strengths` | JSONField | List of identified strengths |
| `suggestions` | TextField | AI-generated improvement tips |
| `created_at` | DateTime | Auto-generated |

---

## 2. API Documentation (REST Endpoints)
If using **Django REST Framework (DRF)** for a decoupled frontend or AJAX calls.

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/auth/register/` | POST | User registration |
| `/api/auth/login/` | POST | User authentication |
| `/api/resume/upload/` | POST | Upload PDF and extract text |
| `/api/analysis/run/` | POST | Send Resume ID + JD text to Groq API |
| `/api/analysis/history/` | GET | Fetch user's previous analyses |
| `/api/analysis/<id>/` | GET | Fetch specific analysis details |

---

## 3. Project Folder Structure
Recommended structure for the Antigravity agent to follow:

```text
atsify_project/
├── core/               # Project settings & WSGI
├── accounts/           # User models, Auth views
├── analyzer/           # Resume parsing, Groq API logic
│   ├── services/       # Groq client, PDF parser service
│   ├── models.py
│   └── views.py
├── templates/          # HTML Templates (Tailwind/DaisyUI)
├── static/             # CSS/JS assets
├── manage.py
└── requirements.txt
```

---

## 4. Environment Variables (`.env`)
Required secrets for the project:
*   `DEBUG=True`
*   `SECRET_KEY=your_django_secret`
*   `DATABASE_URL=mysql://user:pass@localhost/atsify`
*   `GROQ_API_KEY=your_groq_api_key`
*   `LLAMA_MODEL=llama3-8b-8192`

---

## 5. Test Cases for AI Verification
Use these to verify the **Walkthrough Artifacts** in Antigravity.
1.  **Auth Test:** Can a user register and see the "Upload" page?
2.  **Upload Test:** Does the system reject non-PDF files?
3.  **Parsing Test:** Is text correctly extracted from a sample PDF?
4.  **AI Test:** Does the Groq API return a valid JSON response with score and keywords?
5.  **Dashboard Test:** Does the analysis appear in the history after completion?
