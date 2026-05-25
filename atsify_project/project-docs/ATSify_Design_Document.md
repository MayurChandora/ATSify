# ATSify Design Document


# Page 1

Design Document: ATSify - AI Resume
Analyser
1. Project Overview
ATSify  is a modern, AI-powered web application designed to help job seekers optimize
their resumes for Applicant Tracking Systems (ATS). By leveraging the Groq API with
LLaMA  3, the platform provides instant match scores, keyword gap analysis, and
actionable suggestions to improve resume-to-job description alignment.
2. Design Philosophy
To resonate with its primary audience—fresh graduates and career switchers—the design
balances professionalism  with approachability .
Attribute Specification
Visual StyleModern & Minimalist: Clean lines, generous white space, and a focus on
content clarity.
MoodProfessional & Trustworthy: Inspires confidence in the AI’s accuracy while
remaining user-friendly.
Industry HR Technology / EdTech.
Target
AudienceStudents, Junior Developers, and Internship Seekers (e.g., Arjun, 22).

# Page 2

3. Color Palette
The palette uses a “Trust Blue” foundation, common in HR tech, paired with “Success
Green” and “W arning Amber” for functional feedback (match scores).
Core Colors
Color Hex Code Usage
Primary (Trust Blue) #2563EB Buttons, active states, and primary branding.
Secondary (Deep Navy)#1E293B Headings, navigation text, and dark accents.
Background (Soft Gray)#F8FAFC Main page backgrounds to reduce eye strain.
Surface (White) #FFFFFF Cards, modals, and input fields.
Functional Colors
Color Hex Code Meaning
Success#10B981 High match scores (80%+), strengths, and success messages.
Warning#F59E0B Moderate match scores (50-79%) and missing keywords.
Critical#EF4444 Low match scores (<50%) and error states.
4. Typography
The typography system prioritizes readability and ATS-friendly aesthetics.
Primary Font:  Inter (Sans-serif) - Chosen for its exceptional legibility on digital
screens.
Secondary Font:  JetBrains Mono (Monospace) - Used sparingly for “Keywords”
or “Technical Skills” to give a modern, tech-forward feel.

# Page 3

