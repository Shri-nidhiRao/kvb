const express = require("express");
const nodemailer = require("nodemailer");
const cors = require("cors");
const path = require("path");
const fs = require("fs");
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

// --- AUTHENTICATION ---
const ADMIN_TOKEN = "kvb-admin-token-xyz";

app.post("/api/login", (req, res) => {
    const { username, password } = req.body;
    if (username === "kvbgreenenergies@gmail.com" && password === "KVB123") {
        res.json({ success: true, token: ADMIN_TOKEN });
    } else {
        res.status(401).json({ success: false, message: "Invalid credentials" });
    }
});

const authMiddleware = (req, res, next) => {
    const authHeader = req.headers['authorization'];
    if (authHeader === `Bearer ${ADMIN_TOKEN}`) {
        next();
    } else {
        res.status(401).json({ error: 'Unauthorized' });
    }
};

// --- BLOGS API ---
const BLOGS_FILE = path.join(__dirname, 'blogs.json');

// Helper to read blogs
const readBlogs = () => {
    try {
        if (!fs.existsSync(BLOGS_FILE)) {
            fs.writeFileSync(BLOGS_FILE, JSON.stringify([]));
        }
        const data = fs.readFileSync(BLOGS_FILE, 'utf8');
        return JSON.parse(data);
    } catch (error) {
        console.error("Error reading blogs:", error);
        return [];
    }
};

// Helper to write blogs
const writeBlogs = (blogs) => {
    fs.writeFileSync(BLOGS_FILE, JSON.stringify(blogs, null, 2));
};

// GET all blogs
app.get("/api/blogs", (req, res) => {
    res.json(readBlogs());
});

// GET single blog
app.get("/api/blogs/:id", (req, res) => {
    const blogs = readBlogs();
    const blog = blogs.find(b => b.id === req.params.id);
    if (blog) res.json(blog);
    else res.status(404).send("Blog not found");
});

// POST new blog
app.post("/api/blogs", authMiddleware, (req, res) => {
    const blogs = readBlogs();
    const newBlog = {
        id: Date.now().toString(),
        title: req.body.title,
        author: req.body.author || "Admin",
        date: req.body.date || new Date().toISOString().split('T')[0],
        tags: req.body.tags || [],
        imageUrl: req.body.imageUrl || "",
        content: req.body.content || "",
        createdAt: new Date().toISOString()
    };
    blogs.push(newBlog);
    writeBlogs(blogs);
    res.status(201).json(newBlog);
});

// PUT update blog
app.put("/api/blogs/:id", authMiddleware, (req, res) => {
    const blogs = readBlogs();
    const index = blogs.findIndex(b => b.id === req.params.id);
    if (index !== -1) {
        blogs[index] = { ...blogs[index], ...req.body, id: req.params.id };
        writeBlogs(blogs);
        res.json(blogs[index]);
    } else {
        res.status(404).send("Blog not found");
    }
});

// DELETE blog
app.delete("/api/blogs/:id", authMiddleware, (req, res) => {
    let blogs = readBlogs();
    const initialLength = blogs.length;
    blogs = blogs.filter(b => b.id !== req.params.id);
    if (blogs.length < initialLength) {
        writeBlogs(blogs);
        res.json({ success: true });
    } else {
        res.status(404).send("Blog not found");
    }
});

if (process.env.NODE_ENV !== 'production') {
    app.listen(5001, () => {
        console.log("Server running on http://localhost:5001");
    });
}

// Prevent process from exiting on errors
process.on('uncaughtException', (err) => {
    console.error('Uncaught Exception:', err);
});

process.on('unhandledRejection', (reason, promise) => {
    console.error('Unhandled Rejection at:', promise, 'reason:', reason);
});

module.exports = app;