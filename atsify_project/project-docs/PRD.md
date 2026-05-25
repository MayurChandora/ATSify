# Product Requirements Document (PRD)

```
====================================================
AI RESUME ANALYSER - PRODUCT REQUIREMENTS DOCUMENT
====================================================

Version: 1.0
Prepared By: Mayur Chandora
Date: May 2026


====================================================
1. PROJECT OVERVIEW & GOALS
====================================================

1.1 Project Summary
--------------------
AI Resume Analyser is a web application that allows users to upload
their resume (PDF) and paste a job description to receive instant
AI-powered analysis.

The system uses Groq API with LLaMA 3 to:
- Generate match scores
- Identify missing keywords
- Highlight strengths
- Suggest resume improvements

Users must register and log in to use the analyser.
All analyses are saved in the user's dashboard.


1.2 Problem Statement
----------------------
Many job seekers get rejected by ATS systems because their resumes
do not match the job description keywords.

The platform solves this by providing:
- Fast resume analysis
- ATS keyword matching
- AI-generated suggestions
- Resume improvement guidance


1.3 Primary Goals
------------------
• Provide instant resume-to-JD match scoring
• Detect missing keywords and skill gaps
• Generate section-specific AI suggestions
• Save all analyses in dashboard history
• Deploy a live public product


====================================================
2. TARGET AUDIENCE & ENTITIES
====================================================

2.1 Target Audience
--------------------
• Fresh Graduates
• Junior Developers
• Career Switchers
• Internship Seekers


2.2 User Persona
-----------------
Arjun, 22 — BSc CS Graduate

- Applies to multiple jobs weekly
- Gets no callbacks
- Wants to know why ATS rejects his resume
- Needs fast and clear resume feedback


2.3 System Entities
--------------------

Visitor:
- Access landing page
- Register/Login
- About page
- Contact page

User:
- Upload resume
- Run analysis
- View dashboard
- Download reports
- Manage profile

Admin:
- Manage users
- View analyses
- Manage contact queries
- Monitor system usage


====================================================
3. REQUIRED PAGES
====================================================

Public Pages:
---------------
1. Landing Page
2. Register Page
3. Login Page
4. About Page
5. Contact Us Page

Protected Pages:
------------------
6. Analyse Page
7. Results Page
8. Dashboard Page
9. Profile Page


====================================================
4. CORE FEATURES
====================================================

P0 - Must Have Features
-------------------------
• PDF Resume Upload
• Job Description Input
• AI Match Score
• Missing Keywords Detection
• Strengths Panel
• AI Suggestions
• User Authentication
• Dashboard History
• Save Analysis to Database
• Contact Form

P1 - Should Have Features
---------------------------
• Loading Spinner
• Colour-coded Match Score
• Error Handling
• Mobile Responsive Design
• Download PDF Report

P2 - Nice To Have Features
----------------------------
• Google OAuth
• Multi-JD Comparison
• DOCX Support
• Score Trend Chart
• Shareable Result Links


====================================================
5. DEVELOPMENT PHASES
====================================================

Phase 1 - Authentication
-------------------------
• Register
• Login
• Logout
• Session Management

Estimated Time:
2–3 Days


Phase 2 - Core Analysis Flow
------------------------------
• Resume Upload
• PDF Parsing
• Groq API Integration
• AI Results Page

Estimated Time:
3–4 Days


Phase 3 - Database & Dashboard
--------------------------------
• Save analyses
• Dashboard history
• Result retrieval

Estimated Time:
2–3 Days


Phase 4 - UI Polish
---------------------
• Loading states
• Error handling
• Responsive design
• Contact page
• Profile page

Estimated Time:
2–3 Days


Phase 5 - Deployment
----------------------
• PDF Export
• Final Testing
• Deployment
• GitHub README

Estimated Time:
1–2 Days


====================================================
6. USER JOURNEY
====================================================

New User Flow
---------------
Landing Page
   ↓
Register
   ↓
Login
   ↓
Upload Resume + Paste JD
   ↓
AI Analysis
   ↓
View Results
   ↓
Dashboard History


Returning User Flow
---------------------
Login
   ↓
Dashboard
   ↓
View Previous Results
   ↓
New Analysis


====================================================
7. ERROR FLOWS
====================================================

• No PDF uploaded
• Invalid PDF format
• Empty job description
• PDF parsing failure
• Groq API timeout
• Session expiration
• Unauthorized access attempts


====================================================
8. SUCCESS METRICS
====================================================

• 50+ resume analyses in first month
• 30% returning users
• Average 2+ analyses per user
• Complete flow under 2 minutes
• AI response under 10 seconds


====================================================
9. QUALITY BENCHMARKS
====================================================

• Accurate match scores
• Clear keyword detection
• Actionable AI suggestions
• Clean PDF parsing
• Reliable dashboard history


====================================================
10. FINAL TECH STACK
====================================================

Frontend:
-----------
• HTML5
• CSS3
• JavaScript
• Tailwind CSS
• DaisyUI
• Stitch UI Components

Backend:
-----------
• Django

Database:
------------
• MySQL

AI:
------
• Groq API
• LLaMA 3

PDF Parsing:
---------------
• pdfplumber

Authentication:
-----------------
• Django Built-in Authentication

Hosting:
-----------
• Vercel

Database Hosting:
-------------------
• PlanetScale / Railway

Essential Packages:
---------------------
• django
• groq
• pdfplumber
• mysqlclient
• python-dotenv
• Pillow
• WeasyPrint
• whitenoise

Development Tools:
--------------------
• Git
• GitHub
• VS Code
• Postman
• Figma


====================================================
11. PROJECT ARCHITECTURE
====================================================

User
  ↓
Django Templates
  ↓
Django Backend
  ↓
Groq API + MySQL


====================================================
12. DEFINITION OF DONE
====================================================

The project is complete when a registered user can:

• Upload a PDF resume
• Paste a job description
• Receive AI-powered analysis
• View match score
• View missing keywords
• Get improvement suggestions
• Save results to dashboard
• Access the live deployed website
```
