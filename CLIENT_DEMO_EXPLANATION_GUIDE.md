# Apex Institute Admissions CRM & Chatwoot: Client Demo & Explanation Guide

> **Quick Reference Document for College Presentations**  
> **Audience:** Registrar, Dean / Director of Admissions, Admissions Committee & Counsellor Leads  
> **Instance URLs:**
> - **Chatwoot Inbox:** [https://chat.pranavcloud.in](https://chat.pranavcloud.in)
> - **Admissions CRM Dashboard:** [https://chat.pranavcloud.in/admissions-dashboard/](https://chat.pranavcloud.in/admissions-dashboard/)

---

## 1. The 30-Second Elevator Pitch

> *"Think of **Chatwoot** as our **Communication Engine**, and the **Admissions Dashboard** as our **Academic Pipeline Engine**."*

* **Chatwoot** is where counsellors **talk to students**: whether an enquiry comes from WhatsApp, Facebook Ads, Website Chat, or Phone calls, everything lands in one single unified inbox.
* **Admissions CRM Dashboard** is where you **run the admission operations**: tracking student applications through the 7 admission stages, verifying 10th/12th marksheets, collecting token fees, and monitoring counsellor conversion performance.
* **Zero Software Switching:** The Admissions Dashboard is embedded **directly inside Chatwoot** as a native Dashboard App. Counsellors chat with students on the left and update admission files on the right without opening new tabs or third-party tools.

---

## 2. Side-by-Side Comparison: Chatwoot vs Admissions CRM

| Dimension | 💬 Chatwoot (Communication Engine) | 📊 Admissions CRM Dashboard (Pipeline Engine) |
|---|---|---|
| **Core Purpose** | Omnichannel student chatting & engagement | Admission lifecycle, document checks & token fees |
| **Channels Handled** | WhatsApp Business Cloud API, Meta/Facebook, Live Chat, SMS | 5 Ingestion sources aggregated in a central database |
| **Primary Users** | **Counsellors** answering everyday queries | **Dean, Registrar, Team Leads & Counsellors** |
| **Daily Actions** | Send course brochures, voice notes, answer syllabus FAQs | Verify marksheets, advance 7 stages, record token fee payments |
| **Data Tracked** | Response time, chat resolution, CSAT feedback | **Daily admissions, conversion funnel %, ad source ROI, fee collections** |
| **Access Control** | Agent vs Administrator | **Strict RBAC:** Admin (Dean), Team Lead, Scoped Counsellor views |

---

## 3. How Facebook & Instagram Leads Arrive Directly

In educational marketing on Meta (Facebook & Instagram), there are two main types of ads. Both flow **directly** into the system without manual CSV downloading:

### A. Click-to-WhatsApp (CTWA) Ads *(#1 Choice for High Intent)*
1. **Student Action:** Student sees an Instagram/Facebook ad and taps **"Chat on WhatsApp"**.
2. **Instant Delivery:** WhatsApp opens with a pre-filled message (*"Hi, I want details on MBA 2026 admissions"*).
3. **Chatwoot Ingestion:** The message lands **instantly in Chatwoot** with verified phone number and student name.
4. **Auto-Assignment:** Round-robin assigns the conversation to an available counsellor in seconds.

### B. Facebook Lead Generation Forms *(Instant Forms)*
1. **Student Action:** Student fills out native fields on Facebook (Name, Phone, Email, Preferred Course).
2. **Live Webhook Ingestion:** Meta fires a live webhook directly into Chatwoot and the Admissions CRM database.
3. **Duplicate Detection:** The CRM checks if the phone number already exists in the system:
   - If **Duplicate:** Tags the lead and alerts the existing counsellor to avoid double-calling.
   - If **New:** Creates the student record, assigned to the relevant department pod.
4. **Instant WhatsApp Acknowledgment (< 5 seconds):**
   Within 5 seconds, an automated WhatsApp message is delivered to the student’s phone:
   > *"Hi Rahul! Thank you for inquiring about MBA Admissions at Apex Institute. Our counsellor Sneha Patel will connect with you shortly. In the meantime, download our 2026 Course Brochure here: [Link]"*

---

## 4. The 5 Core CRM Features Explained

The Admissions CRM strictly implements the 5 essential educational CRM pillars:

```
[1. Centralized Leads] ➔ [2. 7-Stage Pipeline] ➔ [3. Counsellor Workload]
           │                                                │
           ▼                                                ▼
[4. WhatsApp Automation]                        [5. Management Dashboard]
```

### Feature 1: Centralized Lead Management
- **5 Ingestion Channels:** Website Forms, Facebook/Instagram Ads, WhatsApp Business, Phone Calls, and Bulk CSV/Excel imports.
- **Round-Robin Auto-Assignment:** Automatically distributes incoming students equally among counsellors.
- **Duplicate Lead Detection:** Alerts immediately if a student submits enquiries across multiple channels.

### Feature 2: Complete 7-Stage Admission Pipeline
Maps the complete Indian higher education admission journey:
$$\text{Enquiry} \longrightarrow \text{Counselling} \longrightarrow \text{Follow-up} \longrightarrow \text{Application} \longrightarrow \text{Document Verification} \longrightarrow \text{Fee Payment} \longrightarrow \text{Enrollment}$$
- Visual Kanban board with stage totals and token fee values.
- Student slide-over drawer with 4 tabs: **Profile**, **Documents Checklist** (10th, 12th, Degree, Entrance), **Fees & Receipts**, and **Admission History Notes**.

### Feature 3: Counsellor Management (30 Team Members)
- **Role-Based Access Control (RBAC):** Admin (Full access), Team Lead (Pod supervision), Counsellor (Restricted to assigned students only).
- **Daily Follow-up Queue:** Tracks Overdue and Due Today student callback calls.
- **30-Member Capacity Roster:** Monitors active leads, conversions, and fee collections per counsellor.

### Feature 4: WhatsApp Admissions Automation (4 Core Flows)
1. **Enquiry Acknowledgement:** Fires instantly on new lead creation with prospectus download link.
2. **Follow-up Reminders:** Fired on scheduled counselling callback dates.
3. **Application & Document Notification:** Fired when marksheets are verified or pending.
4. **Admission & Fee Payment Reminder:** Fired when admission is approved to complete token seat reservation.

### Feature 5: Management Dashboard (Executive Oversight)
- **Daily Admissions:** Confirmed seats reserved today.
- **Conversion Funnel Tracking:** Live conversion percentages across all 7 pipeline stages.
- **Lead Source Analysis:** Donut chart breakdown (WhatsApp 36%, Website 28%, Meta Ads 22%, Calls 14%).
- **Fee Collection Reports:** Verified token fees (₹1,11,250 collected against ₹48.6 Lakhs committed total).

---

## 5. Persona Walkthrough: Who Sees What?

### A. The Counsellor Persona (e.g., Sneha Patel · Management Pod)
* **What they see:**
  - **My Leads:** Only their 10 assigned students (cannot view colleagues' leads).
  - **My Pipeline:** Personal Kanban showing their students moving through stages.
  - **My Daily Tasks:** Follow-up call queue for today (e.g., Divya Joshi callback).
* **What is hidden:**
  - 🚫 Executive Management Dashboard & institute financial totals.
  - 🚫 WhatsApp bot flow editor.
  - 🚫 Bulk CSV database import.
  - 🚫 30-member institute workload roster.

### B. The Team Lead Persona (e.g., Priya Sharma · Admissions Central)
* **What they see:**
  - Team Leads Overview across their department/pod.
  - Team Task Queue and Counsellor Roster status.
  - WhatsApp Automation monitoring.
* **What is hidden:**
  - 🚫 Executive Financial revenue totals and Dean's macro reports.

### C. The Executive Persona (Dean / Registrar)
* **What they see:**
  - Full access to all 5 tabs and all 30 counsellors.
  - Executive Management Dashboard with live seat conversions and ₹1.11 Lakh token fee receipts.
  - Bulk CSV import/export capabilities and WhatsApp Cloud API trigger settings.

---

## 6. Step-by-Step Live Client Demo Script

Follow this exact 4-step sequence during your presentation:

### Step 1: Show Lead Arrival in Chatwoot (Omnichannel Ingestion)
1. Open [https://chat.pranavcloud.in](https://chat.pranavcloud.in).
2. Show the Chatwoot inbox with WhatsApp and Facebook labels.
3. **Say:**  
   > *"When a prospective student clicks an Instagram ad or messages our official WhatsApp number, it instantly pops up right here. The system captures their verified phone number and auto-assigns the student to a counsellor via round-robin."*

### Step 2: Show the Counsellor's Focused Workstation
1. Open the Admissions Dashboard tab ([https://chat.pranavcloud.in/admissions-dashboard/](https://chat.pranavcloud.in/admissions-dashboard/)).
2. Switch the top-right role dropdown to **Counsellor · Sneha Patel**.
3. Point out the green **COUNSELLOR** badge and the role banner (*"Restricted to 10 Assigned Students"*).
4. Notice how tabs 4 & 5 (WhatsApp Bot & Executive Dashboard) automatically disappear.
5. Click on **My Daily Tasks** to show Sneha's overdue call with Divya Joshi.
6. **Say:**  
   > *"Notice how the interface adapts. Counsellor Sneha only sees her 10 assigned students and her urgent follow-up tasks for today. Sensitive college financial figures and other teams' data are completely hidden."*

### Step 3: Show the 7-Stage Admission Pipeline & Document Checklist
1. Click the **My Pipeline** tab.
2. Click on student **Ananya Verma** (Stage: Fee Payment).
3. In the slide-over drawer:
   - Show the **Academics** scores (Class 10th: 92%, Class 12th: 89%, JEE: 91 %ile).
   - Show the **Documents Tab**: 4/4 marksheets verified by registrar.
   - Show the **Fees Tab**: Total ₹2,20,000 | Token Fee ₹55,000.
   - Click **Record Payment** to demonstrate instant seat confirmation.
4. **Say:**  
   > *"Everything regarding the student's admission journey is consolidated in one profile drawer: entrance scores, marksheet verification, and token fee deposit."*

### Step 4: Show the Management Dashboard (Registrar / Dean View)
1. Switch the role dropdown to **Administrator (Registrar / Dean)**.
2. Click on the **Management Dashboard** tab.
3. Show the **Executive KPI Cards**, **Admission Conversion Funnel**, **Lead Source Donut Chart**, and **Token Fee Collection Summary**.
4. **Say:**  
   > *"As Registrar or Director, you get complete real-time clarity without waiting for end-of-week reports: exactly how many seats were confirmed today, which ad channel brings the highest ROI, and which counsellors are driving conversions."*

---

## 7. Handling Client Objections & Tough Questions

#### Q1: "Why can't we just use Chatwoot without the Admissions Dashboard?"
> **Answer:** *"Chatwoot is a world-class messaging platform, but it doesn't know what Class 10/12 marksheets are, it doesn't track Indian college token admission fees, and it doesn't have a 7-stage academic pipeline. The Admissions Dashboard adds the exact business logic an educational institute needs, embedded directly inside Chatwoot."*

#### Q2: "Will our 30 counsellors get confused by using two different tools?"
> **Answer:** *"No, because counsellors don't experience them as two tools. The dashboard is embedded as a single tab directly inside their Chatwoot screen. They chat with students on the left, and manage the admission file on the right."*

#### Q3: "What if a student inquires through WhatsApp and also submits a Facebook ad form?"
> **Answer:** *"The built-in duplicate detection automatically catches the identical phone number, prevents double-assigning the student to different counsellors, and notifies the original counsellor of the new enquiry."*

#### Q4: "Can counsellors see college revenue or token fees collected by others?"
> **Answer:** *"No. Role-based permissions strictly lock down counsellors to their own students. Financial metrics, total collections, and the 30-member roster are restricted exclusively to Team Leads and the Registrar."*
