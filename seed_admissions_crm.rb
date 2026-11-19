# seed_admissions_crm.rb
account = Account.find(1)
admin_user = account.users.first

puts "=== Setting up Admissions CRM on Account: #{account.name} (ID: #{account.id}) ==="

# 1. Custom Attributes (14 definitions)
custom_attrs = [
  {
    key: 'admission_stage',
    name: 'Admission Stage',
    type: :list,
    model: :contact_attribute,
    description: 'Current stage in the admission pipeline',
    values: ['Enquiry', 'Counselling', 'Follow-up', 'Application', 'Doc Verification', 'Fee Payment', 'Enrollment']
  },
  {
    key: 'course',
    name: 'Course',
    type: :list,
    model: :contact_attribute,
    description: 'Course applied for',
    values: ['B.Tech CSE', 'MBA', 'B.Com', 'BBA', 'MCA', 'B.Sc Nursing']
  },
  {
    key: 'lead_source',
    name: 'Lead Source',
    type: :list,
    model: :contact_attribute,
    description: 'Channel through which the lead arrived',
    values: ['Website', 'Facebook', 'WhatsApp', 'Phone Call', 'Walk-in', 'Referral', 'CSV Import']
  },
  {
    key: 'application_status',
    name: 'Application Status',
    type: :list,
    model: :contact_attribute,
    description: 'Status of student application form',
    values: ['Not Started', 'Submitted', 'Under Review', 'Approved', 'Rejected']
  },
  {
    key: 'documents_status',
    name: 'Documents Status',
    type: :list,
    model: :contact_attribute,
    description: 'Verification status of required documents',
    values: ['Pending', 'Partial', 'Complete', 'Verified']
  },
  {
    key: 'fee_status',
    name: 'Fee Status',
    type: :list,
    model: :contact_attribute,
    description: 'Payment status of admission fee',
    values: ['Unpaid', 'Partial', 'Paid']
  },
  {
    key: 'admission_fee',
    name: 'Admission Fee (₹)',
    type: :currency,
    model: :contact_attribute,
    description: 'Required token/admission fee',
    values: []
  },
  {
    key: 'total_fee',
    name: 'Total Fee (₹)',
    type: :currency,
    model: :contact_attribute,
    description: 'Total course fee',
    values: []
  },
  {
    key: 'amount_paid',
    name: 'Amount Paid (₹)',
    type: :currency,
    model: :contact_attribute,
    description: 'Amount paid towards admission',
    values: []
  },
  {
    key: 'next_follow_up',
    name: 'Next Follow-up Date',
    type: :date,
    model: :contact_attribute,
    description: 'Scheduled date for counsellor follow-up call',
    values: []
  },
  {
    key: 'enrollment_date',
    name: 'Enrollment Date',
    type: :date,
    model: :contact_attribute,
    description: 'Date student completed enrollment',
    values: []
  },
  {
    key: 'father_name',
    name: "Father / Guardian's Name",
    type: :text,
    model: :contact_attribute,
    description: 'Parent or guardian contact',
    values: []
  },
  {
    key: 'dob',
    name: 'Date of Birth',
    type: :date,
    model: :contact_attribute,
    description: 'Student date of birth',
    values: []
  },
  {
    key: 'address',
    name: 'City / Address',
    type: :text,
    model: :contact_attribute,
    description: 'Student residential address or city',
    values: []
  }
]

custom_attrs.each do |attr|
  existing = CustomAttributeDefinition.find_by(attribute_key: attr[:key], account_id: account.id)
  if existing
    existing.update!(
      attribute_display_name: attr[:name],
      attribute_display_type: attr[:type],
      attribute_description: attr[:description],
      attribute_values: attr[:values]
    )
    puts "Updated Custom Attribute: #{attr[:name]} (#{attr[:key]})"
  else
    CustomAttributeDefinition.create!(
      attribute_key: attr[:key],
      attribute_display_name: attr[:name],
      attribute_display_type: attr[:type],
      attribute_model: attr[:model],
      account_id: account.id,
      attribute_description: attr[:description],
      attribute_values: attr[:values]
    )
    puts "Created Custom Attribute: #{attr[:name]} (#{attr[:key]})"
  end
end

