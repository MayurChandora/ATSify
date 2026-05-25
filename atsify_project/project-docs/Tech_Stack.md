# Tech Stack Document

```
Project Type: AI Resume Analyser Website


Frontend:
• HTML5
• CSS3
• JavaScript
• Tailwind CSS
• DaisyUI
• Stitch UI Components

• Reason: Simple and beginner-friendly frontend stack for Django templates,
  responsive design, faster UI development, and modern AI SaaS appearance.


Backend:
• Django

• Reason: Handles authentication, routing, database operations, file uploads,
  dashboard functionality, session management, and AI API integration.


Database:
• MYSQL

• Reason: MySQL provides reliable production database management and good performance for relational data.


Authentication:
• Django Built-in Authentication

• Reason: Secure login, registration, session handling, password hashing,
  and protected routes without external auth setup.


AI & Resume Processing:
• Groq API
• LLaMA 3
• pdfplumber

• Reason: Fast AI inference for resume analysis, keyword matching,
  suggestions generation, and clean PDF text extraction.


Essential Packages:
• django
• groq
• pdfplumber
• mysqlclient
• python-dotenv
• Pillow
• WeasyPrint
• whitenoise
• django-crispy-forms
• django-allauth

• Reason: Database connectivity, environment management,
  PDF export, static file handling, and improved forms.


UI & Animations:
• DaisyUI components
• Stitch UI sections
• AOS.js / CSS animations

• Reason: Modern responsive UI, reusable components,
  smooth animations, and professional dashboard design.


Deployment:
• Vercel
• GitHub

• Reason: Easy deployment, GitHub integration,
  cloud database hosting, and automatic deployments.


Development Tools:
• Git
• GitHub
• VS Code
• Postman
• Figma

• Reason: Source control, API testing,
  development workflow, and UI planning/design.


Project Architecture:
• User
    ↓
  Django Templates
    ↓
  Django Backend
    ↓
  Groq API + MySQL


Performance & Optimization:
• Tailwind CSS optimization
• Whitenoise static file serving
• Optimized PDF parsing
• Fast Groq inference responses

• Reason: Faster loading speed,
  improved user experience, and efficient AI analysis workflow.
```
