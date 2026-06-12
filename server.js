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
    host: "smtp.zoho.in",
    port: 465,
    secure: true,
    auth: {
        user: "info@kvbgreenenergies.com",
        pass: "wDLyHf3mxaYX"
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
            from: `"Website Form" <info@kvbgreenenergies.com>`,
            replyTo: data.reply_to,
            to: "info@kvbgreenenergies.com",
            subject: `New Inquiry from ${data.from_name}`,
            html: `
                <div style="font-family: sans-serif; max-width: 600px;">
                    <h3 style="color: #3A7D44; border-bottom: 2px solid #3A7D44; padding-bottom: 5px;">New Inquiry</h3>
                    <p><b>Name:</b> ${data.from_name}</p>
                    <p><b>Reference ID:</b> ${data.reference_id}</p>
                    <p><b>Organization:</b> ${data.organization || 'N/A'}</p>
                    <p><b>Email:</b> ${data.reply_to}</p>
                    <p><b>Phone:</b> ${data.phone}</p>
                    <p><b>City:</b> ${data.city || 'N/A'}</p>
                    <p><b>State:</b> ${data.state || 'N/A'}</p>
                    <p><b>Inquiry Type:</b> ${data.inquiryType || 'N/A'}</p>
                    <p><b>Product Interest:</b> ${data.productInterest || 'N/A'}</p>
                    <br>
                    <p><b>Message / Requirements:</b><br>
                    ${data.message.replace(/\n/g, '<br>')}</p>
                </div>
            `
        });

        // AUTO REPLY
        await transporter.sendMail({
            from: `"KVB Green Energies" <info@kvbgreenenergies.com>`,
            to: data.reply_to,
            subject: "We received your inquiry",
            html: `
                <h3>Hello ${data.from_name},</h3>
                <p>Thank you for contacting us. We have received your inquiry (Reference ID: <b>${data.reference_id}</b>) and will respond within 24 hours.</p>
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
    const adminUser = process.env.ADMIN_USERNAME || "kvbgreenenergies@gmail.com";
    const adminPass = process.env.ADMIN_PASSWORD || "KVB123";
    if (username === adminUser && password === adminPass) {
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

// --- ROADMAPS API ---
const ROADMAPS_FILE = path.join(__dirname, 'public', 'roadmaps.json');

const readRoadmaps = () => {
    try {
        if (!fs.existsSync(ROADMAPS_FILE)) {
            const defaultRoadmaps = [
                { id: "1", year: "2020", title: "Company Foundation", description: "", achievements: ["Official company establishment", "Renewable energy vision initiated", "Foundation for future innovations"], icon: "fas fa-seedling" },
                { id: "2", year: "2021", title: "Certification & Official Incorporation", description: "", achievements: ["Partnership firm officially incorporated (11/02/2021)", "16 sq.m Schiffer Dish solar steam system received MNRE cooking test certification", "MSME incorporation and GST registration completed", "4 sq.m test report certified by Savitribai Phule Pune University"], icon: "fas fa-sun" },
                { id: "3", year: "2022", title: "Commercial Installation & Government Recognition", description: "", achievements: ["First commercial solar steam cooking installation completed at Sri Siddharood Math, Hubli", "Empanelled in Karnataka Horticulture Department, Bangalore", "Expanded commercial presence in sustainable energy solutions"], icon: "fas fa-certificate" },
                { id: "4", year: "2023", title: "Startup Recognition & Certification", description: "", achievements: ["Received official startup recognition and certification (30/05/2023)", "Strengthened innovation and business credibility", "Expanded recognition within the renewable energy sector"], icon: "fas fa-globe" },
                { id: "5", year: "2024", title: "Expansion & Multi-site Installations", description: "", achievements: ["Completed multiple successful installations across various locations", "Expanded commercial and operational presence", "Demonstrated scalable renewable energy solutions"], icon: "fas fa-leaf" },
                { id: "6", year: "2025", title: "Performance Recognition & International Empanelment", description: "", achievements: ["Received performance report from UHS Bagalkot for Solar Tunnel Dryers", "Empanelled in UNIDO for CST technology", "Strengthened technical credibility and international recognition"], icon: "fas fa-flask" },
                { id: "7", year: "2026", title: "Recognition & Continuous Growth", description: "", achievements: ["Achieved significant recognition in the renewable energy sector", "Continued expansion and business growth", "Strengthened reputation through successful implementations", "Secured patent recognition for an innovative renewable energy project"], icon: "fas fa-chart-line" }
            ];
            fs.writeFileSync(ROADMAPS_FILE, JSON.stringify(defaultRoadmaps, null, 2));
        }
        return JSON.parse(fs.readFileSync(ROADMAPS_FILE, 'utf8'));
    } catch (error) {
        console.error("Error reading roadmaps:", error);
        return [];
    }
};

const writeRoadmaps = (roadmaps) => {
    fs.writeFileSync(ROADMAPS_FILE, JSON.stringify(roadmaps, null, 2));
};

app.get("/api/roadmaps", (req, res) => res.json(readRoadmaps()));
app.get("/api/roadmaps/:id", (req, res) => {
    const r = readRoadmaps().find(x => x.id === req.params.id);
    if (r) res.json(r); else res.status(404).send("Not found");
});
app.post("/api/roadmaps", authMiddleware, (req, res) => {
    const roadmaps = readRoadmaps();
    const newR = { id: Date.now().toString(), ...req.body };
    roadmaps.push(newR);
    writeRoadmaps(roadmaps);
    res.status(201).json(newR);
});
app.put("/api/roadmaps/:id", authMiddleware, (req, res) => {
    const roadmaps = readRoadmaps();
    const idx = roadmaps.findIndex(x => x.id === req.params.id);
    if (idx !== -1) {
        roadmaps[idx] = { ...roadmaps[idx], ...req.body, id: req.params.id };
        writeRoadmaps(roadmaps);
        res.json(roadmaps[idx]);
    } else {
        res.status(404).send("Not found");
    }
});
app.delete("/api/roadmaps/:id", authMiddleware, (req, res) => {
    let roadmaps = readRoadmaps();
    const initialLen = roadmaps.length;
    roadmaps = roadmaps.filter(x => x.id !== req.params.id);
    if (roadmaps.length < initialLen) {
        writeRoadmaps(roadmaps);
        res.json({ success: true });
    } else {
        res.status(404).send("Not found");
    }
});

// --- BLOGS API ---
const BLOGS_FILE = path.join(__dirname, 'public', 'blogs.json');

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