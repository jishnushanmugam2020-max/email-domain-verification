# Email Address and Domain Verification Service Using Regular Expressions

## 1. Project Overview

The Email Address and Domain Verification Service is a web-based application that validates email addresses and domain names using Regular Expressions (Regex).

The application provides a simple interface where users can enter an email address or domain name and check whether its format is valid. Verification results are stored in MongoDB for future reference.

## 2. Objectives

- To validate email address formats using Regular Expressions.
- To validate domain name formats using Regular Expressions.
- To develop a user-friendly verification interface.
- To store verification records in MongoDB.
- To display previous verification results.
- To support deleting individual and all verification records.

## 3. Technologies Used

**Frontend:**
- React.js
- HTML
- CSS
- Axios

**Backend:**
- Node.js
- Express.js

**Database:**
- MongoDB
- Mongoose

**Validation:**
- JavaScript Regular Expressions

## 4. Main Features

1. Email Address Verification
2. Domain Name Verification
3. Verification History
4. Individual Record Deletion
5. Clear All History
6. MongoDB Database Storage

## 5. Working Principle

1. The user enters an email address or domain name.
2. React sends the input to the backend using Axios.
3. Express receives the request.
4. Regular Expressions validate the input format.
5. The verification result is stored in MongoDB.
6. The result is displayed on the frontend.
7. Users can view or delete previous verification records.

## 6. API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /api/verify-email | Verify email |
| POST | /api/verify-domain | Verify domain |
| GET | /api/history | Retrieve history |
| DELETE | /api/history/:id | Delete one record |
| DELETE | /api/history | Delete all records |

## 7. Database

Database Name: emailVerificationDB

Collection Name: verifications

Each verification record stores:
- Type
- Value
- Validity status
- Verification message
- Creation date

## 8. Conclusion

The project demonstrates the practical application of Regular Expressions in validating email address and domain name formats. It integrates React, Node.js, Express.js, and MongoDB to provide a complete full-stack verification application.