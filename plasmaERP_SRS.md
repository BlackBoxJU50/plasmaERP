# Software Requirements Specification (SRS) for plasmaERP

## 1. Introduction

### 1.1 Purpose
The purpose of this document is to define the software requirements for plasmaERP, a comprehensive Enterprise Resource Planning (ERP) system designed to manage and streamline various business processes including Human Resources, Finance, Sales, Inventory, Procurement, and Core Administration.

### 1.2 Scope
plasmaERP is a modular web-based application built using the Django framework. The system includes the following core modules:
- **Core & Accounts (Administration)**: User, role, and permission management along with company and branch setup.
- **Human Resource Management (HRM)**: Employee records, attendance, leave management, and payroll.
- **Finance & Accounting**: Chart of accounts, journal entries, expenses, and revenue management.
- **Sales**: Customer management, sales orders, invoices, and payments.
- **Inventory**: Product catalog, stock management, warehouses, and stock movements.
- **Procurement**: Supplier management, purchase orders, and goods receipts.
- **Approval & Audit**: System-wide approval workflows and audit logging for security and compliance.
- **Notifications**: Internal alert and notification system.

## 2. Overall Description

### 2.1 User Characteristics
The system will be used by various stakeholders within the organization:
- **Administrators**: Full access to all modules, configuration, user management, and audit logs.
- **HR Managers**: Access to HRM module for managing employees, attendance, leaves, and payroll.
- **Finance Officers**: Access to Finance module for managing ledgers, expenses, revenue, and payroll processing.
- **Sales Representatives**: Access to Sales module for handling customers, orders, and invoicing.
- **Inventory Managers**: Access to Inventory and Procurement modules for tracking stock and ordering supplies.
- **Standard Employees**: Limited access to view personal payroll, submit leave requests, and mark attendance.

### 2.2 Operating Environment
- **Server**: Linux/Unix server running Python (Django), PostgreSQL database.
- **Client**: Modern web browsers (Chrome, Firefox, Safari, Edge) on desktop and mobile devices.

## 3. System Features & Requirements

### 3.1 Accounts & Core Module
- **User Management**: System must allow creation, updating, and deactivation of user accounts linked to employees.
- **Role-Based Access Control (RBAC)**: Define roles (e.g., Admin, HR, Sales) and assign specific permissions.
- **Company Setup**: Manage company details, branches, fiscal years, and cost centers.

### 3.2 Human Resource Management (HRM)
- **Employee Directory**: Maintain detailed employee profiles including designation, department, and branch.
- **Attendance Tracking**: Record daily check-in/check-out times and compute working hours.
- **Leave Management**: Employees can request leaves; managers can approve/reject them based on leave types.
- **Payroll Processing**: Generate monthly salary slips detailing basic salary, allowances, deductions, and net salary.

### 3.3 Finance Module
- **Chart of Accounts**: Hierarchical ledger system classifying assets, liabilities, equity, revenue, and expenses.
- **Journal Entries**: Double-entry bookkeeping system for manual adjustments.
- **Income & Expense Tracking**: Record business revenues and expenses against specific accounts.

### 3.4 Sales Module
- **Customer Management**: Maintain customer records, contact info, and credit limits.
- **Sales Orders**: Draft, confirm, and deliver sales orders.
- **Invoicing**: Generate invoices from sales orders, applying taxes and discounts.
- **Payments**: Record customer payments against specific invoices.

### 3.5 Inventory Module
- **Product Catalog**: Manage products with SKUs, barcodes, categories, and units of measurement.
- **Warehouse Management**: Track multiple warehouse locations.
- **Stock Tracking**: Monitor quantity, reserved quantity, and available quantity per product and warehouse.
- **Stock Movements**: Record stock IN, OUT, TRANSFER, and ADJUSTMENT operations.

### 3.6 Procurement Module
- **Supplier Management**: Maintain a database of suppliers and vendors.
- **Purchase Orders**: Create POs for suppliers, tracking expected delivery dates and total amounts.
- **Goods Receipts**: Record the receipt of items against POs into specific warehouses.

### 3.7 Cross-Functional Features
- **Approval Workflows**: Define multi-step approval processes for critical actions (e.g., Leave Approval, PO Confirmation).
- **Audit Logs**: Automatically track modifications (create, update, delete) to sensitive models.
- **Notifications**: Push internal system notifications for pending approvals, task assignments, and alerts.
- **Reporting**: Generate analytical reports across all modules (e.g., Sales Reports, Stock Valuation, Payroll Summary).

## 4. Non-Functional Requirements

### 4.1 Security
- Secure authentication system with password validation and session management.
- Data encryption in transit (HTTPS) and protection against common web vulnerabilities (CSRF, XSS, SQLi).

### 4.2 Performance
- System should load standard pages within 2 seconds.
- Database queries should be optimized to support concurrent users without locking.

### 4.3 Reliability & Availability
- System architecture must support 99.9% uptime during business hours.
- Automated daily backups of the PostgreSQL database.

## 5. Technology Stack
- **Backend Framework**: Django (Python)
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript (Django Templates)
- **Architecture**: Monolithic architecture with modular Django apps.
