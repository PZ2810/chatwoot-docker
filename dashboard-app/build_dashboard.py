import json

# Script to build index.html for Admissions Dashboard (AdmitDesk)
# Styled to match Chatwoot UI design system and built for high-volume admissions handling.

INDEX_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AdmitDesk · Admissions CRM | Chatwoot Extension</title>
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Chart.js -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            brand: {
              50: '#eff6ff',
              100: '#dbeafe',
              200: '#bfdbfe',
              300: '#93c5fd',
              400: '#60a5fa',
              500: '#3b82f6',
              600: '#1f73e8', // Chatwoot Primary Blue
              700: '#1a68d1',
              800: '#1e40af',
              900: '#1e3a8a'
            },
            woot: {
              primary: '#1f73e8',
              hover: '#1a68d1',
              bg: '#f8fafc',
              border: '#e2e8f0',
              sidebar: '#1f2937'
            },
            wa: {
              bubble: '#dcf8c6',
              darkBubble: '#056162',
              bg: '#efeae2',
              green: '#25D366'
            }
          },
          fontFamily: {
            sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif']
          }
        }
      }
    }
  </script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    body { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }
    .custom-scroll::-webkit-scrollbar { width: 6px; height: 6px; }
    .custom-scroll::-webkit-scrollbar-track { background: transparent; }
    .custom-scroll::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 99px; }
    .custom-scroll::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
    .kanban-col { min-width: 285px; width: 285px; }
  </style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased min-h-screen">

  <!-- Main Container -->
  <div class="max-w-[1520px] mx-auto p-3 sm:p-5 lg:p-6 space-y-4">

    <!-- Top Chatwoot-Style Header Bar -->
    <header class="bg-white rounded-xl p-4 sm:p-5 border border-slate-200/90 shadow-xs flex flex-col md:flex-row md:items-center md:justify-between gap-4">
      <div class="flex items-center space-x-3.5">
        <!-- Chatwoot Brand Badge -->
        <div class="w-10 h-10 rounded-xl bg-blue-600 flex items-center justify-center text-white shadow-xs">
          <i data-lucide="graduation-cap" class="w-5 h-5"></i>
        </div>
        <div>
          <div class="flex items-center gap-2 flex-wrap">
            <h1 class="text-lg sm:text-xl font-bold text-slate-900 tracking-tight flex items-center gap-1.5">
              <span>AdmitDesk</span>
              <span class="text-slate-400 font-normal">|</span>
              <span class="text-blue-600 font-semibold">Admissions CRM</span>
            </h1>
            <span class="text-[11px] px-2 py-0.5 rounded-md font-semibold bg-blue-50 text-blue-700 border border-blue-200">
              Chatwoot App
            </span>
            <span class="inline-flex items-center px-2 py-0.5 rounded-md text-[11px] font-medium bg-emerald-50 text-emerald-700 border border-emerald-200">
              <span class="w-1.5 h-1.5 mr-1.5 rounded-full bg-emerald-500 animate-pulse"></span> Live Synced
            </span>
          </div>
          <p class="text-xs text-slate-500 mt-0.5">Apex Institute of Technology & Management • Academic Intake 2026–27</p>
        </div>
      </div>

      <!-- Header Controls: Role Selector, Add Lead, Import, Chatwoot Link -->
      <div class="flex flex-wrap items-center gap-2">
        
        <!-- Role Switcher -->
        <div class="flex items-center bg-slate-50 border border-slate-200 rounded-lg px-2.5 py-1.5 text-xs">
          <i data-lucide="shield-check" class="w-3.5 h-3.5 text-blue-600 mr-1.5"></i>
          <span class="text-slate-400 mr-1.5 hidden sm:inline">Role:</span>
          <select id="roleSelector" onchange="switchRole(this.value)" class="bg-transparent font-medium text-slate-800 focus:outline-none cursor-pointer">
            <option value="admin">Administrator · Registrar Office</option>
            <option value="lead">Team Lead · Priya Sharma</option>
            <option value="sneha">Counsellor · Sneha Patel</option>
            <option value="amit">Counsellor · Amit Kumar</option>
          </select>
        </div>

        <!-- Quick Add Lead Button -->
        <button onclick="openAddModal()" class="inline-flex items-center px-3 py-1.5 text-xs font-semibold text-white bg-blue-600 hover:bg-blue-700 rounded-lg shadow-xs transition">
          <i data-lucide="plus" class="w-3.5 h-3.5 mr-1"></i> Add Lead
        </button>

        <!-- Bulk CSV Import Button -->
        <button onclick="openImportModal()" class="inline-flex items-center px-3 py-1.5 text-xs font-semibold text-slate-700 bg-white hover:bg-slate-50 border border-slate-200 rounded-lg shadow-xs transition">
          <i data-lucide="upload" class="w-3.5 h-3.5 mr-1 text-slate-500"></i> Import CSV
        </button>

        <!-- Open in Chatwoot -->
        <a href="https://chat.pranavcloud.in" target="_blank" class="inline-flex items-center px-3 py-1.5 text-xs font-semibold text-blue-600 bg-blue-50 hover:bg-blue-100 border border-blue-200 rounded-lg transition" title="Open Chatwoot Inbox in new tab">
          <i data-lucide="external-link" class="w-3.5 h-3.5 mr-1"></i> Open Inbox
        </a>
      </div>
    </header>

    <!-- Navigation Tabs (Chatwoot Clean Design) -->
    <nav class="flex items-center bg-white p-1 rounded-xl border border-slate-200/90 shadow-xs gap-1 overflow-x-auto text-xs font-semibold text-slate-600">
      
      <button onclick="setTab('dash')" id="tab-dash" class="flex items-center gap-1.5 px-3.5 py-2 rounded-lg transition bg-blue-50 text-blue-700 font-bold border border-blue-200/60">
        <i data-lucide="layout-dashboard" class="w-4 h-4"></i>
        <span>Executive Overview</span>
      </button>

      <button onclick="setTab('pipe')" id="tab-pipe" class="flex items-center gap-1.5 px-3.5 py-2 rounded-lg transition hover:bg-slate-50 text-slate-600 border border-transparent">
        <i data-lucide="layers" class="w-4 h-4"></i>
        <span>Leads & Admission Pipeline</span>
        <span class="bg-blue-100 text-blue-800 text-[10px] px-2 py-0.5 rounded-full font-bold ml-0.5" id="pipeLeadCount">28</span>
      </button>

      <button onclick="setTab('tasks')" id="tab-tasks" class="flex items-center gap-1.5 px-3.5 py-2 rounded-lg transition hover:bg-slate-50 text-slate-600 border border-transparent">
        <i data-lucide="check-square" class="w-4 h-4"></i>
        <span>My Daily Tasks & Follow-ups</span>
        <span class="bg-rose-100 text-rose-700 text-[10px] px-2 py-0.5 rounded-full font-bold ml-0.5" id="overdueBadge">2 Overdue</span>
      </button>

      <button onclick="setTab('wa')" id="tab-wa" class="flex items-center gap-1.5 px-3.5 py-2 rounded-lg transition hover:bg-slate-50 text-slate-600 border border-transparent">
        <i data-lucide="message-circle" class="w-4 h-4 text-emerald-600"></i>
        <span>WhatsApp Automation</span>
        <span class="bg-emerald-50 text-emerald-700 text-[10px] px-2 py-0.5 rounded-full font-semibold ml-0.5">6 Active</span>
      </button>

      <button onclick="setTab('team')" id="tab-team" class="flex items-center gap-1.5 px-3.5 py-2 rounded-lg transition hover:bg-slate-50 text-slate-600 border border-transparent">
        <i data-lucide="users" class="w-4 h-4"></i>
        <span>Counsellor Team & Roles</span>
      </button>

    </nav>

    <!-- ========================================== -->
    <!-- VIEW 1: EXECUTIVE DASHBOARD               -->
    <!-- ========================================== -->
    <div id="view-dash" class="space-y-4">
      
      <!-- Top 4 KPI Metric Cards -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        
        <!-- Total Enquiries -->
        <div class="bg-white rounded-xl p-4 sm:p-5 border border-slate-200/90 shadow-xs hover:border-slate-300 transition">
          <div class="flex items-center justify-between">
            <span class="text-xs font-semibold uppercase tracking-wider text-slate-500">Total Enquiries</span>
            <div class="w-8 h-8 rounded-lg bg-blue-50 text-blue-600 flex items-center justify-center">
              <i data-lucide="user-plus" class="w-4 h-4"></i>
            </div>
          </div>
          <div class="mt-2.5 flex items-baseline justify-between">
            <b class="text-2xl sm:text-3xl font-bold text-slate-900" id="kpi-leads">28</b>
            <span class="text-xs font-semibold text-emerald-600 flex items-center">
              <i data-lucide="trending-up" class="w-3.5 h-3.5 mr-0.5"></i> +14% vs last wk
            </span>
          </div>
          <p class="mt-1 text-xs text-slate-400">Captured across WhatsApp, Web & FB Ads</p>
        </div>

        <!-- Active Pipeline -->
        <div class="bg-white rounded-xl p-4 sm:p-5 border border-slate-200/90 shadow-xs hover:border-slate-300 transition">
          <div class="flex items-center justify-between">
            <span class="text-xs font-semibold uppercase tracking-wider text-slate-500">Active In Counselling</span>
            <div class="w-8 h-8 rounded-lg bg-amber-50 text-amber-600 flex items-center justify-center">
              <i data-lucide="phone-call" class="w-4 h-4"></i>
            </div>
          </div>
          <div class="mt-2.5 flex items-baseline justify-between">
            <b class="text-2xl sm:text-3xl font-bold text-slate-900" id="kpi-pipeline">17</b>
            <span class="text-xs font-semibold text-amber-600 flex items-center">
              <i data-lucide="clock" class="w-3.5 h-3.5 mr-0.5"></i> 4 Due Today
            </span>
          </div>
          <p class="mt-1 text-xs text-slate-400">Stages: Counselling, Follow-up, App</p>
        </div>

        <!-- Document Verification Rate -->
        <div class="bg-white rounded-xl p-4 sm:p-5 border border-slate-200/90 shadow-xs hover:border-slate-300 transition">
          <div class="flex items-center justify-between">
            <span class="text-xs font-semibold uppercase tracking-wider text-slate-500">Doc Verification Rate</span>
            <div class="w-8 h-8 rounded-lg bg-purple-50 text-purple-600 flex items-center justify-center">
              <i data-lucide="file-check" class="w-4 h-4"></i>
            </div>
          </div>
          <div class="mt-2.5 flex items-baseline justify-between">
            <b class="text-2xl sm:text-3xl font-bold text-slate-900" id="kpi-docs">64.3%</b>
            <span class="text-xs font-semibold text-purple-600 flex items-center">
              <i data-lucide="check-circle" class="w-3.5 h-3.5 mr-0.5"></i> 18 Verified
            </span>
          </div>
          <p class="mt-1 text-xs text-slate-400">10th, 12th & Govt ID checklists</p>
        </div>

        <!-- Total Fee Collection -->
        <div class="bg-white rounded-xl p-4 sm:p-5 border border-slate-200/90 shadow-xs hover:border-slate-300 transition">
          <div class="flex items-center justify-between">
            <span class="text-xs font-semibold uppercase tracking-wider text-slate-500">Token Fee Collections</span>
            <div class="w-8 h-8 rounded-lg bg-emerald-50 text-emerald-600 flex items-center justify-center">
              <i data-lucide="indian-rupee" class="w-4 h-4"></i>
            </div>
          </div>
          <div class="mt-2.5 flex items-baseline justify-between">
            <b class="text-2xl sm:text-3xl font-bold text-slate-900" id="kpi-fee">₹1,26,250</b>
            <span class="text-xs font-semibold text-emerald-600 flex items-center">
              <i data-lucide="badge-check" class="w-3.5 h-3.5 mr-0.5"></i> 3 Confirmed
            </span>
          </div>
          <p class="mt-1 text-xs text-slate-400">Confirmed seats & admission tokens</p>
        </div>

      </div>

      <!-- Funnel Progress & Channels Breakdown -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-4">
        
        <!-- Admission Pipeline Funnel -->
        <div class="lg:col-span-2 bg-white rounded-xl p-4 sm:p-5 border border-slate-200/90 shadow-xs space-y-4">
          <div class="flex items-center justify-between">
            <div>
              <h2 class="text-sm font-bold text-slate-900">Admissions Pipeline Stage Breakdown</h2>
              <p class="text-xs text-slate-500">Live distribution of all active student leads</p>
            </div>
            <button onclick="setTab('pipe')" class="text-xs text-blue-600 font-semibold hover:underline flex items-center gap-1">
              Open Full Pipeline <i data-lucide="arrow-right" class="w-3 h-3"></i>
            </button>
          </div>

          <!-- Dynamic Funnel Horizontal Bars -->
          <div id="funnelBars" class="space-y-2.5 pt-1">
            <!-- Populated dynamically by JS -->
          </div>
        </div>

        <!-- Lead Channels Distribution Donut -->
        <div class="bg-white rounded-xl p-4 sm:p-5 border border-slate-200/90 shadow-xs flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-3">
              <h2 class="text-sm font-bold text-slate-900">Lead Source Channels</h2>
              <span class="text-xs font-semibold bg-blue-50 text-blue-700 px-2 py-0.5 rounded">All Channels</span>
            </div>
            <p class="text-xs text-slate-500 mb-4">Channel acquisition split for current intake</p>
            
            <div class="relative h-44 flex items-center justify-center">
              <canvas id="sourceDonut"></canvas>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-2 pt-3 border-t border-slate-100 text-xs">
            <div class="flex items-center gap-2">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
              <span class="text-slate-600">WhatsApp (36%)</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="w-2.5 h-2.5 rounded-full bg-blue-600"></span>
              <span class="text-slate-600">Website (28%)</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="w-2.5 h-2.5 rounded-full bg-indigo-500"></span>
              <span class="text-slate-600">FB / Meta Ads (22%)</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="w-2.5 h-2.5 rounded-full bg-amber-500"></span>
              <span class="text-slate-600">Phone / Walk-in (14%)</span>
            </div>
          </div>
        </div>

      </div>

      <!-- Quick Recent Leads Table -->
      <div class="bg-white rounded-xl p-4 sm:p-5 border border-slate-200/90 shadow-xs space-y-3">
        <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2">
          <div>
            <h2 class="text-sm font-bold text-slate-900 flex items-center gap-2">
              <span>Priority Student Enquiries</span>
              <span class="text-xs font-medium text-slate-500 bg-slate-100 px-2 py-0.5 rounded-full">Top 6 recent</span>
            </h2>
            <p class="text-xs text-slate-500">Click any student row to view full profile drawer or advance stage</p>
          </div>
          <button onclick="setTab('pipe')" class="text-xs text-blue-600 font-semibold hover:underline flex items-center gap-1 self-start sm:self-auto">
            View All 28 Leads in Pipeline <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
          </button>
        </div>

        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs">
            <thead>
              <tr class="text-slate-400 font-semibold border-b border-slate-100 uppercase text-[10px] tracking-wider">
                <th class="pb-2.5 font-medium">Student</th>
                <th class="pb-2.5 font-medium">Phone & WhatsApp</th>
                <th class="pb-2.5 font-medium">Course & City</th>
                <th class="pb-2.5 font-medium">Channel</th>
                <th class="pb-2.5 font-medium">Stage</th>
                <th class="pb-2.5 font-medium">Counsellor</th>
                <th class="pb-2.5 font-medium">Follow-up</th>
                <th class="pb-2.5 font-medium text-right">Actions</th>
              </tr>
            </thead>
            <tbody id="quickLeadsTable" class="divide-y divide-slate-100">
              <!-- populated by JS -->
            </tbody>
          </table>
        </div>
      </div>

    </div>

    <!-- ========================================== -->
    <!-- VIEW 2: LEADS & ADMISSION PIPELINE        -->
    <!-- ========================================== -->
    <div id="view-pipe" class="hidden space-y-4">
      
      <!-- Toolbar: View Switcher, Counts, Search, Filters -->
      <div class="bg-white rounded-xl p-4 border border-slate-200/90 shadow-xs space-y-3">
        
        <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-3">
          <div>
            <h2 class="text-base font-bold text-slate-900 flex items-center gap-2">
              <span>Student Leads & Admission Pipeline</span>
              <span id="filteredLeadsBadge" class="text-xs font-medium bg-blue-50 text-blue-700 px-2.5 py-0.5 rounded-full border border-blue-200">
                28 Total Leads
              </span>
            </h2>
            <p class="text-xs text-slate-500 mt-0.5">Manage student enquiries across all 7 admission stages</p>
          </div>

          <!-- Dual View Switcher (Table vs Kanban) -->
          <div class="flex items-center gap-2">
            <div class="flex items-center bg-slate-100 p-1 rounded-lg border border-slate-200 text-xs font-semibold">
              <button onclick="setPipeView('table')" id="btn-view-table" class="flex items-center gap-1.5 px-3 py-1.5 rounded-md bg-white text-slate-800 shadow-xs">
                <i data-lucide="table" class="w-3.5 h-3.5 text-blue-600"></i> Table View
              </button>
              <button onclick="setPipeView('kanban')" id="btn-view-kanban" class="flex items-center gap-1.5 px-3 py-1.5 rounded-md text-slate-600 hover:text-slate-900">
                <i data-lucide="kanban" class="w-3.5 h-3.5"></i> Kanban Board
              </button>
            </div>

            <!-- Export to CSV -->
            <button onclick="exportCurrentLeadsCSV()" class="inline-flex items-center px-3 py-1.5 text-xs font-semibold text-slate-700 bg-white hover:bg-slate-50 border border-slate-200 rounded-lg shadow-xs transition" title="Export current filtered list to CSV">
              <i data-lucide="download" class="w-3.5 h-3.5 mr-1 text-slate-500"></i> Export
            </button>
          </div>
        </div>

        <!-- Search & Multi-Filter Bar -->
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-6 gap-2 pt-1 border-t border-slate-100">
          
          <!-- Instant Search Box -->
          <div class="relative md:col-span-2">
            <i data-lucide="search" class="w-3.5 h-3.5 text-slate-400 absolute left-3 top-3"></i>
            <input type="text" id="leadSearchInput" oninput="applyFilters()" placeholder="Search student name, phone, city, course..." class="w-full pl-9 pr-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:bg-white focus:outline-none focus:ring-1 focus:ring-blue-500 text-slate-800 placeholder-slate-400">
          </div>

          <!-- Stage Filter -->
          <div>
            <select id="filterStage" onchange="applyFilters()" class="w-full px-2.5 py-2 text-xs bg-slate-50 border border-slate-200 rounded-lg text-slate-700 focus:bg-white focus:outline-none focus:ring-1 focus:ring-blue-500 cursor-pointer">
              <option value="">All Stages (7)</option>
              <option value="Enquiry">1. Enquiry</option>
              <option value="Counselling">2. Counselling</option>
              <option value="Follow-up">3. Follow-up</option>
              <option value="Application">4. Application</option>
              <option value="Doc Verification">5. Doc Verification</option>
              <option value="Fee Payment">6. Fee Payment</option>
              <option value="Enrollment">7. Enrollment</option>
            </select>
          </div>

          <!-- Counsellor Filter -->
          <div>
            <select id="filterCounsellor" onchange="applyFilters()" class="w-full px-2.5 py-2 text-xs bg-slate-50 border border-slate-200 rounded-lg text-slate-700 focus:bg-white focus:outline-none focus:ring-1 focus:ring-blue-500 cursor-pointer">
              <option value="">All Counsellors</option>
              <option value="Sneha Patel">Sneha Patel</option>
              <option value="Amit Kumar">Amit Kumar</option>
              <option value="Priya Sharma">Priya Sharma</option>
            </select>
          </div>

          <!-- Course Filter -->
          <div>
            <select id="filterCourse" onchange="applyFilters()" class="w-full px-2.5 py-2 text-xs bg-slate-50 border border-slate-200 rounded-lg text-slate-700 focus:bg-white focus:outline-none focus:ring-1 focus:ring-blue-500 cursor-pointer">
              <option value="">All Courses</option>
              <option value="MBA">MBA</option>
              <option value="B.Tech CSE">B.Tech CSE</option>
              <option value="BBA">BBA</option>
              <option value="MCA">MCA</option>
              <option value="BCA">BCA</option>
              <option value="B.Sc Nursing">B.Sc Nursing</option>
              <option value="Data Science">Data Science</option>
              <option value="B.Des">B.Des</option>
            </select>
          </div>

          <!-- Urgency & Reset Button -->
          <div class="flex items-center gap-1.5">
            <select id="filterUrgency" onchange="applyFilters()" class="w-full px-2.5 py-2 text-xs bg-slate-50 border border-slate-200 rounded-lg text-slate-700 focus:bg-white focus:outline-none focus:ring-1 focus:ring-blue-500 cursor-pointer">
              <option value="">All Follow-ups</option>
              <option value="overdue">🚨 Overdue</option>
              <option value="today">📅 Today</option>
              <option value="upcoming">🗓️ Upcoming</option>
            </select>

            <button onclick="resetFilters()" class="px-2.5 py-2 text-xs text-slate-500 hover:text-slate-800 bg-slate-100 hover:bg-slate-200 rounded-lg transition" title="Clear all filters">
              <i data-lucide="rotate-ccw" class="w-3.5 h-3.5"></i>
            </button>
          </div>

        </div>

      </div>

      <!-- TABLE VIEW CONTAINER -->
      <div id="pipeTableView" class="bg-white rounded-xl border border-slate-200/90 shadow-xs overflow-hidden">
        
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs">
            <thead class="bg-slate-50/80 border-b border-slate-200">
              <tr class="text-slate-500 font-semibold uppercase text-[10px] tracking-wider">
                <th class="p-3 w-10 text-center">#</th>
                <th class="py-3 px-2 font-medium">Student Name & Contact</th>
                <th class="py-3 px-2 font-medium">Course & Intake</th>
                <th class="py-3 px-2 font-medium">Source</th>
                <th class="py-3 px-2 font-medium">Counsellor</th>
                <th class="py-3 px-2 font-medium">Admission Stage</th>
                <th class="py-3 px-2 font-medium">Documents</th>
                <th class="py-3 px-2 font-medium">Fee Status</th>
                <th class="py-3 px-2 font-medium">Follow-up</th>
                <th class="py-3 px-3 font-medium text-right">Actions</th>
              </tr>
            </thead>
            <tbody id="pipeTableBody" class="divide-y divide-slate-100">
              <!-- Populated by JS -->
            </tbody>
          </table>
        </div>

        <!-- Pagination Controls Footer -->
        <div class="px-4 py-3 bg-slate-50/60 border-t border-slate-200 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-slate-500">
          <div class="flex items-center gap-2">
            <span>Rows per page:</span>
            <select id="pageSizeSelect" onchange="changePageSize(this.value)" class="bg-white border border-slate-200 rounded px-2 py-1 text-xs text-slate-700 cursor-pointer">
              <option value="10">10</option>
              <option value="25">25</option>
              <option value="all">All</option>
            </select>
            <span id="paginationInfo" class="ml-2 font-medium text-slate-700">Showing 1 to 10 of 28</span>
          </div>

          <div class="flex items-center gap-1">
            <button onclick="prevPage()" id="btnPrevPage" class="px-2.5 py-1 rounded border border-slate-200 bg-white text-slate-700 hover:bg-slate-50 disabled:opacity-40 disabled:cursor-not-allowed">
              Previous
            </button>
            <div id="paginationPageBtns" class="flex items-center gap-1">
              <!-- Page number buttons populated by JS -->
            </div>
            <button onclick="nextPage()" id="btnNextPage" class="px-2.5 py-1 rounded border border-slate-200 bg-white text-slate-700 hover:bg-slate-50 disabled:opacity-40 disabled:cursor-not-allowed">
              Next
            </button>
          </div>
        </div>

      </div>

      <!-- KANBAN VIEW CONTAINER -->
      <div id="pipeKanbanView" class="hidden">
        <div class="flex gap-3 overflow-x-auto pb-4 custom-scroll" id="kanbanBoard">
          <!-- 7 Stage Columns populated dynamically by JS -->
        </div>
      </div>

    </div>

    <!-- ========================================== -->
    <!-- VIEW 3: MY FOLLOW-UPS (DAILY TASKS)        -->
    <!-- ========================================== -->
    <div id="view-tasks" class="hidden space-y-4">
      
      <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2">
        <div>
          <h2 class="text-base font-bold text-slate-900 flex items-center gap-2">
            <span>Counsellor Daily Tasks & Follow-ups</span>
            <span class="text-xs bg-slate-100 text-slate-600 px-2.5 py-0.5 rounded-full font-medium" id="taskCounsellorName">
              All Team
            </span>
          </h2>
          <p class="text-xs text-slate-500 mt-0.5">Prioritized schedule of student callbacks, follow-ups, and document requests</p>
        </div>

        <div class="flex items-center gap-2">
          <span class="text-xs px-2.5 py-1 rounded-md bg-rose-50 text-rose-700 font-semibold border border-rose-200 flex items-center gap-1">
            <span class="w-2 h-2 rounded-full bg-rose-500 animate-pulse"></span>
            <span id="taskOverdueCount">2 Overdue</span>
          </span>
          <span class="text-xs px-2.5 py-1 rounded-md bg-amber-50 text-amber-700 font-semibold border border-amber-200 flex items-center gap-1">
            <i data-lucide="calendar" class="w-3.5 h-3.5"></i>
            <span id="taskTodayCount">4 Due Today</span>
          </span>
        </div>
      </div>

      <!-- 1. OVERDUE FOLLOW-UPS (IMMEDIATE ATTENTION) -->
      <div class="bg-white rounded-xl p-4 sm:p-5 border border-rose-200 shadow-xs space-y-3">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2">
            <div class="w-7 h-7 rounded-lg bg-rose-100 text-rose-700 flex items-center justify-center font-bold text-xs">
              <i data-lucide="alert-triangle" class="w-4 h-4"></i>
            </div>
            <div>
              <h3 class="text-sm font-bold text-rose-900">Overdue Follow-ups (Action Required)</h3>
              <p class="text-xs text-rose-600">These student follow-ups have passed their scheduled call date</p>
            </div>
          </div>
          <span class="text-xs font-bold text-rose-700 bg-rose-50 px-2 py-0.5 rounded border border-rose-200" id="overdueCountLabel">
            2 Students
          </span>
        </div>

        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs">
            <thead>
              <tr class="text-slate-400 font-semibold border-b border-rose-100 uppercase text-[10px]">
                <th class="pb-2">Student</th>
                <th class="pb-2">Phone</th>
                <th class="pb-2">Course</th>
                <th class="pb-2">Stage</th>
                <th class="pb-2">Scheduled Date</th>
                <th class="pb-2">Assigned To</th>
                <th class="pb-2 text-right">Quick Action</th>
              </tr>
            </thead>
            <tbody id="overdueTasksTable" class="divide-y divide-rose-50">
              <!-- populated by JS -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- 2. DUE TODAY TABLE -->
      <div class="bg-white rounded-xl p-4 sm:p-5 border border-slate-200/90 shadow-xs space-y-3">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2">
            <div class="w-7 h-7 rounded-lg bg-amber-100 text-amber-700 flex items-center justify-center font-bold text-xs">
              <i data-lucide="clock" class="w-4 h-4"></i>
            </div>
            <div>
              <h3 class="text-sm font-bold text-slate-900">Scheduled for Today (19 Nov 2026)</h3>
              <p class="text-xs text-slate-500">Call students, update notes, or mark follow-up completed</p>
            </div>
          </div>
          <span class="text-xs font-bold text-amber-700 bg-amber-50 px-2 py-0.5 rounded border border-amber-200" id="todayTasksCountLabel">
            4 Students
          </span>
        </div>

        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs">
            <thead>
              <tr class="text-slate-400 font-semibold border-b border-slate-100 uppercase text-[10px]">
                <th class="pb-2">Student</th>
                <th class="pb-2">Phone</th>
                <th class="pb-2">Course</th>
                <th class="pb-2">Stage</th>
                <th class="pb-2">Assigned To</th>
                <th class="pb-2">Last Note</th>
                <th class="pb-2 text-right">Quick Action</th>
              </tr>
            </thead>
            <tbody id="dueTodayTasksTable" class="divide-y divide-slate-100">
              <!-- populated by JS -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- 3. UPCOMING FOLLOW-UPS -->
      <div class="bg-white rounded-xl p-4 sm:p-5 border border-slate-200/90 shadow-xs space-y-3">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2">
            <div class="w-7 h-7 rounded-lg bg-blue-100 text-blue-700 flex items-center justify-center font-bold text-xs">
              <i data-lucide="calendar" class="w-4 h-4"></i>
            </div>
            <div>
              <h3 class="text-sm font-bold text-slate-900">Upcoming Next 7 Days</h3>
              <p class="text-xs text-slate-500">Scheduled follow-up consultations in queue</p>
            </div>
          </div>
          <span class="text-xs font-bold text-blue-700 bg-blue-50 px-2 py-0.5 rounded border border-blue-200" id="upcomingCountLabel">
            Upcoming
          </span>
        </div>

        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs">
            <thead>
              <tr class="text-slate-400 font-semibold border-b border-slate-100 uppercase text-[10px]">
                <th class="pb-2">Student</th>
                <th class="pb-2">Phone</th>
                <th class="pb-2">Course</th>
                <th class="pb-2">Stage</th>
                <th class="pb-2">Scheduled Date</th>
                <th class="pb-2">Assigned To</th>
                <th class="pb-2 text-right">Quick Action</th>
              </tr>
            </thead>
            <tbody id="upcomingTasksTable" class="divide-y divide-slate-100">
              <!-- populated by JS -->
            </tbody>
          </table>
        </div>
      </div>

    </div>

    <!-- ========================================== -->
    <!-- VIEW 4: WHATSAPP AUTOMATION & TEMPLATES    -->
    <!-- ========================================== -->
    <div id="view-wa" class="hidden space-y-4">
      
      <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2">
        <div>
          <h2 class="text-base font-bold text-slate-900 flex items-center gap-2">
            <span>WhatsApp Admissions Automation</span>
            <span class="text-xs bg-emerald-50 text-emerald-700 px-2 py-0.5 rounded-full border border-emerald-200 font-semibold">
              WhatsApp Business Cloud API
            </span>
          </h2>
          <p class="text-xs text-slate-500 mt-0.5">Automated student messages triggered on pipeline stage transitions</p>
        </div>

        <button onclick="triggerBroadcastModal()" class="px-3.5 py-1.5 text-xs font-semibold bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg shadow-xs transition flex items-center gap-1.5 self-start sm:self-auto">
          <i data-lucide="send" class="w-3.5 h-3.5"></i> Test Trigger Live Message
        </button>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-5">
        
        <!-- Left: Template Rules List (7 cols) -->
        <div class="lg:col-span-7 space-y-3" id="templateList">
          <!-- Populated by JS -->
        </div>

        <!-- Right: Interactive Smartphone Preview (5 cols) -->
        <div class="lg:col-span-5 flex flex-col items-center">
          
          <div class="w-full max-w-[340px] bg-slate-900 rounded-[38px] p-3 shadow-xl border-4 border-slate-800">
            <!-- Phone Notch & Speaker -->
            <div class="w-28 h-4 bg-slate-800 rounded-full mx-auto mb-2 flex items-center justify-center">
              <span class="w-8 h-1 bg-slate-700 rounded-full"></span>
            </div>

            <!-- Screen Container -->
            <div class="bg-[#efeae2] rounded-[28px] overflow-hidden flex flex-col h-[520px] shadow-inner text-xs">
              
              <!-- WhatsApp Header -->
              <div class="bg-[#075E54] text-white p-3 flex items-center space-x-2.5">
                <i data-lucide="arrow-left" class="w-4 h-4 cursor-pointer"></i>
                <div class="w-8 h-8 rounded-full bg-white/20 flex items-center justify-center font-bold text-xs text-white">
                  AI
                </div>
                <div class="flex-1 min-w-0">
                  <div class="font-bold text-xs truncate">Apex Admissions Office</div>
                  <div class="text-[10px] text-emerald-200 flex items-center">
                    <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 mr-1 inline-block"></span> Official Verified Account
                  </div>
                </div>
                <i data-lucide="phone" class="w-3.5 h-3.5"></i>
              </div>

              <!-- Chat Message Bubble Area -->
              <div class="flex-1 p-3 space-y-3 overflow-y-auto custom-scroll flex flex-col justify-end" id="waPreviewArea">
                <div class="text-center">
                  <span class="bg-white/80 text-slate-500 text-[10px] px-2.5 py-0.5 rounded-md shadow-xs">Today</span>
                </div>

                <!-- WhatsApp Message Bubble -->
                <div class="bg-white rounded-lg p-3 shadow-xs border border-slate-200/60 max-w-[92%] self-start relative">
                  <div class="text-[11px] font-bold text-emerald-700 mb-1" id="previewSender">Apex Admissions Bot</div>
                  <p class="text-slate-800 leading-relaxed text-[11px]" id="phoneBubbleText">
                    Hi Rahul Sharma, thank you for your enquiry for MBA at Apex Institute. Your counsellor Sneha Patel will call you shortly.
                  </p>
                  <div class="text-[9px] text-slate-400 text-right mt-1.5 flex items-center justify-end gap-1">
                    <span>10:45 AM</span>
                    <i data-lucide="check-check" class="w-3 h-3 text-blue-500"></i>
                  </div>
                </div>
              </div>

              <!-- WhatsApp Input Bar (Mock) -->
              <div class="bg-[#f0f2f5] p-2 flex items-center space-x-1.5 border-t border-slate-200">
                <div class="flex-1 bg-white rounded-full px-3 py-1.5 text-[11px] text-slate-400 flex items-center">
                  <span>Type a reply...</span>
                </div>
                <div class="w-7 h-7 rounded-full bg-[#128C7E] flex items-center justify-center text-white">
                  <i data-lucide="send" class="w-3.5 h-3.5"></i>
                </div>
              </div>

            </div>
          </div>

          <p class="text-xs text-slate-400 mt-2 text-center">
            Simulates dynamic variables: <code class="text-blue-600 bg-blue-50 px-1 py-0.5 rounded">{name}</code>, <code class="text-blue-600 bg-blue-50 px-1 py-0.5 rounded">{course}</code>, <code class="text-blue-600 bg-blue-50 px-1 py-0.5 rounded">{counsellor}</code>
          </p>

        </div>

      </div>

    </div>

    <!-- ========================================== -->
    <!-- VIEW 5: COUNSELLORS & ROLES               -->
    <!-- ========================================== -->
    <div id="view-team" class="hidden space-y-4">
      
      <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2">
        <div>
          <h2 class="text-base font-bold text-slate-900">Admissions Team Performance & Workload</h2>
          <p class="text-xs text-slate-500 mt-0.5">Role-based access, lead distribution, conversion rates, and token fees collected</p>
        </div>

        <div class="flex items-center gap-2">
          <span class="text-xs font-medium text-slate-500 bg-slate-100 px-3 py-1.5 rounded-lg border border-slate-200">
            Auto-Assignment: Round-Robin Active
          </span>
        </div>
      </div>

      <!-- Team Members Performance Table -->
      <div class="bg-white rounded-xl border border-slate-200/90 shadow-xs overflow-hidden">
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs">
            <thead class="bg-slate-50/80 border-b border-slate-200">
              <tr class="text-slate-500 font-semibold uppercase text-[10px] tracking-wider">
                <th class="p-3">Team Member</th>
                <th class="py-3 px-2">Role & Department</th>
                <th class="py-3 px-2">Active Leads</th>
                <th class="py-3 px-2">Today's Tasks</th>
                <th class="py-3 px-2">Enrolled Confirmed</th>
                <th class="py-3 px-2">Conversion %</th>
                <th class="py-3 px-2">Token Fees Collected</th>
                <th class="py-3 px-2 text-right">Workload Status</th>
              </tr>
            </thead>
            <tbody id="counsellorTableBody" class="divide-y divide-slate-100">
              <!-- populated by JS -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- Role Permissions Matrix (Chatwoot Roles) -->
      <div class="bg-white rounded-xl p-5 border border-slate-200/90 shadow-xs space-y-3">
        <h3 class="text-sm font-bold text-slate-900">Role-Based Access Control (RBAC) in Chatwoot</h3>
        <p class="text-xs text-slate-500">AdmitDesk integrates natively with Chatwoot's user roles and permissions</p>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-3 pt-2">
          <div class="p-3 rounded-lg border border-slate-200 bg-slate-50/50 space-y-2">
            <div class="flex items-center justify-between">
              <b class="text-xs font-bold text-slate-800">1. Administrator / Registrar</b>
              <span class="text-[10px] bg-blue-100 text-blue-800 px-2 py-0.5 rounded font-semibold">Full Access</span>
            </div>
            <p class="text-[11px] text-slate-500 leading-relaxed">
              Full visibility into all counsellors, financial fee reports, stage transitions, macro triggers, and bulk Excel imports.
            </p>
          </div>

          <div class="p-3 rounded-lg border border-slate-200 bg-slate-50/50 space-y-2">
            <div class="flex items-center justify-between">
              <b class="text-xs font-bold text-slate-800">2. Team Lead</b>
              <span class="text-[10px] bg-purple-100 text-purple-800 px-2 py-0.5 rounded font-semibold">Supervisor</span>
            </div>
            <p class="text-[11px] text-slate-500 leading-relaxed">
              Reassign leads between counsellors, resolve stalled follow-ups, oversee document verification, and manage team schedules.
            </p>
          </div>

          <div class="p-3 rounded-lg border border-slate-200 bg-slate-50/50 space-y-2">
            <div class="flex items-center justify-between">
              <b class="text-xs font-bold text-slate-800">3. Admissions Counsellor</b>
              <span class="text-[10px] bg-emerald-100 text-emerald-800 px-2 py-0.5 rounded font-semibold">Assigned Only</span>
            </div>
            <p class="text-[11px] text-slate-500 leading-relaxed">
              Manages assigned enquiries, conducts phone/WhatsApp consultations, updates document statuses, and schedules next follow-ups.
            </p>
          </div>
        </div>
      </div>

    </div>

  </div> <!-- End Main Container -->

  <!-- ========================================== -->
  <!-- SLIDE-OVER STUDENT PROFILE DRAWER         -->
  <!-- ========================================== -->
  <div id="studentDrawerBackdrop" onclick="closeDrawer()" class="fixed inset-0 bg-slate-900/40 backdrop-blur-xs z-40 hidden transition-opacity"></div>
  
  <div id="studentDrawer" class="fixed right-0 top-0 bottom-0 w-full max-w-[520px] bg-white shadow-2xl z-50 transform translate-x-full transition-transform duration-200 ease-in-out flex flex-col">
    
    <!-- Drawer Header -->
    <div class="p-4 sm:p-5 border-b border-slate-200 bg-slate-50/70 flex items-start justify-between">
      <div class="flex items-center space-x-3">
        <div class="w-11 h-11 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold text-sm shadow-xs" id="drawerAvatar">
          RS
        </div>
        <div>
          <div class="flex items-center gap-2">
            <h3 class="text-base font-bold text-slate-900" id="drawerName">Student Name</h3>
            <span class="text-[11px] font-semibold px-2 py-0.5 rounded-full" id="drawerStagePill">Enquiry</span>
          </div>
          <p class="text-xs text-slate-500" id="drawerSubline">Course • City • Application ID</p>
        </div>
      </div>

      <button onclick="closeDrawer()" class="text-slate-400 hover:text-slate-700 p-1 rounded-lg hover:bg-slate-200 transition">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>
    </div>

    <!-- Quick Action Bar (Open in Chatwoot, WhatsApp, Call) -->
    <div class="px-4 py-2.5 bg-white border-b border-slate-200 flex items-center gap-2 text-xs">
      <a id="drawerChatwootLink" href="https://chat.pranavcloud.in" target="_blank" class="flex-1 py-1.5 px-3 bg-blue-50 text-blue-700 hover:bg-blue-100 border border-blue-200 rounded-lg font-semibold flex items-center justify-center gap-1.5 transition">
        <i data-lucide="message-square" class="w-3.5 h-3.5"></i> Open in Chatwoot
      </a>
      <button onclick="drawerQuickWhatsApp()" class="flex-1 py-1.5 px-3 bg-emerald-50 text-emerald-700 hover:bg-emerald-100 border border-emerald-200 rounded-lg font-semibold flex items-center justify-center gap-1.5 transition">
        <i data-lucide="message-circle" class="w-3.5 h-3.5"></i> WhatsApp
      </button>
      <button onclick="drawerQuickCall()" class="py-1.5 px-3 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-lg font-semibold flex items-center justify-center gap-1.5 transition">
        <i data-lucide="phone" class="w-3.5 h-3.5"></i> Call
      </button>
    </div>

    <!-- 7-Stage Interactive Pipeline Progress Bar -->
    <div class="p-4 bg-slate-50 border-b border-slate-200 space-y-2">
      <div class="flex items-center justify-between text-xs">
        <span class="font-bold text-slate-700 flex items-center gap-1">
          <i data-lucide="git-commit" class="w-3.5 h-3.5 text-blue-600"></i> Admission Pipeline Progress
        </span>
        <button onclick="advanceCurrentStudentStage()" class="font-semibold text-blue-600 hover:text-blue-800 flex items-center gap-1" id="drawerNextStageBtn">
          Advance Stage <i data-lucide="arrow-right" class="w-3 h-3"></i>
        </button>
      </div>

      <!-- Stage Stepper Blocks -->
      <div class="grid grid-cols-7 gap-1 pt-1" id="drawerStepperBars">
        <!-- 7 blocks populated by JS -->
      </div>
      <div class="flex justify-between text-[10px] text-slate-400 px-0.5">
        <span>Enquiry</span>
        <span>Counselling</span>
        <span>Follow-up</span>
        <span>App</span>
        <span>Docs</span>
        <span>Fee</span>
        <span>Enrolled</span>
      </div>
    </div>

    <!-- Drawer Navigation Tabs -->
    <div class="flex border-b border-slate-200 text-xs font-semibold bg-white px-2">
      <button onclick="setDrawerTab('info')" id="dtab-info" class="py-2.5 px-3 text-blue-600 border-b-2 border-blue-600 font-bold">
        Overview
      </button>
      <button onclick="setDrawerTab('docs')" id="dtab-docs" class="py-2.5 px-3 text-slate-500 hover:text-slate-800 border-b-2 border-transparent">
        Documents <span id="drawerDocsBadge" class="ml-1 text-[10px] bg-slate-100 text-slate-700 px-1.5 py-0.2 rounded-full">0/4</span>
      </button>
      <button onclick="setDrawerTab('fees')" id="dtab-fees" class="py-2.5 px-3 text-slate-500 hover:text-slate-800 border-b-2 border-transparent">
        Fees & Token
      </button>
      <button onclick="setDrawerTab('notes')" id="dtab-notes" class="py-2.5 px-3 text-slate-500 hover:text-slate-800 border-b-2 border-transparent">
        Activity & Notes
      </button>
      <button onclick="setDrawerTab('wa')" id="dtab-wa" class="py-2.5 px-3 text-slate-500 hover:text-slate-800 border-b-2 border-transparent">
        WhatsApp
      </button>
    </div>

    <!-- Drawer Content Scroll Area -->
    <div class="flex-1 overflow-y-auto p-4 sm:p-5 space-y-4 custom-scroll text-xs">
      
      <!-- TAB 1: OVERVIEW & ACADEMIC INFO -->
      <div id="dview-info" class="space-y-4">
        
        <div class="bg-slate-50 rounded-xl p-3.5 border border-slate-200 space-y-2.5">
          <b class="text-xs font-bold text-slate-900 block">Contact & Personal Details</b>
          <div class="grid grid-cols-2 gap-2 text-[11px]">
            <div>
              <span class="text-slate-400 block">Phone</span>
              <span class="font-semibold text-slate-800" id="infoPhone">+91 00000 00000</span>
            </div>
            <div>
              <span class="text-slate-400 block">Email</span>
              <span class="font-semibold text-slate-800 truncate block" id="infoEmail">student@email.com</span>
            </div>
            <div>
              <span class="text-slate-400 block">City / State</span>
              <span class="font-semibold text-slate-800" id="infoCity">City</span>
            </div>
            <div>
              <span class="text-slate-400 block">Lead Source</span>
              <span class="font-semibold text-slate-800" id="infoSource">WhatsApp</span>
            </div>
            <div>
              <span class="text-slate-400 block">Assigned Counsellor</span>
              <span class="font-semibold text-blue-700" id="infoCounsellor">Sneha Patel</span>
            </div>
            <div>
              <span class="text-slate-400 block">Next Follow-up</span>
              <span class="font-semibold text-slate-800" id="infoFollowUp">Today</span>
            </div>
          </div>
        </div>

        <div class="bg-slate-50 rounded-xl p-3.5 border border-slate-200 space-y-2.5">
          <b class="text-xs font-bold text-slate-900 block">Academic Background & Scores</b>
          <div class="grid grid-cols-2 gap-2 text-[11px]" id="infoAcademicsGrid">
            <!-- Populated by JS -->
          </div>
        </div>

        <div class="bg-slate-50 rounded-xl p-3.5 border border-slate-200 space-y-2.5">
          <b class="text-xs font-bold text-slate-900 block">Guardian / Parent Details</b>
          <div class="grid grid-cols-2 gap-2 text-[11px]">
            <div>
              <span class="text-slate-400 block">Father / Guardian</span>
              <span class="font-semibold text-slate-800" id="infoFather">Mr. Parent Name</span>
            </div>
            <div>
              <span class="text-slate-400 block">Guardian Phone</span>
              <span class="font-semibold text-slate-800" id="infoParentPhone">+91 98XXX XXXXX</span>
            </div>
          </div>
        </div>

      </div>

      <!-- TAB 2: DOCUMENTS VERIFICATION CHECKLIST -->
      <div id="dview-docs" class="hidden space-y-3">
        <div class="flex items-center justify-between">
          <span class="font-bold text-slate-800">Required Documents (4 Items)</span>
          <span class="text-[11px] text-slate-500">Click to verify/unverify</span>
        </div>
        <div id="drawerDocsList" class="space-y-2">
          <!-- Populated by JS -->
        </div>
      </div>

      <!-- TAB 3: FEES & TOKEN PAYMENT -->
      <div id="dview-fees" class="hidden space-y-4">
        
        <div class="bg-slate-50 rounded-xl p-4 border border-slate-200 space-y-3">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-slate-800">Fee Structure & Ledger</span>
            <span id="drawerFeeBadge" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-50 text-amber-700 border border-amber-200">
              Token Due
            </span>
          </div>

          <div class="grid grid-cols-2 gap-3 text-xs pt-1">
            <div class="p-2.5 bg-white rounded-lg border border-slate-200">
              <span class="text-[11px] text-slate-400 block">Total Course Fee</span>
              <b class="text-sm text-slate-900" id="drawerTotalFee">₹1,85,000</b>
            </div>
            <div class="p-2.5 bg-white rounded-lg border border-slate-200">
              <span class="text-[11px] text-slate-400 block">Token Admission Fee</span>
              <b class="text-sm text-blue-700" id="drawerAdmFee">₹46,250</b>
            </div>
            <div class="p-2.5 bg-white rounded-lg border border-slate-200">
              <span class="text-[11px] text-slate-400 block">Amount Paid So Far</span>
              <b class="text-sm text-emerald-600" id="drawerAmountPaid">₹0</b>
            </div>
            <div class="p-2.5 bg-white rounded-lg border border-slate-200">
              <span class="text-[11px] text-slate-400 block">Balance Pending</span>
              <b class="text-sm text-rose-600" id="drawerBalance">₹46,250</b>
            </div>
          </div>

          <button onclick="openRecordPaymentModal()" class="w-full py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg font-semibold flex items-center justify-center gap-1.5 transition">
            <i data-lucide="receipt" class="w-4 h-4"></i> Record Token Fee Payment
          </button>
        </div>

        <div class="space-y-2">
          <b class="text-xs font-bold text-slate-800 block">Payment Transactions History</b>
          <div id="drawerPaymentHistory" class="space-y-1.5 text-xs">
            <!-- Populated by JS -->
          </div>
        </div>

      </div>

      <!-- TAB 4: ACTIVITY & NOTES -->
      <div id="dview-notes" class="hidden space-y-3">
        <!-- Add Note Input -->
        <div class="space-y-2">
          <label class="text-xs font-bold text-slate-700 block">Add Counsellor Call Note (Synced with Chatwoot)</label>
          <div class="flex gap-2">
            <input type="text" id="drawerNoteInput" placeholder="e.g. Student requested fee structure brochure on WhatsApp..." class="flex-1 px-3 py-2 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:bg-white focus:outline-none focus:ring-1 focus:ring-blue-500">
            <button onclick="addCurrentStudentNote()" class="px-3.5 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-semibold transition shrink-0">
              Save Note
            </button>
          </div>
        </div>

        <!-- Notes Timeline -->
        <div class="pt-2">
          <b class="text-xs font-bold text-slate-800 block mb-2">History & Timeline</b>
          <div id="drawerNotesList" class="space-y-2">
            <!-- Populated by JS -->
          </div>
        </div>
      </div>

      <!-- TAB 5: WHATSAPP QUICK SENDER -->
      <div id="dview-wa" class="hidden space-y-3">
        <b class="text-xs font-bold text-slate-800 block">Trigger WhatsApp Template to Student</b>
        <p class="text-xs text-slate-500">Select an official template to send instantly via WhatsApp Cloud API:</p>
        
        <div class="space-y-2" id="drawerWaTemplates">
          <!-- Populated by JS -->
        </div>
      </div>

    </div>

  </div> <!-- End Slide-Over Drawer -->

  <!-- ========================================== -->
  <!-- MODAL 1: ADD NEW STUDENT LEAD              -->
  <!-- ========================================== -->
  <div id="modalAddLead" class="fixed inset-0 bg-slate-900/40 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl max-w-lg w-full p-5 sm:p-6 shadow-2xl border border-slate-200 space-y-4">
      
      <div class="flex items-center justify-between border-b border-slate-100 pb-3">
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 rounded-lg bg-blue-50 text-blue-600 flex items-center justify-center font-bold">
            <i data-lucide="user-plus" class="w-4 h-4"></i>
          </div>
          <div>
            <h3 class="text-sm font-bold text-slate-900">Add New Student Enquiry</h3>
            <p class="text-xs text-slate-500">Creates lead in AdmitDesk and syncs with Chatwoot Contact DB</p>
          </div>
        </div>
        <button onclick="closeAddModal()" class="text-slate-400 hover:text-slate-600">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <!-- Live Duplicate Detection Banner -->
      <div id="addLeadDupeAlert" class="hidden p-3 rounded-lg bg-amber-50 border border-amber-200 text-xs text-amber-800 flex items-start gap-2">
        <i data-lucide="alert-triangle" class="w-4 h-4 text-amber-600 shrink-0 mt-0.5"></i>
        <div>
          <b class="block font-semibold">Duplicate Lead Detected!</b>
          <span id="addLeadDupeText">This phone number already exists in system.</span>
        </div>
      </div>

      <form onsubmit="submitNewLead(event)" class="space-y-3 text-xs">
        <div>
          <label class="block font-semibold text-slate-700 mb-1">Student Full Name *</label>
          <input type="text" id="newLeadName" required placeholder="e.g. Aditi Roy" class="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:bg-white focus:outline-none focus:ring-1 focus:ring-blue-500">
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block font-semibold text-slate-700 mb-1">Mobile Phone (10-Digit) *</label>
            <input type="tel" id="newLeadPhone" required oninput="checkDuplicatePhone(this.value)" placeholder="9820123456" class="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:bg-white focus:outline-none focus:ring-1 focus:ring-blue-500">
          </div>
          <div>
            <label class="block font-semibold text-slate-700 mb-1">Email Address</label>
            <input type="email" id="newLeadEmail" placeholder="student@gmail.com" class="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:bg-white focus:outline-none focus:ring-1 focus:ring-blue-500">
          </div>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block font-semibold text-slate-700 mb-1">Target Course *</label>
            <select id="newLeadCourse" required class="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:bg-white focus:outline-none focus:ring-1 focus:ring-blue-500 cursor-pointer">
              <option value="MBA">MBA (2 Years)</option>
              <option value="B.Tech CSE">B.Tech CSE (4 Years)</option>
              <option value="BBA">BBA (3 Years)</option>
              <option value="MCA">MCA (2 Years)</option>
              <option value="BCA">BCA (3 Years)</option>
              <option value="B.Sc Nursing">B.Sc Nursing (4 Years)</option>
              <option value="Data Science">M.Sc Data Science</option>
              <option value="B.Des">B.Des Design</option>
            </select>
          </div>
          <div>
            <label class="block font-semibold text-slate-700 mb-1">Lead Source *</label>
            <select id="newLeadSource" required class="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:bg-white focus:outline-none focus:ring-1 focus:ring-blue-500 cursor-pointer">
              <option value="WhatsApp">WhatsApp Inbound</option>
              <option value="Website">Website Form</option>
              <option value="Facebook">Facebook / Instagram Ad</option>
              <option value="Phone Call">Phone Inbound</option>
              <option value="Walk-in">Campus Walk-in</option>
              <option value="Referral">Student Referral</option>
            </select>
          </div>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block font-semibold text-slate-700 mb-1">City / Location</label>
            <input type="text" id="newLeadCity" placeholder="e.g. Pune" class="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:bg-white focus:outline-none focus:ring-1 focus:ring-blue-500">
          </div>
          <div>
            <label class="block font-semibold text-slate-700 mb-1">Assign to Counsellor</label>
            <select id="newLeadCounsellor" class="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:bg-white focus:outline-none focus:ring-1 focus:ring-blue-500 cursor-pointer">
              <option value="auto">Auto-Assign (Round Robin)</option>
              <option value="Sneha Patel">Sneha Patel</option>
              <option value="Amit Kumar">Amit Kumar</option>
              <option value="Priya Sharma">Priya Sharma</option>
            </select>
          </div>
        </div>

        <div>
          <label class="block font-semibold text-slate-700 mb-1">Initial Enquiry Notes</label>
          <textarea id="newLeadNotes" rows="2" placeholder="Student asked about eligibility criteria and scholarship options..." class="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:bg-white focus:outline-none focus:ring-1 focus:ring-blue-500"></textarea>
        </div>

        <div class="flex items-center justify-end gap-2 pt-2 border-t border-slate-100">
          <button type="button" onclick="closeAddModal()" class="px-3 py-2 text-slate-600 hover:bg-slate-100 rounded-lg font-semibold transition">
            Cancel
          </button>
          <button type="submit" id="submitLeadBtn" class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-semibold transition shadow-xs">
            Save & Sync to Chatwoot
          </button>
        </div>
      </form>

    </div>
  </div>

  <!-- ========================================== -->
  <!-- MODAL 2: BULK CSV IMPORT                   -->
  <!-- ========================================== -->
  <div id="modalImport" class="fixed inset-0 bg-slate-900/40 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl max-w-lg w-full p-5 sm:p-6 shadow-2xl border border-slate-200 space-y-4 text-xs">
      
      <div class="flex items-center justify-between border-b border-slate-100 pb-3">
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 rounded-lg bg-blue-50 text-blue-600 flex items-center justify-center font-bold">
            <i data-lucide="upload-cloud" class="w-4 h-4"></i>
          </div>
          <div>
            <h3 class="text-sm font-bold text-slate-900">Bulk CSV Lead Import</h3>
            <p class="text-xs text-slate-500">Import student lists with automatic duplicate check and auto-assignment</p>
          </div>
        </div>
        <button onclick="closeImportModal()" class="text-slate-400 hover:text-slate-600">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <div class="space-y-2">
        <div class="flex items-center justify-between">
          <label class="font-semibold text-slate-700">Paste CSV Data (Name, Phone, Course, City)</label>
          <button onclick="loadSampleCSV()" class="text-blue-600 font-semibold hover:underline">
            Load Sample CSV
          </button>
        </div>
        <textarea id="importCSVText" rows="6" placeholder="Name, Phone, Course, City