# 2. Pipeline Labels (7 Stages + Lost)
labels = [
  { title: 'enquiry', color: '#1f93ff', description: 'Stage 1: New lead enquiry received' },
  { title: 'counselling', color: '#28a745', description: 'Stage 2: Active counselling in progress' },
  { title: 'follow_up', color: '#ffc107', description: 'Stage 3: Follow-up call scheduled' },
  { title: 'application', color: '#6f42c1', description: 'Stage 4: Application submitted / under review' },
  { title: 'doc_verification', color: '#e83e8c', description: 'Stage 5: Document verification stage' },
  { title: 'fee_payment', color: '#fd7e14', description: 'Stage 6: Fee payment pending / in process' },
  { title: 'enrollment', color: '#20c997', description: 'Stage 7: Enrolled student confirmed' },
  { title: 'lead_lost', color: '#dc3545', description: 'Lead not interested or dropped out' }
]

labels.each do |lbl|
  existing = account.labels.find_by(title: lbl[:title])
  if existing
    existing.update!(color: lbl[:color], description: lbl[:description], show_on_sidebar: true)
    puts "Updated Label: #{lbl[:title]}"
  else
    account.labels.create!(
      title: lbl[:title],
      color: lbl[:color],
      description: lbl[:description],
      show_on_sidebar: true
    )
    puts "Created Label: #{lbl[:title]}"
  end
end

# 3. Teams
counselling_team = account.teams.find_or_create_by!(name: 'Admissions Counselling Team') do |t|
  t.description = 'Handles student enquiries, course counselling, and follow-ups'
  t.allow_auto_assign = true
end

accounts_team = account.teams.find_or_create_by!(name: 'Admissions Registrar & Accounts') do |t|
  t.description = 'Document verification, fee approvals, and final enrollments'
  t.allow_auto_assign = false
end
puts "Configured Teams: #{counselling_team.name}, #{accounts_team.name}"

# 4. Custom Roles
counsellor_role = CustomRole.find_or_create_by!(name: 'Counsellor', account_id: account.id) do |r|
  r.description = 'Counsellor handling own leads and follow-up tasks'
  r.permissions = ['conversation_participating_manage', 'contact_manage']
end

team_lead_role = CustomRole.find_or_create_by!(name: 'Team Lead', account_id: account.id) do |r|
  r.description = 'Supervises counselling team, lead reassignment and reports'
  r.permissions = ['conversation_unassigned_manage', 'conversation_manage', 'contact_manage', 'report_manage']
end
puts "Configured Custom Roles: Counsellor, Team Lead"

# 5. Counsellor Users
counsellors_data = [
  { name: 'Priya Sharma (Team Lead)', email: 'priya.sharma@admissions.edu', role: team_lead_role },
  { name: 'Sneha Patel (Counsellor)', email: 'sneha.patel@admissions.edu', role: counsellor_role },
  { name: 'Amit Kumar (Counsellor)', email: 'amit.kumar@admissions.edu', role: counsellor_role }
]

created_users = []
counsellors_data.each do |c|
  user = User.find_by(email: c[:email])
  unless user
    user = User.new(
      name: c[:name],
      email: c[:email],
      password: 'CounsellorPass@2026',
      password_confirmation: 'CounsellorPass@2026'
    )
    user.save!(validate: false)
  end

  acc_user = account.account_users.find_by(user_id: user.id)
  unless acc_user
    acc_user = account.account_users.create!(
      user: user,
      role: :agent,
      custom_role_id: c[:role].id
    )
  end

  # Add to counselling team
  counselling_team.team_members.find_or_create_by!(user: user)
  created_users << user
  puts "Ensured Agent User: #{c[:name]} (#{c[:email]})"
end