Type Scale
Element Size Weight Line Height
H1 (Hero) 48px Bold (700) 1.2
H2 (Section) 32px Semibold (600) 1.3
H3 (Card Title) 20px Semibold (600) 1.4
Body (Main) 16px Regular (400) 1.6
Small (Label) 14px Medium (500) 1.5
5. Layout & Spacing
The layout follows a 8px Grid System  to ensure consistency across all components.
Container W idth:  Max-width of 1280px for desktop, with 24px side padding.
Spacing Units:
xs: 4px | sm: 8px | md: 16px | lg: 24px | xl: 48px | 2xl: 64px
Border Radius:  12px for cards and buttons to provide a modern, soft feel.
Elevation:  Subtle shadows ( 0 4px 6px -1px rgb(0 0 0 / 0.1)) to separate
layers without clutter .
6. UI Component Specifications
6.1 Action Buttons
Primary:  Solid #2563EB background, white text, 12px border-radius. Hover state:
#1D4ED8.
Secondary:  Bordered (2px #2563EB), primary color text. Hover state: Light blue tint
background.

# Page 4

6.2 File Upload Zone
Style:  Dashed border ( #CBD5E1), centered icon, and drag-and-drop support.
Interaction:  Changes to solid #2563EB border on file hover .
6.3 Match Score Gauge
Visual:  A semi-circular or circular progress ring.
Logic:  Color transitions from Red → Amber → Green based on the percentage.
7. Responsive Design Considerations
ATSify follows a Mobile-First  approach.
Mobile (<768px):  Single-column layout. Navigation collapses into a hamburger
menu. Match scores take full width.
Tablet (768px - 1024px):  Two-column layout for the dashboard (Sidebar + Content).
Desktop (>1024px):  Full dashboard with persistent sidebar and multi-panel results
view (Resume Preview | Analysis Results).
8. Page-Specific Design Guidelines
8.1 Landing Page
Hero Section:  Bold headline with a clear “T ry for Free” CT A.
Visuals:  Use abstract “Scanning” or “AI Pulse” animations to represent the analysis
process.
8.2 Analyse Page
Focus:  Minimalist. Only two main inputs: “Resume Upload” and “Job Description
Textarea.”

# Page 5

State:  Clear “Analysing…” loading spinner with progress micro-copy (e.g.,
“Extracting keywords…”, “Comparing skills…”).
8.3 Results Page
Hierarchy:  Match score at the top, followed by “Missing Keywords” (tags), then “AI
Suggestions” (list).
Interactivity:  Clickable keyword tags that explain why they are important for the
specific JD.
8.4 Dashboard
History T able:  Clean rows showing Date, Job Title, and Score.
Quick Actions:  Icons for “V iew,” “Download PDF ,” and “Delete.”
9. Technical Implementation Notes
Framework:  Tailwind CSS for rapid styling.
Components:  DaisyUI for accessible, pre-built base components (Modals, Tabs).
Icons:  Lucide-React or Heroicons for a clean, consistent icon set.

# Page 6

10. Detailed UI Component Specifications
10.1 Navigation Bar
Specification Desktop (>1024px)Tablet (768px -
1024px)Mobile (<768px)
Dimensions Height: 64px Height: 64px Height: 56px
Background
Color#FFFFFF (White) #FFFFFF (White)#FFFFFF (White)
Text Color #1E293B (Deep Navy)#1E293B (Deep
Navy)#1E293B (Deep Navy)
TypographyInter, 16px, Semibold
(600)Inter, 16px,
Semibold (600)Inter, 16px,
Semibold (600)
Hover State
(Links)Text color: #2563EB
(Primary Blue), Underline:
2px solid #2563EBText color: #2563EB
(Primary Blue)Background: #F8FAFC
(Soft Gray)
Active State
(Links)Text color: #2563EB
(Primary Blue), Underline:
2px solid #2563EBText color: #2563EB
(Primary Blue)Background: #F8FAFC
(Soft Gray)
ElementsLogo (left), Nav Links
(center), CTA Button (right)Logo (left), Nav Links
(center), CTA Button
(right)Logo (left), Hamburger
Menu (right)
Responsive
BehaviorStandard layout Standard layoutHamburger menu
toggles full-screen
overlay navigation.

# Page 7

10.2 Hero Section
Specification Desktop (>1024px) Tablet (768px - 1024px)Mobile (<768px)
Dimensions Min-height: 500px Min-height: 400px Min-height: 300px
BackgroundGradient or subtle
pattern, #F8FAFC baseGradient or subtle
pattern, #F8FAFC base#F8FAFC base
Headline
TypographyInter, 48px, Bold
(700), #1E293BInter, 36px, Bold
(700), #1E293BInter, 28px, Bold
(700), #1E293B
Subheadline
TypographyInter, 18px,
Regular (400),
#475569Inter, 16px,
Regular (400),
#475569Inter, 14px, Regular
(400), #475569
Padding96px vertical, 24px
horizontal64px vertical, 24px
horizontal48px vertical, 16px
horizontal
ElementsHeadline, Subheadline,
Primary CTA, Secondary
CTA,
Illustration/AnimationHeadline, Subheadline,
Primary CTA, Secondary
CTA,
Illustration/AnimationHeadline, Subheadline,
Primary CTA (stacked),
Illustration/Animation
(optional)
Responsive
BehaviorText and CTAs centered,
illustration scales.Text and CTAs centered,
illustration scales.Text and CTAs stacked,
illustration may be
hidden or simplified.

# Page 8

10.3 Call-to-Action Buttons
Specification Primary Button Secondary Button
DimensionsHeight: 48px, Padding:
16px horizontalHeight: 48px, Padding: 16px horizontal
Background
Color#2563EB (Primary Blue) Transparent
Border None 2px solid #2563EB (Primary Blue)
Text Color #FFFFFF (White) #2563EB (Primary Blue)
TypographyInter, 16px, Semibold
(600)Inter, 16px, Semibold (600)
Border Radius12px 12px
Hover StateBackground: #1D4ED8
(Darker Blue)Background: #E0F2FE (Light Blue Tint),
Text: #1D4ED8
Active StateBackground: #1E40AF (Even
Darker Blue)Background: #BFDBFE (Slightly Darker
Blue Tint), Text: #1E40AF
Responsive
BehaviorFull width on mobile, fixed
width on desktop.Full width on mobile, fixed width on
desktop.

