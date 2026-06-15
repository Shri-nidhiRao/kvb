document.addEventListener("DOMContentLoaded", () => {
  // Check Authentication
  const adminToken = localStorage.getItem("adminToken");
  if (!adminToken) {
    window.location.replace("login.html");
    return;
  }

  const API_BASE =
    window.location.hostname === "localhost" ||
    window.location.hostname === "127.0.0.1"
      ? "http://localhost:5001/api/blogs"
      : "/api/blogs"; // Fallback

  const tableBody = document.getElementById("blogTableBody");
  const modal = document.getElementById("blogModal");
  const form = document.getElementById("blogForm");
  const modalTitle = document.getElementById("modalTitle");
  const blockContainer = document.getElementById("blockBuilderContainer");

  let blogs = [];
  window.blogBlocks = []; // Array of { type: 'subtitle' | 'paragraph' | 'points', value: '' }

  // Toast Notification logic
  const showToast = (message, isError = false) => {
    const toast = document.getElementById("toastNotification");
    if (!toast) return;
    const msg = document.getElementById("toastMsg");
    const icon = toast.querySelector("i");

    msg.innerText = message;
    if (isError) {
      toast.style.background = "#D32F2F";
      icon.className = "fas fa-exclamation-circle";
    } else {
      toast.style.background = "#3A7D44";
      icon.className = "fas fa-check-circle";
    }

    toast.style.transform = "translateY(0)";
    toast.style.opacity = "1";

    setTimeout(() => {
      toast.style.transform = "translateY(100px)";
      toast.style.opacity = "0";
    }, 3000);
  };

  // Fetch and render blogs
  const fetchBlogs = async () => {
    tableBody.innerHTML = `<tr><td colspan="4" class="loading-spinner"><i class="fas fa-spinner fa-spin fa-2x"></i><br>Loading blogs...</td></tr>`;
    try {
      const res = await fetch(API_BASE);
      if (!res.ok) throw new Error("Failed to fetch");
      blogs = await res.json();
      renderBlogs();
    } catch (error) {
      console.error("Error fetching blogs:", error);
      tableBody.innerHTML = `<tr><td colspan="4" style="text-align:center; color:red; padding: 2rem;">Error loading blogs. Make sure the Node server is running on localhost:5001.</td></tr>`;
    }
  };

  const renderBlogs = () => {
    if (blogs.length === 0) {
      tableBody.innerHTML = `<tr><td colspan="4" style="text-align:center; padding: 2rem; color: #888;">No blogs found. Create your first blog!</td></tr>`;
      return;
    }

    tableBody.innerHTML = blogs
      .map(
        (blog) => `
            <tr>
                <td>
                    <div class="blog-title-cell">
                        <div>
                            <strong style="display:block; font-size:1.1rem; margin-bottom:4px;">${blog.title}</strong>
                            <span style="color:#888; font-size:0.85rem;">
                                ${blog.tags ? blog.tags.map((t) => `<span style="background:#eee; padding:2px 6px; border-radius:4px; margin-right:4px;">${t}</span>`).join("") : ""}
                            </span>
                        </div>
                    </div>
                </td>
                <td>${blog.author || "Admin"}</td>
                <td>${new Date(blog.date).toLocaleDateString()}</td>
                <td>
                    <div class="action-btns">
                        <button class="btn-icon btn-edit" onclick="editBlog('${blog.id}')" title="Edit"><i class="fas fa-edit"></i></button>
                        <button class="btn-icon btn-delete" onclick="deleteBlog('${blog.id}')" title="Delete"><i class="fas fa-trash-alt"></i></button>
                    </div>
                </td>
            </tr>
        `,
      )
      .join("");
  };

  /* =========================================
       BLOCK BUILDER LOGIC
       ========================================= */

  window.addBlock = (type) => {
    window.blogBlocks.push({ type: type, value: "" });
    renderBlocks();
  };

  window.removeBlock = (index) => {
    window.blogBlocks.splice(index, 1);
    renderBlocks();
  };

  window.updateBlockValue = (index, value) => {
    window.blogBlocks[index].value = value;
  };

  const renderBlocks = () => {
    blockContainer.innerHTML = "";
    if (window.blogBlocks.length === 0) {
      blockContainer.innerHTML =
        '<div style="text-align:center; padding: 2rem; color:#aaa; border: 1px dashed #ddd; border-radius: 8px;">No blocks added yet. Use the buttons below to start building.</div>';
      return;
    }

    window.blogBlocks.forEach((block, index) => {
      const blockEl = document.createElement("div");
      blockEl.className = "builder-block";

      let icon = "";
      let label = "";
      let inputHtml = "";

      if (block.type === "subtitle") {
        icon = '<i class="fas fa-heading"></i>';
        label = "Subtitle";
        inputHtml = `<input type="text" value="${escapeHtml(block.value)}" oninput="updateBlockValue(${index}, this.value)" placeholder="Enter subtitle..." style="font-weight: 600; font-size: 1.1rem;">`;
      } else if (block.type === "paragraph") {
        icon = '<i class="fas fa-paragraph"></i>';
        label = "Paragraph";
        inputHtml = `<textarea oninput="updateBlockValue(${index}, this.value)" placeholder="Write your paragraph..." style="min-height: 100px;">${escapeHtml(block.value)}</textarea>`;
      } else if (block.type === "points") {
        icon = '<i class="fas fa-list-ul"></i>';
        label = "Bullet Points (One per line)";
        inputHtml = `<textarea class="points-input" oninput="updateBlockValue(${index}, this.value)" placeholder="Point 1\nPoint 2\nPoint 3...">${escapeHtml(block.value)}</textarea>`;
      } else if (block.type === "legacy") {
        icon = '<i class="fas fa-code"></i>';
        label = "Legacy HTML (Raw)";
        inputHtml = `<textarea oninput="updateBlockValue(${index}, this.value)" placeholder="Raw HTML..." style="min-height: 200px; font-family: monospace;">${escapeHtml(block.value)}</textarea>`;
      }

      blockEl.innerHTML = `
                <div class="builder-block-header">
                    <span>${icon} ${label}</span>
                    <button type="button" class="builder-block-remove" onclick="removeBlock(${index})"><i class="fas fa-times"></i> Remove</button>
                </div>
                ${inputHtml}
            `;
      blockContainer.appendChild(blockEl);
    });
  };

  // Helper to prevent XSS in builder inputs
  const escapeHtml = (unsafe) => {
    return (unsafe || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  };

  /* =========================================
       MODAL & FORM LOGIC
       ========================================= */

  const openModal = () => {
    renderBlocks();
    modal.classList.add("active");
  };

  const closeModal = () => {
    modal.classList.remove("active");
    form.reset();
    document.getElementById("blogId").value = "";
    window.blogBlocks = []; // clear blocks
    modalTitle.innerText = "Create New Blog";
  };

  document.getElementById("openModalBtn").addEventListener("click", () => {
    closeModal(); // Reset form
    // Add a default paragraph block to start
    window.blogBlocks = [{ type: "paragraph", value: "" }];
    openModal();
  });

  document
    .getElementById("closeModalBtn")
    .addEventListener("click", closeModal);
  document.getElementById("cancelBtn").addEventListener("click", closeModal);

  // Form Submit (Create or Update)
  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const id = document.getElementById("blogId").value;
    const tagsStr = document.getElementById("blogTags").value;

    // Compile Blocks into HTML
    let compiledHtml = "";
    window.blogBlocks.forEach((block) => {
      const val = block.value.trim();
      if (!val) return;

      if (block.type === "subtitle") {
        compiledHtml += `\n<h3 style="color: var(--deep-blue); margin-top: 2rem; margin-bottom: 1rem; font-size: 1.6rem;">${val}</h3>\n`;
      } else if (block.type === "paragraph") {
        // Split by double newline to wrap multiple paragraphs if user typed them
        const paras = val.split(/\n\s*\n/);
        paras.forEach((p) => {
          compiledHtml += `<p style="margin-bottom: 1.5rem; color: #1C1C1C; line-height: 1.8;">${p.replace(/\n/g, "<br>")}</p>\n`;
        });
      } else if (block.type === "points") {
        const points = val.split("\n").filter((p) => p.trim() !== "");
        compiledHtml += `<ul style="margin-bottom: 1.5rem; padding-left: 1.5rem; color: #1C1C1C; line-height: 1.8;">\n`;
        points.forEach((p) => {
          compiledHtml += `  <li style="margin-bottom: 0.5rem;">${p.trim()}</li>\n`;
        });
        compiledHtml += `</ul>\n`;
      } else if (block.type === "legacy") {
        compiledHtml += val + "\n";
      }
    });

    // Embed the block data as a JSON comment so we can reconstruct it when editing!
    // This is a neat trick to save complex state without altering the backend schema.
    const blocksJson = JSON.stringify(window.blogBlocks);
    const finalContent = `<!-- BLOCKS: ${blocksJson} -->\n${compiledHtml}`;

    const blogData = {
      title: document.getElementById("blogTitle").value,
      author: document.getElementById("blogAuthor").value || "KVB Team",
      imageUrl: "",
      tags: tagsStr ? tagsStr.split(",").map((t) => t.trim()) : [],
      content: finalContent,
      date: new Date().toISOString().split("T")[0], // Always set current date on update
    };

    const method = id ? "PUT" : "POST";
    const url = id ? `${API_BASE}/${id}` : API_BASE;

    try {
      const res = await fetch(url, {
        method: method,
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${adminToken}`,
        },
        body: JSON.stringify(blogData),
      });

      if (res.ok) {
        closeModal();
        fetchBlogs();
        showToast(
          id ? "Blog updated successfully!" : "Blog published successfully!",
        );
      } else {
        showToast("Failed to save blog.", true);
      }
    } catch (error) {
      console.error("Error saving blog:", error);
      showToast("Error communicating with the server.", true);
    }
  });

  // Helper to parse legacy raw HTML into blocks
  const parseLegacyHTML = (htmlStr) => {
    const parser = new DOMParser();
    const doc = parser.parseFromString(htmlStr, "text/html");
    const blocks = [];
    const children = Array.from(doc.body.children);

    if (children.length === 0) {
      const raw = htmlStr.trim();
      if (raw)
        blocks.push({
          type: "paragraph",
          value: raw
            .replace(/<br\s*[\/]?>/gi, "\n")
            .replace(/<\/?[^>]+(>|$)/g, ""),
        });
      return blocks;
    }

    children.forEach((el) => {
      const tag = el.tagName.toUpperCase();
      if (["H1", "H2", "H3", "H4", "H5", "H6"].includes(tag)) {
        blocks.push({ type: "subtitle", value: el.textContent.trim() });
      } else if (tag === "UL" || tag === "OL") {
        const liItems = Array.from(el.querySelectorAll("li")).map((li) =>
          li.textContent.trim(),
        );
        if (liItems.length > 0) {
          blocks.push({ type: "points", value: liItems.join("\n") });
        }
      } else if (tag === "P") {
        // Convert <br> to newlines, then strip other tags
        let text = el.innerHTML.replace(/<br\s*[\/]?>/gi, "\n");
        // Create a temporary div to decode HTML entities securely
        let temp = document.createElement("div");
        temp.innerHTML = text;
        text = temp.textContent || temp.innerText || "";
        if (text.trim()) {
          blocks.push({ type: "paragraph", value: text.trim() });
        }
      } else {
        if (el.textContent.trim()) {
          blocks.push({ type: "paragraph", value: el.textContent.trim() });
        }
      }
    });

    return blocks.length > 0
      ? blocks
      : [{ type: "paragraph", value: htmlStr.trim() }];
  };

  // Edit Blog
  window.editBlog = (id) => {
    const blog = blogs.find((b) => b.id === id);
    if (!blog) return;

    document.getElementById("blogId").value = blog.id;
    document.getElementById("blogTitle").value = blog.title;
    document.getElementById("blogAuthor").value = blog.author || "";
    document.getElementById("blogTags").value = blog.tags
      ? blog.tags.join(", ")
      : "";

    // Try to parse the hidden JSON blocks from the content string
    const contentStr = blog.content || "";
    const blockMatch = contentStr.match(/<!-- BLOCKS: (.*?) -->/);

    if (blockMatch && blockMatch[1]) {
      try {
        window.blogBlocks = JSON.parse(blockMatch[1]);
      } catch (e) {
        console.error(
          "Failed to parse blocks, fallback to parsing legacy HTML",
        );
        window.blogBlocks = parseLegacyHTML(contentStr);
      }
    } else {
      // Legacy blog without block data - parse HTML directly into blocks!
      window.blogBlocks = parseLegacyHTML(contentStr);
    }

    modalTitle.innerText = "Edit Blog";
    openModal();
  };

  // Delete Blog
  window.deleteBlog = async (id) => {
    if (
      !confirm(
        "Are you sure you want to delete this blog? This action cannot be undone.",
      )
    )
      return;

    try {
      const res = await fetch(`${API_BASE}/${id}`, {
        method: "DELETE",
        headers: { Authorization: `Bearer ${adminToken}` },
      });
      if (res.ok) {
        fetchBlogs();
        showToast("Blog deleted successfully!");
      } else {
        showToast("Failed to delete blog.", true);
      }
    } catch (error) {
      console.error("Error deleting blog:", error);
      showToast("Error communicating with the server.", true);
    }
  };

  /* =========================================
       ROADMAP LOGIC
       ========================================= */
  const ROADMAP_API_BASE =
    window.location.hostname === "localhost" ||
    window.location.hostname === "127.0.0.1"
      ? "http://localhost:5001/api/roadmaps"
      : "/api/roadmaps";

  let roadmaps = [];
  const roadmapTableBody = document.getElementById("roadmapTableBody");
  const roadmapModal = document.getElementById("roadmapModal");
  const roadmapForm = document.getElementById("roadmapForm");
  const roadmapModalTitle = document.getElementById("roadmapModalTitle");

  // Navigation Toggling
  const navBlogs = document.getElementById("navBlogs");
  const navRoadmaps = document.getElementById("navRoadmaps");
  const blogsSection = document.getElementById("blogsSection");
  const roadmapsSection = document.getElementById("roadmapsSection");

  navBlogs.addEventListener("click", (e) => {
    e.preventDefault();
    navBlogs.classList.add("active");
    navRoadmaps.classList.remove("active");
    blogsSection.style.display = "block";
    roadmapsSection.style.display = "none";
  });

  navRoadmaps.addEventListener("click", (e) => {
    e.preventDefault();
    navRoadmaps.classList.add("active");
    navBlogs.classList.remove("active");
    roadmapsSection.style.display = "block";
    blogsSection.style.display = "none";
    if (roadmaps.length === 0) fetchRoadmaps();
  });

  const fetchRoadmaps = async () => {
    roadmapTableBody.innerHTML = `<tr><td colspan="3" class="loading-spinner"><i class="fas fa-spinner fa-spin fa-2x"></i><br>Loading roadmaps...</td></tr>`;
    try {
      const res = await fetch(ROADMAP_API_BASE);
      if (!res.ok) throw new Error("Failed to fetch");
      roadmaps = await res.json();
      renderRoadmaps();
    } catch (error) {
      console.error("Error fetching roadmaps:", error);
      roadmapTableBody.innerHTML = `<tr><td colspan="3" style="text-align:center; color:red; padding: 2rem;">Error loading roadmaps.</td></tr>`;
    }
  };

  const renderRoadmaps = () => {
    if (roadmaps.length === 0) {
      roadmapTableBody.innerHTML = `<tr><td colspan="3" style="text-align:center; padding: 2rem; color: #888;">No roadmaps found. Create your first point!</td></tr>`;
      return;
    }

    // Sort by year
    roadmaps.sort((a, b) => {
      const ya = parseInt(a.year) || 0;
      const yb = parseInt(b.year) || 0;
      return ya - yb;
    });

    roadmapTableBody.innerHTML = roadmaps
      .map(
        (r) => `
            <tr>
                <td>
                    <div style="display:flex; align-items:center; gap:15px;">
                        <div style="width: 40px; height: 40px; border-radius: 50%; background: #eee; display: flex; align-items: center; justify-content: center; color: var(--admin-primary); font-size: 1.2rem;">
                            <i class="${r.icon || "fas fa-circle"}"></i>
                        </div>
                        <div>
                            <strong style="display:block; font-size:1.1rem; margin-bottom:4px;">${r.title}</strong>
                            <span style="color:#888; font-weight:bold;">${r.year}</span>
                        </div>
                    </div>
                </td>
                <td>${r.description || (r.achievements && r.achievements.length > 0 ? r.achievements[0] + "..." : "No description")}</td>
                <td>
                    <div class="action-btns">
                        <button class="btn-icon btn-edit" onclick="editRoadmap('${r.id}')" title="Edit"><i class="fas fa-edit"></i></button>
                        <button class="btn-icon btn-delete" onclick="deleteRoadmap('${r.id}')" title="Delete"><i class="fas fa-trash-alt"></i></button>
                    </div>
                </td>
            </tr>
        `,
      )
      .join("");
  };

  const openRoadmapModal = () => {
    roadmapModal.classList.add("active");
  };

  const closeRoadmapModal = () => {
    roadmapModal.classList.remove("active");
    roadmapForm.reset();
    document.getElementById("roadmapId").value = "";
    roadmapModalTitle.innerText = "Create New Roadmap Point";
  };

  document
    .getElementById("openRoadmapModalBtn")
    .addEventListener("click", () => {
      closeRoadmapModal();
      openRoadmapModal();
    });
  document
    .getElementById("closeRoadmapModalBtn")
    .addEventListener("click", closeRoadmapModal);
  document
    .getElementById("cancelRoadmapBtn")
    .addEventListener("click", closeRoadmapModal);

  roadmapForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const id = document.getElementById("roadmapId").value;
    const achievementsStr = document.getElementById(
      "roadmapAchievements",
    ).value;
    const achievements = achievementsStr
      .split("\n")
      .filter((a) => a.trim() !== "");

    const roadmapData = {
      year: document.getElementById("roadmapYear").value,
      title: document.getElementById("roadmapTitle").value,
      color: document.getElementById("roadmapColor").value,
      description: document.getElementById("roadmapDesc").value,
      achievements: achievements,
    };

    const method = id ? "PUT" : "POST";
    const url = id ? `${ROADMAP_API_BASE}/${id}` : ROADMAP_API_BASE;

    try {
      const res = await fetch(url, {
        method: method,
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${adminToken}`,
        },
        body: JSON.stringify(roadmapData),
      });

      if (res.ok) {
        closeRoadmapModal();
        fetchRoadmaps();
        showToast(
          id ? "Roadmap updated successfully!" : "Roadmap added successfully!",
        );
      } else {
        showToast("Failed to save roadmap.", true);
      }
    } catch (error) {
      console.error("Error saving roadmap:", error);
      showToast("Error communicating with the server.", true);
    }
  });

  window.editRoadmap = (id) => {
    const r = roadmaps.find((x) => x.id === id);
    if (!r) return;

    document.getElementById("roadmapId").value = r.id;
    document.getElementById("roadmapYear").value = r.year || "";
    document.getElementById("roadmapTitle").value = r.title || "";
    document.getElementById("roadmapColor").value = r.color || "#FF6F00";
    document.getElementById("roadmapDesc").value = r.description || "";
    document.getElementById("roadmapAchievements").value = r.achievements
      ? r.achievements.join("\n")
      : "";

    roadmapModalTitle.innerText = "Edit Roadmap Point";
    openRoadmapModal();
  };

  window.deleteRoadmap = async (id) => {
    if (!confirm("Are you sure you want to delete this roadmap point?")) return;

    try {
      const res = await fetch(`${ROADMAP_API_BASE}/${id}`, {
        method: "DELETE",
        headers: { Authorization: `Bearer ${adminToken}` },
      });
      if (res.ok) {
        fetchRoadmaps();
        showToast("Roadmap deleted successfully!");
      } else {
        showToast("Failed to delete roadmap.", true);
      }
    } catch (error) {
      console.error("Error deleting roadmap:", error);
      showToast("Error communicating with the server.", true);
    }
  };

  // Logout
  window.logout = (e) => {
    if (e) e.preventDefault();
    localStorage.removeItem("adminToken");
    window.location.replace("login.html");
  };

  // Initial fetch
  fetchBlogs();
});