Aditi Sen, 9823411122, MBA, Kolkata
Rajeev Menon, 9845022233, B.Tech CSE, Kochi
Karan Joshi, 9811233344, BBA, Delhi" class="w-full font-mono text-[11px] p-3 bg-slate-50 border border-slate-200 rounded-lg focus:bg-white focus:outline-none focus:ring-1 focus:ring-blue-500"></textarea>
      </div>

      <div class="p-3 bg-blue-50/60 rounded-lg border border-blue-100 text-slate-600 space-y-1">
        <span class="font-semibold text-blue-900 block">Import Rules:</span>
        <ul class="list-disc list-inside text-[11px] space-y-0.5">
          <li>Duplicate phone numbers already in system will be automatically skipped.</li>
          <li>New leads will be evenly round-robin assigned to counselling team.</li>
          <li>Initial stage will be set to: <b>Enquiry</b>.</li>
        </ul>
      </div>

      <div class="flex items-center justify-end gap-2 pt-2 border-t border-slate-100">
        <button type="button" onclick="closeImportModal()" class="px-3 py-2 text-slate-600 hover:bg-slate-100 rounded-lg font-semibold transition">
          Cancel
        </button>
        <button onclick="executeCSVImport()" class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-semibold transition shadow-xs">
          Process & Import Leads
        </button>
      </div>

    </div>
  </div>

  <!-- ========================================== -->
  <!-- MODAL 3: RECORD PAYMENT                    -->
  <!-- ========================================== -->
  <div id="modalPayment" class="fixed inset-0 bg-slate-900/40 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl max-w-md w-full p-5 sm:p-6 shadow-2xl border border-slate-200 space-y-4 text-xs">
      
      <div class="flex items-center justify-between border-b border-slate-100 pb-3">
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 rounded-lg bg-emerald-50 text-emerald-600 flex items-center justify-center font-bold">
            <i data-lucide="receipt" class="w-4 h-4"></i>
          </div>
          <div>
            <h3 class="text-sm font-bold text-slate-900">Record Fee Payment</h3>
            <p class="text-xs text-slate-500" id="paymentModalStudentName">Student Name</p>
          </div>
        </div>
        <button onclick="closePaymentModal()" class="text-slate-400 hover:text-slate-600">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <form onsubmit="submitPayment(event)" class="space-y-3">
        <div>
          <label class="block font-semibold text-slate-700 mb-1">Payment Amount (₹ INR) *</label>
          <input type="number" id="payAmount" required class="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-lg text-sm font-bold text-slate-900 focus:bg-white focus:outline-none focus:ring-1 focus:ring-emerald-500">
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block font-semibold text-slate-700 mb-1">Payment Mode *</label>
            <select id="payMode" class="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:bg-white focus:outline-none focus:ring-1 focus:ring-emerald-500 cursor-pointer">
              <option value="UPI / QR">UPI (GPay / PhonePe)</option>
              <option value="NEFT / RTGS">Net Banking (NEFT/RTGS)</option>
              <option value="Card">Debit / Credit Card</option>
              <option value="Cash / DD">Cash / Demand Draft</option>
            </select>
          </div>
          <div>
            <label class="block font-semibold text-slate-700 mb-1">Transaction / UTR Ref</label>
            <input type="text" id="payRef" placeholder="e.g. UTR8273910" class="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:bg-white focus:outline-none focus:ring-1 focus:ring-emerald-500 font-mono">
          </div>
        </div>

        <div>
          <label class="block font-semibold text-slate-700 mb-1">Internal Note / Remarks</label>
          <input type="text" id="payRemarks" placeholder="Seat confirmation token for Batch 2026" class="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-lg focus:bg-white focus:outline-none focus:ring-1 focus:ring-emerald-500">
        </div>

        <div class="flex items-center justify-end gap-2 pt-2 border-t border-slate-100">
          <button type="button" onclick="closePaymentModal()" class="px-3 py-2 text-slate-600 hover:bg-slate-100 rounded-lg font-semibold transition">
            Cancel
          </button>
          <button type="submit" class="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg font-semibold transition shadow-xs">
            Confirm & Generate Receipt
          </button>
        </div>
      </form>

    </div>
  </div>

  <!-- Toast Notification Container -->
  <div id="toast" class="fixed bottom-5 right-5 z-50 bg-slate-900 text-white px-4 py-3 rounded-xl shadow-xl flex items-center space-x-2.5 text-xs font-semibold transform translate-y-20 opacity-0 transition-all duration-300 pointer-events-none">
    <i data-lucide="check-circle" class="w-4 h-4 text-emerald-400"></i>
    <span id="toastMsg">Action completed</span>
  </div>

  <!-- JAVASCRIPT APPLICATION LOGIC -->
  <script>
    // ----------------------------------------------------
    // 1. DATA MODELS & INITIAL STATE
    // ----------------------------------------------------
    const STAGES = ['Enquiry', 'Counselling', 'Follow-up', 'Application', 'Doc Verification', 'Fee Payment', 'Enrollment'];
    
    const STAGE_PILLS = {
      'Enquiry': 'bg-slate-100 text-slate-700 border-slate-200',
      'Counselling': 'bg-blue-50 text-blue-700 border-blue-200',
      'Follow-up': 'bg-amber-50 text-amber-700 border-amber-200',
      'Application': 'bg-purple-50 text-purple-700 border-purple-200',
      'Doc Verification': 'bg-indigo-50 text-indigo-700 border-indigo-200',
      'Fee Payment': 'bg-rose-50 text-rose-700 border-rose-200',
      'Enrollment': 'bg-emerald-50 text-emerald-700 border-emerald-200'
    };

    const DOC_NAMES = ['10th Marksheet', '12th / Grad Marksheet', 'Govt ID (Aadhaar)', 'Transfer Certificate'];

    const COUNSELLORS = [
      { id: 'sneha', name: 'Sneha Patel', role: 'Senior Counsellor', active: 10, enrolled: 1, conv: '24.5%', fee: '₹46,250', overdue: 1 },
      { id: 'amit', name: 'Amit Kumar', role: 'Counsellor', active: 10, enrolled: 0, conv: '18.2%', fee: '₹0', overdue: 1 },
      { id: 'lead', name: 'Priya Sharma', role: 'Team Lead', active: 8, enrolled: 2, conv: '28.0%', fee: '₹80,000', overdue: 0 }
    ];

    const TEMPLATES = [
      { id: 'ack', name: '1. Enquiry Acknowledgement', trigger: 'When a new lead arrives via WhatsApp/Web', on: true, text: 'Hi {name}, thank you for your enquiry for {course} at Apex Institute! Your assigned counsellor {counsellor} will reach out shortly. Reply anytime with questions.' },
      { id: 'follow', name: '2. Follow-up Call Reminder', trigger: 'Scheduled follow-up reminder to student', on: true, text: 'Hi {name}, this is a reminder regarding your {course} admission consultation with {counsellor}. Does today at 4 PM work for our quick call?' },
      { id: 'app', name: '3. Application Form Link', trigger: 'When stage moves to Application', on: true, text: 'Hi {name}, your {course} admission application has been initiated! Click here to complete your online form: https://apex.edu/apply?id={id}' },
      { id: 'doc', name: '4. Document Submission Checklist', trigger: 'When stage moves to Doc Verification', on: true, text: 'Hi {name}, please submit your 10th/12th marksheets & Aadhaar copy for {course} verification. Upload here: https://apex.edu/docs?id={id}' },
      { id: 'pay', name: '5. Token Fee Payment Link', trigger: 'When stage moves to Fee Payment', on: true, text: 'Hi {name}, your documents for {course} are verified! Complete your token fee payment to reserve your seat: https://apex.edu/pay?id={id}' },
      { id: 'enr', name: '6. Admission Confirmed Letter', trigger: 'When stage moves to Enrollment', on: true, text: '🎉 Congratulations {name}! Your admission to {course} for batch 2026-27 is officially confirmed. Welcome to Apex Institute!' }
    ];

    // Rich dataset of 28 realistic student leads
    let leads = [
      { id: 101, name: 'Rahul Sharma', phone: '+91 98201 23456', email: 'rahul.sharma@gmail.com', course: 'MBA', source: 'WhatsApp', stage: 'Counselling', counsellor: 'Sneha Patel', counsellorId: 'sneha', totalFee: 185000, admFee: 46250, paid: 0, city: 'Mumbai', followUp: '19 Nov 2026', isOverdue: false, docs: [true, false, false, false], father: 'Mr. Ashok Sharma', academics: { t10: '85%', t12: '82%', grad: 'B.Com 78%', test: 'CAT 84 %ile' }, notes: ['Student completed B.Com. Interested in Marketing & Finance electives.'] },
      { id: 102, name: 'Ananya Verma', phone: '+91 98765 43210', email: 'ananya.verma@gmail.com', course: 'B.Tech CSE', source: 'Website', stage: 'Fee Payment', counsellor: 'Sneha Patel', counsellorId: 'sneha', totalFee: 220000, admFee: 55000, paid: 0, city: 'Pune', followUp: 'Today', isOverdue: false, docs: [true, true, true, true], father: 'Dr. Suresh Verma', academics: { t10: '92%', t12: '89%', grad: 'N/A', test: 'JEE 91 %ile' }, notes: ['All Class 12 and entrance scores verified. Token fee payment link sent.'] },
      { id: 103, name: 'Rohit Gupta', phone: '+91 98112 23344', email: 'rohit.gupta@outlook.com', course: 'BBA', source: 'Facebook', stage: 'Enquiry', counsellor: 'Amit Kumar', counsellorId: 'amit', totalFee: 140000, admFee: 35000, paid: 0, city: 'Delhi NCR', followUp: 'Today', isOverdue: false, docs: [false, false, false, false], father: 'Mr. Rajesh Gupta', academics: { t10: '76%', t12: '74%', grad: 'N/A', test: 'CUET 78%' }, notes: ['Saw FB ad. Asked about last date of submission and hostel options.'] },
      { id: 104, name: 'Tanya Reddy', phone: '+91 99887 76655', email: 'tanya.reddy@yahoo.com', course: 'MCA', source: 'WhatsApp', stage: 'Application', counsellor: 'Amit Kumar', counsellorId: 'amit', totalFee: 160000, admFee: 40000, paid: 0, city: 'Hyderabad', followUp: '22 Nov 2026', isOverdue: false, docs: [true, true, false, false], father: 'Mr. V. Reddy', academics: { t10: '81%', t12: '80%', grad: 'BCA 8.2 CGPA', test: 'N/A' }, notes: ['Online application form submitted. Application ID: MCA-2026-089.'] },
      { id: 105, name: 'Vikram Singh Rathore', phone: '+91 97123 45678', email: 'vikram.singh@gmail.com', course: 'B.Sc Nursing', source: 'Walk-in', stage: 'Enrollment', counsellor: 'Priya Sharma', counsellorId: 'lead', totalFee: 120000, admFee: 30000, paid: 30000, city: 'Jaipur', followUp: 'Completed', isOverdue: false, docs: [true, true, true, true], father: 'Mr. Bhanwar Singh', academics: { t10: '78%', t12: '75%', grad: 'N/A', test: 'State Entrance' }, notes: ['Token fee paid via NEFT UTR98234710. Seat officially confirmed!'] },
      { id: 106, name: 'Divya Joshi', phone: '+91 94250 12345', email: 'divya.joshi@gmail.com', course: 'MBA', source: 'Phone Call', stage: 'Follow-up', counsellor: 'Sneha Patel', counsellorId: 'sneha', totalFee: 185000, admFee: 46250, paid: 0, city: 'Indore', followUp: '17 Nov 2026', isOverdue: true, docs: [true, false, false, false], father: 'Mr. M.K. Joshi', academics: { t10: '88%', t12: '85%', grad: 'B.Com 79%', test: 'MAT 88 %ile' }, notes: ['OVERDUE: Father wanted to discuss education loan assistance options.'] },
      { id: 107, name: 'Arjun Nair', phone: '+91 98450 99887', email: 'arjun.nair@gmail.com', course: 'B.Tech CSE', source: 'Google Ads', stage: 'Counselling', counsellor: 'Amit Kumar', counsellorId: 'amit', totalFee: 220000, admFee: 55000, paid: 0, city: 'Bangalore', followUp: '20 Nov 2026', isOverdue: false, docs: [true, false, false, false], father: 'Mr. K. Nair', academics: { t10: '94%', t12: '91%', grad: 'N/A', test: 'JEE 94 %ile' }, notes: ['Looking for Artificial Intelligence specialization in CSE.'] },
      { id: 108, name: 'Megha Sundaram', phone: '+91 94440 11223', email: 'megha.sundaram@gmail.com', course: 'Data Science', source: 'Website', stage: 'Doc Verification', counsellor: 'Sneha Patel', counsellorId: 'sneha', totalFee: 190000, admFee: 47500, paid: 0, city: 'Chennai', followUp: '21 Nov 2026', isOverdue: false, docs: [true, true, true, false], father: 'Mr. Sundaram R.', academics: { t10: '89%', t12: '87%', grad: 'B.Sc Maths 82%', test: 'N/A' }, notes: ['Aadhaar and Graduation marksheets uploaded. Migration certificate pending.'] },
      { id: 109, name: 'Kartik Iyer', phone: '+91 98200 44556', email: 'kartik.iyer@yahoo.com', course: 'BBA', source: 'Walk-in', stage: 'Application', counsellor: 'Priya Sharma', counsellorId: 'lead', totalFee: 140000, admFee: 35000, paid: 0, city: 'Mumbai', followUp: '23 Nov 2026', isOverdue: false, docs: [true, false, false, false], father: 'Mr. S. Iyer', academics: { t10: '80%', t12: '79%', grad: 'N/A', test: 'CUET 81%' }, notes: ['Visited campus with parents. Filled physical application form.'] },
      { id: 110, name: 'Pooja Deshmukh', phone: '+91 98222 33445', email: 'pooja.deshmukh@gmail.com', course: 'MCA', source: 'WhatsApp', stage: 'Follow-up', counsellor: 'Amit Kumar', counsellorId: 'amit', totalFee: 160000, admFee: 40000, paid: 0, city: 'Nagpur', followUp: '16 Nov 2026', isOverdue: true, docs: [false, false, false, false], father: 'Mr. Dilip Deshmukh', academics: { t10: '79%', t12: '76%', grad: 'BCA 74%', test: 'MAH-CET' }, notes: ['OVERDUE: Student was travelling. Needed scholarship guidance call.'] },
      { id: 111, name: 'Sameer Khan', phone: '+91 99350 12389', email: 'sameer.khan@gmail.com', course: 'MBA', source: 'Facebook', stage: 'Enquiry', counsellor: 'Sneha Patel', counsellorId: 'sneha', totalFee: 185000, admFee: 46250, paid: 0, city: 'Lucknow', followUp: 'Today', isOverdue: false, docs: [false, false, false, false], father: 'Mr. Tariq Khan', academics: { t10: '82%', t12: '80%', grad: 'BBA 76%', test: 'CMAT 80 %ile' }, notes: ['Inquired via FB lead form. Sent course brochure PDF.'] },
      { id: 112, name: 'Ritu Agarwal', phone: '+91 98310 98765', email: 'ritu.agarwal@gmail.com', course: 'B.Des', source: 'Instagram', stage: 'Fee Payment', counsellor: 'Priya Sharma', counsellorId: 'lead', totalFee: 175000, admFee: 43750, paid: 0, city: 'Kolkata', followUp: 'Today', isOverdue: false, docs: [true, true, true, true], father: 'Mr. Sanjay Agarwal', academics: { t10: '86%', t12: '88%', grad: 'N/A', test: 'Design Portfolio' }, notes: ['Portfolio evaluated and approved with grade A. Fee due today.'] },
      { id: 113, name: 'Aditya Choudhury', phone: '+91 94370 55667', email: 'aditya.c@gmail.com', course: 'BCA', source: 'Website', stage: 'Counselling', counsellor: 'Amit Kumar', counsellorId: 'amit', totalFee: 130000, admFee: 32500, paid: 0, city: 'Bhubaneswar', followUp: '21 Nov 2026', isOverdue: false, docs: [true, false, false, false], father: 'Mr. B. Choudhury', academics: { t10: '84%', t12: '81%', grad: 'N/A', test: 'N/A' }, notes: ['Enquired about software development syllabus and labs.'] },
      { id: 114, name: 'Snehal Kulkarni', phone: '+91 98500 12378', email: 'snehal.k@gmail.com', course: 'B.Tech CSE', source: 'Referral', stage: 'Doc Verification', counsellor: 'Sneha Patel', counsellorId: 'sneha', totalFee: 220000, admFee: 55000, paid: 0, city: 'Nashik', followUp: '22 Nov 2026', isOverdue: false, docs: [true, true, false, false], father: 'Mr. V. Kulkarni', academics: { t10: '91%', t12: '88%', grad: 'N/A', test: 'MHT-CET 92 %ile' }, notes: ['Referred by alumnus. Submitted 10th and 12th marksheet copies.'] },
      { id: 115, name: 'Manish Tiwari', phone: '+91 94500 88990', email: 'manish.tiwari@gmail.com', course: 'MBA', source: 'WhatsApp', stage: 'Enrollment', counsellor: 'Priya Sharma', counsellorId: 'lead', totalFee: 185000, admFee: 46250, paid: 46250, city: 'Varanasi', followUp: 'Completed', isOverdue: false, docs: [true, true, true, true], father: 'Mr. R.P. Tiwari', academics: { t10: '83%', t12: '81%', grad: 'B.Tech 75%', test: 'CAT 86 %ile' }, notes: ['Token fee paid via UPI ref UPI9283740. ID card issued.'] },
      { id: 116, name: 'Neha Singhal', phone: '+91 98170 33441', email: 'neha.singhal@gmail.com', course: 'BBA', source: 'Facebook', stage: 'Follow-up', counsellor: 'Amit Kumar', counsellorId: 'amit', totalFee: 140000, admFee: 35000, paid: 0, city: 'Chandigarh', followUp: 'Today', isOverdue: false, docs: [true, false, false, false], father: 'Mr. Vinod Singhal', academics: { t10: '78%', t12: '77%', grad: 'N/A', test: 'CUET 76%' }, notes: ['Scheduled callback for 2:30 PM regarding hostel room allocation.'] },
      { id: 117, name: 'Pranav Mehta', phone: '+91 98250 66778', email: 'pranav.mehta@gmail.com', course: 'Data Science', source: 'Website', stage: 'Application', counsellor: 'Sneha Patel', counsellorId: 'sneha', totalFee: 190000, admFee: 47500, paid: 0, city: 'Ahmedabad', followUp: '24 Nov 2026', isOverdue: false, docs: [true, true, false, false], father: 'Mr. Hiren Mehta', academics: { t10: '87%', t12: '85%', grad: 'B.E. 81%', test: 'GATE' }, notes: ['Application filled online. Preparing for technical interview round.'] },
      { id: 118, name: 'Kavita Chauhan', phone: '+91 94120 77889', email: 'kavita.c@gmail.com', course: 'B.Sc Nursing', source: 'Phone Call', stage: 'Enquiry', counsellor: 'Priya Sharma', counsellorId: 'lead', totalFee: 120000, admFee: 30000, paid: 0, city: 'Dehradun', followUp: 'Today', isOverdue: false, docs: [false, false, false, false], father: 'Mr. S.S. Chauhan', academics: { t10: '75%', t12: '73%', grad: 'N/A', test: 'State Entrance' }, notes: ['Called for hostel facilities for female students and hospital tie-ups.'] },
      { id: 119, name: 'Harish Nambiar', phone: '+91 94470 12890', email: 'harish.nambiar@gmail.com', course: 'B.Tech CSE', source: 'Google Ads', stage: 'Fee Payment', counsellor: 'Amit Kumar', counsellorId: 'amit', totalFee: 220000, admFee: 55000, paid: 0, city: 'Kochi', followUp: '20 Nov 2026', isOverdue: false, docs: [true, true, true, true], father: 'Mr. C. Nambiar', academics: { t10: '95%', t12: '93%', grad: 'N/A', test: 'KEAM Rank 1450' }, notes: ['All documents verified. Ready to pay admission token fee.'] },
      { id: 120, name: 'Shreya Banerjee', phone: '+91 98300 44321', email: 'shreya.b@gmail.com', course: 'B.Des', source: 'Website', stage: 'Counselling', counsellor: 'Priya Sharma', counsellorId: 'lead', totalFee: 175000, admFee: 43750, paid: 0, city: 'Kolkata', followUp: '21 Nov 2026', isOverdue: false, docs: [true, false, false, false], father: 'Mr. Subhash Banerjee', academics: { t10: '85%', t12: '84%', grad: 'N/A', test: 'NID Prelims' }, notes: ['Interested in UX/UI and Fashion communication tracks.'] },
      { id: 121, name: 'Kunal Malhotra', phone: '+91 98100 87654', email: 'kunal.m@gmail.com', course: 'MBA', source: 'WhatsApp', stage: 'Fee Payment', counsellor: 'Sneha Patel', counsellorId: 'sneha', totalFee: 185000, admFee: 46250, paid: 0, city: 'Gurgaon', followUp: '20 Nov 2026', isOverdue: false, docs: [true, true, true, true], father: 'Mr. O.P. Malhotra', academics: { t10: '88%', t12: '86%', grad: 'B.Com 80%', test: 'CMAT 92 %ile' }, notes: ['Documents clear. Awaiting net banking payment from father.'] },
      { id: 122, name: 'Deepali Patil', phone: '+91 98230 45612', email: 'deepali.patil@gmail.com', course: 'MCA', source: 'Referral', stage: 'Doc Verification', counsellor: 'Amit Kumar', counsellorId: 'amit', totalFee: 160000, admFee: 40000, paid: 0, city: 'Aurangabad', followUp: '22 Nov 2026', isOverdue: false, docs: [true, true, false, false], father: 'Mr. A. Patil', academics: { t10: '80%', t12: '78%', grad: 'B.Sc CS 76%', test: 'N/A' }, notes: ['Graduation marksheet uploaded. Degree certificate pending university dispatch.'] },
      { id: 123, name: 'Amanpreet Kaur', phone: '+91 98140 12398', email: 'amanpreet.k@gmail.com', course: 'BBA', source: 'Walk-in', stage: 'Enrollment', counsellor: 'Priya Sharma', counsellorId: 'lead', totalFee: 140000, admFee: 35000, paid: 35000, city: 'Ludhiana', followUp: 'Completed', isOverdue: false, docs: [true, true, true, true], father: 'Sardar Jaswant Singh', academics: { t10: '82%', t12: '80%', grad: 'N/A', test: 'Merit List' }, notes: ['Paid token fee ₹35,000 via NetBanking. Enrolled confirmed!'] },
      { id: 124, name: 'Abhishek Pandey', phone: '+91 94310 99881', email: 'abhishek.p@gmail.com', course: 'BCA', source: 'Facebook', stage: 'Enquiry', counsellor: 'Amit Kumar', counsellorId: 'amit', totalFee: 130000, admFee: 32500, paid: 0, city: 'Patna', followUp: 'Today', isOverdue: false, docs: [false, false, false, false], father: 'Mr. S.K. Pandey', academics: { t10: '77%', t12: '75%', grad: 'N/A', test: 'N/A' }, notes: ['Enquired about BCA eligibility for students with non-maths background.'] },
      { id: 125, name: 'Sanya Mirza', phone: '+91 99490 22334', email: 'sanya.mirza@gmail.com', course: 'Data Science', source: 'WhatsApp', stage: 'Counselling', counsellor: 'Sneha Patel', counsellorId: 'sneha', totalFee: 190000, admFee: 47500, paid: 0, city: 'Hyderabad', followUp: '21 Nov 2026', isOverdue: false, docs: [true, false, false, false], father: 'Mr. Asif Mirza', academics: { t10: '90%', t12: '89%', grad: 'B.Tech IT 8.4 CGPA', test: 'N/A' }, notes: ['Discussed AI laboratory resources and industry placement records.'] },
      { id: 126, name: 'Gaurav Bhatt', phone: '+91 94250 88776', email: 'gaurav.bhatt@gmail.com', course: 'B.Tech CSE', source: 'Phone Call', stage: 'Follow-up', counsellor: 'Sneha Patel', counsellorId: 'sneha', totalFee: 220000, admFee: 55000, paid: 0, city: 'Bhopal', followUp: 'Today', isOverdue: false, docs: [true, false, false, false], father: 'Mr. P.C. Bhatt', academics: { t10: '89%', t12: '87%', grad: 'N/A', test: 'JEE 89 %ile' }, notes: ['Called yesterday. Student wants to clarify cloud computing electives.'] },
      { id: 127, name: 'Aishwarya Sen', phone: '+91 98640 12345', email: 'aishwarya.sen@gmail.com', course: 'MBA', source: 'Website', stage: 'Application', counsellor: 'Priya Sharma', counsellorId: 'lead', totalFee: 185000, admFee: 46250, paid: 0, city: 'Guwahati', followUp: '23 Nov 2026', isOverdue: false, docs: [true, true, false, false], father: 'Mr. B. Sen', academics: { t10: '84%', t12: '82%', grad: 'B.A. Eco 78%', test: 'MAT 82 %ile' }, notes: ['Submitted application. Waiting for verification of graduation transcript.'] },
      { id: 128, name: 'Nitin Rawat', phone: '+91 94180 55443', email: 'nitin.rawat@gmail.com', course: 'B.Sc Nursing', source: 'Walk-in', stage: 'Doc Verification', counsellor: 'Amit Kumar', counsellorId: 'amit', totalFee: 120000, admFee: 30000, paid: 0, city: 'Shimla', followUp: '22 Nov 2026', isOverdue: false, docs: [true, true, true, false], father: 'Mr. Mohan Rawat', academics: { t10: '76%', t12: '74%', grad: 'N/A', test: 'State Nursing CET' }, notes: ['Physical documents presented at registrar counter. Migration pending.'] }
    ];

    // Current State
    let currentRole = 'admin'; // 'admin', 'lead', 'sneha', 'amit'
    let currentPipeView = 'table'; // 'table' or 'kanban'
    let activeStudentId = null;
    let selectedTplId = 'ack';
    
    // Pagination & Filter State
    let currentPage = 1;
    let pageSize = 10;
    let filteredLeads = [...leads];

    // ----------------------------------------------------
    // 2. HELPER FUNCTIONS
    // ----------------------------------------------------
    function inr(num) {
      if (!num && num !== 0) return '₹0';
      return '₹' + Number(num).toLocaleString('en-IN');
    }

    function showToast(msg) {
      const toast = document.getElementById('toast');
      const toastMsg = document.getElementById('toastMsg');
      toastMsg.textContent = msg;
      toast.classList.remove('translate-y-20', 'opacity-0');
      setTimeout(() => {
        toast.classList.add('translate-y-20', 'opacity-0');
      }, 3200);
    }

    function getInitials(name) {
      if (!name) return 'ST';
      const parts = name.trim().split(' ');
      if (parts.length === 1) return parts[0].substring(0, 2).toUpperCase();
      return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
    }

    // ----------------------------------------------------
    // 3. TAB & VIEW NAVIGATION
    // ----------------------------------------------------
    function setTab(tabId) {
      const tabs = ['dash', 'pipe', 'tasks', 'wa', 'team'];
      tabs.forEach(t => {
        const btn = document.getElementById(`tab-${t}`);
        const view = document.getElementById(`view-${t}`);
        if (t === tabId) {
          btn.className = 'flex items-center gap-1.5 px-3.5 py-2 rounded-lg transition bg-blue-50 text-blue-700 font-bold border border-blue-200/60';
          view.classList.remove('hidden');
        } else {
          btn.className = 'flex items-center gap-1.5 px-3.5 py-2 rounded-lg transition hover:bg-slate-50 text-slate-600 border border-transparent';
          view.classList.add('hidden');
        }
      });
      lucide.createIcons();
    }

    function setPipeView(viewMode) {
      currentPipeView = viewMode;
      const btnTable = document.getElementById('btn-view-table');
      const btnKanban = document.getElementById('btn-view-kanban');
      const tableWrap = document.getElementById('pipeTableView');
      const kanbanWrap = document.getElementById('pipeKanbanView');

      if (viewMode === 'table') {
        btnTable.className = 'flex items-center gap-1.5 px-3 py-1.5 rounded-md bg-white text-slate-800 shadow-xs';
        btnKanban.className = 'flex items-center gap-1.5 px-3 py-1.5 rounded-md text-slate-600 hover:text-slate-900';
        tableWrap.classList.remove('hidden');
        kanbanWrap.classList.add('hidden');
      } else {
        btnKanban.className = 'flex items-center gap-1.5 px-3 py-1.5 rounded-md bg-white text-slate-800 shadow-xs';
        btnTable.className = 'flex items-center gap-1.5 px-3 py-1.5 rounded-md text-slate-600 hover:text-slate-900';
        kanbanWrap.classList.remove('hidden');
        tableWrap.classList.add('hidden');
      }
      renderPipelineView();
      lucide.createIcons();
    }

    // ----------------------------------------------------
    // 4. ROLE SWITCHING & FILTERING
    // ----------------------------------------------------
    function switchRole(roleVal) {
      currentRole = roleVal;
      const roleNames = {
        'admin': 'Administrator (Registrar Office)',
        'lead': 'Team Lead · Priya Sharma',
        'sneha': 'Counsellor · Sneha Patel',
        'amit': 'Counsellor · Amit Kumar'
      };
      showToast(`Viewing system as: ${roleNames[roleVal]}`);
      
      // Auto-set counsellor filter if switched to counsellor
      const filterC = document.getElementById('filterCounsellor');
      if (roleVal === 'sneha') filterC.value = 'Sneha Patel';
      else if (roleVal === 'amit') filterC.value = 'Amit Kumar';
      else filterC.value = '';

      applyFilters();
      renderAll();
    }

    // ----------------------------------------------------
    // 5. SEARCH & MULTI-FILTER ENGINE
    // ----------------------------------------------------
    function applyFilters() {
      const q = document.getElementById('leadSearchInput').value.trim().toLowerCase();
      const stage = document.getElementById('filterStage').value;
      const counsellor = document.getElementById('filterCounsellor').value;
      const course = document.getElementById('filterCourse').value;
      const urgency = document.getElementById('filterUrgency').value;

      filteredLeads = leads.filter(l => {
        // Role access check
        if (currentRole === 'sneha' && l.counsellorId !== 'sneha') return false;
        if (currentRole === 'amit' && l.counsellorId !== 'amit') return false;

        // Search text
        if (q) {
          const match = l.name.toLowerCase().includes(q) ||
                        l.phone.replace(/\\D/g, '').includes(q.replace(/\\D/g, '')) ||
                        l.city.toLowerCase().includes(q) ||
                        l.course.toLowerCase().includes(q) ||
                        (l.email && l.email.toLowerCase().includes(q)) ||
                        String(l.id).includes(q);
          if (!match) return false;
        }

        // Filters
        if (stage && l.stage !== stage) return false;
        if (counsellor && l.counsellor !== counsellor) return false;
        if (course && l.course !== course) return false;
        if (urgency === 'overdue' && !l.isOverdue) return false;
        if (urgency === 'today' && l.followUp !== 'Today') return false;
        if (urgency === 'upcoming' && (l.isOverdue || l.followUp === 'Today' || l.followUp === 'Completed')) return false;

        return true;
      });

      currentPage = 1;
      renderPipelineView();
      updateFilterBadges();
      lucide.createIcons();
    }

    function resetFilters() {
      document.getElementById('leadSearchInput').value = '';
      document.getElementById('filterStage').value = '';
      document.getElementById('filterCounsellor').value = (currentRole === 'sneha' ? 'Sneha Patel' : (currentRole === 'amit' ? 'Amit Kumar' : ''));
      document.getElementById('filterCourse').value = '';
      document.getElementById('filterUrgency').value = '';
      applyFilters();
      showToast('Filters reset to default');
    }

    function updateFilterBadges() {
      const badge = document.getElementById('filteredLeadsBadge');
      if (badge) {
        badge.textContent = `${filteredLeads.length} of ${leads.length} Leads`;
      }
    }

    // ----------------------------------------------------
    // 6. PIPELINE RENDERING (TABLE & KANBAN)
    // ----------------------------------------------------
    function renderPipelineView() {
      if (currentPipeView === 'table') {
        renderTable();
      } else {
        renderKanban();
      }
    }

    function renderTable() {
      const tbody = document.getElementById('pipeTableBody');
      tbody.innerHTML = '';

      if (filteredLeads.length === 0) {
        tbody.innerHTML = `<tr><td colspan="10" class="py-8 text-center text-slate-400">No leads found matching your filters. Try resetting search filters.</td></tr>`;
        document.getElementById('paginationInfo').textContent = 'Showing 0 of 0';
        document.getElementById('btnPrevPage').disabled = true;
        document.getElementById('btnNextPage').disabled = true;
        return;
      }

      // Pagination slice
      let startIndex = 0;
      let endIndex = filteredLeads.length;

      if (pageSize !== 'all') {
        const size = Number(pageSize);
        startIndex = (currentPage - 1) * size;
        endIndex = Math.min(startIndex + size, filteredLeads.length);
      }

      const pageRows = filteredLeads.slice(startIndex, endIndex);

      pageRows.forEach((l, idx) => {
        const verifiedDocs = l.docs.filter(Boolean).length;
        const totalDocs = l.docs.length;
        const rowNum = startIndex + idx + 1;

        let followUpBadge = `<span class="text-slate-600 bg-slate-100 px-2 py-0.5 rounded font-medium">${l.followUp}</span>`;
        if (l.isOverdue) {
          followUpBadge = `<span class="bg-rose-50 text-rose-700 font-bold px-2 py-0.5 rounded border border-rose-200 flex items-center gap-1 w-max"><i data-lucide="alert-circle" class="w-3 h-3 text-rose-500"></i> Overdue (${l.followUp})</span>`;
        } else if (l.followUp === 'Today') {
          followUpBadge = `<span class="bg-amber-50 text-amber-700 font-bold px-2 py-0.5 rounded border border-amber-200 flex items-center gap-1 w-max"><i data-lucide="clock" class="w-3 h-3 text-amber-500"></i> Today</span>`;
        }

        const feeBadge = l.paid >= l.admFee 
          ? `<span class="bg-emerald-50 text-emerald-700 font-semibold px-2 py-0.5 rounded border border-emerald-200">Paid (${inr(l.paid)})</span>`
          : `<span class="text-slate-600">Token Due: ${inr(l.admFee)}</span>`;

        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-50/80 transition cursor-pointer group';
        tr.onclick = (e) => {
          if (!e.target.closest('button') && !e.target.closest('a')) {
            openStudentDrawer(l.id);
          }
        };

        tr.innerHTML = `
          <td class="p-3 text-center text-slate-400 font-mono text-[11px]">${rowNum}</td>
          <td class="py-3 px-2">
            <div class="flex items-center space-x-2.5">
              <div class="w-8 h-8 rounded-full bg-blue-100 text-blue-700 font-bold flex items-center justify-center text-xs shrink-0">
                ${getInitials(l.name)}
              </div>
              <div>
                <b class="text-slate-900 group-hover:text-blue-600 transition font-semibold block">${l.name}</b>
                <span class="text-[11px] text-slate-400">${l.city} • ID #${l.id}</span>
              </div>
            </div>
          </td>
          <td class="py-3 px-2">
            <b class="text-slate-800">${l.course}</b>
            <span class="text-[11px] text-slate-400 block">Intake 2026-27</span>
          </td>
          <td class="py-3 px-2">
            <span class="text-[11px] font-medium text-slate-600 bg-slate-100 px-2 py-0.5 rounded">
              ${l.source}
            </span>
          </td>
          <td class="py-3 px-2">
            <span class="font-medium text-slate-700">${l.counsellor}</span>
          </td>
          <td class="py-3 px-2">
            <span class="text-[11px] font-semibold px-2.5 py-0.5 rounded-full border ${STAGE_PILLS[l.stage]}">
              ${l.stage}
            </span>
          </td>
          <td class="py-3 px-2">
            <span class="text-[11px] font-medium ${verifiedDocs === totalDocs ? 'text-emerald-700 bg-emerald-50' : 'text-slate-600 bg-slate-100'} px-2 py-0.5 rounded border border-slate-200">
              ${verifiedDocs}/${totalDocs} Docs
            </span>
          </td>
          <td class="py-3 px-2">
            ${feeBadge}
          </td>
          <td class="py-3 px-2">
            ${followUpBadge}
          </td>
          <td class="py-3 px-3 text-right">
            <div class="flex items-center justify-end space-x-1">
              <button onclick="quickWhatsApp(${l.id})" title="Send WhatsApp Message" class="p-1.5 rounded-lg text-emerald-600 hover:bg-emerald-50 transition">
                <i data-lucide="message-circle" class="w-4 h-4"></i>
              </button>
              <button onclick="advanceStage(${l.id})" title="Advance Stage" class="p-1.5 rounded-lg text-blue-600 hover:bg-blue-50 transition">
                <i data-lucide="arrow-right-circle" class="w-4 h-4"></i>
              </button>
              <button onclick="openStudentDrawer(${l.id})" title="View Full Profile" class="p-1.5 rounded-lg text-slate-500 hover:bg-slate-100 transition">
                <i data-lucide="eye" class="w-4 h-4"></i>
              </button>
            </div>
          </td>
        `;
        tbody.appendChild(tr);
      });

      // Update Pagination Bar
      updatePaginationControls(startIndex, endIndex);
    }

    function updatePaginationControls(startIndex, endIndex) {
      const info = document.getElementById('paginationInfo');
      info.textContent = `Showing ${filteredLeads.length === 0 ? 0 : startIndex + 1} to ${endIndex} of ${filteredLeads.length} leads`;

      const totalPages = pageSize === 'all' ? 1 : Math.ceil(filteredLeads.length / Number(pageSize));
      document.getElementById('btnPrevPage').disabled = currentPage <= 1;
      document.getElementById('btnNextPage').disabled = currentPage >= totalPages;

      const btnContainer = document.getElementById('paginationPageBtns');
      btnContainer.innerHTML = '';
      for (let p = 1; p <= totalPages; p++) {
        const btn = document.createElement('button');
        btn.textContent = p;
        btn.className = (p === currentPage)
          ? 'px-2.5 py-1 rounded bg-blue-600 text-white font-bold text-xs'
          : 'px-2.5 py-1 rounded border border-slate-200 bg-white text-slate-700 hover:bg-slate-50 text-xs';
        btn.onclick = () => { currentPage = p; renderTable(); lucide.createIcons(); };
        btnContainer.appendChild(btn);
      }
    }

    function prevPage() {
      if (currentPage > 1) {
        currentPage--;
        renderTable();
        lucide.createIcons();
      }
    }

    function nextPage() {
      const totalPages = pageSize === 'all' ? 1 : Math.ceil(filteredLeads.length / Number(pageSize));
      if (currentPage < totalPages) {
        currentPage++;
        renderTable();
        lucide.createIcons();
      }
    }

    function changePageSize(val) {
      pageSize = val;
      currentPage = 1;
      renderTable();
      lucide.createIcons();
    }

    function renderKanban() {
      const board = document.getElementById('kanbanBoard');
      board.innerHTML = '';

      STAGES.forEach((stg, stgIdx) => {
        const stageLeads = filteredLeads.filter(l => l.stage === stg);
        const stageValue = stageLeads.reduce((acc, cur) => acc + cur.admFee, 0);

        const col = document.createElement('div');
        col.className = 'kanban-col bg-slate-100/80 rounded-xl p-3 border border-slate-200/90 flex flex-col max-h-[720px] shadow-2xs';

        // Column Header
        col.innerHTML = `
          <div class="flex items-center justify-between pb-2 mb-2 border-b border-slate-200">
            <div class="flex items-center gap-1.5">
              <span class="w-2.5 h-2.5 rounded-full ${stg === 'Enrollment' ? 'bg-emerald-500' : 'bg-blue-600'}"></span>
              <b class="text-xs font-bold text-slate-800">${stg}</b>
              <span class="bg-white text-slate-600 text-[10px] font-bold px-1.5 py-0.5 rounded-full shadow-2xs border border-slate-200">
                ${stageLeads.length}
              </span>
            </div>
            <span class="text-[10px] text-slate-400 font-medium">${inr(stageValue)}</span>
          </div>

          <div class="flex-1 overflow-y-auto space-y-2.5 pr-1 custom-scroll" id="col-leads-${stgIdx}">
            <!-- Lead Cards -->
          </div>
        `;

        const cardContainer = col.querySelector(`#col-leads-${stgIdx}`);

        if (stageLeads.length === 0) {
          cardContainer.innerHTML = `<div class="p-4 text-center text-slate-400 text-xs border border-dashed border-slate-200 rounded-lg">No leads in ${stg}</div>`;
        } else {
          stageLeads.forEach(l => {
            const card = document.createElement('div');
            card.className = 'bg-white rounded-lg p-3 border border-slate-200 shadow-2xs hover:shadow-xs hover:border-blue-300 transition cursor-pointer space-y-2';
            card.onclick = (e) => {
              if (!e.target.closest('button')) openStudentDrawer(l.id);
            };

            const verifiedDocs = l.docs.filter(Boolean).length;
            let followTag = '';
            if (l.isOverdue) {
              followTag = `<span class="bg-rose-50 text-rose-700 text-[10px] font-bold px-1.5 py-0.5 rounded border border-rose-200 flex items-center gap-0.5"><i data-lucide="alert-circle" class="w-3 h-3 text-rose-500"></i> Overdue</span>`;
            } else if (l.followUp === 'Today') {
              followTag = `<span class="bg-amber-50 text-amber-700 text-[10px] font-bold px-1.5 py-0.5 rounded border border-amber-200">Today</span>`;
            }

            card.innerHTML = `
              <div class="flex items-start justify-between">
                <div>
                  <b class="text-xs text-slate-900 block hover:text-blue-600 transition">${l.name}</b>
                  <span class="text-[10px] text-slate-400 font-medium">${l.course} • ${l.city}</span>
                </div>
                ${followTag}
              </div>

              <div class="flex items-center justify-between text-[11px] text-slate-500 pt-1 border-t border-slate-50">
                <span class="truncate max-w-[120px]"><i data-lucide="user" class="w-3 h-3 inline mr-0.5 text-slate-400"></i>${l.counsellor}</span>
                <span class="font-medium text-slate-600">${inr(l.admFee)}</span>
              </div>

              <div class="flex items-center justify-between pt-1">
                <span class="text-[10px] text-slate-400">${verifiedDocs}/4 Docs</span>
                <div class="flex items-center gap-1">
                  <button onclick="quickWhatsApp(${l.id})" class="p-1 text-emerald-600 hover:bg-emerald-50 rounded" title="Send WhatsApp">
                    <i data-lucide="message-circle" class="w-3.5 h-3.5"></i>
                  </button>
                  ${stgIdx < 6 ? `
                    <button onclick="advanceStage(${l.id})" class="text-[10px] font-semibold text-blue-600 hover:text-blue-800 bg-blue-50 px-2 py-0.5 rounded hover:bg-blue-100 transition flex items-center gap-0.5">
                      Next <i data-lucide="chevron-right" class="w-3 h-3"></i>
                    </button>
                  ` : `
                    <span class="text-[10px] font-bold text-emerald-600 flex items-center"><i data-lucide="check" class="w-3 h-3 mr-0.5"></i>Enrolled</span>
                  `}
                </div>
              </div>
            `;
            cardContainer.appendChild(card);
          });
        }

        board.appendChild(col);
      });
    }

    // ----------------------------------------------------
    // 7. EXECUTIVE DASHBOARD & COUNTERS
    // ----------------------------------------------------
    function updateExecutiveStats() {
      // Total leads
      document.getElementById('kpi-leads').textContent = leads.length;
      document.getElementById('pipeLeadCount').textContent = leads.length;

      // Active pipeline
      const activeCount = leads.filter(l => l.stage !== 'Enquiry' && l.stage !== 'Enrollment').length;
      document.getElementById('kpi-pipeline').textContent = activeCount;

      // Overdue badge
      const overdueCount = leads.filter(l => l.isOverdue).length;
      document.getElementById('overdueBadge').textContent = `${overdueCount} Overdue`;
      document.getElementById('taskOverdueCount').textContent = `${overdueCount} Overdue`;

      // Fee collected
      const totalPaid = leads.reduce((acc, cur) => acc + (cur.paid || 0), 0);
      document.getElementById('kpi-fee').textContent = inr(totalPaid);

      // Doc verification rate
      const totalDocsPossible = leads.length * 4;
      const totalDocsDone = leads.reduce((acc, cur) => acc + cur.docs.filter(Boolean).length, 0);
      const rate = Math.round((totalDocsDone / totalDocsPossible) * 100);
      document.getElementById('kpi-docs').textContent = `${rate}%`;

      // Funnel Bars
      const funnelContainer = document.getElementById('funnelBars');
      funnelContainer.innerHTML = '';
      STAGES.forEach(stg => {
        const count = leads.filter(l => l.stage === stg).length;
        const pct = Math.round((count / leads.length) * 100);
        
        const row = document.createElement('div');
        row.className = 'space-y-1';
        row.innerHTML = `
          <div class="flex justify-between text-xs font-semibold text-slate-700">
            <span>${stg}</span>
            <span class="text-slate-500">${count} students (${pct}%)</span>
          </div>
          <div class="w-full bg-slate-100 rounded-full h-2 overflow-hidden">
            <div class="h-2 rounded-full ${stg === 'Enrollment' ? 'bg-emerald-500' : 'bg-blue-600'}" style="width: ${Math.max(pct, 6)}%"></div>
          </div>
        `;
        funnelContainer.appendChild(row);
      });

      // Quick Recent Leads Table (top 6)
      renderQuickLeadsTable();
    }

    function renderQuickLeadsTable() {
      const tbody = document.getElementById('quickLeadsTable');
      tbody.innerHTML = '';
      const topRecent = leads.slice(0, 6);

      topRecent.forEach(l => {
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-50/80 transition cursor-pointer';
        tr.onclick = (e) => {
          if (!e.target.closest('button')) openStudentDrawer(l.id);
        };

        tr.innerHTML = `
          <td class="py-2.5">
            <b class="text-slate-900 block font-semibold">${l.name}</b>
            <span class="text-[11px] text-slate-400">ID #${l.id}</span>
          </td>
          <td class="py-2.5 font-mono text-[11px] text-slate-600">${l.phone}</td>
          <td class="py-2.5">
            <b class="text-slate-800">${l.course}</b>
            <span class="text-[11px] text-slate-400 block">${l.city}</span>
          </td>
          <td class="py-2.5 text-slate-600 font-medium">${l.source}</td>
          <td class="py-2.5">
            <span class="text-[10px] font-semibold px-2 py-0.5 rounded-full border ${STAGE_PILLS[l.stage]}">
              ${l.stage}
            </span>
          </td>
          <td class="py-2.5 text-slate-700 font-medium">${l.counsellor}</td>
          <td class="py-2.5">
            ${l.isOverdue 
              ? `<span class="text-rose-600 font-bold bg-rose-50 px-2 py-0.5 rounded border border-rose-200">Overdue</span>`
              : (l.followUp === 'Today' ? `<span class="text-amber-700 font-bold bg-amber-50 px-2 py-0.5 rounded border border-amber-200">Today</span>` : `<span class="text-slate-600">${l.followUp}</span>`)
            }
          </td>
          <td class="py-2.5 text-right">
            <div class="flex items-center justify-end space-x-1">
              <button onclick="quickWhatsApp(${l.id})" class="p-1 text-emerald-600 hover:bg-emerald-50 rounded">
                <i data-lucide="message-circle" class="w-3.5 h-3.5"></i>
              </button>
              <button onclick="openStudentDrawer(${l.id})" class="p-1 text-slate-500 hover:bg-slate-100 rounded">
                <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
              </button>
            </div>
          </td>
        `;
        tbody.appendChild(tr);
      });
    }

    // ----------------------------------------------------
    // 8. TASKS & FOLLOW-UPS VIEW
    // ----------------------------------------------------
    function renderTasksView() {
      const taskCounsellorName = document.getElementById('taskCounsellorName');
      if (currentRole === 'sneha') taskCounsellorName.textContent = 'Counsellor: Sneha Patel';
      else if (currentRole === 'amit') taskCounsellorName.textContent = 'Counsellor: Amit Kumar';
      else taskCounsellorName.textContent = 'All Counsellors';

      const userLeads = leads.filter(l => {
        if (currentRole === 'sneha' && l.counsellorId !== 'sneha') return false;
        if (currentRole === 'amit' && l.counsellorId !== 'amit') return false;
        return true;
      });

      // 1. Overdue
      const overdueList = userLeads.filter(l => l.isOverdue);
      document.getElementById('overdueCountLabel').textContent = `${overdueList.length} Students`;
      const overdueTable = document.getElementById('overdueTasksTable');
      overdueTable.innerHTML = '';
      if (overdueList.length === 0) {
        overdueTable.innerHTML = `<tr><td colspan="7" class="py-4 text-center text-slate-400">🎉 No overdue follow-ups! Great job.</td></tr>`;
      } else {
        overdueList.forEach(l => {
          const tr = document.createElement('tr');
          tr.className = 'hover:bg-rose-50/50';
          tr.innerHTML = `
            <td class="py-2.5">
              <b class="text-slate-900 font-semibold cursor-pointer hover:text-blue-600" onclick="openStudentDrawer(${l.id})">${l.name}</b>
              <span class="text-[11px] text-slate-400 block">${l.city}</span>
            </td>
            <td class="py-2.5 font-mono text-[11px]">${l.phone}</td>
            <td class="py-2.5 font-semibold text-slate-800">${l.course}</td>
            <td class="py-2.5"><span class="px-2 py-0.5 rounded text-[10px] font-semibold ${STAGE_PILLS[l.stage]}">${l.stage}</span></td>
            <td class="py-2.5 text-rose-700 font-bold">${l.followUp}</td>
            <td class="py-2.5 text-slate-600">${l.counsellor}</td>
            <td class="py-2.5 text-right">
              <div class="flex items-center justify-end space-x-1.5">
                <button onclick="quickWhatsApp(${l.id})" class="px-2 py-1 bg-emerald-50 text-emerald-700 font-semibold rounded hover:bg-emerald-100 flex items-center gap-1">
                  <i data-lucide="message-circle" class="w-3 h-3"></i> WhatsApp
                </button>
                <button onclick="markTaskDone(${l.id})" class="px-2 py-1 bg-blue-600 text-white font-semibold rounded hover:bg-blue-700 flex items-center gap-1">
                  <i data-lucide="check" class="w-3 h-3"></i> Done
                </button>
              </div>
            </td>
          `;
          overdueTable.appendChild(tr);
        });
      }

      // 2. Today
      const todayList = userLeads.filter(l => l.followUp === 'Today');
      document.getElementById('todayTasksCountLabel').textContent = `${todayList.length} Students`;
      const todayTable = document.getElementById('dueTodayTasksTable');
      todayTable.innerHTML = '';
      if (todayList.length === 0) {
        todayTable.innerHTML = `<tr><td colspan="7" class="py-4 text-center text-slate-400">No calls scheduled for today yet.</td></tr>`;
      } else {
        todayList.forEach(l => {
          const lastNote = l.notes && l.notes.length > 0 ? l.notes[0] : 'No notes recorded yet';
          const tr = document.createElement('tr');
          tr.className = 'hover:bg-slate-50/80';
          tr.innerHTML = `
            <td class="py-2.5">
              <b class="text-slate-900 font-semibold cursor-pointer hover:text-blue-600" onclick="openStudentDrawer(${l.id})">${l.name}</b>
              <span class="text-[11px] text-slate-400 block">${l.city}</span>
            </td>
            <td class="py-2.5 font-mono text-[11px]">${l.phone}</td>
            <td class="py-2.5 font-semibold text-slate-800">${l.course}</td>
            <td class="py-2.5"><span class="px-2 py-0.5 rounded text-[10px] font-semibold ${STAGE_PILLS[l.stage]}">${l.stage}</span></td>
            <td class="py-2.5 text-slate-600">${l.counsellor}</td>
            <td class="py-2.5 text-slate-500 max-w-[200px] truncate" title="${lastNote}">${lastNote}</td>
            <td class="py-2.5 text-right">
              <div class="flex items-center justify-end space-x-1.5">
                <button onclick="quickWhatsApp(${l.id})" class="px-2 py-1 bg-emerald-50 text-emerald-700 font-semibold rounded hover:bg-emerald-100 flex items-center gap-1">
                  <i data-lucide="message-circle" class="w-3 h-3"></i>
                </button>
                <button onclick="rescheduleTask(${l.id}, 1)" class="px-2 py-1 bg-slate-100 text-slate-700 font-semibold rounded hover:bg-slate-200" title="Reschedule +1 Day">
                  +1d
                </button>
                <button onclick="markTaskDone(${l.id})" class="px-2.5 py-1 bg-blue-600 text-white font-semibold rounded hover:bg-blue-700 flex items-center gap-1">
                  <i data-lucide="check" class="w-3 h-3"></i> Done
                </button>
              </div>
            </td>
          `;
          todayTable.appendChild(tr);
        });
      }

      // 3. Upcoming
      const upcomingList = userLeads.filter(l => !l.isOverdue && l.followUp !== 'Today' && l.followUp !== 'Completed');
      document.getElementById('upcomingCountLabel').textContent = `${upcomingList.length} Students`;
      const upcomingTable = document.getElementById('upcomingTasksTable');
      upcomingTable.innerHTML = '';
      if (upcomingList.length === 0) {
        upcomingTable.innerHTML = `<tr><td colspan="7" class="py-4 text-center text-slate-400">No upcoming tasks scheduled.</td></tr>`;
      } else {
        upcomingList.forEach(l => {
          const tr = document.createElement('tr');
          tr.className = 'hover:bg-slate-50/80';
          tr.innerHTML = `
            <td class="py-2.5">
              <b class="text-slate-900 font-semibold cursor-pointer hover:text-blue-600" onclick="openStudentDrawer(${l.id})">${l.name}</b>
              <span class="text-[11px] text-slate-400 block">${l.city}</span>
            </td>
            <td class="py-2.5 font-mono text-[11px]">${l.phone}</td>
            <td class="py-2.5 font-semibold text-slate-800">${l.course}</td>
            <td class="py-2.5"><span class="px-2 py-0.5 rounded text-[10px] font-semibold ${STAGE_PILLS[l.stage]}">${l.stage}</span></td>
            <td class="py-2.5 text-blue-700 font-medium">${l.followUp}</td>
            <td class="py-2.5 text-slate-600">${l.counsellor}</td>
            <td class="py-2.5 text-right">
              <button onclick="openStudentDrawer(${l.id})" class="text-blue-600 hover:underline font-semibold">
                View Profile →
              </button>
            </td>
          `;
          upcomingTable.appendChild(tr);
        });
      }
    }

    function markTaskDone(leadId) {
      const lead = leads.find(l => l.id === leadId);
      if (lead) {
        lead.isOverdue = false;
        lead.followUp = '24 Nov 2026';
        lead.notes.unshift(`Follow-up completed on 19 Nov 2026. Next follow-up set for 24 Nov.`);
        showToast(`Follow-up marked completed for ${lead.name}`);
        renderAll();
      }
    }

    function rescheduleTask(leadId, days) {
      const lead = leads.find(l => l.id === leadId);
      if (lead) {
        lead.isOverdue = false;
        lead.followUp = `20 Nov 2026`;
        lead.notes.unshift(`Follow-up rescheduled by +${days} day.`);
        showToast(`Rescheduled follow-up for ${lead.name}`);
        renderAll();
      }
    }

    // ----------------------------------------------------
    // 9. WHATSAPP AUTOMATION & SMARTPHONE PREVIEW
    // ----------------------------------------------------
    function renderWhatsAppView() {
      const list = document.getElementById('templateList');
      list.innerHTML = '';

      TEMPLATES.forEach(t => {
        const isSelected = (t.id === selectedTplId);
        const card = document.createElement('div');
        card.className = `p-4 rounded-xl border transition cursor-pointer ${isSelected ? 'bg-blue-50/50 border-blue-400 shadow-xs' : 'bg-white border-slate-200 hover:border-slate-300'}`;
        card.onclick = () => selectTemplate(t.id);

        card.innerHTML = `
          <div class="flex items-center justify-between mb-1.5">
            <div class="flex items-center space-x-2">
              <span class="w-6 h-6 rounded-md bg-emerald-100 text-emerald-700 flex items-center justify-center font-bold text-xs">
                WA
              </span>
              <b class="text-xs font-bold text-slate-900">${t.name}</b>
            </div>
            
            <label class="relative inline-flex items-center cursor-pointer" onclick="event.stopPropagation()">
              <input type="checkbox" ${t.on ? 'checked' : ''} onchange="toggleTemplate('${t.id}', this.checked)" class="sr-only peer">
              <div class="w-8 h-4 bg-slate-200 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-3 after:w-3 after:transition-all peer-checked:bg-emerald-600"></div>
            </label>
          </div>

          <p class="text-[11px] text-slate-500 mb-2"><b>Trigger:</b> ${t.trigger}</p>
          <div class="p-2.5 bg-slate-50 rounded-lg border border-slate-200 text-[11px] text-slate-700 font-mono leading-relaxed">
            ${t.text}
          </div>
        `;
        list.appendChild(card);
      });

      updatePhonePreview();
    }

    function selectTemplate(tplId) {
      selectedTplId = tplId;
      renderWhatsAppView();
    }

    function toggleTemplate(tplId, isChecked) {
      const t = TEMPLATES.find(x => x.id === tplId);
      if (t) {
        t.on = isChecked;
        showToast(`${t.name} is now ${isChecked ? 'Active' : 'Paused'}`);
      }
    }

    function updatePhonePreview() {
      const t = TEMPLATES.find(x => x.id === selectedTplId) || TEMPLATES[0];
      const sampleLead = leads[0];
      
      let rendered = t.text
        .replace('{name}', sampleLead.name)
        .replace('{course}', sampleLead.course)
        .replace('{counsellor}', sampleLead.counsellor)
        .replace('{id}', sampleLead.id);

      document.getElementById('phoneBubbleText').textContent = rendered;
      document.getElementById('previewSender').textContent = `Apex Admissions • ${t.name}`;
      lucide.createIcons();
    }

    function triggerBroadcastModal() {
      const t = TEMPLATES.find(x => x.id === selectedTplId) || TEMPLATES[0];
      showToast(`Test WhatsApp message triggered successfully!`);
    }

    function quickWhatsApp(leadId) {
      const lead = leads.find(l => l.id === leadId);
      if (!lead) return;
      const cleanPhone = lead.phone.replace(/\\D/g, '');
      const url = `https://wa.me/${cleanPhone}?text=Hi%20${encodeURIComponent(lead.name)},%20this%20is%20${encodeURIComponent(lead.counsellor)}%20from%20Apex%20Institute%20Admissions.`;
      window.open(url, '_blank');
      showToast(`Opening WhatsApp chat with ${lead.name}`);
    }

    // ----------------------------------------------------
    // 10. COUNSELLORS & ROLES VIEW
    // ----------------------------------------------------
    function renderCounsellorsView() {
      const tbody = document.getElementById('counsellorTableBody');
      tbody.innerHTML = '';

      COUNSELLORS.forEach(c => {
        // Calculate dynamic counts
        const assignedLeads = leads.filter(l => l.counsellor === c.name);
        const overdue = assignedLeads.filter(l => l.isOverdue).length;
        const todayTasks = assignedLeads.filter(l => l.followUp === 'Today').length;
        const enrolled = assignedLeads.filter(l => l.stage === 'Enrollment').length;
        const totalFee = assignedLeads.reduce((acc, cur) => acc + (cur.paid || 0), 0);
        const convRate = assignedLeads.length > 0 ? Math.round((enrolled / assignedLeads.length) * 100) : 0;

        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-50 transition';
        tr.innerHTML = `
          <td class="p-3">
            <div class="flex items-center space-x-2.5">
              <div class="w-8 h-8 rounded-full bg-blue-100 text-blue-700 font-bold flex items-center justify-center text-xs">
                ${getInitials(c.name)}
              </div>
              <div>
                <b class="text-slate-900 block font-semibold">${c.name}</b>
                <span class="text-[11px] text-slate-400">${c.name.toLowerCase().replace(' ', '.')}@apex.edu</span>
              </div>
            </div>
          </td>
          <td class="py-3 px-2">
            <span class="text-[11px] font-semibold bg-slate-100 text-slate-700 px-2 py-0.5 rounded border border-slate-200">
              ${c.role}
            </span>
          </td>
          <td class="py-3 px-2 font-bold text-slate-800">${assignedLeads.length} Leads</td>
          <td class="py-3 px-2">
            <span class="${overdue > 0 ? 'text-rose-600 font-bold' : 'text-slate-600'}">
              ${overdue} Overdue • ${todayTasks} Today
            </span>
          </td>
          <td class="py-3 px-2 font-bold text-emerald-700">${enrolled} Enrolled</td>
          <td class="py-3 px-2 font-semibold text-slate-700">${convRate}%</td>
          <td class="py-3 px-2 font-bold text-slate-900">${inr(totalFee)}</td>
          <td class="py-3 px-2 text-right">
            <span class="text-[11px] px-2 py-0.5 rounded-full font-semibold ${assignedLeads.length > 10 ? 'bg-amber-50 text-amber-700 border border-amber-200' : 'bg-emerald-50 text-emerald-700 border border-emerald-200'}">
              ${assignedLeads.length > 10 ? 'Heavy Load' : 'Available'}
            </span>
          </td>
        `;
        tbody.appendChild(tr);
      });
    }

    // ----------------------------------------------------
    // 11. SLIDE-OVER STUDENT DRAWER
    // ----------------------------------------------------
    function openStudentDrawer(leadId) {
      activeStudentId = leadId;
      const lead = leads.find(l => l.id === leadId);
      if (!lead) return;

      document.getElementById('drawerAvatar').textContent = getInitials(lead.name);
      document.getElementById('drawerName').textContent = lead.name;
      document.getElementById('drawerSubline').textContent = `${lead.course} • ${lead.city} • Application ID: #${lead.id}`;
      
      const stagePill = document.getElementById('drawerStagePill');
      stagePill.textContent = lead.stage;
      stagePill.className = `text-[11px] font-semibold px-2.5 py-0.5 rounded-full border ${STAGE_PILLS[lead.stage]}`;

      document.getElementById('drawerChatwootLink').href = `https://chat.pranavcloud.in`;

      // 7-Stage Stepper
      const curStageIdx = STAGES.indexOf(lead.stage);
      const stepperContainer = document.getElementById('drawerStepperBars');
      stepperContainer.innerHTML = '';
      STAGES.forEach((stg, sIdx) => {
        const bar = document.createElement('div');
        bar.className = (sIdx <= curStageIdx) 
          ? 'h-2 rounded-sm bg-blue-600' 
          : 'h-2 rounded-sm bg-slate-200';
        bar.title = stg;
        stepperContainer.appendChild(bar);
      });

      const nextBtn = document.getElementById('drawerNextStageBtn');
      if (curStageIdx < 6) {
        nextBtn.innerHTML = `Advance to ${STAGES[curStageIdx + 1]} <i data-lucide="arrow-right" class="w-3 h-3 ml-1"></i>`;
        nextBtn.classList.remove('hidden');
      } else {
        nextBtn.classList.add('hidden');
      }

      // Tab 1: Overview
      document.getElementById('infoPhone').textContent = lead.phone;
      document.getElementById('infoEmail').textContent = lead.email || 'N/A';
      document.getElementById('infoCity').textContent = lead.city;
      document.getElementById('infoSource').textContent = lead.source;
      document.getElementById('infoCounsellor').textContent = lead.counsellor;
      document.getElementById('infoFollowUp').textContent = lead.isOverdue ? `Overdue (${lead.followUp})` : lead.followUp;
      document.getElementById('infoFather').textContent = lead.father || 'Not recorded';

      const acadGrid = document.getElementById('infoAcademicsGrid');
      acadGrid.innerHTML = '';
      if (lead.academics) {
        acadGrid.innerHTML = `
          <div><span class="text-slate-400 block">Class 10th Score</span><b class="text-slate-800">${lead.academics.t10 || 'N/A'}</b></div>
          <div><span class="text-slate-400 block">Class 12th Score</span><b class="text-slate-800">${lead.academics.t12 || 'N/A'}</b></div>
          <div><span class="text-slate-400 block">Graduation / Degree</span><b class="text-slate-800">${lead.academics.grad || 'N/A'}</b></div>
          <div><span class="text-slate-400 block">Entrance Exam Score</span><b class="text-slate-800">${lead.academics.test || 'N/A'}</b></div>
        `;
      }

      // Tab 2: Docs
      const docsList = document.getElementById('drawerDocsList');
      docsList.innerHTML = '';
      let verifiedCount = 0;
      DOC_NAMES.forEach((docName, dIdx) => {
        const isVer = lead.docs[dIdx];
        if (isVer) verifiedCount++;

        const div = document.createElement('div');
        div.className = `p-3 rounded-lg border flex items-center justify-between transition ${isVer ? 'bg-emerald-50/60 border-emerald-200' : 'bg-slate-50 border-slate-200'}`;
        div.innerHTML = `
          <div class="flex items-center space-x-2.5">
            <div class="w-6 h-6 rounded-full flex items-center justify-center ${isVer ? 'bg-emerald-600 text-white' : 'bg-slate-200 text-slate-400'}">
              <i data-lucide="${isVer ? 'check' : 'clock'}" class="w-3.5 h-3.5"></i>
            </div>
            <div>
              <b class="text-xs font-semibold ${isVer ? 'text-emerald-900' : 'text-slate-700'}">${docName}</b>
              <span class="text-[10px] text-slate-400 block">${isVer ? 'Verified by Registrar' : 'Pending submission from student'}</span>
            </div>
          </div>

          <button onclick="toggleDocVerification(${lead.id}, ${dIdx})" class="px-2.5 py-1 text-xs font-semibold rounded ${isVer ? 'bg-white text-rose-600 border border-rose-200 hover:bg-rose-50' : 'bg-blue-600 text-white hover:bg-blue-700'} transition">
            ${isVer ? 'Mark Unverified' : 'Verify Document'}
          </button>
        `;
        docsList.appendChild(div);
      });
      document.getElementById('drawerDocsBadge').textContent = `${verifiedCount}/4`;

      // Tab 3: Fees
      document.getElementById('drawerTotalFee').textContent = inr(lead.totalFee);
      document.getElementById('drawerAdmFee').textContent = inr(lead.admFee);
      document.getElementById('drawerAmountPaid').textContent = inr(lead.paid || 0);
      document.getElementById('drawerBalance').textContent = inr(lead.admFee - (lead.paid || 0));

      const feeBadge = document.getElementById('drawerFeeBadge');
      if (lead.paid >= lead.admFee) {
        feeBadge.textContent = 'Token Paid · Confirmed';
        feeBadge.className = 'text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200';
      } else {
        feeBadge.textContent = 'Token Due';
        feeBadge.className = 'text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-50 text-amber-700 border border-amber-200';
      }

      const payHistory = document.getElementById('drawerPaymentHistory');
      payHistory.innerHTML = '';
      if (lead.paid > 0) {
        payHistory.innerHTML = `
          <div class="p-2.5 rounded-lg border border-emerald-200 bg-emerald-50/50 flex items-center justify-between">
            <div>
              <b class="text-emerald-900 block font-semibold">${inr(lead.paid)} Received (Token Fee)</b>
              <span class="text-[10px] text-slate-500">Ref: UTR8291048 • Payment Verified</span>
            </div>
            <span class="text-[10px] font-bold text-emerald-700 bg-white px-2 py-0.5 rounded border border-emerald-200">
              Receipt Issued
            </span>
          </div>
        `;
      } else {
        payHistory.innerHTML = `<div class="p-3 text-center text-slate-400 bg-slate-50 rounded-lg">No payment transactions recorded yet.</div>`;
      }

      // Tab 4: Notes
      const notesList = document.getElementById('drawerNotesList');
      notesList.innerHTML = '';
      (lead.notes || []).forEach(note => {
        const item = document.createElement('div');
        item.className = 'p-2.5 bg-slate-50 rounded-lg border border-slate-200 text-slate-700 text-xs leading-relaxed';
        item.textContent = note;
        notesList.appendChild(item);
      });

      // Tab 5: WhatsApp Templates
      const waContainer = document.getElementById('drawerWaTemplates');
      waContainer.innerHTML = '';
      TEMPLATES.forEach(t => {
        const box = document.createElement('div');
        box.className = 'p-3 rounded-lg border border-slate-200 bg-slate-50/50 space-y-1.5';
        box.innerHTML = `
          <div class="flex items-center justify-between">
            <b class="text-xs font-semibold text-slate-800">${t.name}</b>
            <button onclick="sendQuickWhatsAppTemplate(${lead.id}, '${t.id}')" class="px-2 py-1 text-xs bg-emerald-600 hover:bg-emerald-700 text-white rounded font-medium transition flex items-center gap-1">
              <i data-lucide="send" class="w-3 h-3"></i> Send Now
            </button>
          </div>
          <p class="text-[11px] text-slate-500 font-mono">${t.text.replace('{name}', lead.name).replace('{course}', lead.course).replace('{counsellor}', lead.counsellor).replace('{id}', lead.id)}</p>
        `;
        waContainer.appendChild(box);
      });

      // Default to info tab
      setDrawerTab('info');

      // Show drawer
      document.getElementById('studentDrawerBackdrop').classList.remove('hidden');
      document.getElementById('studentDrawer').classList.remove('translate-x-full');
      lucide.createIcons();
    }

    function closeDrawer() {
      document.getElementById('studentDrawerBackdrop').classList.add('hidden');
      document.getElementById('studentDrawer').classList.add('translate-x-full');
      activeStudentId = null;
    }

    function setDrawerTab(tabName) {
      const tabs = ['info', 'docs', 'fees', 'notes', 'wa'];
      tabs.forEach(t => {
        const btn = document.getElementById(`dtab-${t}`);
        const view = document.getElementById(`dview-${t}`);
        if (t === tabName) {
          btn.className = 'py-2.5 px-3 text-blue-600 border-b-2 border-blue-600 font-bold';
          view.classList.remove('hidden');
        } else {
          btn.className = 'py-2.5 px-3 text-slate-500 hover:text-slate-800 border-b-2 border-transparent';
          view.classList.add('hidden');
        }
      });
      lucide.createIcons();
    }

    function advanceStage(leadId) {
      const lead = leads.find(l => l.id === leadId);
      if (!lead) return;
      const curIdx = STAGES.indexOf(lead.stage);
      if (curIdx < STAGES.length - 1) {
        const nextStage = STAGES[curIdx + 1];
        lead.stage = nextStage;
        lead.notes.unshift(`Stage advanced to ${nextStage} on 19 Nov 2026. Auto-notification sent to student.`);
        showToast(`Stage advanced to ${nextStage} for ${lead.name}`);
        renderAll();
        if (activeStudentId === leadId) openStudentDrawer(leadId);
      }
    }

    function advanceCurrentStudentStage() {
      if (activeStudentId) advanceStage(activeStudentId);
    }

    function toggleDocVerification(leadId, docIdx) {
      const lead = leads.find(l => l.id === leadId);
      if (!lead) return;
      lead.docs[docIdx] = !lead.docs[docIdx];
      const statusText = lead.docs[docIdx] ? 'verified' : 'marked unverified';
      lead.notes.unshift(`Document '${DOC_NAMES[docIdx]}' ${statusText} by Registrar on 19 Nov 2026.`);
      showToast(`Document ${statusText}`);
      openStudentDrawer(leadId);
      renderAll();
    }

    function addCurrentStudentNote() {
      if (!activeStudentId) return;
      const input = document.getElementById('drawerNoteInput');
      const text = input.value.trim();
      if (!text) return;
      const lead = leads.find(l => l.id === activeStudentId);
      lead.notes.unshift(`Counsellor Call Note: ${text}`);
      input.value = '';
      showToast('Internal note saved and synced to Chatwoot');
      openStudentDrawer(activeStudentId);
      renderAll();
    }

    function drawerQuickWhatsApp() {
      if (activeStudentId) quickWhatsApp(activeStudentId);
    }

    function drawerQuickCall() {
      const lead = leads.find(l => l.id === activeStudentId);
      if (lead) {
        window.open(`tel:${lead.phone.replace(/\\D/g, '')}`, '_self');
      }
    }

    function sendQuickWhatsAppTemplate(leadId, tplId) {
      const lead = leads.find(l => l.id === leadId);
      const t = TEMPLATES.find(x => x.id === tplId);
      if (lead && t) {
        lead.notes.unshift(`WhatsApp Template sent: '${t.name}' on 19 Nov 2026.`);
        showToast(`WhatsApp message '${t.name}' sent to ${lead.name}!`);
        openStudentDrawer(leadId);
        renderAll();
      }
    }

    // ----------------------------------------------------
    // 12. RECORD PAYMENT MODAL
    // ----------------------------------------------------
    function openRecordPaymentModal() {
      if (!activeStudentId) return;
      const lead = leads.find(l => l.id === activeStudentId);
      document.getElementById('paymentModalStudentName').textContent = `${lead.name} (${lead.course})`;
      document.getElementById('payAmount').value = lead.admFee - (lead.paid || 0);
      document.getElementById('payRef').value = 'UTR' + Math.floor(1000000 + Math.random() * 9000000);
      document.getElementById('modalPayment').classList.remove('hidden');
    }

    function closePaymentModal() {
      document.getElementById('modalPayment').classList.add('hidden');
    }

    function submitPayment(e) {
      e.preventDefault();
      if (!activeStudentId) return;
      const lead = leads.find(l => l.id === activeStudentId);
      const amount = Number(document.getElementById('payAmount').value);
      const mode = document.getElementById('payMode').value;
      const ref = document.getElementById('payRef').value;
      
      lead.paid = (lead.paid || 0) + amount;
      if (lead.paid >= lead.admFee && lead.stage === 'Fee Payment') {
        lead.stage = 'Enrollment';
      }
      lead.notes.unshift(`Fee Payment Recorded: ${inr(amount)} via ${mode} (Ref: ${ref}).`);
      
      closePaymentModal();
      showToast(`Payment of ${inr(amount)} recorded! Receipt generated.`);
      openStudentDrawer(activeStudentId);
      renderAll();
    }

    // ----------------------------------------------------
    // 13. ADD NEW LEAD MODAL & DUPLICATE CHECK
    // ----------------------------------------------------
    function openAddModal() {
      document.getElementById('addLeadDupeAlert').classList.add('hidden');
      document.getElementById('newLeadName').value = '';
      document.getElementById('newLeadPhone').value = '';
      document.getElementById('newLeadEmail').value = '';
      document.getElementById('newLeadCity').value = '';
      document.getElementById('newLeadNotes').value = '';
      document.getElementById('modalAddLead').classList.remove('hidden');
    }

    function closeAddModal() {
      document.getElementById('modalAddLead').classList.add('hidden');
    }

    function checkDuplicatePhone(phoneInput) {
      const clean = phoneInput.replace(/\\D/g, '');
      const alertBox = document.getElementById('addLeadDupeAlert');
      const dupeText = document.getElementById('addLeadDupeText');

      if (clean.length >= 8) {
        const existing = leads.find(l => l.phone.replace(/\\D/g, '').includes(clean));
        if (existing) {
          dupeText.textContent = `Warning: ${existing.name} is already registered with this number (${existing.phone}) under Counsellor ${existing.counsellor} in stage '${existing.stage}'.`;
          alertBox.classList.remove('hidden');
          return;
        }
      }
      alertBox.classList.add('hidden');
    }

    function submitNewLead(e) {
      e.preventDefault();
      const name = document.getElementById('newLeadName').value.trim();
      const rawPhone = document.getElementById('newLeadPhone').value.trim();
      const email = document.getElementById('newLeadEmail').value.trim();
      const course = document.getElementById('newLeadCourse').value;
      const source = document.getElementById('newLeadSource').value;
      const city = document.getElementById('newLeadCity').value.trim() || 'New Delhi';
      const counChoice = document.getElementById('newLeadCounsellor').value;
      const notes = document.getElementById('newLeadNotes').value.trim();

      // Check duplicate
      const cleanPhone = rawPhone.replace(/\\D/g, '');
      const existing = leads.find(l => l.phone.replace(/\\D/g, '').includes(cleanPhone));
      if (existing) {
        if (!confirm(`Duplicate detected: ${existing.name} already exists. Do you still want to proceed?`)) {
          return;
        }
      }

      // Assign Counsellor
      let counsellor = counChoice;
      let counsellorId = 'sneha';
      if (counChoice === 'auto') {
        const pool = ['Sneha Patel', 'Amit Kumar', 'Priya Sharma'];
        counsellor = pool[leads.length % pool.length];
      }
      if (counsellor === 'Amit Kumar') counsellorId = 'amit';
      if (counsellor === 'Priya Sharma') counsellorId = 'lead';

      // Course Fee Mapping
      const feeMap = {
        'MBA': { total: 185000, adm: 46250 },
        'B.Tech CSE': { total: 220000, adm: 55000 },
        'BBA': { total: 140000, adm: 35000 },
        'MCA': { total: 160000, adm: 40000 },
        'BCA': { total: 130000, adm: 32500 },
        'B.Sc Nursing': { total: 120000, adm: 30000 },
        'Data Science': { total: 190000, adm: 47500 },
        'B.Des': { total: 175000, adm: 43750 }
      };

      const fees = feeMap[course] || { total: 150000, adm: 37500 };
      const newId = 100 + leads.length + 1;

      const newLeadObj = {
        id: newId,
        name: name,
        phone: rawPhone.startsWith('+91') ? rawPhone : '+91 ' + rawPhone,
        email: email || `${name.toLowerCase().replace(/\\s+/g, '.')}@gmail.com`,
        course: course,
        source: source,
        stage: 'Enquiry',
        counsellor: counsellor,
        counsellorId: counsellorId,
        totalFee: fees.total,
        admFee: fees.adm,
        paid: 0,
        city: city,
        followUp: 'Today',
        isOverdue: false,
        docs: [false, false, false, false],
        father: 'Parent Contact Pending',
        academics: { t10: 'N/A', t12: 'N/A', grad: 'N/A', test: 'N/A' },
        notes: [notes || `Enquiry received via ${source}. Assigned to ${counsellor}. Auto-acknowledgement WhatsApp queued.`]
      };

      leads.unshift(newLeadObj);
      closeAddModal();
      showToast(`New student enquiry for ${name} created and assigned to ${counsellor}!`);
      applyFilters();
      renderAll();
    }

    // ----------------------------------------------------
    // 14. BULK CSV IMPORT
    // ----------------------------------------------------
    function openImportModal() {
      document.getElementById('modalImport').classList.remove('hidden');
    }

    function closeImportModal() {
      document.getElementById('modalImport').classList.add('hidden');
    }

    function loadSampleCSV() {
      const sample = `Name, Phone, Course, City
Aditi Sen, 9823411122, MBA, Kolkata
Rajeev Menon, 9845022233, B.Tech CSE, Kochi
Karan Joshi, 9811233344, BBA, Delhi
Fatima Sheikh, 9876544455, MCA, Lucknow
Naveen Reddy, 9988755566, Data Science, Bangalore`;
      document.getElementById('importCSVText').value = sample;
    }

    function executeCSVImport() {
      const raw = document.getElementById('importCSVText').value.trim();
      if (!raw) {
        alert('Please paste CSV rows to import');
        return;
      }

      const lines = raw.split('\\n').map(l => l.trim()).filter(Boolean);
      let imported = 0;
      let dupes = 0;

      const counsellorsList = ['Sneha Patel', 'Amit Kumar', 'Priya Sharma'];

      lines.forEach((line, idx) => {
        if (idx === 0 && line.toLowerCase().includes('name') && line.toLowerCase().includes('phone')) {
          return; // Skip header
        }

        const cols = line.split(',').map(c => c.trim());
        if (cols.length < 2) return;

        const name = cols[0];
        const phone = cols[1];
        const course = cols[2] || 'MBA';
        const city = cols[3] || 'Pune';

        // Check duplicate
        const clean = phone.replace(/\\D/g, '');
        if (leads.some(l => l.phone.replace(/\\D/g, '').includes(clean))) {
          dupes++;
          return;
        }

        const coun = counsellorsList[(leads.length) % counsellorsList.length];
        const cid = coun === 'Amit Kumar' ? 'amit' : (coun === 'Priya Sharma' ? 'lead' : 'sneha');

        leads.unshift({
          id: 200 + leads.length + 1,
          name: name,
          phone: phone.startsWith('+91') ? phone : '+91 ' + phone,
          email: `${name.toLowerCase().replace(/\\s+/g, '.')}@admitdesk.edu`,
          course: course,
          source: 'CSV Import',
          stage: 'Enquiry',
          counsellor: coun,
          counsellorId: cid,
          totalFee: 180000,
          admFee: 45000,
          paid: 0,
          city: city,
          followUp: 'Today',
          isOverdue: false,
          docs: [false, false, false, false],
          father: 'Parent Details Pending',
          academics: { t10: 'N/A', t12: 'N/A', grad: 'N/A', test: 'N/A' },
          notes: ['Imported via bulk CSV intake list. Auto-assigned to counsellor.']
        });
        imported++;
      });

      closeImportModal();
      showToast(`Import completed: ${imported} leads added, ${dupes} duplicates skipped.`);
      applyFilters();
      renderAll();
    }

    // ----------------------------------------------------
    // 15. CSV EXPORT
    // ----------------------------------------------------
    function exportCurrentLeadsCSV() {
      if (filteredLeads.length === 0) {
        showToast('No leads to export');
        return;
      }

      const headers = ['ID', 'Name', 'Phone', 'Email', 'Course', 'City', 'Source', 'Stage', 'Counsellor', 'Token Fee', 'Amount Paid', 'Follow Up'];
      const rows = filteredLeads.map(l => [
        l.id,
        `"${l.name}"`,
        `"${l.phone}"`,
        `"${l.email || ''}"`,
        `"${l.course}"`,
        `"${l.city}"`,
        `"${l.source}"`,
        `"${l.stage}"`,
        `"${l.counsellor}"`,
        l.admFee,
        l.paid || 0,
        `"${l.followUp}"`
      ]);

      const csvContent = 'data:text/csv;charset=utf-8,' + [headers.join(','), ...rows.map(r => r.join(','))].join('\\n');
      const encodedUri = encodeURI(csvContent);
      const link = document.createElement('a');
      link.setAttribute('href', encodedUri);
      link.setAttribute('download', `AdmitDesk_Leads_Export_${new Date().toISOString().slice(0, 10)}.csv`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      showToast(`Exported ${filteredLeads.length} leads to CSV`);
    }

    // ----------------------------------------------------
    // 16. MASTER RENDER & INIT
    // ----------------------------------------------------
    function renderAll() {
      updateExecutiveStats();
      renderPipelineView();
      renderTasksView();
      renderWhatsAppView();
      renderCounsellorsView();
      updateFilterBadges();
      lucide.createIcons();
    }

    // Window Load
    window.onload = function() {
      applyFilters();
      renderAll();

      // Lead Source Donut Chart
      const ctx = document.getElementById('sourceDonut').getContext('2d');
      new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: ['WhatsApp', 'Website Form', 'Facebook Ads', 'Phone / Walk-in'],
          datasets: [{
            data: [36, 28, 22, 14],
            backgroundColor: ['#10b981', '#2563eb', '#6366f1', '#f59e0b'],
            borderWidth: 2,
            borderColor: '#ffffff'
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { display: false }
          },
          cutout: '72%'
        }
      });

      lucide.createIcons();
    };
  </script>
</body>
</html>
"""

with open('/home/ubuntu/chatwoot/dashboard-app/public/index.html', 'w', encoding='utf-8') as f:
    f.write(INDEX_HTML)

print(f"Successfully generated index.html with {len(INDEX_HTML)} bytes")