# 6. One-Click Stage Macros
macros_data = [
  {
    name: '1. Advance to Counselling',
    actions: [
      { action_name: 'remove_label', action_params: ['enquiry'] },
      { action_name: 'add_label', action_params: ['counselling'] },
      { action_name: 'add_private_note', action_params: ['Stage advanced to: Counselling. Initial course consultation initiated.'] }
    ]
  },
  {
    name: '2. Advance to Follow-up',
    actions: [
      { action_name: 'remove_label', action_params: ['counselling'] },
      { action_name: 'add_label', action_params: ['follow_up'] },
      { action_name: 'add_private_note', action_params: ['Stage advanced to: Follow-up. Student requested time to discuss with parents.'] }
    ]
  },
  {
    name: '3. Advance to Application',
    actions: [
      { action_name: 'remove_label', action_params: ['follow_up'] },
      { action_name: 'add_label', action_params: ['application'] },
      { action_name: 'add_private_note', action_params: ['Stage advanced to: Application. Application form link shared with student.'] }
    ]
  },
  {
    name: '4. Advance to Doc Verification',
    actions: [
      { action_name: 'remove_label', action_params: ['application'] },
      { action_name: 'add_label', action_params: ['doc_verification'] },
      { action_name: 'add_private_note', action_params: ['Stage advanced to: Document Verification. 10th/12th marksheets & ID requested.'] }
    ]
  },
  {
    name: '5. Advance to Fee Payment',
    actions: [
      { action_name: 'remove_label', action_params: ['doc_verification'] },
      { action_name: 'add_label', action_params: ['fee_payment'] },
      { action_name: 'add_private_note', action_params: ['Stage advanced to: Fee Payment. Documents verified. Admission fee token due.'] }
    ]
  },
  {
    name: '6. Confirm Enrollment (Complete)',
    actions: [
      { action_name: 'remove_label', action_params: ['fee_payment'] },
      { action_name: 'add_label', action_params: ['enrollment'] },
      { action_name: 'add_private_note', action_params: ['🎉 Admission fee received and seat confirmed! Student officially Enrolled.'] },
      { action_name: 'resolve_conversation', action_params: [] }
    ]
  }
]

macros_data.each do |m|
  macro = Macro.find_or_initialize_by(name: m[:name], account_id: account.id)
  macro.visibility = :global
  macro.created_by = admin_user
  macro.updated_by = admin_user
  macro.actions = m[:actions]
  macro.save!
  puts "Configured Macro: #{m[:name]}"
end

# 7. Seed 6 Sample Realistic Student Leads with Conversations & Custom Attributes
inbox = account.inboxes.first # talkar WhatsApp inbox
sneha = created_users[1] || admin_user
amit = created_users[2] || admin_user
priya = created_users[0] || admin_user

sample_leads = [
  {
    name: 'Rahul Sharma',
    phone: '+919820123456',
    email: 'rahul.sharma@gmail.com',
    counsellor: sneha,
    stage: 'Counselling',
    label: 'counselling',
    course: 'MBA',
    source: 'WhatsApp',
    app_status: 'Not Started',
    doc_status: 'Pending',
    fee_status: 'Unpaid',
    admission_fee: 46250,
    total_fee: 185000,
    amount_paid: 0,
    next_follow_up: Date.today + 1,
    enrollment_date: nil,
    city: 'Mumbai',
    last_msg: 'Hi Maam, I completed B.Com with 78%. Can I know the placement statistics and MBA specializations offered?'
  },
  {
    name: 'Ananya Verma',
    phone: '+919876543210',
    email: 'ananya.verma@gmail.com',
    counsellor: sneha,
    stage: 'Fee Payment',
    label: 'fee_payment',
    course: 'B.Tech CSE',
    source: 'Website',
    app_status: 'Approved',
    doc_status: 'Verified',
    fee_status: 'Unpaid',
    admission_fee: 55000,
    total_fee: 220000,
    amount_paid: 0,
    next_follow_up: Date.today,
    enrollment_date: nil,
    city: 'Pune',
    last_msg: 'All my documents are submitted. Can you please resend the token admission fee payment link?'
  },
  {
    name: 'Rohit Gupta',
    phone: '+919811223344',
    email: 'rohit.gupta@outlook.com',
    counsellor: amit,
    stage: 'Enquiry',
    label: 'enquiry',
    course: 'BBA',
    source: 'Facebook',
    app_status: 'Not Started',
    doc_status: 'Pending',
    fee_status: 'Unpaid',
    admission_fee: 35000,
    total_fee: 140000,
    amount_paid: 0,
    next_follow_up: Date.today,
    enrollment_date: nil,
    city: 'Delhi NCR',
    last_msg: 'Saw your Facebook ad for BBA 2026-27 batch. What is the last date to apply?'
  },
  {
    name: 'Tanya Reddy',
    phone: '+919988776655',
    email: 'tanya.reddy@yahoo.com',
    counsellor: amit,
    stage: 'Application',
    label: 'application',
    course: 'MCA',
    source: 'WhatsApp',
    app_status: 'Submitted',
    doc_status: 'Partial',
    fee_status: 'Unpaid',
    admission_fee: 40000,
    total_fee: 160000,
    amount_paid: 0,
    next_follow_up: Date.today + 3,
    enrollment_date: nil,
    city: 'Hyderabad',
    last_msg: 'Submitted the online application form! Application ID is MCA-2026-089. Please check.'
  },
  {
    name: 'Vikram Singh Rathore',
    phone: '+919712345678',
    email: 'vikram.singh@gmail.com',
    counsellor: priya,
    stage: 'Enrollment',
    label: 'enrollment',
    course: 'B.Sc Nursing',
    source: 'Walk-in',
    app_status: 'Approved',
    doc_status: 'Verified',
    fee_status: 'Paid',
    admission_fee: 30000,
    total_fee: 120000,
    amount_paid: 30000,
    next_follow_up: nil,
    enrollment_date: Date.today,
    city: 'Jaipur',
    last_msg: 'Token fee paid via NEFT. Reference ID: UTR98234710. Excited to join the batch!'
  },
  {
    name: 'Divya Joshi',
    phone: '+919425012345',
    email: 'divya.joshi@gmail.com',
    counsellor: sneha,
    stage: 'Follow-up',
    label: 'follow_up',
    course: 'MBA',
    source: 'Phone Call',
    app_status: 'Not Started',
    doc_status: 'Pending',
    fee_status: 'Unpaid',
    admission_fee: 46250,
    total_fee: 185000,
    amount_paid: 0,
    next_follow_up: Date.today - 1, # OVERDUE!
    enrollment_date: nil,
    city: 'Indore',
    last_msg: 'Spoke yesterday. Father wants to discuss education loan assistance options today.'
  }
]

