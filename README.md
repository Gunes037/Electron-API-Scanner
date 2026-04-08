# 🛡️ Electron API Key Scanner (Static Analysis Automation)

<p align="center">
  <img src="https://images.seeklogo.com/logo-png/61/1/istinye-universitesi-logo-png_seeklogo-610039.png" alt="Istinye University Logo" width="200">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Focus-Security-red.svg" alt="Security">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

---

## 🎓 Academic Information
* **University:** Istinye University (ISU)
* **Course:** Reverse Engineering
* **Instructor:** Keyvan Arasteh
* **Project Title:** 28. API Key Leakage in Electron
* **Student:** Güneş Bingül (2320191055)

---

## 📖 Table of Contents
1. [About the Project](#-about-the-project)
2. [Key Features](#-key-features)
3. [Software Architecture](#-software-architecture)
4. [Installation & Usage](#-installation--usage)
5. [Security Best Practices](#-security-best-practices)

---

## ℹ️ About the Project
This project is a security automation tool designed to audit Electron-based desktop applications for sensitive data exposure. Since Electron apps bundle their source code within `.asar` packages, they often contain hardcoded credentials. This tool automates the extraction and scanning process to identify leaked **AWS and Google Cloud API keys** using optimized Regular Expressions (Regex).

## ✨ Key Features
* **Automated Extraction:** Backend extraction of `.asar` files without manual terminal overhead.
* **Deep Scanning:** Recursive directory traversal to scan `.js`, `.json`, and `.html` files.
* **Regex Engine:** Specialized patterns to detect high-entropy keys (AWS AKIA and Google AIza).
* **Cleanup:** Automatic temporary directory wiping after analysis to maintain disk integrity.

## 🏗️ Software Architecture
To ensure high code quality and satisfy academic requirements, the project has been refactored from a monolithic script into modular components:
* **`scanner_engine.py`:** Core logic containing regex rules and the scanning algorithm.
* **`extractor_utils.py`:** Utility module for ASAR extraction and directory cleanup.
* **`main.py`:** Main entry point handling the execution flow and user input.

## 🚀 Installation & Usage

### 1. Requirements
Ensure you have Node.js and Python 3.x installed. Install the global `asar` dependency:
```bash
npm install -g asar
