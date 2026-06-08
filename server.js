const express = require("express");
const nodemailer = require("nodemailer");
const cors = require("cors");
const path = require("path");
require("dotenv").config();

const app = express();
app.use(cors());
app.use(express.json());

// Serve static files from the public directory
app.use(express.static(path.join(__dirname, 'public')));

const transporter = nodemailer.createTransport({
    service: "gmail",
    auth: {
        user: process.env.EMAIL_USER,
        pass: process.env.EMAIL_PASS
    },
    tls: {
        rejectUnauthorized: false
    }
});

// Verify connection configuration
transporter.verify(function (error, success) {
    if (error) {
        console.error("Transporter Error Details:", error);
    } else {
        console.log("Server is ready to send emails");
    }
});

const logError = (msg, err) => {
    console.error(`[${new Date().toISOString()}] ${msg}:`, err);
};

app.post("/send-email", async (req, res) => {
    const data = req.body;
    console.log("Received inquiry from:", data.reply_to);

    try {
        // ADMIN EMAIL
        await transporter.sendMail({
            from: `"Website Form" <kvbgreenenergies@gmail.com>`,
            replyTo: data.reply_to,
            to: "kvbgreenenergies@gmail.com",
            subject: `New Inquiry from ${data.from_name}`,
            html: `
                <h3>New Inquiry</h3>
                <p><b>Name:</b> ${data.from_name}</p>
                <p><b>Email:</b> ${data.reply_to}</p>
                <p><b>Phone:</b> ${data.phone}</p>
                <p><b>Message:</b> ${data.message}</p>
            `
        });

        // AUTO REPLY
        await transporter.sendMail({
            from: `"KVB Green Energies" <kvbgreenenergies@gmail.com>`,
            to: data.reply_to,
            subject: "We received your inquiry",
            html: `
                <h3>Hello ${data.from_name},</h3>
                <p>Thank you for contacting us. We have received your inquiry and will respond within 24 hours.</p>
                <p>Best regards,<br>KVB Green Energies Team</p>
            `
        });

        res.status(200).send("Email sent");
    } catch (error) {
        logError("SEND ERROR", error);
        res.status(500).send("Error sending email");
    }
});

const PORT = process.env.PORT || 5001;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});

// Prevent process from exiting on errors
process.on('uncaughtException', (err) => {
    console.error('Uncaught Exception:', err);
});

process.on('unhandledRejection', (reason, promise) => {
    console.error('Unhandled Rejection at:', promise, 'reason:', reason);
});

module.exports = app;