sample_leads.each do |lead|
  contact = account.contacts.find_or_initialize_by(phone_number: lead[:phone])
  contact.name = lead[:name]
  contact.email = lead[:email]
  contact.location = lead[:city]
  contact.custom_attributes = {
    'admission_stage' => lead[:stage],
    'course' => lead[:course],
    'lead_source' => lead[:source],
    'application_status' => lead[:app_status],
    'documents_status' => lead[:doc_status],
    'fee_status' => lead[:fee_status],
    'admission_fee' => lead[:admission_fee],
    'total_fee' => lead[:total_fee],
    'amount_paid' => lead[:amount_paid],
    'next_follow_up' => lead[:next_follow_up]&.to_s,
    'enrollment_date' => lead[:enrollment_date]&.to_s,
    'address' => lead[:city]
  }
  contact.save!

  # Ensure contact inbox
  contact_inbox = ContactInbox.find_or_create_by!(contact: contact, inbox: inbox) do |ci|
    ci.source_id = lead[:phone]
  end

  # Ensure conversation
  conversation = Conversation.find_or_create_by!(
    account: account,
    inbox: inbox,
    contact: contact,
    contact_inbox: contact_inbox
  ) do |conv|
    conv.assignee = lead[:counsellor]
    conv.team = counselling_team
    conv.status = lead[:stage] == 'Enrollment' ? :resolved : :open
    conv.additional_attributes = { 'lead_source' => lead[:source] }
  end

  # Tag with label
  conversation.add_labels([lead[:label]])

  # Add incoming student message
  if conversation.messages.where(message_type: :incoming).empty?
    conversation.messages.create!(
      account: account,
      inbox: inbox,
      sender: contact,
      message_type: :incoming,
      content: lead[:last_msg]
    )
  end

  # Add Counsellor History Note
  Note.find_or_create_by!(
    account: account,
    contact: contact,
    content: "Admission History: Lead entered as #{lead[:source]} for #{lead[:course]}. Current stage: #{lead[:stage]}. Assigned to: #{lead[:counsellor].name}."
  )

  puts "Created Student Lead: #{lead[:name]} (#{lead[:course]} - #{lead[:stage]})"
end

puts "\n=== Admissions CRM Seed Completed Successfully! ==="