# Page 9

10.4 Cards/Content Blocks
Specification Default Card Highlighted Card
DimensionsMin-height: 150px, adaptable
widthMin-height: 150px, adaptable width
Background
Color#FFFFFF (White) #FFFFFF (White)
Border Radius12px 12px
Shadow0 4px 6px -1px rgb(0 0 0 /
0.1)0 10px 15px -3px rgb(0 0 0 /
0.1) (more pronounced)
Padding 24px all sides 24px all sides
Title TypographyInter, 20px, Semibold (600),
#1E293BInter, 20px, Semibold (600),
#2563EB
Body
TypographyInter, 16px, Regular (400),
#475569Inter, 16px, Regular (400),
#475569
Hover StateSlight lift (translateY: -2px), subtle
shadow increase.Slight lift (translateY: -2px), subtle
shadow increase.
Responsive
BehaviorStack vertically on mobile, grid
layout on tablet/desktop.Stack vertically on mobile, grid layout
on tablet/desktop.

# Page 10

10.5 Forms (Input Fields & Textareas)
Specification Input Field Textarea
Dimensions Height: 48px, Full width Min-height: 120px, Full width
Background
Color#FFFFFF (White) #FFFFFF (White)
Border 1px solid #CBD5E1 (Light Gray)1px solid #CBD5E1 (Light Gray)
Border Radius8px 8px
Text Color #1E293B (Deep Navy) #1E293B (Deep Navy)
Placeholder
Color#94A3B8 (Slate Gray) #94A3B8 (Slate Gray)
Typography Inter, 16px, Regular (400)Inter, 16px, Regular (400)
Focus StateBorder: 2px solid #2563EB
(Primary Blue), subtle shadow.Border: 2px solid #2563EB
(Primary Blue), subtle shadow.
Error StateBorder: 2px solid #EF4444 (Critical
Red)Border: 2px solid #EF4444 (Critical
Red)
Responsive
BehaviorAlways full width. Always full width.

# Page 11

10.6 Footer
Specification Desktop (>1024px)Tablet (768px -
1024px)Mobile (<768px)
DimensionsHeight: auto, based on
contentHeight: auto, based
on contentHeight: auto, based on
content
Background
Color#1E293B (Deep Navy)#1E293B (Deep
Navy)#1E293B (Deep Navy)
Text Color #E2E8F0 (Light Gray)#E2E8F0 (Light Gray)#E2E8F0 (Light Gray)
Link Color#94A3B8 (Slate Gray)#94A3B8 (Slate
Gray)#94A3B8 (Slate Gray)
Link Hover
State#FFFFFF (White) #FFFFFF (White)#FFFFFF (White)
TypographyInter, 14px, Regular
(400)Inter, 14px,
Regular (400)Inter, 12px,
Regular (400)
Padding48px vertical, 24px
horizontal32px vertical, 24px
horizontal24px vertical, 16px
horizontal
ElementsLogo, Copyright,
Navigation Links (e.g.,
About, Contact, Privacy),
Social Media IconsLogo, Copyright,
Navigation Links
(stacked), Social
Media IconsLogo, Copyright,
Navigation Links
(stacked), Social Media
Icons (stacked)
Responsive
BehaviorMulti-column layout.Two-column or
stacked layout.Single-column stacked
layout.
